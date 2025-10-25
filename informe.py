#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import subprocess
import shutil

# ===================== Configuración =====================
BASE_PATH = Path("/var/www/html/dam2526")
OUTPUT_FILE = BASE_PATH / "informe.md"
EXCLUDE_DIRS = {".git", ".vscode"}
TARGET_SUBFOLDER = "101-Ejercicios"
TZ = ZoneInfo("Europe/Madrid")

OLLAMA_MODEL = "llama3.1:8b-instruct-q4_0"  # Cambia si prefieres otro

# Límites de seguridad
MAX_SUBUNIT_PROMPT_CHARS = 20000   # total por subunidad
PER_FILE_SNIPPET_CHARS   = 2500    # máximo por archivo
MAX_FILES_PER_SUBUNIT    = 40      # por si hay demasiados archivos
MAX_FILE_SIZE_BYTES      = 2 * 1024 * 1024  # ignora >2MB
# =========================================================


def human_date(ts: float) -> str:
    """Devuelve la fecha YYYY-MM-DD local."""
    return datetime.fromtimestamp(ts, TZ).strftime("%Y-%m-%d")


def file_birth_or_mtime(p: Path) -> float:
    st = p.stat()
    return getattr(st, "st_birthtime", st.st_mtime)


def list_dir_clean(p: Path):
    if not p.is_dir():
        return []
    for child in sorted(p.iterdir(), key=lambda x: x.name.lower()):
        if child.name in EXCLUDE_DIRS:
            continue
        yield child


def is_text_file(path: Path) -> bool:
    """Detecta si un archivo es de texto mediante heurística."""
    try:
        if not path.is_file():
            return False
        if path.stat().st_size == 0:
            return False
        if path.stat().st_size > MAX_FILE_SIZE_BYTES:
            return False  # saltar archivos demasiado grandes
        with path.open("rb") as fh:
            head = fh.read(4096)
        if b"\x00" in head:
            return False  # archivo binario
        # si se decodifica parcialmente como UTF-8, lo consideramos texto
        head.decode("utf-8", errors="ignore")
        return True
    except Exception:
        return False


def safe_read_text(path: Path, limit: int = PER_FILE_SNIPPET_CHARS) -> str:
    """Lee texto (UTF-8) limitado, con muestras del inicio, medio y final."""
    try:
        data = path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return ""
    if len(data) <= limit:
        return data
    chunk = limit // 3
    start = data[:chunk]
    mid_start = max((len(data) - chunk) // 2, 0)
    middle = data[mid_start: mid_start + chunk]
    end = data[-chunk:]
    return f"{start}\n...\n{middle}\n...\n{end}"


def summarize_dates(folder: Path):
    if not (folder.exists() and folder.is_dir()):
        return None
    files = [f for f in folder.iterdir() if f.is_file()]
    if not files:
        return None
    times = [file_birth_or_mtime(f) for f in files]
    return min(times), max(times)


def build_ollama_prompt(subunit_name: str, file_snippets: list[str]) -> str:
    header = (
        "Eres un experto que resume materiales de aprendizaje.\n"
        f"Redacta **un único párrafo en español** que describa brevemente los contenidos "
        f"de los archivos de la subunidad '{subunit_name}'.\n"
        "Enfócate en los temas, conceptos o ejercicios principales. No hagas listas ni numeraciones.\n\n"
    )
    body = "\n\n".join(file_snippets)
    return (header + body)[:MAX_SUBUNIT_PROMPT_CHARS]


def run_ollama(model: str, prompt: str) -> str | None:
    """Ejecuta 'ollama run <model>' y devuelve el texto."""
    if shutil.which("ollama") is None:
        return None
    try:
        proc = subprocess.run(
            ["ollama", "run", model],
            input=prompt,
            text=True,
            capture_output=True,
            check=False,
            timeout=120
        )
        out = (proc.stdout or "").strip()
        if not out:
            return None
        return out
    except Exception:
        return None


def build_report(base: Path) -> str:
    lines = []
    lines.append("# Informe de 101-Ejercicios")
    lines.append("")
    lines.append(f"_Base:_ `{base}`")
    lines.append(f"_Generado:_ {human_date(datetime.now(TZ).timestamp())}")
    lines.append(f"_Modelo Ollama:_ `{OLLAMA_MODEL}`")
    lines.append("")

    any_course = False

    for curso in list_dir_clean(base):
        if not curso.is_dir():
            continue
        course_lines, course_has = [f"## Curso: `{curso.name}`"], False

        for asignatura in list_dir_clean(curso):
            if not asignatura.is_dir():
                continue
            subject_lines, subject_has = [f"### Asignatura: `{asignatura.name}`"], False

            for unidad in list_dir_clean(asignatura):
                if not unidad.is_dir():
                    continue
                unit_lines, unit_has = [f"#### Unidad: `{unidad.name}`"], False

                for subunidad in list_dir_clean(unidad):
                    if not subunidad.is_dir():
                        continue

                    ejercicios_dir = subunidad / TARGET_SUBFOLDER
                    resumen_fechas = summarize_dates(ejercicios_dir)
                    if not resumen_fechas:
                        continue

                    # Recolectar archivos de texto
                    text_files = [
                        f for f in sorted(ejercicios_dir.iterdir(), key=lambda x: x.name.lower())
                        if is_text_file(f)
                    ]
                    if not text_files:
                        continue

                    snippets = []
                    total_chars = 0
                    for f in text_files[:MAX_FILES_PER_SUBUNIT]:
                        snippet = f"### {f.name}\n{safe_read_text(f)}"
                        if not snippet.strip():
                            continue
                        if total_chars + len(snippet) > MAX_SUBUNIT_PROMPT_CHARS:
                            break
                        snippets.append(snippet)
                        total_chars += len(snippet)

                    if not snippets:
                        continue

                    earliest, latest = resumen_fechas
                    d1, d2 = human_date(earliest), human_date(latest)
                    date_str = d1 if d1 == d2 else f"{d1} → {d2}"

                    prompt = build_ollama_prompt(subunidad.name, snippets)
                    summary = run_ollama(OLLAMA_MODEL, prompt)

                    unit_lines.append(f"- `{subunidad.name}` — {date_str}")
                    if summary:
                        unit_lines.append(f"  - **Resumen:** {summary}")
                    else:
                        unit_lines.append("  - **Resumen:** _No disponible (error o sin Ollama)._")

                    unit_has = True

                if unit_has:
                    subject_lines.extend(unit_lines + [""])
                    subject_has = True

            if subject_has:
                course_lines.extend(subject_lines + [""])
                course_has = True

        if course_has:
            lines.extend(course_lines + [""])
            any_course = True

    if not any_course:
        lines.append("_No se encontraron subunidades con archivos de texto en `101-Ejercicios`._")
        lines.append("")

    return "\n".join(lines)


if __name__ == "__main__":
    report = build_report(BASE_PATH)
    OUTPUT_FILE.write_text(report, encoding="utf-8")
    print(f"✅ Informe generado: {OUTPUT_FILE}")

