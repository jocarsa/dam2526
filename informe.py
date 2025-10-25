#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo

# Settings
BASE_PATH = Path("/var/www/html/dam2526")
OUTPUT_FILE = BASE_PATH / "informe.md"
EXCLUDE_DIRS = {".git", ".vscode"}
TARGET_SUBFOLDER = "101-Ejercicios"
TZ = ZoneInfo("Europe/Madrid")

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

def summarize_dates(folder: Path):
    if not (folder.exists() and folder.is_dir()):
        return None
    files = [f for f in folder.iterdir() if f.is_file()]
    if not files:
        return None
    times = [file_birth_or_mtime(f) for f in files]
    return min(times), max(times)

def build_report(base: Path) -> str:
    lines = []
    lines.append("# Informe de 101-Ejercicios")
    lines.append("")
    lines.append(f"_Base:_ `{base}`")
    lines.append(f"_Generado:_ {human_date(datetime.now(TZ).timestamp())}")
    lines.append("")

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
                    resumen = summarize_dates(subunidad / TARGET_SUBFOLDER)
                    if not resumen:
                        continue  # skip empty/no-date subunits
                    earliest, latest = resumen
                    d1, d2 = human_date(earliest), human_date(latest)
                    date_str = d1 if d1 == d2 else f"{d1} → {d2}"
                    unit_lines.append(f"- `{subunidad.name}` — {date_str}")
                    unit_has = True

                if unit_has:
                    subject_lines.extend(unit_lines + [""])
                    subject_has = True

            if subject_has:
                course_lines.extend(subject_lines + [""])
                course_has = True

        if course_has:
            lines.extend(course_lines + [""])

    return "\n".join(lines)

if __name__ == "__main__":
    report = build_report(BASE_PATH)
    OUTPUT_FILE.write_text(report, encoding="utf-8")
    print(f"✅ Informe generado: {OUTPUT_FILE}")

