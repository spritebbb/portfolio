"""Shrink the five memory photos for the web build.

Originals stay in ../assets (full size, for reference). This rewrites the copies in
src/assets/photos so the page does not ship 2.3 MB of JPEG on first paint.
"""
from pathlib import Path

from PIL import Image

target_dir = Path(__file__).resolve().parent.parent / "src" / "assets" / "photos"
max_width = 1600
quality = 80

for path in sorted(target_dir.glob("*.jpg")):
    before = path.stat().st_size
    with Image.open(path) as im:
        im = im.convert("RGB")
        w, h = im.size
        if w > max_width:
            im = im.resize((max_width, round(h * max_width / w)), Image.LANCZOS)
        im.save(path, "JPEG", quality=quality, optimize=True, progressive=True)
    after = path.stat().st_size
    print(f"{path.name:62s} {w}x{h} -> {im.size[0]}x{im.size[1]}  "
          f"{before/1024:7.1f} KB -> {after/1024:6.1f} KB")
