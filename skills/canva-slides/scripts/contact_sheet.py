#!/usr/bin/env python3
"""Build one contact sheet from per-page Canva thumbnail URLs (or local PNGs).

Input file: one line per page, `page<TAB>url_or_path`. Produce it from get-design-thumbnail
results inside an editing transaction (get-design-pages only fills page 1).

Usage: uv run --with pillow python contact_sheet.py thumbs.tsv sheet.png [cols=3] [cell_w=640]
Pages are labelled in the corner. Review the sheet for: baseline drift, uneven margins, text
clipped by a box, cards wrapping differently, low contrast, empty bottom halves.
"""
import io
import sys
import urllib.request
from pathlib import Path

from PIL import Image, ImageDraw


def load(src):
    if src.startswith(("http://", "https://")):
        return Image.open(io.BytesIO(urllib.request.urlopen(src, timeout=60).read())).convert("RGB")
    return Image.open(src).convert("RGB")


def main():
    if len(sys.argv) < 3:
        raise SystemExit(__doc__)
    rows = [ln.split("\t", 1) for ln in Path(sys.argv[1]).read_text().splitlines() if "\t" in ln and ln.split("\t", 1)[1].strip()]
    cols = int(sys.argv[3]) if len(sys.argv) > 3 else 3
    cw = int(sys.argv[4]) if len(sys.argv) > 4 else 640
    ch, gap = round(cw * 9 / 16), 12
    cells = []
    for page, src in rows:
        raw = load(src.strip())
        # keep aspect: fit inside a 16:9 cell on a white letterbox so non-slide diagrams are not stretched
        scale = min(cw / raw.width, ch / raw.height)
        im = Image.new("RGB", (cw, ch), "white")
        fitted = raw.resize((max(1, round(raw.width * scale)), max(1, round(raw.height * scale))))
        im.paste(fitted, ((cw - fitted.width) // 2, (ch - fitted.height) // 2))
        d = ImageDraw.Draw(im)
        # label in the bottom-right corner so it never covers a title or a diagram
        lw = 14 + 9 * len(page)
        d.rectangle([cw - lw, ch - 26, cw, ch], fill="black")
        d.text((cw - lw + 7, ch - 20), page, fill="white")
        cells.append(im)
    n = len(cells)
    r = (n + cols - 1) // cols
    sheet = Image.new("RGB", (cols * cw + (cols + 1) * gap, r * ch + (r + 1) * gap), "white")
    for i, im in enumerate(cells):
        rr, cc = divmod(i, cols)
        sheet.paste(im, (gap + cc * (cw + gap), gap + rr * (ch + gap)))
    sheet.save(sys.argv[2])
    print(f"ok {n} pages -> {sys.argv[2]} {sheet.size}")


if __name__ == "__main__":
    main()
