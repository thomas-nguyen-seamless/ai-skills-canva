#!/usr/bin/env python3
"""Render slide diagrams as PNG at FINAL slide size, with Vietnamese-safe fonts.

Usage:  uv run --with pillow python diagrams.py spec.json out.png
        uv run --with pillow python diagrams.py --example chain > spec.json

Why: Canva's editing operations cannot add shapes or text boxes, so a custom diagram
is rendered here, uploaded (create-upload-url) and placed with insert_fill. Render it at the
exact pixel size you will place it (1 image px = 1 slide px on a 1920x1080 slide) so label
sizes are what you designed, and paint the slide background colour into the PNG so it can
also hide leftover decoration underneath.

Spec keys common to every kind:
  kind        chain | cycle | spiral | matrix | timeline | pyramid | bars | venn
  size        [w, h]   default [1600, 760]
  bg          hex      default #F7F8FA  (sample the real slide thumbnail)
  colors      {ink, accent, mid, soft, muted}  hex overrides
  title_px / body_px   label sizes, default 40 / 30  (keep body >= 28 for a classroom)
Kinds and their data are shown by --example KIND.
"""
import json
import math
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

S = 3  # supersampling factor
FONT_REG = [
    "/System/Library/Fonts/Supplemental/Arial.ttf",
    "/Library/Fonts/Arial.ttf",
    "C:/Windows/Fonts/arial.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf",
]
FONT_BOLD = [
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/Library/Fonts/Arial Bold.ttf",
    "C:/Windows/Fonts/arialbd.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf",
]
DEFAULT_COLORS = {"ink": "#0F2740", "accent": "#1B4F72", "mid": "#4A90C2", "soft": "#E3EDF5", "muted": "#5A6978"}


def find_font(cands, size):
    for p in cands:
        if Path(p).exists():
            return ImageFont.truetype(p, size)
    raise SystemExit("No Vietnamese-capable TTF found; add a path to FONT_REG/FONT_BOLD")


class Canvas:
    def __init__(self, spec):
        self.w, self.h = spec.get("size", [1600, 760])
        self.bg = spec.get("bg", "#F7F8FA")
        c = dict(DEFAULT_COLORS)
        c.update(spec.get("colors", {}))
        self.c = c
        self.title_px = spec.get("title_px", 40)
        self.body_px = spec.get("body_px", 30)
        self.img = Image.new("RGB", (self.w * S, self.h * S), self.bg)
        self.d = ImageDraw.Draw(self.img)

    def font(self, px, bold=False):
        return find_font(FONT_BOLD if bold else FONT_REG, int(px * S))

    def wrap(self, text, font, max_w):
        lines = []
        for para in str(text).split("\n"):
            cur = ""
            for word in para.split():
                trial = (cur + " " + word).strip()
                if font.getlength(trial) <= max_w * S or not cur:
                    cur = trial
                else:
                    lines.append(cur)
                    cur = word
            lines.append(cur)
        return lines

    def text(self, x, y, text, px, color, bold=False, anchor="la", max_w=None, line_gap=1.25):
        f = self.font(px, bold)
        lines = self.wrap(text, f, max_w) if max_w else str(text).split("\n")
        for i, ln in enumerate(lines):
            self.d.text((x * S, (y + i * px * line_gap) * S), ln, font=f, fill=color, anchor=anchor)
        return len(lines) * px * line_gap

    def box(self, x, y, w, h, fill, radius=14, outline=None, width=0):
        self.d.rounded_rectangle([x * S, y * S, (x + w) * S, (y + h) * S], radius=radius * S, fill=fill,
                                 outline=outline, width=width * S)

    def centered(self, cx, cy, text, px, color, bold=False, max_w=None):
        f = self.font(px, bold)
        lines = self.wrap(text, f, max_w) if max_w else str(text).split("\n")
        total = len(lines) * px * 1.25
        for i, ln in enumerate(lines):
            self.d.text((cx * S, (cy - total / 2 + (i + 0.5) * px * 1.25) * S), ln, font=f, fill=color, anchor="mm")

    def arrow(self, x1, y1, x2, y2, color, width=6, head=22):
        self.d.line([(x1 * S, y1 * S), (x2 * S, y2 * S)], fill=color, width=width * S)
        ang = math.atan2(y2 - y1, x2 - x1)
        # solid triangular head
        a1 = (x2 - head * math.cos(ang - 0.45), y2 - head * math.sin(ang - 0.45))
        a2 = (x2 - head * math.cos(ang + 0.45), y2 - head * math.sin(ang + 0.45))
        self.d.polygon([(x2 * S, y2 * S), (a1[0] * S, a1[1] * S), (a2[0] * S, a2[1] * S)], fill=color)

    def vtext(self, cx, cy, text, px, color, bold=True):
        """Text rotated 90 degrees counter-clockwise, centred on (cx, cy)."""
        f = self.font(px, bold)
        tw = int(f.getlength(str(text))) + 8
        th = int(px * S * 1.4)
        tmp = Image.new("RGBA", (tw, th), (0, 0, 0, 0))
        ImageDraw.Draw(tmp).text((tw // 2, th // 2), str(text), font=f, fill=color, anchor="mm")
        rot = tmp.rotate(90, expand=True)
        self.img.paste(rot, (int(cx * S - rot.width / 2), int(cy * S - rot.height / 2)), rot)
        self.d = ImageDraw.Draw(self.img)

    def save(self, path):
        self.img.resize((self.w, self.h), Image.LANCZOS).save(path)


# --------------------------------------------------------------------------- kinds
def chain(cv, spec):
    items = spec["items"]
    n = len(items)
    gap = spec.get("gap", 110)
    box_w = (cv.w - 2 * 20 - gap * (n - 1)) / n
    box_h = spec.get("box_h", 190)
    y = spec.get("y", (cv.h - box_h) / 2 - 40)
    shades = [cv.c["ink"], cv.c["accent"], cv.c["ink"], cv.c["accent"], cv.c["ink"]]
    for i, it in enumerate(items):
        x = 20 + i * (box_w + gap)
        fill = it.get("fill", shades[i % len(shades)] if i != 1 or n < 3 else cv.c["accent"])
        cv.box(x, y, box_w, box_h, fill)
        cv.centered(x + box_w / 2, y + box_h / 2, it["label"], cv.title_px, "#FFFFFF", True, box_w - 30)
        if it.get("caption"):
            cv.text(x + box_w / 2, y + box_h + 24, it["caption"], cv.body_px, cv.c["muted"], anchor="ma", max_w=box_w)
        if i < n - 1:
            ax1, ax2 = x + box_w + 14, x + box_w + gap - 14
            cv.arrow(ax1, y + box_h / 2, ax2, y + box_h / 2, cv.c["accent"])
            lab = (spec.get("arrow_labels") or [None] * n)[i]
            if lab:
                cv.centered((ax1 + ax2) / 2, y + box_h / 2 - 52, lab, spec.get("arrow_px", 28), cv.c["muted"], False, gap + 40)
    if spec.get("footer"):
        cv.text(cv.w / 2, cv.h - 120, spec["footer"], cv.body_px + 2, cv.c["ink"], anchor="ma", max_w=cv.w - 200)


def cycle(cv, spec):
    items = spec["items"]
    n = len(items)
    cx, cy = cv.w / 2, cv.h / 2 - 10
    r = spec.get("radius", min(cv.w, cv.h) * 0.34)
    bw, bh = spec.get("box_w", 330), spec.get("box_h", 130)
    start = -math.pi / 2
    pts = []
    for i in range(n):
        a = start + i * 2 * math.pi / n
        pts.append((cx + r * 1.35 * math.cos(a), cy + r * math.sin(a)))
    for i in range(n):  # arrows first so boxes sit above
        x1, y1 = pts[i]
        x2, y2 = pts[(i + 1) % n]
        ang = math.atan2(y2 - y1, x2 - x1)
        off = 0.0
        sx = x1 + math.cos(ang) * (bw / 2 + 12)
        sy = y1 + math.sin(ang) * (bh / 2 + 12)
        ex = x2 - math.cos(ang) * (bw / 2 + 18)
        ey = y2 - math.sin(ang) * (bh / 2 + 18)
        cv.arrow(sx, sy, ex, ey, cv.c["accent"])
    for i, it in enumerate(items):
        x, y = pts[i]
        fill = it.get("fill", cv.c["accent"] if i % 2 else cv.c["ink"])
        cv.box(x - bw / 2, y - bh / 2, bw, bh, fill)
        cv.centered(x, y, it["label"], cv.title_px - 6, "#FFFFFF", True, bw - 24)
    if spec.get("center"):
        cv.centered(cx, cy + r * 0.30, spec["center"], cv.body_px - 4, cv.c["muted"], False, 250)


def spiral(cv, spec):
    marks = spec["marks"]  # [{turn: 0|1|2|3, title, sub}]
    turns = spec.get("turns", 3)
    a_x, b_y = spec.get("rx", 200), spec.get("ry", 70)
    rise, drift = spec.get("rise", 135), spec.get("drift", 26)
    cx, base_y = spec.get("cx", cv.w * 0.29), spec.get("base_y", cv.h - 110)
    pts = []
    steps = 1600
    for i in range(steps + 1):
        t = i / steps * turns * 2 * math.pi
        pts.append(((cx + a_x * math.cos(t) + drift * t / (2 * math.pi)) * S,
                    (base_y - b_y * math.sin(t) - rise * t / (2 * math.pi)) * S))
    cv.d.line(pts, fill=cv.c["accent"], width=10 * S, joint="curve")
    lx = spec.get("label_x", cv.w * 0.61)
    for m in marks:
        t = m["turn"] * 2 * math.pi
        x = cx + a_x * math.cos(t) + drift * t / (2 * math.pi)
        y = base_y - b_y * math.sin(t) - rise * t / (2 * math.pi)
        cv.d.ellipse([(x - 11) * S, (y - 11) * S, (x + 11) * S, (y + 11) * S], fill=cv.c["ink"])
        cv.d.line([((x + 11) * S, y * S), ((lx - 22) * S, y * S)], fill=cv.c["mid"], width=3 * S)
        cv.text(lx, y - cv.title_px * 0.7, m["title"], cv.title_px + 4, cv.c["ink"], True)
        if m.get("sub"):
            cv.text(lx, y + cv.title_px * 0.5, m["sub"], cv.body_px, cv.c["muted"])
    if spec.get("note"):
        cv.text(12, 8, spec["note"], cv.body_px - 2, cv.c["muted"])


def matrix(cv, spec):
    pad = 70
    gw, gh = (cv.w - 2 * pad) / 2, (cv.h - 2 * pad - 20) / 2
    cells = spec["cells"]  # 4 dicts: title, sub  (order: TL, TR, BL, BR)
    shades = [cv.c["soft"], cv.c["accent"], cv.c["mid"], cv.c["ink"]]
    for i, c in enumerate(cells):
        r, k = divmod(i, 2)
        x, y = pad + k * gw, pad + r * gh
        cv.box(x + 6, y + 6, gw - 12, gh - 12, c.get("fill", shades[i]))
        dark = (c.get("fill", shades[i]) != cv.c["soft"])
        col = "#FFFFFF" if dark else cv.c["ink"]
        cv.centered(x + gw / 2, y + gh / 2 - 22, c["title"], cv.title_px, col, True, gw - 60)
        if c.get("sub"):
            cv.centered(x + gw / 2, y + gh / 2 + 34, c["sub"], cv.body_px - 2, col, False, gw - 80)
    if spec.get("x_label"):
        cv.centered(cv.w / 2, cv.h - 22, spec["x_label"], cv.body_px, cv.c["muted"], True)
    if spec.get("y_label"):
        cv.vtext(26, cv.h / 2, spec["y_label"], cv.body_px, cv.c["muted"])


def timeline(cv, spec):
    ev = spec["events"]
    n = len(ev)
    y0 = cv.h / 2
    cv.d.line([(40 * S, y0 * S), ((cv.w - 40) * S, y0 * S)], fill=cv.c["accent"], width=8 * S)
    step = (cv.w - 160) / max(n - 1, 1)
    for i, e in enumerate(ev):
        x = 80 + i * step
        cv.d.ellipse([(x - 16) * S, (y0 - 16) * S, (x + 16) * S, (y0 + 16) * S], fill=cv.c["ink"])
        up = i % 2 == 0
        ty = y0 - 150 if up else y0 + 40
        cv.text(x, ty, e["label"], cv.title_px - 4, cv.c["ink"], True, anchor="ma", max_w=step * 1.7)
        if e.get("caption"):
            cv.text(x, ty + cv.title_px * 1.1, e["caption"], cv.body_px - 2, cv.c["muted"], anchor="ma", max_w=step * 1.7)


def pyramid(cv, spec):
    lv = spec["levels"]  # top to bottom
    n = len(lv)
    top_w, base_w = spec.get("top_w", 260), cv.w * 0.82
    h = (cv.h - 60) / n
    for i, label in enumerate(lv):
        w1 = top_w + (base_w - top_w) * i / n
        w2 = top_w + (base_w - top_w) * (i + 1) / n
        y1, y2 = 30 + i * h, 30 + (i + 1) * h - 6
        cx = cv.w / 2
        fill = [cv.c["ink"], cv.c["accent"], cv.c["mid"], cv.c["soft"]][min(i, 3)]
        cv.d.polygon([((cx - w1 / 2) * S, y1 * S), ((cx + w1 / 2) * S, y1 * S), ((cx + w2 / 2) * S, y2 * S), ((cx - w2 / 2) * S, y2 * S)], fill=fill)
        col = "#FFFFFF" if fill != cv.c["soft"] else cv.c["ink"]
        cv.centered(cx, (y1 + y2) / 2, label, cv.title_px - 6, col, True, w2 - 60)


def bars(cv, spec):
    data = spec["data"]  # [{label, value}]
    pad_l, pad_b, pad_t = 90, 110, 40
    mx = max(d["value"] for d in data) * 1.15
    n = len(data)
    bw = (cv.w - pad_l - 40) / n * 0.6
    gap = (cv.w - pad_l - 40) / n
    cv.d.line([(pad_l * S, pad_t * S), (pad_l * S, (cv.h - pad_b) * S)], fill=cv.c["muted"], width=3 * S)
    cv.d.line([(pad_l * S, (cv.h - pad_b) * S), ((cv.w - 30) * S, (cv.h - pad_b) * S)], fill=cv.c["muted"], width=3 * S)
    for i, d in enumerate(data):
        x = pad_l + 30 + i * gap
        hh = (cv.h - pad_b - pad_t) * d["value"] / mx
        y = cv.h - pad_b - hh
        cv.box(x, y, bw, hh, d.get("fill", cv.c["accent"] if i % 2 else cv.c["ink"]), radius=8)
        cv.text(x + bw / 2, y - cv.body_px * 1.35, str(d.get("display", d["value"])), cv.body_px, cv.c["ink"], True, anchor="ma")
        cv.text(x + bw / 2, cv.h - pad_b + 16, d["label"], cv.body_px - 2, cv.c["muted"], anchor="ma", max_w=gap)
    if spec.get("y_label"):
        cv.text(10, 4, spec["y_label"], cv.body_px - 2, cv.c["muted"])


def venn(cv, spec):
    sets = spec["sets"]  # 2 or 3 labels
    n = len(sets)
    r = spec.get("radius", cv.h * 0.30)
    cx, cy = cv.w / 2, cv.h / 2
    if n == 2:
        ctrs = [(cx - r * 0.55, cy), (cx + r * 0.55, cy)]
    else:
        ctrs = [(cx - r * 0.6, cy + r * 0.35), (cx + r * 0.6, cy + r * 0.35), (cx, cy - r * 0.55)]
    ov = Image.new("RGBA", cv.img.size, (0, 0, 0, 0))
    od = ImageDraw.Draw(ov)
    cols = [(27, 79, 114, 120), (74, 144, 194, 120), (15, 39, 64, 110)]
    for (x, y), col in zip(ctrs, cols):
        od.ellipse([(x - r) * S, (y - r) * S, (x + r) * S, (y + r) * S], fill=col)
    cv.img.paste(ov, (0, 0), ov)
    cv.d = ImageDraw.Draw(cv.img)
    for (x, y), lab in zip(ctrs, sets):
        dx = (x - cx) * 1.3 if n == 2 else (x - cx) * 1.25
        dy = (y - cy) * 1.25 if n == 3 else 0
        cv.centered(x + dx * 0.35, y + dy * 0.35, lab, cv.title_px - 6, cv.c["ink"], True, r)
    if spec.get("overlap"):
        cv.centered(cx, cy + (r * 0.05 if n == 2 else r * 0.12), spec["overlap"], cv.body_px, "#FFFFFF", True, r * 0.7)


KINDS = {"chain": chain, "cycle": cycle, "spiral": spiral, "matrix": matrix, "timeline": timeline,
         "pyramid": pyramid, "bars": bars, "venn": venn}

EXAMPLES = {
    "chain": {"kind": "chain", "size": [1600, 560], "items": [
        {"label": "HẠT LÚA", "caption": "Điểm xuất phát"}, {"label": "CÂY LÚA", "caption": "Hạt bị phủ định"},
        {"label": "HẠT LÚA MỚI", "caption": "Nhiều hơn, chất lượng mới"}],
        "arrow_labels": ["nảy mầm", "kết hạt"], "footer": "Phủ định của phủ định: lặp lại ở trình độ cao hơn"},
    "cycle": {"kind": "cycle", "items": [{"label": "CÁI CŨ"}, {"label": "PHỦ ĐỊNH"}, {"label": "CÁI MỚI"}],
              "center": "Chu kỳ tiếp theo ở trình độ cao hơn"},
    "spiral": {"kind": "spiral", "marks": [{"turn": 0, "title": "Bắt đầu", "sub": "cái cũ"},
               {"turn": 1, "title": "Lần 1", "sub": "phủ định cái cũ"}, {"turn": 2, "title": "Lần 2", "sub": "tái lập trên cơ sở mới"},
               {"turn": 3, "title": "Chu kỳ mới", "sub": "cao hơn về chất"}],
               "note": "Mỗi vòng lặp lại điểm xuất phát, nhưng ở trình độ cao hơn"},
    "matrix": {"kind": "matrix", "cells": [{"title": "Phủ định sạch trơn", "sub": "đứt đoạn phát triển"},
               {"title": "Phủ định biện chứng", "sub": "kế thừa có chọn lọc"},
               {"title": "Bảo thủ", "sub": "giữ nguyên xi"}, {"title": "Kế thừa biện chứng", "sub": "cải biến ở trình độ mới"}],
               "x_label": "Mức kế thừa  →", "y_label": "Mức phủ định"},
    "timeline": {"kind": "timeline", "events": [{"label": "1950s", "caption": "Đèn điện tử"}, {"label": "1960s", "caption": "Transistor"},
                 {"label": "1970s", "caption": "Vi mạch"}, {"label": "2000s", "caption": "Đa nhân"}]},
    "pyramid": {"kind": "pyramid", "levels": ["Tự do", "Kế thừa có chọn lọc", "Phát triển", "Mâu thuẫn nội tại"]},
    "bars": {"kind": "bars", "data": [{"label": "Vòng 1", "value": 1}, {"label": "Vòng 2", "value": 2.2}, {"label": "Vòng 3", "value": 4.1}],
             "y_label": "Trình độ phát triển"},
    "venn": {"kind": "venn", "sets": ["Cái cũ", "Cái mới"], "overlap": "Kế thừa"},
}


def main():
    if len(sys.argv) >= 3 and sys.argv[1] == "--example":
        print(json.dumps(EXAMPLES[sys.argv[2]], ensure_ascii=False, indent=2))
        return
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    spec = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    cv = Canvas(spec)
    KINDS[spec["kind"]](cv, spec)
    cv.save(sys.argv[2])
    print(f"saved {sys.argv[2]} {cv.w}x{cv.h}")


if __name__ == "__main__":
    main()
