#!/usr/bin/env python3
"""Predict wrapping and height of Vietnamese text in a Canva text box BEFORE you replace_text.

Usage: uv run --with pillow python fit_check.py "<text>" --width 440 --px 34 [--bold] [--scale 1.0] [--lh 1.3] [--max-h 120]
       echo "<text>" | uv run --with pillow python fit_check.py - --width 1450 --px 52 --bold

Method: measures the string with Arial (full Vietnamese coverage) x `--scale`, greedy word wrap, then
height = lines x px x line-height. Canva's generated theme font is not Arial, so CALIBRATE once:
find one wrapped line in a real thumbnail, run this tool, and adjust `--scale` until the break lands in
the same place (observed 1.00-1.06 on the deck built in this skill's session: default 1.04 is a
conservative start). It is a prediction, not a measurement: always render after the edit.

Exit code 1 when the text would exceed --max-h (if given) so it can gate a batch.
"""
import argparse
import sys
from pathlib import Path

from PIL import ImageFont

REG = ["/System/Library/Fonts/Supplemental/Arial.ttf", "/Library/Fonts/Arial.ttf", "C:/Windows/Fonts/arial.ttf",
       "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]
BOLD = ["/System/Library/Fonts/Supplemental/Arial Bold.ttf", "/Library/Fonts/Arial Bold.ttf", "C:/Windows/Fonts/arialbd.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"]


def font(px, bold):
    for p in (BOLD if bold else REG):
        if Path(p).exists():
            return ImageFont.truetype(p, 200)  # measure at 200 and scale: avoids hinting jitter
    raise SystemExit("no Vietnamese-capable TTF found")


def wrap(text, f, px, width, scale):
    unit = px / 200 * scale
    lines = []
    for para in text.split("\n"):
        cur = ""
        for w in para.split():
            t = (cur + " " + w).strip()
            if f.getlength(t) * unit <= width or not cur:
                cur = t
            else:
                lines.append(cur)
                cur = w
        lines.append(cur)
    return lines


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("text")
    ap.add_argument("--width", type=float, required=True, help="text box width in slide px")
    ap.add_argument("--px", type=float, required=True, help="font size in slide px")
    ap.add_argument("--bold", action="store_true")
    ap.add_argument("--scale", type=float, default=1.04, help="width multiplier vs Arial (calibrate)")
    ap.add_argument("--lh", type=float, default=1.3, help="line height multiplier")
    ap.add_argument("--max-h", type=float, default=None)
    a = ap.parse_args()
    text = sys.stdin.read().strip() if a.text == "-" else a.text
    f = font(a.px, a.bold)
    lines = wrap(text, f, a.px, a.width, a.scale)
    h = len(lines) * a.px * a.lh
    for i, ln in enumerate(lines, 1):
        w = f.getlength(ln) * a.px / 200 * a.scale
        print(f"{i:>2} | {w:6.0f}px | {ln}")
    orphan = len(lines) > 1 and len(lines[-1].split()) == 1
    print(f"\n{len(lines)} lines, height ~{h:.0f}px at {a.px:g}px x {a.lh} (box width {a.width:g})"
          + ("  [WARN one-word last line: shorten or break by hand]" if orphan else ""))
    if a.max_h is not None and h > a.max_h:
        print(f"OVERFLOW: {h:.0f}px > max {a.max_h:g}px")
        sys.exit(1)


if __name__ == "__main__":
    main()
