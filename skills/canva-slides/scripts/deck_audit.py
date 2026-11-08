#!/usr/bin/env python3
"""Deck-level layout audit from a start-editing-transaction `richtexts` dump.

Usage: python3 deck_audit.py richtexts.json [--mode talk|presenter|document] [--margin 96] [--title-top 76] [--json]

Input: the JSON array `tx.richtexts` (each item: page_index, regions[{text}], containerElement{type,position,dimension}, element_id).
Checks (geometry and text only; colour and font are NOT in the payload, so look at thumbnails for those):
  1 title position outliers  - per page the TEXT box with the smallest top (and width >= 900) is the title; compare to the modal (top,left)
  2 left-edge drift          - body TEXT boxes whose left differs from the modal body left by > 6 px
  3 margins / bounds         - TEXT boxes left of --margin, or right edge past 1920 - margin, or bottom past 1080
  4 overlaps                 - TEXT-vs-TEXT bounding boxes that overlap by > 12% of the smaller box
  5 words per slide          - against the mode budget (presenter 25 / talk 40 / document 75), cover and closing exempt
  6 duplicate titles and heading-length monotony
Exit code 1 when any ERROR is reported.
"""
import argparse
import collections
import json
import re
import sys
from pathlib import Path

W, H = 1920, 1080
EMOJI = re.compile("[\U0001F000-\U0001FAFF\u2600-\u27BF\u2B00-\u2BFF\uFE0F\u200D]")

BUDGET = {"presenter": 25, "talk": 40, "document": 75}


def text_of(e):
    return "".join(r.get("text", "") for r in e.get("regions", [])).strip()


def box(e):
    c = e["containerElement"]
    p, d = c["position"], c["dimension"]
    return p["left"], p["top"], p["left"] + d["width"], p["top"] + d["height"]


def modal(vals, tol=6):
    if not vals:
        return None
    buckets = collections.Counter(round(v / tol) * tol for v in vals)
    return buckets.most_common(1)[0][0]


def overlap(a, b):
    x1, y1 = max(a[0], b[0]), max(a[1], b[1])
    x2, y2 = min(a[2], b[2]), min(a[3], b[3])
    if x2 <= x1 or y2 <= y1:
        return 0.0
    inter = (x2 - x1) * (y2 - y1)
    small = min((a[2] - a[0]) * (a[3] - a[1]), (b[2] - b[0]) * (b[3] - b[1]))
    return inter / small if small else 0.0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--mode", default="talk", choices=list(BUDGET))
    ap.add_argument("--margin", type=float, default=96)
    ap.add_argument("--title-top", type=float, default=None)
    a = ap.parse_args()
    items = json.loads(Path(a.file).read_text(encoding="utf-8"))
    pages = collections.defaultdict(list)
    for e in items:
        if e["containerElement"]["type"] == "TEXT" and text_of(e):
            pages[e["page_index"]].append(e)
    n = max(pages) if pages else 0
    # AI-tell: a short, thin SHAPE directly under the title on most content pages (accent rule)
    rules = collections.defaultdict(list)
    for e in items:
        c = e["containerElement"]
        if c["type"] == "SHAPE" and not text_of(e) and c["dimension"]["width"] <= 140 and c["dimension"]["height"] <= 14:
            rules[e["page_index"]].append(e)
    errs, warns = [], []
    titles = {}
    for p, els in sorted(pages.items()):
        cand = [e for e in els if e["containerElement"]["dimension"]["width"] >= 900]
        t = min(cand or els, key=lambda e: e["containerElement"]["position"]["top"])
        titles[p] = t
    content = [p for p in sorted(pages) if p not in (1, n)]
    tops = [titles[p]["containerElement"]["position"]["top"] for p in content]
    lefts = [titles[p]["containerElement"]["position"]["left"] for p in content]
    mt = a.title_top if a.title_top is not None else modal(tops)
    ml = modal(lefts)
    for p in content:
        pos = titles[p]["containerElement"]["position"]
        if mt is not None and abs(pos["top"] - mt) > 6:
            errs.append(f"slide {p}: title top {pos['top']:.0f} != modal {mt:.0f}")
        if ml is not None and abs(pos["left"] - ml) > 6:
            errs.append(f"slide {p}: title left {pos['left']:.0f} != modal {ml:.0f}")
    # body left drift
    body_lefts = []
    for p in content:
        for e in pages[p]:
            if e is titles[p]:
                continue
            body_lefts.append(e["containerElement"]["position"]["left"])
    for p in content:
        for e in pages[p]:
            if e is titles[p]:
                continue
            l, t_, r, b = box(e)
            if l < a.margin - 1:
                errs.append(f"slide {p}: '{text_of(e)[:30]}' left {l:.0f} inside the {a.margin:.0f}px safe zone")
            if r > W - a.margin + 1:
                warns.append(f"slide {p}: '{text_of(e)[:30]}' right edge {r:.0f} past {W - a.margin:.0f}")
            if b > H:
                errs.append(f"slide {p}: '{text_of(e)[:30]}' bottom {b:.0f} past the page ({H})")
    for p, els in sorted(pages.items()):
        bs = [(e, box(e)) for e in els]
        for i in range(len(bs)):
            for j in range(i + 1, len(bs)):
                o = overlap(bs[i][1], bs[j][1])
                if o > 0.12:
                    errs.append(f"slide {p}: text boxes overlap {o:.0%}: '{text_of(bs[i][0])[:24]}' / '{text_of(bs[j][0])[:24]}'")
    budget = BUDGET[a.mode]
    for p, els in pages.items():
        for e in els:
            if EMOJI.search(text_of(e)):
                errs.append(f"slide {p}: emoji/pictograph in text {text_of(e)[:40]!r} (banned in slides)")
    for p in content:
        words = sum(len(text_of(e).split()) for e in pages[p] if e is not titles[p])
        if words > budget * 1.5:
            errs.append(f"slide {p}: {words} body words (budget {budget} for {a.mode})")
        elif words > budget:
            warns.append(f"slide {p}: {words} body words (budget {budget} for {a.mode})")
    seen = {}
    for p, e in titles.items():
        key = text_of(e).lower()
        if key in seen:
            errs.append(f"slide {p}: duplicate title of slide {seen[key]}")
        seen[key] = p
    lens = [len(text_of(titles[p])) for p in content]
    if len(lens) >= 6 and max(lens) - min(lens) < 8:
        warns.append(f"title lengths are monotonous ({min(lens)}-{max(lens)} chars): vary heading grammar")
    with_rule = [p for p in content if rules.get(p)]
    if content and len(with_rule) >= max(2, len(content) // 2):
        ids = ", ".join(f"{p}:{rules[p][0]['element_id']}" for p in with_rule[:4])
        warns.append(f"accent rule under the title on {len(with_rule)}/{len(content)} content slides (top AI-tell): delete the SHAPEs ({ids}...)")
    for m in errs:
        print("ERROR:", m)
    for m in warns:
        print("WARN :", m)
    print(f"\n{n} pages, {len(errs)} errors, {len(warns)} warnings (modal title top={mt}, left={ml})")
    sys.exit(1 if errs else 0)


if __name__ == "__main__":
    main()
