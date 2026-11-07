"""Verify the RENDERED pdf text (what PowerPoint actually drew) against plan.json.
Every planned title, point and diagram label must appear (whitespace/NBSP/punctuation-normalised).
Reports planned strings missing from the PDF, and PDF lines not covered by the plan (for review)."""
import json, re, sys, unicodedata
import pymupdf
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
plan = json.loads((ROOT / "plan.json").read_text(encoding="utf-8"))
doc = pymupdf.open(ROOT / "build" / "render.pdf")

def norm(t):
    t = unicodedata.normalize("NFC", t).replace("\u00a0", " ")
    t = re.sub(r"[:;,.\-–—·]", " ", t)
    return re.sub(r"\s+", " ", t).strip().lower()

missing, extra = [], []
for i, (sec, page) in enumerate(zip(plan["sections"], doc), 1):
    pdf = norm(page.get_text())
    want = [("title", sec["title"])] + [("point", p) for p in sec["points"]] + [("label", l) for l in sec.get("labels", [])]
    for kind, w in want:
        if norm(w) not in pdf:
            # headings/bodies are separate boxes: accept if both halves are present
            parts = [x for x in re.split(r": ", w, maxsplit=1)]
            if len(parts) == 2 and all(norm(x) in pdf for x in parts):
                continue
            missing.append((i, kind, w))
    covered = norm(" ".join([sec["title"]] + sec["points"] + sec.get("labels", []) + ["quy luật phủ định của phủ định", str(i)]))
    for line in page.get_text().splitlines():
        n = norm(line)
        if n and n not in covered:
            extra.append((i, line.strip()))
print("planned strings missing from the rendered PDF:", len(missing))
for m in missing: print("  MISSING", m)
print("rendered lines not covered by the plan (review):", len(extra))
for e in extra: print("  EXTRA  ", e)
sys.exit(1 if missing else 0)
