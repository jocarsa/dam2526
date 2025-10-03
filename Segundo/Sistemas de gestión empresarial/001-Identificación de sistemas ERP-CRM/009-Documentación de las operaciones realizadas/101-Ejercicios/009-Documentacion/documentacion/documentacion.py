from arbol import draw_tree
from cabeceras import draw_markdown

ruta = "../"


with open("erp.md", "w", encoding="utf-8") as f:
  tree_lines = draw_tree(ruta, show_hidden=False, max_depth=None)
  f.write("\n".join(tree_lines))

  md_lines = draw_markdown(
        ruta,
        show_hidden=False,
        max_depth=None,                  # e.g. 2 to limit depth
        base_level=1,                    # root as H1
        files_as_headings=False,         # True: files as headings; False: bullet list
        link_files=True,
    )
    
  f.write("\n".join(md_lines))
