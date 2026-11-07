#!/usr/bin/env python3
"""Build the 20-slide deck natively (editable text and shapes) from plan.json.

Canvas: 1920x1080 px  ->  13.333 x 7.5 in  (1 px = 6350 EMU, 1 px = 0.5 pt).
Every text box height is MEASURED with Arial metrics so layout is deterministic.
Also writes layout.json (richtexts-shaped) for scripts/deck_audit.py and deck_text.txt for text_diff.py.
"""
import json
import sys
from pathlib import Path

from PIL import ImageFont
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Emu, Pt
from pptx.oxml.ns import qn
from lxml import etree

ROOT = Path(__file__).resolve().parent.parent
PLAN = json.loads((ROOT / "plan.json").read_text(encoding="utf-8"))
SEC = PLAN["sections"]
A = ROOT / "assets"

W, H = 1920, 1080
ML = 130
CW = 1660
FONT = "Arial"
INK, ACC, MUTED, BORDER, CARD, BG, WHITE = "0F2A43", "1F5FA8", "5B6B7B", "C9D3DE", "FFFFFF", "F7F8FA", "FFFFFF"
LH = 1.15  # Arial line box / px

_fonts = {}


def font(px, bold):
    key = (px, bold)
    if key not in _fonts:
        f = "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf"
        _fonts[key] = ImageFont.truetype(f, px)
    return _fonts[key]


def bind(t):
    # no NBSP: PowerPoint's PDF text layer fuses words across it ("phủđịnh")
    return t


def wrap(text, px, bold, width):
    f = font(px, bold)
    lines, cur = [], ""
    for word in text.split(" "):
        t = word if not cur else cur + " " + word
        if f.getlength(t) <= width * 0.98:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def E(px):
    return Emu(int(round(px * 6350)))


prs = Presentation()
prs.slide_width = E(W)
prs.slide_height = E(H)
BLANK = prs.slide_layouts[6]
layout_items = []  # for deck_audit
texts = {}  # page -> list of strings
cur_page = 0


def rgb(h):
    return RGBColor.from_string(h)


def new_slide():
    global cur_page
    cur_page += 1
    s = prs.slides.add_slide(BLANK)
    bg = s.background.fill
    bg.solid()
    bg.fore_color.rgb = rgb(BG)
    texts[cur_page] = []
    return s


def rect(s, x, y, w, h, fill=None, line=None, lw=2, shape=MSO_SHAPE.RECTANGLE):
    sh = s.shapes.add_shape(shape, E(x), E(y), E(w), E(h))
    sh.shadow.inherit = False
    if fill:
        sh.fill.solid()
        sh.fill.fore_color.rgb = rgb(fill)
    else:
        sh.fill.background()
    if line:
        sh.line.color.rgb = rgb(line)
        sh.line.width = Emu(int(lw * 6350))
    else:
        sh.line.fill.background()
    layout_items.append({"page_index": cur_page, "regions": [], "containerElement": {"type": "SHAPE", "position": {"top": y, "left": x}, "dimension": {"width": w, "height": h}}, "element_id": f"P{cur_page}-shape{len(layout_items)}"})
    return sh


def write_paras(tf, paras, align=PP_ALIGN.LEFT):
    first = True
    for pr in paras:
        p = tf.paragraphs[0] if first else tf.add_paragraph()
        first = False
        p.alignment = align
        p.line_spacing = 1.0
        p.space_after = Pt(pr.get("after", 0) / 2)
        r = p.add_run()
        r.text = pr["text"]
        r.font.name = FONT
        r.font.size = Pt(pr["px"] / 2)
        r.font.bold = bool(pr.get("bold"))
        r.font.color.rgb = rgb(pr.get("color", INK))
        rpr = r._r.get_or_add_rPr()
        for tag in ("a:ea", "a:cs"):
            el = etree.SubElement(rpr, qn(tag))
            el.set("typeface", FONT)


def measure(paras, width):
    h = 0
    for pr in paras:
        n = len(wrap(pr["text"], pr["px"], pr.get("bold", False), width))
        h += n * pr["px"] * LH + pr.get("after", 0)
    return h - (paras[-1].get("after", 0) if paras else 0)


def _textbox(s, x, y, w, pr, align, h):
    box = s.shapes.add_textbox(E(x), E(y), E(w), E(h))
    tf = box.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = MSO_ANCHOR.TOP
    write_paras(tf, [dict(pr, after=0)], align)
    texts[cur_page].append(pr["text"])
    layout_items.append({"page_index": cur_page, "regions": [{"text": pr["text"]}], "containerElement": {"type": "TEXT", "position": {"top": y, "left": x}, "dimension": {"width": w, "height": h}}, "element_id": f"P{cur_page}-text{len(layout_items)}"})


def tb(s, x, y, w, paras, align=PP_ALIGN.LEFT, h=None):
    """Text block. Every paragraph is its OWN text box stacked at measured heights, because Canva's PPTX
    import drops paragraph spacing and shape insets. Returns the total measured height."""
    paras = [dict(pr, text=bind(pr["text"])) for pr in paras]
    cy = y
    for pr in paras:
        ph = measure([pr], w)
        _textbox(s, x, cy, w, pr, align, ph)
        cy += ph + pr.get("after", 0)
    return cy - y - (paras[-1].get("after", 0) if paras else 0)


def box_text(s, x, y, w, h, paras, fill=None, line=None, align=PP_ALIGN.CENTER, pad=24, lw=2, anchor=MSO_ANCHOR.MIDDLE):
    """Rectangle plus SEPARATE text boxes (no shape insets, which Canva's import ignores)."""
    paras = [dict(pr, text=bind(pr["text"])) for pr in paras]
    rect(s, x, y, w, h, fill, line, lw)
    mh = measure(paras, w - 2 * pad)
    if mh > h - 24:
        print(f"  !! page {cur_page}: text needs {mh:.0f}px, box has {h - 24:.0f}px: {paras[0]['text'][:40]!r}", file=sys.stderr)
    ty = y + (h - mh) / 2 if anchor == MSO_ANCHOR.MIDDLE else y + 12
    tb(s, x + pad, ty, w - 2 * pad, paras, align)


def pic(s, path, x, y, w=None, h=None):
    from PIL import Image
    im = Image.open(path)
    if w and not h:
        h = w * im.height / im.width
    if h and not w:
        w = h * im.width / im.height
    s.shapes.add_picture(str(path), E(x), E(y), E(w), E(h))
    layout_items.append({"page_index": cur_page, "regions": [], "containerElement": {"type": "SHAPE", "position": {"top": y, "left": x}, "dimension": {"width": w, "height": h}}, "element_id": f"P{cur_page}-pic{len(layout_items)}"})
    return w, h


def arrow_shape(s, x, y, w, h, kind="right", fill=ACC):
    shp = {"right": MSO_SHAPE.RIGHT_ARROW, "down": MSO_SHAPE.DOWN_ARROW, "up": MSO_SHAPE.UP_ARROW}[kind]
    rect(s, x, y, w, h, fill=fill, shape=shp)


def poly(s, pts, fill):
    """Filled freeform polygon (Canva keeps fills; it flattens freeform STROKES to hairlines)."""
    ff = s.shapes.build_freeform(E(pts[0][0]), E(pts[0][1]))
    ff.add_line_segments([(E(x), E(y)) for x, y in pts[1:]], close=True)
    sh = ff.convert_to_shape()
    sh.shadow.inherit = False
    sh.fill.solid()
    sh.fill.fore_color.rgb = rgb(fill)
    sh.line.fill.background()
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    layout_items.append({"page_index": cur_page, "regions": [], "containerElement": {"type": "SHAPE", "position": {"top": min(ys), "left": min(xs)}, "dimension": {"width": max(xs) - min(xs), "height": max(ys) - min(ys)}}, "element_id": f"P{cur_page}-poly{len(layout_items)}"})


def ribbon(s, path, width, fill):
    """Thicken a polyline into a filled polygon (path must not cross itself)."""
    import math
    left, right = [], []
    n = len(path)
    for i, (x, y) in enumerate(path):
        x0, y0 = path[max(i - 1, 0)]
        x1, y1 = path[min(i + 1, n - 1)]
        dx, dy = x1 - x0, y1 - y0
        L = math.hypot(dx, dy) or 1
        nx, ny = -dy / L * width / 2, dx / L * width / 2
        left.append((x + nx, y + ny))
        right.append((x - nx, y - ny))
    poly(s, left + right[::-1], fill)


def arrowhead(s, path, size, fill):
    import math
    (x0, y0), (x1, y1) = path[-3], path[-1]
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy) or 1
    ux, uy = dx / L, dy / L
    tip = (x1 + ux * size, y1 + uy * size)
    b1 = (x1 - uy * size * 0.6, y1 + ux * size * 0.6)
    b2 = (x1 + uy * size * 0.6, y1 - ux * size * 0.6)
    poly(s, [tip, b1, b2], fill)


def title(s, text):
    n = len(wrap(text, 52, True, CW))
    tb(s, ML, 76, CW, [{"text": text, "px": 52, "bold": True}])
    if n > 2:
        print(f"  !! page {cur_page}: title wraps to {n} lines", file=sys.stderr)


def footer(s, n_total):
    tb(s, ML, 1010, 900, [{"text": "Quy luật phủ định của phủ định", "px": 24, "color": MUTED}])
    tb(s, 1690, 1010, 100, [{"text": str(cur_page), "px": 24, "color": MUTED}], align=PP_ALIGN.RIGHT)


def split(pt):
    a, b = pt.split(": ", 1)
    return a, b


CONTENT_TOP = 270


def card_metrics(items, w, head_px, body_px, pad=36):
    iw = w - 2 * pad
    head_lines = max(len(wrap(hd, head_px, True, iw)) for hd, _ in items)
    head_h = head_lines * head_px * LH
    body_h = max(len(wrap(bd, body_px, False, iw)) for _, bd in items) * body_px * LH
    return head_h, body_h


def cards(s, items, highlight=None, y=CONTENT_TOP + 20, head_px=52, body_px=46, min_h=0, gap=40, pad=36, hi_all_plain=False):
    """Equal cards in one row; height follows the tallest content. Returns bottom y."""
    n = len(items)
    w = (CW - gap * (n - 1)) / n
    iw = w - 2 * pad
    head_h, body_h = card_metrics(items, w, head_px, body_px, pad)
    h = max(min_h, pad + head_h + 28 + body_h + pad)
    for i, (hd, bd) in enumerate(items):
        x = ML + i * (w + gap)
        hi = (i == highlight)
        rect(s, x, y, w, h, fill=ACC if hi else CARD, line=None if hi else BORDER)
        col = WHITE if hi else INK
        tb(s, x + pad, y + pad, iw, [{"text": hd, "px": head_px, "bold": True, "color": col}])
        tb(s, x + pad, y + pad + head_h + 28, iw, [{"text": bd, "px": body_px, "color": col}])
    return y + h


def bar(s, text, y, h=130, px=44):
    box_text(s, ML, y, CW, h, [{"text": text, "px": px, "bold": True, "color": WHITE}], fill=ACC, align=PP_ALIGN.LEFT, pad=40)


def chain(s, labels, y, h=150, box_w=None, px=40, hi_last=True, gap=100):
    n = len(labels)
    box_w = box_w or (CW - gap * (n - 1)) / n
    xs = []
    for i, lb in enumerate(labels):
        x = ML + i * (box_w + gap)
        xs.append(x)
        last = hi_last and i == n - 1
        box_text(s, x, y, box_w, h, [{"text": lb, "px": px, "bold": True, "color": WHITE if last else INK}], fill=ACC if last else CARD, line=None if last else BORDER)
        if i < n - 1:
            arrow_shape(s, x + box_w + 18, y + h / 2 - 28, gap - 36, 56)
    return xs, box_w


def sections():
    out = []
    for i, sec in enumerate(SEC, 1):
        out.append((i, sec))
    return out


def cap(t):
    return t[0].upper() + t[1:]


def build():
    n = len(SEC)
    for i, sec in sections():
        s = new_slide()
        pts = sec["points"]
        lab = sec.get("labels", [])
        if i == 1:  # cover
            pic(s, A / "ink_nautilus.png", 1010, 110, h=860)
            tb(s, ML, 230, 860, [{"text": "Quy luật phủ định của phủ định", "px": 100, "bold": True, "color": INK}])
            tb(s, ML, 600, 860, [{"text": pts[0], "px": 52, "bold": True, "color": ACC}])
            src1, src2 = pts[1].split(", Chương", 1)
            tb(s, ML, 720, 860, [{"text": src1, "px": 36, "color": MUTED}, {"text": "Chương" + src2, "px": 36, "color": MUTED, "after": 28}, {"text": pts[2], "px": 40, "color": INK}])
            continue
        if i == n:  # closing
            title(s, sec["title"])
            pic(s, A / "ink_nautilus.png", 1300, 270, h=620)
            tb(s, ML, 290, 1100, [{"text": pts[0], "px": 48, "after": 34}, {"text": pts[1], "px": 48}])
            rect(s, ML, 590, 1100, 2, fill=BORDER)
            tb(s, ML, 620, 1100, [{"text": pts[2], "px": 40, "color": INK}])
            tb(s, ML, 820, 1100, [{"text": pts[3], "px": 50, "bold": True, "color": ACC}])
            continue
        title(s, sec["title"])
        if i == 2:  # three laws as full-width rows; the third is the subject
            for k, pt in enumerate(pts):
                hd, bd = split(pt)
                y = 290 + k * 214
                hi = k == 2
                rect(s, ML, y, CW, 190, fill=ACC if hi else CARD, line=None if hi else BORDER)
                tb(s, ML + 44, y + 28, 800, [{"text": hd, "px": 50, "bold": True, "color": WHITE if hi else INK}])
                tb(s, ML + 920, y + 28, 700, [{"text": "cho biết " + bd, "px": 46, "color": WHITE if hi else INK}])
        elif i == 3:  # agenda
            for k, pt in enumerate(pts):
                y = 290 + k * 165
                tb(s, ML, y, 110, [{"text": str(k + 1), "px": 76, "bold": True, "color": ACC}])
                tb(s, ML + 150, y + 10, 1450, [{"text": pt, "px": 56, "color": INK}])
                rect(s, ML, y + 130, CW, 2, fill=BORDER)
        elif i == 4:
            tb(s, ML, 290, CW, [{"text": pts[0], "px": 48, "color": INK}])
            chain(s, lab, 420, h=220, hi_last=True, px=54)
            bar(s, pts[1], 740, h=180, px=52)
        elif i == 5:
            items = [split(p) for p in pts]
            items = [("Duy vật biện chứng" if k == 2 else hd, bd) for k, (hd, bd) in enumerate(items)]
            cards(s, items, highlight=2, y=300, head_px=52, body_px=46, min_h=520)
        elif i == 6:
            d1, d2 = pts[0].split(", là ", 1)
            tb(s, ML, 290, CW, [{"text": d1 + ",", "px": 54, "bold": True, "color": INK}, {"text": "là " + d2, "px": 54, "bold": True, "color": INK}])
            for k, pt in enumerate(pts[1:]):
                hd, bd = split(pt)
                x = ML + k * (815 + 30)
                rect(s, x, 500, 815, 400, fill=CARD, line=BORDER)
                tb(s, x + 44, 550, 727, [{"text": hd, "px": 40, "color": MUTED, "after": 28}, {"text": cap(bd), "px": 72, "bold": True, "color": ACC}])
        elif i == 7:
            tb(s, ML, 300, 740, [{"text": p, "px": 44, "after": 50} for p in pts])
            bx, bw = 960, 830
            for k, lb in enumerate(lab):
                y = 290 + k * 240
                last = k == len(lab) - 1
                box_text(s, bx, y, bw, 170, [{"text": lb, "px": 44, "bold": True, "color": WHITE if last else INK}], fill=ACC if last else CARD, line=None if last else BORDER)
                if k < len(lab) - 1:
                    arrow_shape(s, bx + bw / 2 - 32, y + 170 + 8, 64, 54, "down")
        elif i == 8:
            items = [split(p) for p in pts[:3]]
            yb = cards(s, items, highlight=None, y=290, head_px=52, body_px=46, min_h=380)
            bar(s, pts[3], yb + 50, h=160, px=52)
        elif i == 9:
            heads, bodies = [], []
            for p in pts[:3]:
                a_, b_ = split(p)
                heads.append(a_)
                bodies.append(b_)
            xs, bw = chain(s, heads, 300, h=210, hi_last=False, px=44)
            for x, bd in zip(xs, bodies):
                tb(s, x, 545, bw, [{"text": bd, "px": 42, "color": INK}])
            bar(s, pts[3], 790, h=150, px=52)
        elif i == 10:
            box_text(s, ML, 290, 640, 230, [{"text": lab[0], "px": 44, "bold": True, "color": WHITE}], fill=ACC)
            arrow_shape(s, ML + 320 - 38, 540, 76, 130, "up")
            box_text(s, ML, 690, 640, 230, [{"text": lab[1], "px": 44, "bold": True, "color": INK}], fill=CARD, line=BORDER)
            for k, pt in enumerate(pts):
                hd, bd = split(pt)
                y = 290 + k * 220
                tb(s, 880, y, 910, [{"text": hd, "px": 50, "bold": True, "color": ACC, "after": 12}, {"text": bd, "px": 44, "color": INK}])
                if k < 2:
                    rect(s, 880, y + 180, 910, 2, fill=BORDER)
        elif i == 11:
            import math
            tb(s, ML, 300, 520, [{"text": p, "px": 42, "after": 50} for p in pts])
            cx, a_x, b_y, rise, drift, base_y = 790, 190, 62, 150, 26, 930
            def at(t):
                return (cx + a_x * math.cos(t) + drift * t / (2 * math.pi), base_y - b_y * math.sin(t) - rise * t / (2 * math.pi))
            for k in range(6):  # half-turn pieces never cross themselves
                path = [at(math.pi * k + math.pi * j / 40) for j in range(42)]
                ribbon(s, path, 10, "1F5FA8")
            lx = 1190
            for k, lb in enumerate(lab):
                x, y = at(2 * math.pi * k)
                rect(s, x + 16, y - 1.5, lx - 24 - (x + 16), 3, fill="7FA3CF")
                rect(s, x - 12, y - 12, 24, 24, fill=INK, shape=MSO_SHAPE.OVAL)
                head, sub = lb.split(": ", 1) if ": " in lb else (lb, "")
                paras = [{"text": head, "px": 40, "bold": True, "color": INK}]
                if sub:
                    paras.append({"text": sub, "px": 32, "color": MUTED})
                mh = measure(paras, 600)
                tb(s, lx, y - mh / 2, 600, paras)
        elif i == 12:
            tb(s, ML, 275, CW, [{"text": pts[0], "px": 44, "color": INK}])
            tw, th, gap = 440, 330, 170
            y0 = 360
            from PIL import Image
            rice = Image.open(A / "ink_rice3.png")
            # split the three vignettes at the two widest empty columns of the ink alpha
            import numpy as np
            col = np.asarray(rice.getchannel("A")).astype(float).sum(axis=0)
            third = rice.width // 3
            cuts = []
            for c0 in (third, 2 * third):
                lo, hi = c0 - 120, c0 + 120
                cuts.append(lo + int(np.argmin(col[lo:hi])))
            parts = [rice.crop((0, 0, cuts[0], rice.height)), rice.crop((cuts[0], 0, cuts[1], rice.height)), rice.crop((cuts[1], 0, rice.width, rice.height))]
            for k, im in enumerate(parts):
                bb = im.getchannel("A").point(lambda v: 255 if v > 24 else 0).getbbox()
                im = im.crop(bb)
                p_ = A / f"ink_rice_{k}.png"
                im.save(p_)
                x = ML + k * (tw + gap)
                rect(s, x, y0, tw, th, fill=CARD, line=BORDER)
                sc = min((tw - 80) / im.width, (th - 60) / im.height)
                pw, ph = im.width * sc, im.height * sc
                pic(s, p_, x + (tw - pw) / 2, y0 + (th - ph) / 2, w=pw, h=ph)
                tb(s, x, y0 + th + 20, tw, [{"text": lab[k], "px": 46, "bold": True, "color": INK}], align=PP_ALIGN.CENTER)
                if k < 2:
                    arrow_shape(s, x + tw + 36, y0 + th / 2 - 30, gap - 72, 60)
            tb(s, ML, 800, CW, [{"text": pts[1], "px": 50, "bold": True, "color": ACC}])
            tb(s, ML, 900, CW, [{"text": pts[2], "px": 30, "color": MUTED}])
        elif i == 13:
            rows = [split(p) for p in pts]
            rh, gap = 155, 12
            for k, (hd, bd) in enumerate(rows):
                y = 290 + k * (rh + gap)
                last = k == len(rows) - 1
                box_text(s, ML, y, 640, rh, [{"text": hd, "px": 44, "bold": True, "color": WHITE if last else INK}], fill=ACC if last else CARD, line=None if last else BORDER, align=PP_ALIGN.LEFT, pad=32)
                box_text(s, ML + 654, y, CW - 654, rh, [{"text": cap(bd), "px": 46, "bold": last, "color": WHITE if last else INK}], fill=ACC if last else CARD, line=None if last else BORDER, align=PP_ALIGN.LEFT, pad=32)
        elif i == 14:
            tb(s, ML, 275, CW, [{"text": pts[0], "px": 46, "color": INK}])
            tiles = ["ink_egg", "ink_larva", "ink_cocoon", "ink_moth", "ink_egg"]
            tw, th, gap = 270, 300, 77.5
            y0 = 360
            from PIL import Image
            for k, (tname, lb) in enumerate(zip(tiles, lab)):
                x = ML + k * (tw + gap)
                rect(s, x, y0, tw, th, fill=CARD, line=BORDER)
                im = Image.open(A / f"{tname}.png")
                sc = min((tw - 30) / im.width, (th - 30) / im.height)
                pw, ph = im.width * sc, im.height * sc
                pic(s, A / f"{tname}.png", x + (tw - pw) / 2, y0 + (th - ph) / 2, w=pw, h=ph)
                tb(s, x, y0 + th + 22, tw, [{"text": lb, "px": 48, "bold": True, "color": INK}], align=PP_ALIGN.CENTER)
                if k < 4:
                    arrow_shape(s, x + tw + 10, y0 + th / 2 - 24, gap - 20, 48)
                    tb(s, x + tw, y0 + th / 2 + 36, gap, [{"text": str(k + 1), "px": 34, "bold": True, "color": ACC}], align=PP_ALIGN.CENTER)
            bar(s, pts[1], 790, h=120, px=48)
            tb(s, ML, 930, CW, [{"text": pts[2], "px": 38, "color": INK}])
        elif i in (15, 16):
            box_text(s, ML, 275, CW, 76, [{"text": pts[0], "px": 34, "color": INK}], fill=None, line=ACC, align=PP_ALIGN.LEFT, pad=28, lw=3)
            big, caps = lab[:3], lab[3:6]
            xs, bw = chain(s, big, 400, h=200, px=(88 if i == 16 else 50), hi_last=True, gap=100)
            for x, c in zip(xs, caps):
                if ": " in c:
                    h_, b_ = c.split(": ", 1)
                    tb(s, x, 640, bw, [{"text": h_ + ":", "px": 38, "bold": True, "color": INK, "after": 6}, {"text": b_, "px": 38, "color": INK}])
                else:
                    tb(s, x, 640, bw, [{"text": c, "px": 38, "color": INK}])
            tb(s, ML, 840, CW, [{"text": pts[1], "px": 46, "bold": True, "color": ACC}])
            if i == 15:
                tb(s, ML, 950, CW, [{"text": lab[6], "px": 28, "color": MUTED}])
        elif i == 17:
            import math
            tb(s, ML, 300, 660, [{"text": p, "px": 42, "after": 50} for p in pts])
            gx, gy, gw, gh = 860, 330, 900, 540
            base = gy + gh - 40
            ribbon(s, [(gx, base), (gx + gw, base - 120)], 6, "8A97A6")
            path = []
            for t in range(91):
                u = t / 90
                path.append((gx + u * gw, base - u * 360 - 70 * math.sin(u * 6 * math.pi)))
            ribbon(s, path, 10, "1F5FA8")
            arrowhead(s, path, 30, "1F5FA8")
            tb(s, gx + gw - 330, base - 120 + 40, 330, [{"text": lab[0], "px": 32, "color": MUTED}], align=PP_ALIGN.RIGHT)
            tb(s, gx, gy - 30, 800, [{"text": lab[1], "px": 38, "bold": True, "color": ACC}])
            for k in range(3):
                cx_ = gx + (k * 2 + 1) / 6 * gw
                tb(s, cx_ - 110, gy + gh + 8, 220, [{"text": lab[2 + k], "px": 30, "color": MUTED}], align=PP_ALIGN.CENTER)
        elif i == 18:
            hd1, bd1 = split(pts[0])
            hd2, bd2 = split(pts[1])
            cw_ = (CW - 40) / 2
            hh = 470
            rect(s, ML, 290, cw_, hh, fill=CARD, line=BORDER)
            tb(s, ML + 44, 340, cw_ - 88, [{"text": hd1, "px": 46, "bold": True, "color": MUTED, "after": 28}, {"text": cap(bd1), "px": 54, "color": INK}])
            rect(s, ML + cw_ + 40, 290, cw_, hh, fill=ACC)
            tb(s, ML + cw_ + 84, 340, cw_ - 88, [{"text": hd2, "px": 46, "bold": True, "color": WHITE, "after": 28}, {"text": cap(bd2), "px": 54, "color": WHITE}])
            tb(s, ML, 830, CW, [{"text": pts[2], "px": 50, "bold": True, "color": ACC}])
        elif i == 19:
            hd1, bd1 = split(pts[0])
            hd2, bd2 = split(pts[1])
            cw_ = (CW - 40) / 2
            hh = 400
            rect(s, ML, 290, cw_, hh, fill=CARD, line=BORDER)
            tb(s, ML + 44, 340, cw_ - 88, [{"text": hd1, "px": 46, "bold": True, "color": ACC, "after": 28}, {"text": cap(bd1), "px": 50, "color": INK}])
            rect(s, ML + cw_ + 40, 290, cw_, hh, fill=CARD, line=BORDER)
            tb(s, ML + cw_ + 84, 340, cw_ - 88, [{"text": hd2, "px": 46, "bold": True, "color": ACC, "after": 28}, {"text": cap(bd2), "px": 50, "color": INK}])
            bar(s, pts[2], 750, h=160, px=52)
        footer(s, n)


build()
out = ROOT / "deck.pptx"
prs.save(out)
(ROOT / "build" / "layout.json").write_text(json.dumps(layout_items, ensure_ascii=False), encoding="utf-8")
dump = []
for p in sorted(texts):
    dump.append("\n".join(texts[p]))
(ROOT / "build" / "deck_text.txt").write_text("\n\n".join(dump), encoding="utf-8")
print("wrote", out, "pages", cur_page)
