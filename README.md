# ai-skills-canva

Agent skills for building and maintaining **Canva** presentations, verified against the live Canva MCP server (`https://api.canva.com/connect/v1/mcp`) and the Canva Connect REST APIs.

| Skill | What it does |
|---|---|
| [`skills/canva-slides`](skills/canva-slides/SKILL.md) | End-to-end deck workflow: intake → narrative plan → generate (Canva AI) or build natively → verify text against the plan → look at every rendered page → repair typography/alignment → diagrams → export → import/update in Canva. Vietnamese coursework, lectures, thesis defence and team decks are first-class. |

## Why this exists

Most "make me a deck" skills assume the generation call works and that the returned deck can be fixed afterwards. Both assumptions fail in practice: the AI-credit allowance runs out, `start-editing-transaction` can return 503 for hours, and a generated deck cannot be repaired structurally (no operation inserts a text box). This skill encodes the limits it actually hit, keeps a slide-to-source ledger for textbook-faithful decks, and has a fallback that does not depend on Canva AI at all: build a native editable PPTX locally and import it with the official CLI/REST import.

## Install

**omp** (managed skill):

```sh
cp -R skills/canva-slides ~/.omp/agent/managed-skills/canva-slides
```

**Any other agent that reads `SKILL.md`** (Claude Code, Codex, etc.): copy `skills/canva-slides` into that agent's skills directory. `SKILL.md` is the router; `references/` holds one file per phase and is loaded on demand.

## Requirements

- A Canva account. Two access paths, either is enough to start:
  - **MCP** — a Canva Developer app mounted as `canva` in your MCP client (`https://api.canva.com/connect/v1/mcp`, static OAuth).
  - **Canva CLI** — `npx -y @canva/cli@latest` with Node ≥ 24, then `canva login` (needed for local-file import, export and in-place updates).
- Python 3 with `pillow` (art/diagram/QA scripts), optionally `python-pptx`, `pymupdf`, `numpy`, `scipy` for the PPTX fallback.
- macOS + Microsoft PowerPoint only for the `templates/pptx-fallback/render.sh` fidelity render; the MCP workflow is platform independent.

## Quick start

```sh
# 1. plan (fails the lint until the deck is coherent)
python3 scripts/plan_check.py plan.json --ghost

# 2. generate with Canva AI (needs credits) …
#    or build a native editable PPTX and import it (no credits)
npx -y @canva/cli@latest api design-imports create --file deck.pptx --title "My deck" \
  --mime-type application/vnd.openxmlformats-officedocument.presentationml.presentation

# 3. later updates keep the same design id, link and sharing settings
scripts/update_canva_deck.sh <TARGET_ID> deck.pptx "tmp import" --pages "5,7,12"
```

`--pages` is the default because decks are usually shared: only the pages you list are replaced, and any manual edit on the other pages survives. `--all` exists for decks nobody else touches.

## Hard-won facts encoded here

- `create-design` and `generate-image` spend the account's monthly **AI allowance** (Premium AI tools); on Free ≈ 20 uses/month, reset 00:00 UTC on the 1st. The failure is synchronous `quota_exceeded`, not a rate limit.
- `start-editing-transaction` can 503 for hours while reads, `copy-design`, `merge-designs`, `export-design`, uploads and the CLI all keep working. Degrade by capability, not all-or-nothing.
- Canva's PPTX importer drops shape text insets and paragraph spacing and flattens freeform strokes. Build with one text box per paragraph, plain shapes plus separate text, and filled polygons for curves.
- `POST /v1/merges` with `modify_existing_design` edits pages **in place**: design id, link and public sharing survive; one operation per request by default.
- No API can share a design publicly or delete a design; both are UI-only.

Full verification log, per-item sources and the decision log: [`skills/canva-slides/SOURCES.md`](skills/canva-slides/SOURCES.md).

## Repo layout

```
skills/canva-slides/
  SKILL.md              router: 10 rules, phases, shortcuts, tool list, script index
  SOURCES.md            provenance, conflict decisions, dated verification log
  references/00..11     one file per phase (plan, generation, visual system, QA, editing,
                        structure/assets, delivery, brand, education playbooks, quirks, PPTX)
  scripts/              plan_check, text_diff, deck_audit, fit_check, contrast, diagrams,
                        contact_sheet, post_upload, update_canva_deck
  templates/            plan.json, brief-vi.md, deck-rules.md, speaker-notes.md,
                        pptx-fallback/ (native builder, art prep, render, text verify)
  research/             reading notes on the skills surveyed (summaries, sources cited)
```

## License

MIT for this repository's own text and code. See [LICENSE](LICENSE) and [NOTICE.md](NOTICE.md) for third-party attribution.
