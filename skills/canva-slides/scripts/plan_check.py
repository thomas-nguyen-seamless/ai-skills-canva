#!/usr/bin/env python3
"""Lint a slide plan BEFORE calling create-design. Exit 1 when any ERROR is found.

Usage: python3 plan_check.py plan.json [--ghost]
plan.json:
{
  "title": "...", "minutes": 15, "audience": "...", "language": "vi",
  "mode": "talk",                       # presenter | talk (default) | document
  "spine": "one sentence",              # optional but WARNed when missing
  "sections": [ {"title": "...", "description": "...", "points": ["...", "..."],
                  "role": "cover|agenda|content|example|diagram|summary|closing|backup"} ]
}
`role` is optional; the first section defaults to cover and the last to closing.

Mode budgets (per content slide): presenter <= 3 points / 25 words; talk <= 4 / 40; document <= 6 / 75.
Other thresholds (see references/01-discovery-and-narrative.md and 03-visual-system.md):
  title <= 65 chars, unique, a claim not a bare topic label
  each point <= 12 words (warn >12, error >18)
  no emoji or pictographic symbols anywhere (title, points, description, labels): hard error
  pace: flag decks outside 0.7-3 min per content slide
  a deck > 6 slides wants an agenda; >= 8 slides wants >= 2 examples; always a closing slide
  at most 2 consecutive slides of the same role (rhythm); crossheads <= 2 in a row
--ghost prints the titles in order: read them alone, they must tell the argument (ghost-deck test)
"""
import json
import re
import sys
import unicodedata
from pathlib import Path

errs, warns, infos = [], [], []


# Emoji and pictographs are banned in slide content: they render as vendor-dependent colour
# glyphs, break an academic register, and cannot be restyled. Arrows, +, -, x and maths signs are fine.
EMOJI = re.compile("[\U0001F000-\U0001FAFF\u2600-\u27BF\u2B00-\u2BFF\uFE0F\u200D]")


def emoji_hits(text):
    t = (text or "").replace("\u2713", "").replace("\u2717", "").replace("\u2605", "")
    return [m.group(0) for m in EMOJI.finditer(t)]


def words(s):
    return [w for w in re.split(r"\s+", s.strip()) if w]


def norm(s):
    return unicodedata.normalize("NFC", s).lower()


MODES = {"presenter": (3, 25), "talk": (4, 40), "document": (6, 75)}


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) != 1:
        raise SystemExit(__doc__)
    ghost = "--ghost" in sys.argv
    plan = json.loads(Path(args[0]).read_text(encoding="utf-8"))
    mode = plan.get("mode", "talk")
    if mode not in MODES:
        raise SystemExit(f"mode must be one of {list(MODES)}")
    max_pts, max_words = MODES[mode]
    secs = plan["sections"]
    n = len(secs)
    minutes = plan.get("minutes")
    if not plan.get("spine"):
        warns.append("no spine sentence: if you cannot state the deck's one-sentence argument it is not ready")
    seen = {}
    content = 0
    examples = 0
    roles = []
    for i, s in enumerate(secs, 1):
        role = s.get("role") or ("cover" if i == 1 else "closing" if i == n else "content")
        roles.append(role)
        t = s["title"].strip()
        pts = s.get("points", [])
        tag = f"slide {i} [{t[:40]}]"
        for field, val in (("title", t), ("description", s.get("description", ""))):
            hits = emoji_hits(val)
            if hits:
                errs.append(f"{tag}: {field} has emoji/pictograph {''.join(hits)!r} (banned in slides)")
        for p_ in pts:
            hits = emoji_hits(p_)
            if hits:
                errs.append(f"{tag}: point has emoji/pictograph {''.join(hits)!r} (banned in slides)")
        for lb in s.get("labels", []):
            hits = emoji_hits(lb)
            if hits:
                errs.append(f"{tag}: label has emoji/pictograph {''.join(hits)!r} (banned in slides)")
        if len(t) > 65:
            errs.append(f"{tag}: title is {len(t)} chars (max 65)")
        key = norm(t)
        if key in seen:
            errs.append(f"{tag}: duplicate title of slide {seen[key]}")
        seen[key] = i
        if role not in ("cover", "closing", "agenda", "divider", "backup"):
            content += 1
            if role == "example" or norm(t).startswith(("ví dụ", "example", "case")):
                examples += 1
            if not pts and not s.get("description"):
                errs.append(f"{tag}: title-only slide")
            if len(pts) > max_pts:
                errs.append(f"{tag}: {len(pts)} points (max {max_pts} in {mode} mode)")
            if role in ("content", "definition") and 0 < len(pts) < 2 and not s.get("description"):
                warns.append(f"{tag}: only {len(pts)} point; merge with a neighbour or add the example")
            total = 0
            for p in pts:
                wc = len(words(p))
                total += wc
                if wc > 18:
                    errs.append(f"{tag}: point has {wc} words: {p[:50]!r}")
                elif wc > 12:
                    warns.append(f"{tag}: point has {wc} words (aim <= 12): {p[:50]!r}")
            if total > max_words:
                errs.append(f"{tag}: {total} words of points (max {max_words} in {mode} mode)")
            if len(words(t)) <= 2 and role in ("content", "definition"):
                warns.append(f"{tag}: title looks like a topic label; state the claim instead")
        elif role in ("cover", "closing") and len(pts) > 4:
            warns.append(f"{tag}: {role} slide carries {len(pts)} points")
    if minutes:
        per = minutes / max(content, 1)
        infos.append(f"{content} content slides for {minutes} min = {per:.1f} min/slide")
        if per < 0.7:
            errs.append(f"too many slides for {minutes} min ({per:.1f} min/slide); cut to <= {int(minutes / 0.7)}")
        elif per > 3:
            warns.append(f"too few slides for {minutes} min ({per:.1f} min/slide); add examples or diagrams")
    if "agenda" not in roles and n > 6:
        warns.append("no agenda slide in a deck longer than 6 slides")
    if examples < 2 and n >= 8:
        warns.append(f"only {examples} example slide(s); lessons and defences land better with >= 2")
    if "closing" not in roles:
        errs.append("no closing slide")
    run = 1
    for i in range(1, n):
        run = run + 1 if roles[i] == roles[i - 1] and roles[i] in ("content", "diagram", "divider") else 1
        if run > 2 and roles[i] == "content":
            warns.append(f"slides {i - 1}-{i + 1}: three consecutive plain content slides; vary the form (diagram, example, table)")
            break
    if ghost:
        print("GHOST DECK (titles only):")
        for i, s in enumerate(secs, 1):
            print(f"  {i:>2}. {s['title']}")
        print()
    for tag, bucket in (("ERROR", errs), ("WARN", warns), ("INFO", infos)):
        for m in bucket:
            print(f"{tag}: {m}")
    print(f"\n{n} slides, {len(errs)} errors, {len(warns)} warnings")
    sys.exit(1 if errs else 0)


if __name__ == "__main__":
    main()
