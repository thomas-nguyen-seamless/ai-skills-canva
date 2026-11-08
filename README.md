<div align="center">

<img src="assets/hero.svg" alt="canva-slides — agent skill for Canva presentations" width="100%">

### Build Canva decks that survive real Canva limits

**Plan · Build · Verify · Publish** — source-faithful, fully editable, one link that never changes.

[![License: MIT](https://img.shields.io/badge/license-MIT-1F5FA8)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.1.0-1F5FA8)](skills/canva-slides/SKILL.md)
[![Skill](https://img.shields.io/badge/skills-1-1F5FA8)](#repo-layout)
[![Canva MCP + CLI](https://img.shields.io/badge/Canva-MCP%20%2B%20CLI-1F5FA8)](skills/canva-slides/references/00-preflight-and-environment.md)
[![Checked against live API](https://img.shields.io/badge/verified-live%20API-7BE0C3)](skills/canva-slides/SOURCES.md)

**English** · [中文](README.zh.md) · [Tiếng Việt](README.vi.md) · [Русский](README.ru.md) · [Français](README.fr.md) · [Español](README.es.md)

</div>

---

## Contents

- [Why this exists](#why-this-exists)
- [What you get](#what-you-get)
- [Install](#install)
- [Quick start](#quick-start)
- [How a deck is built](#how-a-deck-is-built)
- [Updating a shared deck](#updating-a-shared-deck)
- [Scripts](#scripts)
- [Repo layout](#repo-layout)
- [Limits this skill encodes](#limits-this-skill-encodes)
- [License](#license)

## Why this exists

Most "make me a deck" skills assume two things that are routinely false:

1. **The AI generation call works.** It does not when the account's monthly AI allowance is spent — `create-design` then fails synchronously with `quota_exceeded`, and no amount of retrying helps.
2. **A generated deck can be fixed afterwards.** It cannot be repaired structurally: no Canva editing operation inserts a text box, and the editing service itself can return `503` for hours.

This skill encodes what actually held up under live testing: a plan gate before any pixel is drawn, a text diff against the source, a look at **every** rendered page, and a fallback that needs no Canva AI at all — build a native, editable PPTX locally and import it through the official Canva REST import.

## What you get

- **Design intake first** — before building, a tailored questionnaire generated from the topic (theme, density, visual language, imagery, citations, special slides); the answers are recorded in the plan and the linter blocks the build until they exist.
- **Narrative plan first** — spine, mode (presenter / talk / document), per-slide action titles, word budgets, example coverage; a linter blocks a bad structure before generation.
- **Source-faithful decks** — a slide-to-page ledger (`nguon-doi-chieu.md`) for textbook or PDF-based work; examples outside the source are labelled on the slide.
- **Visual system, not vibes** — px type scale for 1920×1080, one accent, grid and margins, an explicit anti-slop veto list, native diagrams.
- **Proof, not promises** — text diff against the plan, per-page render, contact sheet, measured layout audit (drift, overflow, overlap, safe zones).
- **Same link forever** — page-level replacement through `POST /v1/merges`; design id, link and public sharing survive updates.
- **Native, editable output** — real text boxes and vector shapes in Canva, never slide-sized images.
- **Graceful degradation** — MCP → CLI/REST → local PPTX, chosen by what actually works right now.
- **Vietnamese-first** — diacritics, wrap prediction, classroom type sizes, coursework playbooks.

## Install

```bash
# omp managed skills
cp -R skills/canva-slides ~/.omp/agent/managed-skills/canva-slides

# any agent that reads SKILL.md (Claude Code, Codex, …)
git clone https://github.com/thomas-nguyen-seamless/ai-skills-canva
cp -R ai-skills-canva/skills/canva-slides <your-skills-dir>/
```

Then let the skill prepare the machine:

```bash
skills/canva-slides/scripts/bootstrap.sh # asks once per missing tool
skills/canva-slides/scripts/bootstrap.sh --check # report only, install nothing
```

`bootstrap.sh` **only installs what is missing** — present tools are reported as `[ok] … (already installed, skipped)` and are never reinstalled. It then checks the two things it cannot do for you: the Canva CLI login and the MCP mount.

| Checked | If already present | If missing |
|---|---|---|
| `uv`, `python3`, `git`, `node ≥ 22`, `npx` | reported, untouched | installed via Homebrew (or the official installer for `uv`) |
| Canva CLI | reported, not re-fetched | fetched once through `npx` (cached, no global install) |
| Python libs (`pillow`, `numpy`, `scipy`, `python-pptx`, `lxml`, `pymupdf`, `pypdf`) | import test passes → skipped | pre-warmed into the uv cache |
| Canva CLI login | account name printed | `canva login`, **you approve in the browser** |
| MCP `canva` mount | confirmed in `mcp.json` | snippet printed; config never overwritten |

## Quick start

**New deck**

```text
/skill:canva-slides make a 20-slide deck on "law of the negation of the negation"
from @triethocmaclenin.pdf — 15 minutes, Vietnamese, large type for a lecture hall
```

**Edit an existing deck, keep the link**

```bash
scripts/update_canva_deck.sh DAHaPZNNOhs deck.pptx "tmp import" --pages "5,9"
```

**Review only, change nothing**

```text
/skill:canva-slides review this Canva deck: https://canva.link/… — score it, list defects
```

## How a deck is built

<div align="center"><img src="assets/workflow.svg" alt="Plan, build, verify, publish, export" width="100%"></div>

| # | Phase | Gate before moving on |
|---|---|---|
| 1 | **Plan** — intake, source ledger, terminology, per-slide record, examples | `plan_check.py --ghost` reports **0 errors** |
| 2 | **Build** — Canva AI (`create-design`) *or* native PPTX in Arial, measured text | page count equals the plan |
| 3 | **Verify** — text diff, per-page render, layout audit, contrast | every planned string present, no hard fail open |
| 4 | **Publish** — import once, then page-level updates on the same design | page count matches, link and sharing intact |
| 5 | **Export** — PDF/PPTX, page count verified, notes as a sidecar file | definition of done ticked |

## Updating a shared deck

The default is **per page**, because decks usually have more than one author:

```bash
scripts/update_canva_deck.sh <ID> deck.pptx "tmp" --pages "5,7,12-14" # only these pages change
scripts/update_canva_deck.sh <ID> deck.pptx "tmp" --all # every page (solo decks only)
scripts/update_canva_deck.sh <ID> deck.pptx "tmp" # refuses to run
```

Two merge jobs per page (insert + delete) keep the page count constant, so numbering never drifts while you work. Verified on a 20-page design: replacing page 5 changed **only** page 5 (1,266 px), the other 19 pages exported pixel-identical, and the design id, short link and `Can view` sharing all stayed the same.

> A replaced page is a fresh page from your local build, so manual Canva edits **on that page** are lost. Every other page is untouched.

## Scripts

| Script | Purpose |
|---|---|
| `bootstrap.sh` | install missing prerequisites; verify login and MCP mount |
| `intake_prompt.py` | tailored pre-build questionnaire derived from the topic |
| `plan_check.py` | plan linter: budgets, titles, duplicates, pace, agenda, examples, ghost-deck |
| `text_diff.py` | planned strings vs generated/imported text |
| `deck_audit.py` | measured layout audit: title drift, safe zone, overflow, overlap, accent-rule tells |
| `fit_check.py` | predict Vietnamese line wrapping and height before an edit |
| `contrast.py` | WCAG contrast for projection |
| `diagrams.py` | 8 diagram kinds rendered at final slide size |
| `contact_sheet.py` | one image of every page, labelled |
| `post_upload.sh` | single-use asset upload helper |
| `update_canva_deck.sh` | push a PPTX into an existing design, keeping id, link and sharing |
| `templates/pptx-fallback/` | native builder (`build_deck.py`), ink-only art prep, PowerPoint render, rendered-text verifier |

## Repo layout

```text
ai-skills-canva/
├── assets/ hero + workflow diagrams
├── README.md this file (EN · VI · ZH · RU · FR · ES)
└── skills/canva-slides/ the skill (one, deep)
 ├── SKILL.md router: rules, phases, shortcuts, tools, scripts
 ├── SOURCES.md provenance, conflict decisions, dated verification log
 ├── references/00…12 one file per phase
 ├── scripts/ the 10 scripts above
 ├── templates/ plan.json, brief-vi, deck-rules, speaker-notes,
 │ mcp-canva.snippet.json, pptx-fallback/
 └── research/ reading notes on the skills surveyed (sources cited)
```

## Limits this skill encodes

| Reality | What the skill does |
|---|---|
| `create-design` / `generate-image` spend the monthly **AI allowance** (`quota_exceeded`, synchronous) | stops immediately, switches to the no-credit path, reports the reset date |
| `start-editing-transaction` can return `503` for hours | degrades to reads + export + page-level merges; never claims an edit landed |
| Canva's PPTX importer drops shape insets, paragraph spacing, freeform strokes | builds one text box per paragraph, plain shapes + separate text, filled polygons for curves |
| No API shares a design publicly or deletes it | UI steps documented; never invented |
| Generated decks paraphrase and can swap doctrinal terms | text diff against the plan; fix in place, never regenerate to fix text |

Full evidence, dates and sources: [`skills/canva-slides/SOURCES.md`](skills/canva-slides/SOURCES.md).

## License

MIT — see [LICENSE](LICENSE). Third-party attribution in [NOTICE.md](NOTICE.md). Canva is a trademark of Canva Pty Ltd; this project is not affiliated with or endorsed by Canva.
