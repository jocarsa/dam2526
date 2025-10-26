#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import subprocess
import shutil
import re

# ===================== Configuración =====================
BASE_PATH = Path("/var/www/html/dam2526")
OUTPUT_FILE = BASE_PATH / "informe.md"
EXCLUDE_DIRS = {".git", ".vscode"}
TARGET_SUBFOLDER = "101-Ejercicios"
TZ = ZoneInfo("Europe/Madrid")

OLLAMA_MODEL = "llama3.1:8b-instruct-q4_0"  # o 'qwen2.5-coder:7b'

# Límites de seguridad
MAX_SUBUNIT_PROMPT_CHARS = 20000   # total por subunidad
PER_FILE_SNIPPET_CHARS   = 2500    # máximo por archivo
MAX_FILES_PER_SUBUNIT    = 40      # tope de archivos por subunidad
MAX_FILE_SIZE_BYTES      = 2 * 1024 * 1024  # ignora >2MB

# Longitud objetivo del párrafo final
MAX_SUMMARY_WORDS = 180
# =========================================================


def human_date(ts: float) -> str:
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
    """Heurística robusta para detectar archivos de texto (independiente de extensión)."""
    try:
        if not path.is_file():
            return False
        size = path.stat().st_size
        if size == 0 or size > MAX_FILE_SIZE_BYTES:
            return False
        with path.open("rb") as fh:
            head = fh.read(4096)
        if b"\x00" in head:
            return False  # binario
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
    chunk = max(1, limit // 3)
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
    """Prompt reforzado: una sola salida de párrafo, sin listas ni intro."""
    guardrails = (
        "TAREA: Redacta exactamente UN PÁRRAFO en español que resuma los temas, objetivos y ejercicios "
        f"presentes en los archivos de la subunidad «{subunit_name}».\n"
        "REQUISITOS OBLIGATORIOS:\n"
        "1) Un solo párrafo; sin saltos de línea dobles.\n"
        "2) Prohibido usar encabezados, listas, viñetas o enumeraciones.\n"
        "3) Prohibido introducirte (nada de 'Aquí te presento...', 'En esta sección...', 'A continuación...').\n"
        "4) Integra ideas de forma concisa y cohesionada; tono técnico y claro; máximo ~160 palabras.\n"
        "5) No describas el código paso a paso ni listados de funciones; resume el propósito y los conceptos.\n\n"
        "Fragmentos de archivos (pueden contener ruido o plantillas repetidas):\n\n"
    )
    body = "\n\n".join(file_snippets)
    return (guardrails + body)[:MAX_SUBUNIT_PROMPT_CHARS]


def run_ollama(model: str, prompt: str) -> str | None:
    """Ejecuta 'ollama run <model>' y devuelve la salida como texto."""
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
        return out if out else None
    except Exception:
        return None


# --------------------- Sanitizador de salida ---------------------

INTRO_PATTERNS = [
    r"^\s*aqu[ií] te presento.*?$",
    r"^\s*en (esta|la) (secci[oó]n|subunidad).*?$",
    r"^\s*a continuaci[oó]n.*?$",
    r"^\s*este (documento|c[oó]digo|m[oó]dulo).*?$",
    r"^\s*el c[oó]digo proporcionado.*?$",
    r"^\s*en general,.*?$",
    r"^\s*resumen:?\s*",
]
INTRO_REGEXES = [re.compile(pat, re.IGNORECASE | re.MULTILINE) for pat in INTRO_PATTERNS]

def clean_to_single_paragraph(text: str, max_words: int = MAX_SUMMARY_WORDS) -> str:
    if not text:
        return ""

    # Elimina fences y encabezados/bullets obvios
    text = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)   # bloques de código
    text = re.sub(r"`[^`]*`", " ", text)                      # inline code
    text = re.sub(r"^\s*#{1,6}\s+.*$", " ", text, flags=re.MULTILINE)  # # encabezados
    text = re.sub(r"^\s*[-*•]\s+", " ", text, flags=re.MULTILINE)      # viñetas
    text = re.sub(r"^\s*\d+[\.)]\s+", " ", text, flags=re.MULTILINE)   # enumeraciones

    # Quita párrafos introductorios metadiscursivos al inicio
    # Tomamos primeras 3 líneas y si matchean, las eliminamos
    lines = text.splitlines()
    cleaned_lines = []
    for i, ln in enumerate(lines):
        if i < 3:
            skip = any(rx.match(ln.strip()) for rx in INTRO_REGEXES)
            if skip:
                continue
        cleaned_lines.append(ln)
    text = "\n".join(cleaned_lines)

    # Colapsa saltos de línea a espacios (un solo párrafo)
    text = re.sub(r"\s*\n\s*", " ", text)
    # Quita múltiples espacios
    text = re.sub(r"\s{2,}", " ", text).strip(" \t\r\n-—:;")

    # Si todavía empieza con intro típica, corta esa frase inicial
    for rx in INTRO_REGEXES:
        text = rx.sub("", text).strip()

    # Forzar límite de palabras
    words = text.split()
    if len(words) > max_words:
        text = " ".join(words[:max_words]).rstrip(",.;:") + "."

    # Asegura que no se cuele más de un punto y aparte
    text = re.sub(r"\s*\n\s*", " ", text).strip()
    return text


# --------------------- Generación del informe ---------------------

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

                    # Archivos de texto
                    text_files = [
                        f for f in sorted(ejercicios_dir.iterdir(), key=lambda x: x.name.lower())
                        if is_text_file(f)
                    ]
                    if not text_files:
                        continue

                    # Snippets limitados
                    snippets, total_chars = [], 0
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

                    # LLM -> resumen
                    prompt = build_ollama_prompt(subunidad.name, snippets)
                    raw_summary = run_ollama(OLLAMA_MODEL, prompt)
                    summary = clean_to_single_paragraph(raw_summary or "")

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

