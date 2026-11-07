#!/usr/bin/env python3
"""Compare the plan you sent to create-design with the text Canva actually produced.

create-design PARAPHRASES outline text and has been seen swapping doctrinal terms
(e.g. 'Phổ biến' became 'Phát triển'). Run this after every generation.

Usage: python3 text_diff.py plan.json generated.txt [threshold=0.82]
generated.txt: the `text` returned by get-design-content (one slide's elements are
separated by newlines), or the joined regions of start-editing-transaction richtexts.
Reports each planned title/point as OK, PARAPHRASED (best match shown) or MISSING, plus
terms that appear in the plan but nowhere in the generated text.
"""
import difflib
import json
import re
import sys
import unicodedata
from pathlib import Path


def norm(s):
    s = unicodedata.normalize("NFC", s).lower()
    return re.sub(r"[^\w\s]", " ", s).strip()


def best(needle, lines):
    """Best fuzzy match over single lines and 2-3 consecutive lines (Canva splits one planned
    bullet across text runs/elements). Returns (score, matched text). Exact containment = 1.0;
    otherwise max(sequence ratio, 0.95 * token coverage) so a bullet whose words all survive in
    a merged line scores high, while a swapped term drops coverage below 1."""
    n = norm(needle)
    ntoks = set(n.split())
    cands = list(lines)
    cands += [" ".join(lines[i:i + k]) for k in (2, 3) for i in range(len(lines) - k + 1)]
    top = (0.0, "")
    for ln in cands:
        nl = norm(ln)
        if n and n in nl:
            return (1.0, ln)
        r = difflib.SequenceMatcher(None, n, nl).ratio()
        cov = len(ntoks & set(nl.split())) / max(len(ntoks), 1)
        tight = len(nl.split()) <= 2 * len(ntoks) + 3  # coverage only counts when the line is not a big merge
        sc = max(r, 0.95 * cov if (cov >= 0.85 and tight) else 0.0)
        if sc > top[0]:
            top = (sc, ln)
    return top


def main():
    if len(sys.argv) < 3:
        raise SystemExit(__doc__)
    plan = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    text = Path(sys.argv[2]).read_text(encoding="utf-8")
    thr = float(sys.argv[3]) if len(sys.argv) > 3 else 0.82
    lines = [ln for ln in text.splitlines() if ln.strip()]
    gen_words = set(norm(text).split())
    bad = 0
    for i, s in enumerate(plan["sections"], 1):
        items = [("title", s["title"])] + [("point", p) for p in s.get("points", [])]
        for kind, planned in items:
            r, got = best(planned, lines)
            if r >= 0.999:
                continue
            if r >= thr:
                print(f"slide {i} {kind}: PARAPHRASED ({r:.2f})\n   plan: {planned}\n   got : {got}")
            else:
                bad += 1
                print(f"slide {i} {kind}: MISSING ({r:.2f})\n   plan: {planned}\n   best: {got}")
    plan_words = set(w for s in plan["sections"] for w in norm(" ".join([s["title"]] + s.get("points", []))).split() if len(w) > 3)
    lost = sorted(plan_words - gen_words)
    if lost:
        print("\nterms in plan but absent from generated text (check for swapped terminology):")
        print("  " + ", ".join(lost))
    print(f"\n{bad} planned strings missing; fix with replace_text or regenerate if structure is wrong")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:
        sys.exit(1)
