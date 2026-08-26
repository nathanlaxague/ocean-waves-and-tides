"""Loader for the repo-root figure_style.py.

Notebooks in this folder use the unmodified `import figure_style as fs` line,
which resolves to this file. It executes the shared style module one directory
up and re-exports its public names, so the style lives in exactly one place.
Do not put a copy of the real style module here.
"""

import importlib.util as _ilu
from pathlib import Path as _Path

_root = _Path(__file__).resolve().parent.parent / "figure_style.py"
_spec = _ilu.spec_from_file_location("_figure_style_shared", _root)
_shared = _ilu.module_from_spec(_spec)
_spec.loader.exec_module(_shared)

figure_style = _shared.figure_style
color_list = _shared.color_list
fullwidth = _shared.fullwidth
fullheight = _shared.fullheight
fsize = _shared.fsize
