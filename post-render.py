#!/usr/bin/env python3
"""Post-render: create symlink for ref/ in output directory (cross-platform)."""
import os
import sys
import subprocess
from pathlib import Path

script_dir = Path(__file__).resolve().parent
output_dir = script_dir / "docs"

links = [
    (script_dir / "ref", output_dir / "ref"),
    (script_dir / "css", output_dir / "css"),
]

for src, dst in links:
    if not src.exists():
        print(f"SKIP (source not found): {src}")
        continue
    if dst.exists() or dst.is_symlink():
        continue
    dst.parent.mkdir(parents=True, exist_ok=True)
    if sys.platform == "win32":
        if src.is_dir():
            subprocess.run(["cmd", "/c", "mklink", "/J", str(dst), str(src)], check=True)
        else:
            os.link(str(src), str(dst))
    else:
        os.symlink(str(src), str(dst))
    print(f"Linked: {dst} -> {src}")
