---
name: canva-slides
license: MIT
version: 1.1.0
description: "End-to-end Canva slide-deck workflow: intake, narrative plan, create-design or native-PPTX build, official CLI import (canva api design-imports create), text-diff verification, render-and-look QA, typography/alignment passes, custom diagrams, page structure (merge/copy), export, speaker notes and Q&A. Vietnamese coursework, lecture, thesis-defence and team decks are first-class. Use for any request to make, redo, edit, review, translate, resize, import or deliver a Canva presentation."
---

# Canva Slides

Published skill: https://github.com/thomas-nguyen-seamless/ai-skills-canva (`skills/canva-slides`).

One workflow for making slides in Canva through the **mounted Canva MCP** (`https://api.canva.com/connect/v1/mcp`) and, when the MCP cannot generate or edit, through a **native PPTX imported with the official Canva CLI/REST import**. Built from ~60 GitHub skills plus live testing; every limit below was verified on this mount (see `SOURCES.md`). This file is the router and the non-negotiables. **Read the reference for the phase you are in** (index at the bottom); do not load them all.

Skill directory (this folder): `references/`, `scripts/`, `templates/`, `research/`. In omp it installs to `~/.omp/agent/managed-skills/canva-slides/`; elsewhere use the folder you copied. All script paths below are relative to it.

## The rules that matter most (setup + ten)

0. **Make the machine ready first.** New machine or a `command not found`: run `scripts/bootstrap.sh` (it installs uv, Node, the Canva CLI through npx, and the Python libs, then verifies login and the MCP mount). Never hand a "cannot run" answer back before that check.

1. **Plan before paint.** The plan (spine, mode, per-slide record, examples, terminology) exists on screen and passes `scripts/plan_check.py` before any `create-design`. Structure cannot be repaired afterwards. **Credits are finite**: `create-design` and `generate-image` are Canva AI generations ("Generate a design with Canva AI" = Premium AI tool) and draw on the account's monthly AI allowance (Free ~20 uses/month, resets 00:00 UTC on the 1st; observed `quota_exceeded` synchronously, no job id, reset 2026-12-01). Then: no-credit mode (`02` s.8), or native PPTX + CLI import (`11`).
2. **`format:"Presentation (16:9)"` + a full `outline`** (one section = one slide) on every deck. Put **every string you will ever need** in the outline: no operation inserts a text box.
3. **The generator paraphrases and can swap doctrinal terms.** After generation: page count, then `scripts/text_diff.py` against the plan. Fix in place; never regenerate to fix text. With a user source PDF the source wording wins: keep a slide-to-page ledger and label examples outside the source.
4. **Look at pixels.** Per-page thumbnails inside a transaction (or, when the transaction service is down, per-page PNG `export-design` / `canva api exports`), **show every image**, contact sheet, three-pass scan. Gates are `PASS` / `FAIL` / `NOT_RUN`.
5. **Never claim what the tools did not confirm**: saved (before `commit` returned), verified, exported, a font change, a notes write, an animation. No `font-family`, no new text boxes, no background change, no presenter-notes write, no delete-design tool.
6. **Classroom type, px on 1920x1080**: body **34-38** (floor 32), support 30-34 (floor 28), tag floor 24, slide title 52-60. <= 2 font families, 1 accent, <= 4 sizes per slide. Never shrink type to fit: cut, split, widen.
7. **Alignment is the cheapest quality signal**: left margin 130, title top 76, identical cards and line counts, 8-px spacing; audit with `scripts/deck_audit.py`.
8. **Real diagrams, many examples, all text editable**: a diagram for every mechanism; never bake labels into a PNG (the user must be able to edit in Canva). Use native shapes/filled polygons; pictures only for pure artwork. 3-4 sourced worked examples, one idea per slide, action titles. **No emoji or pictographic symbols anywhere** - titles, points, labels, captions, diagram art, notes; `plan_check.py` and `deck_audit.py` reject them.
9. **Never touch the user's original.** "Làm lại" = build a new design and hand back the new link. Multi-page edits get a `copy-design` backup first (no undo, no delete tool).
10. **Learn and record**: read `deck-rules.md` first; append every user correction (`templates/deck-rules.md`).

## Workflow (phases, gates, where to read)

| Phase | Do | Gate before moving on | Read |
|---|---|---|---|
| **0 Setup** | `scripts/bootstrap.sh` — installs uv/node/Canva CLI/python libs if missing, checks login + MCP mount; report-only with `--no-install` | readiness line printed; `exit 0` before promising anything | `references/12-setup-and-bootstrap.md` |
| **0 Pre-flight** | pick the mode; `get-logged-in-account-details`; probe credits (first `create-design` response) and the transaction service (`start-editing-transaction` + cancel); `list-brand-kits` (empty = normal); read `deck-rules.md`; decide original vs copy | mode named; account stated; capability limits stated before promising | `references/00-preflight-and-environment.md` |
| **1 Plan** | **design intake** (`intake_prompt.py`: theme, density, visual language, imagery, citations, special slides - ask 4-6 at a time with defaults); challenge-before-acting intake; source + terminology sheet; **mode token** presenter/talk/document; spine sentence; slide count from minutes; per-slide record; 3-4 examples; design stance; ghost-deck test | `plan_check.py plan.json --ghost` = 0 errors; user confirms if > 10 slides or graded | `01-discovery-and-narrative.md`, `09-education-playbooks.md`, `templates/plan.json` |
| **2 Generate** | brief from `templates/brief-vi.md` + outline = plan; `create-design`; poll `get-create-design-async-job` (>= 15 s, status `completed`); max 2 generations. **If `quota_exceeded` or transactions 503: go to `11`** | `design_id`, edit link, slide count == plan | `02-outline-and-generation.md` |
| **3 Verify** | `get-design` page count; `get-design-content` -> `text_diff.py`; transaction inspect; thumbnails per page; contact sheet | no hard fail left unlisted | `04-review-and-qa.md` s.2-3 |
| **4 Repair** | backup if > 3 pages; declared passes: terminology -> typography -> alignment -> delete AI-tell shapes; one batched transaction; commit | all touched pages re-rendered and looked at | `05-editing-operations.md`, `03-visual-system.md` |
| **5 Visuals and structure** | diagram PNG/native; clone donors with `copy-design` + retext + `merge-designs`; read titles back | page order == plan; no stale labels | `06-structure-and-assets.md` |
| **6 Review rounds** | >= 2 rounds; scored rubric; reader test; `deck_audit.py` | status `READY` or an honest `DRAFT - ...` | `04-review-and-qa.md` |
| **7 Deliver** | export PDF/PPTX, verify page count; notes file; Q&A sheet; hand-off; definition of done | DoD ticked in `07` s.8 | `07-delivery.md` |

**Native route (credits exhausted, transactions down, or exact source text required):** plan -> art (omp `generate_image`) -> `templates/pptx-fallback/build_deck.py` (native text/shapes, Arial) -> `render.sh` (PowerPoint) -> `verify_text.py` -> **`npx -y @canva/cli@latest api design-imports create --file deck.pptx --title ...`** (needs one `canva login`; poll `design-imports get`; check `api users me` for the account) -> export PNG/PDF from the imported design and re-verify text. Details, importer behaviour and limits: `references/11-native-pptx-fallback.md`.

## Shortcuts: what to do when the user says...

| User says | Do |
|---|---|
| "làm slide về X" | Phase 0 -> 1 -> 2 -> 3 -> 6 -> 7. Run `intake_prompt.py --topic "X"` and ask the 4-6 style questions (theme, density, visual language, imagery, citations) with defaults before building. With a source PDF: read it, build the ledger first. |
| "làm lại slide này" + link | read original, keep it untouched, build a **new** design from a plan that keeps every source fact, then review. |
| "font bự hơn / nhỏ quá" | declared **typography pass** (`05` s.7), render **all** pages, append to `deck-rules.md`. |
| "lệch / không đều" | `deck_audit.py` + alignment edit (`05` s.8). |
| "thêm ví dụ / thêm slide" | clone the nearest donor (`06` s.2), retext, merge, read titles back. |
| "sơ đồ / minh hoạ đẹp hơn" | native shapes / filled polygons (editable); `diagrams.py` PNG only when editing is not needed. |
| "thêm ảnh của tôi" | crop whole, upload, `insert_fill`; bookend on cover + closing. |
| "dịch / song ngữ" | `copy-design` -> one batched `replace_text` -> overflow pass (`06` s.6). |
| "xuất PDF / PPTX / notes" | `07`; notes as a **sidecar file**. |
| "đưa file PPTX/PDF lên Canva" | `canva api design-imports create` (`11`); never host the file publicly for MCP `import-design-from-url`. |
| "cập nhật deck đang có / giữ nguyên link" | `scripts/update_canva_deck.sh <id> deck.pptx "title" [--pages "5,7"]`; on a shared design use `--pages` only, never all-pages (`11`). |
| "nhận xét / chấm slide" | read-only review (`04`). |
| deck or image generation requested | try once; on `quota_exceeded` stop (no retry loop), tell the user the reset date; use `11` and the image ladder (`06` s.5; omp `generate_image` needs `generate_image.enabled`). |

## Tools (live-verified names; `user_intent` on every call)

Generate/read: `create-design`, `get-create-design-async-job`, `get-design`, `get-design-content`, `get-design-pages` (real thumbnail for page 1 only), `get-presenter-notes` (read-only), `search-designs`, `resolve-shortlink`.
Edit: `start-editing-transaction` -> `perform-editing-operations` (`replace_text`, `find_and_replace_text`, `format_text`, `position_element`, `resize_element`, `insert_fill`, `update_fill`, `delete_element`, `update_title`) -> `get-design-thumbnail` (needs `transaction_id`) -> `commit-editing-transaction` | `cancel-editing-transaction`.
Structure: `copy-design`, `merge-designs` (`insert_pages`, `move_pages`, `delete_pages`, `create_new_design`), `resize-design` (Pro), `import-design-from-url` (public URL only; forbids local/generated files).
Assets: `create-upload-url` (+ `scripts/post_upload.sh`; images/PDF, **rejects PPTX**), `upload-asset-from-url`, `generate-image` (AI allowance), `get-assets`.
Deliver: `get-export-formats`, `export-design` (credit-free; per-page PNG 960x540 is the transaction-free review path). Review: `list-comments`, `reply-to-comment`, `comment-on-design`. Brand: `list-brand-kits`, `search-brand-templates`, legacy `generate-design`. **Not mounted:** `autofill-design`, `generate-design-structured`, any notes-write.
**Canva CLI** (`npx -y @canva/cli@latest`, Node >= 24): `canva login`; `canva api users me|profile|capabilities`; `canva api design-imports create|get` (local PPTX/PDF -> editable design, scope `design:content:write`); `canva api exports create|get`; `canva api designs|assets|folders|merges|resizes|autofill ...`; `canva api describe <group> <cmd>`; `--dry-run`.
Failure domains seen 2026-11-07: **AI allowance** (`create-design`, `generate-image`) and the **editing-transaction service** (503, 35+ min) while reads, `copy-design`, `merge-designs`, `export-design`, uploads and the CLI import all worked. Matrix: `00` s.2; ladders: `05` s.10, `02` s.8, `11`.
Quirks: grouped-child `delete_element` is a silent no-op (use `pageId-groupId`); inserted fills land on top; runs fuse when joined naively; merge insert order may reverse; upload URLs are single-use. Catalogue: `10`.

## Scripts (`scripts/`; run with `uv run --with pillow python ...` where Pillow is needed)

| Script | Use |
|---|---|
| `plan_check.py plan.json [--ghost]` | lint the plan: mode budgets, title <= 65, duplicates, pace, agenda/examples/closing, ghost-deck titles |
| `text_diff.py plan.json generated.txt` | planned titles/points vs generated text |
| `deck_audit.py richtexts.json --mode talk` | title/left drift, safe zone, overlaps, bottom overflow, word budgets, accent-rule AI-tell |
| `fit_check.py "<text>" --width 440 --px 34 [--bold]` | predict Vietnamese wrap and height |
| `contrast.py FG BG [px] [bold]` | WCAG ratio; aim 7:1 |
| `diagrams.py spec.json out.png` (`--example KIND`) | PNG diagrams (labels baked: use only when not editable-critical) |
| `contact_sheet.py thumbs.tsv sheet.png [cols cell]` | one image of all pages; labels bottom-right |
| `post_upload.sh "<uploadUrl>" file.png` | single-use upload -> `{"mediaId"}` |
| `intake_prompt.py --topic "..." [--lang vi\|en]` | tailored pre-build questionnaire (style, theme, density, imagery, examples, citations) derived from the topic |
| `bootstrap.sh [--yes\|--no-install]` | installs missing uv/node/Canva CLI/python libs, checks Canva CLI login and MCP mount |
| `templates/pptx-fallback/` | `build_deck.py` (native PPTX builder with measured text), `prep_assets.py` (ink-only art), `render.sh` (PowerPoint render), `verify_text.py` (rendered/Canva PDF text vs plan) |

## Honesty and output discipline

- State capability limits **before** promising (`00` s.3). When something is impossible say it in one line, give the nearest alternative, never silently switch method.
- Show every thumbnail you fetch. Report gates as PASS / FAIL / NOT_RUN and the status `READY` / `DRAFT - FIXES REQUIRED` / `DRAFT - VERIFICATION INCOMPLETE`.
- Generated art and facts on it are **drafts** until the user checks them. Never fabricate quotes, numbers, sources; label illustrative numbers and examples outside the user's source.
- Ask only when a missing item would change the deck. Destructive operations and granting access (e.g. `canva login`) need explicit approval; a request that names the whole job approves a batch commit.
- Keep the user's folder tidy: `plan.json`, `nguon-doi-chieu.md`, assets, exports, `deck-rules.md`, backup/import ids.

## Reference index (read on demand)

| File | When |
|---|---|
| `references/00-preflight-and-environment.md` | start of any job; mode routing; capability and tool-health matrix; rate budget; MCP vs CLI |
| `references/01-discovery-and-narrative.md` | intake, sources, mode token, spine, timing, per-slide record, examples, plan gate, style stance |
| `references/02-outline-and-generation.md` | brief + outline schema, `create-design` and polling, screening, regenerate-or-repair, no-credit mode (s.8) |
| `references/03-visual-system.md` | type scale, colour, grid, density, archetypes, anti-slop, media, diagrams, accessibility |
| `references/04-review-and-qa.md` | review procedure, lenses, hard fails, scoring, transaction-free review |
| `references/05-editing-operations.md` | transactions, ops cookbook, group ids, typography pass, alignment, failure ladder |
| `references/06-structure-and-assets.md` | merge/copy, donors, diagram pipeline, image ladder (incl. omp `generate_image`), quota, translation, resize |
| `references/07-delivery.md` | export, notes, time budget, Q&A, hand-off, definition of done |
| `references/08-templates-and-brand.md` | brand kit, templates, bulk runs, terminology guard |
| `references/09-education-playbooks.md` | Vietnamese coursework, concept lecture, defence, rubric |
| `references/10-troubleshooting-and-quirks.md` | any error or odd behaviour |
| `references/12-setup-and-bootstrap.md` | new machine, missing CLI/library/module, MCP mount, login, fonts, offline machines |
| `references/11-native-pptx-fallback.md` | native PPTX -> Canva CLI import route, importer behaviour (what is kept/dropped), limits |
| `templates/` | `plan.json`, `brief-vi.md`, `deck-rules.md`, `speaker-notes.md`, `pptx-fallback/` |
| `SOURCES.md`, `research/` | provenance, decision log, verification dates, full evidence |
