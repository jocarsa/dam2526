import os
from typing import Iterable, Optional, List, Set, Dict

# --- reuse your listing helper ---
def list_entries(path: str, show_hidden: bool = False) -> Iterable[os.DirEntry]:
    with os.scandir(path) as it:
        entries = [e for e in it if show_hidden or not e.name.startswith(".")]
    # Directories first, then files; case-insensitive
    entries.sort(key=lambda e: (e.is_file(), e.name.casefold()))
    return entries

def _md_escape(text: str) -> str:
    """Minimal Markdown escape for headings/links."""
    for ch in ["[", "]", "(", ")", "#", "*", "_", "`"]:
        text = text.replace(ch, f"\\{ch}")
    return text

def _rel_link(from_dir: str, target_path: str) -> str:
    try:
        return os.path.relpath(target_path, start=from_dir)
    except ValueError:
        return os.path.basename(target_path)

def _infer_lang_from_ext(ext: str, mapping: Optional[Dict[str, str]] = None) -> str:
    default_map = {
        "py": "python","js": "javascript","ts": "typescript","tsx": "tsx","jsx": "jsx",
        "json": "json","yml": "yaml","yaml": "yaml","md": "markdown","html": "html","htm":"html",
        "css":"css","php":"php","sql":"sql","sh":"bash","bash":"bash","ini":"","cfg":"","txt":"",
        "xml":"xml","csv":"","toml":"toml","rs":"rust","go":"go","java":"java","kt":"kotlin",
        "c":"c","h":"c","cpp":"cpp","hpp":"cpp","cs":"csharp","rb":"ruby","lua":"lua",
        "r":"r","pl":"perl","swift":"swift","makefile":"make","dockerfile":"dockerfile","env":""
    }
    mp = {**default_map, **(mapping or {})}
    return mp.get(ext.lower(), "")

def _read_text_file_safely(path: str, max_bytes: Optional[int] = 262_144) -> str:
    """
    Read file safely with size cap and robust decoding.
    Try utf-8, utf-8-sig, cp1252, latin-1.
    """
    try:
        if max_bytes is not None and os.path.getsize(path) > max_bytes:
            return f"[Contenido omitido: archivo mayor de {max_bytes} bytes]"
        with open(path, "rb") as fh:
            data = fh.read(None if max_bytes is None else max_bytes)
        for enc in ("utf-8", "utf-8-sig", "cp1252", "latin-1"):
            try:
                return data.decode(enc)
            except UnicodeDecodeError:
                continue
        # last resort with replacement
        return data.decode("utf-8", errors="replace")
    except Exception as e:
        return f"[No se pudo leer el archivo: {e}]"

def _fenced_block(content: str, lang: str = "") -> List[str]:
    """Return a Markdown fenced code block; switch to tildes if content has backticks."""
    if "```" in content:
        start = f"~~~{lang}" if lang else "~~~"
        end = "~~~"
        return [start, content, end]
    else:
        start = f"```{lang}" if lang else "```"
        end = "```"
        return [start, content, end]

def draw_markdown(
    path: str,
    show_hidden: bool = False,
    max_depth: Optional[int] = None,
    base_level: int = 1,
    files_as_headings: bool = False,
    link_files: bool = True,
    allowed_extensions: Optional[Set[str]] = None,   # e.g. {"py","js","md"}
    max_file_bytes: Optional[int] = 262_144,         # None = sin límite
    lang_override: Optional[Dict[str, str]] = None,  # ext->lang
    use_emojis: bool = True,                         # Desactívalo si tu visor no es UTF-8
    _current_depth: int = 0,
    _root_dir: Optional[str] = None,
) -> List[str]:
    """
    Markdown directory index with optional inline file contents (code fences).
    """
    lines: List[str] = []
    if _root_dir is None:
        _root_dir = os.path.abspath(path)

    if allowed_extensions is not None:
        allowed_extensions = {ext.lower().lstrip(".") for ext in allowed_extensions}

    # Heading
    level = min(max(1, base_level + _current_depth), 6)
    name = os.path.basename(os.path.normpath(path)) or path
    folder_icon = "📁 " if use_emojis else ""
    lines.append(f'{"#" * level} {folder_icon}{_md_escape(name)}')

    # Depth stop
    if max_depth is not None and _current_depth >= max_depth:
        return lines

    # List entries
    try:
        entries = list_entries(path, show_hidden=show_hidden)
    except PermissionError:
        lines.append("> ⛔ Permiso denegado")
        return lines
    except FileNotFoundError:
        lines.append("> ⚠️  Carpeta no encontrada")
        return lines

    dirs = [e for e in entries if e.is_dir(follow_symlinks=False)]
    files = [e for e in entries if e.is_file(follow_symlinks=False)]
    others = [e for e in entries if not e.is_dir(follow_symlinks=False) and not e.is_file(follow_symlinks=False)]

    file_icon = "📄 " if use_emojis else ""
    link_icon = "🔗 " if use_emojis else ""

    # Files
    if files_as_headings:
        for f in files:
            file_level = min(level + 1, 6)
            display_text = f"{file_icon}{_md_escape(f.name)}"
            rel = _rel_link(_root_dir, f.path) if link_files else None
            display = f"[{display_text}]({_md_escape(rel)})" if rel else display_text
            lines.append(f'{"#" * file_level} {display}')
            ext = os.path.splitext(f.name)[1].lstrip(".").lower()
            if (allowed_extensions is None) or (ext in allowed_extensions):
                lang = _infer_lang_from_ext(ext, lang_override)
                content = _read_text_file_safely(f.path, max_file_bytes)
                lines.extend(_fenced_block(content, lang))
    else:
        if files or others:
            lines.append("")  # blank line before the list
        for f in files:
            title = _md_escape(f.name)
            rel = _rel_link(_root_dir, f.path) if link_files else None
            label = f"[{title}]({_md_escape(rel)})" if rel else title
            lines.append(f"- {file_icon}{label}")
            ext = os.path.splitext(f.name)[1].lstrip(".").lower()
            if (allowed_extensions is None) or (ext in allowed_extensions):
                lang = _infer_lang_from_ext(ext, lang_override)
                content = _read_text_file_safely(f.path, max_file_bytes)
                fenced = _fenced_block(content, lang)
                # Ensure proper nesting: blank line + 4 spaces indentation
                lines.append("")
                lines.extend(["    " + ln if ln else "    " for ln in fenced])

        for o in others:
            lines.append(f"- {link_icon}{_md_escape(o.name)}")

    # Recurse
    for d in dirs:
        lines.extend(
            draw_markdown(
                d.path,
                show_hidden=show_hidden,
                max_depth=max_depth,
                base_level=base_level,
                files_as_headings=files_as_headings,
                link_files=link_files,
                allowed_extensions=allowed_extensions,
                max_file_bytes=max_file_bytes,
                lang_override=lang_override,
                use_emojis=use_emojis,
                _current_depth=_current_depth + 1,
                _root_dir=_root_dir,
            )
        )
    return lines

if __name__ == "__main__":
    root = "."
    md_lines = draw_markdown(
        root,
        show_hidden=False,
        max_depth=None,
        base_level=1,
        files_as_headings=False,
        link_files=True,
        allowed_extensions={"js","py","md","html","css"},  # extensiones permitidas
        max_file_bytes=200_000,
        lang_override=None,
        use_emojis=True,  # pon False si ves mojibake en títulos/listas
    )
    print("\n".join(md_lines))

