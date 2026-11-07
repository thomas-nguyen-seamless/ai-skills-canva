#!/usr/bin/env python3
"""WCAG 2.x contrast check for slide colour pairs.

Usage: python3 contrast.py FG BG [font_px] [bold]
  python3 contrast.py "#5A6978" "#F7F8FA" 30
Verdict uses the WCAG large-text rule (>= 24px regular or >= 18.66px bold needs 3:1), else 4.5:1.
For projected slides aim higher: body >= 7:1 where the palette allows, captions never below 4.5:1.
"""
import sys


def lum(hexcolor):
    h = hexcolor.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    f = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)


def ratio(a, b):
    la, lb = lum(a), lum(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def main():
    if len(sys.argv) < 3:
        raise SystemExit(__doc__)
    fg, bg = sys.argv[1], sys.argv[2]
    px = float(sys.argv[3]) if len(sys.argv) > 3 else 30
    bold = len(sys.argv) > 4 and sys.argv[4].lower() in ("bold", "1", "true")
    r = ratio(fg, bg)
    large = px >= 24 or (bold and px >= 18.66)
    need = 3.0 if large else 4.5
    verdict = "PASS" if r >= need else "FAIL"
    print(f"{fg} on {bg}: {r:.2f}:1 at {px:g}px{' bold' if bold else ''} -> need {need}:1 -> {verdict}"
          + ("" if r >= 7 else "  (below 7:1 projector target)"))
    sys.exit(0 if verdict == "PASS" else 1)


if __name__ == "__main__":
    main()
