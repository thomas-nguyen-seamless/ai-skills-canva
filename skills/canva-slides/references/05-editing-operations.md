# 05 - Editing operations (transactions, ops cookbook, passes)

Everything here was verified against the mounted Canva MCP (Connect endpoint) on 2026-11-06/07 unless marked `[UNVERIFIED]`.
Sources merged: official `edit-design`, `implement-feedback`, `presentation-time-fitting` (canva-sdks, Apache-2.0); 10x
`canva-presentation` preservation rules; design-director transaction discipline; our own live tests.

## 1. Pick the editing mode first

| Mode | Allowed | Typical trigger | Ends with |
|---|---|---|---|
| **Inspect** | open transaction, read, `get-design-thumbnail`, then **cancel** | "check my deck" | review report |
| **Surgical edit** (default) | `replace_text`, `find_and_replace_text`, `update_title`, minimal `position_element` | fix a typo, change a term | thumbnail review of touched pages |
| **Declared pass** | adds `format_text`, `resize_element`, `position_element`, `insert_fill`, `update_fill`, `delete_element` | "font bự hơn", "đổi sơ đồ", "căn lại" | **full-deck** thumbnail review |
| **Structure** | `merge-designs`, `copy-design`, `resize-design` (not a transaction) | add / move / delete slides | read titles back, then review |

The official "never restyle what was not asked" rule (10x `canva-presentation`: no unrequested font size, colour, alignment, position or background
change; never add elements) is the **default**. A user request that names a pass ("font bigger", "redo the diagram", "align everything") is the
explicit unlock. Say which pass you are running before you start it.

## 2. Backup before any multi-page change

There is **no delete-design tool and no undo after commit**. Before a declared pass or a batch that touches more than ~3 pages:

1. `copy-design { design_id }` -> new design (the backup). Title it with a suffix such as `- backup 2026-11-07` only if you can rename later (rename = `update_title` in a transaction on the copy).
2. Tell the user the backup id and link.
3. Work on the original (the user's link keeps working) unless the user asked for a rebuild, in which case **build a new design and leave the original untouched** (verified workflow: original `DAHaJXAHeDY` stayed untouched while the rebuild lived in a new design).

## 3. The transaction protocol

```
start-editing-transaction {design_id}
  -> transaction {transaction_id, status:"open"}, edit_design_url, richtexts[], fills[], pages[], thumbnails[1]
perform-editing-operations {transaction_id, operations[], page_index, pages}   (repeatable, batched)
get-design-thumbnail {transaction_id, page_index}                              (one page per call; SHOW every image you fetch)
commit-editing-transaction {transaction_id}   |   cancel-editing-transaction {transaction_id}
```

Rules:

- **Open the transaction early** (before long thinking) and keep **one** open at a time. Long gaps raise timeouts (official `presentation-time-fitting`).
- Pass the `pages` array from the **latest** response and the 1-based `page_index` of the first page you change. Multiple pages in one call are fine.
- `start-editing-transaction` returns **one thumbnail only** (page 1). Every other page needs `get-design-thumbnail {transaction_id, page_index}`. `get-design-pages` also fills a real thumbnail for page 1 only. Batch the per-page thumbnail calls inside one transaction, then cancel (read-only) or commit.
- After commit or cancel the id is dead. A failed commit loses the whole draft: start over.
- An abandoned transaction is harmless but untidy: cancel it and say so.
- Rate budget (TerminalSkills table, per user per minute): start 20, perform 50, commit 20, cancel 20, thumbnails 100, copy 20. A 16-slide pass is 1 transaction + 1 perform call + 16 thumbnails + 1 commit. A single call with ~75 operations succeeded here, but a failed op in a huge batch is hard to localise: for risky batches use 15-20 ops per call and verify geometry between calls (academic-poster rule).

### Approval gate (resolving the official contradiction)

`edit-design` demands approval before every commit; `implement-feedback` forbids asking twice. Resolution used here:

- **Default**: show what changed + thumbnails, ask once, commit on yes.
- **Pre-authorised batch**: when the user's request already names the whole job ("làm lại toàn bộ slide", "font bự hơn trên tất cả"), that request **is** the approval. Verify by thumbnails, commit, then report. Never ask "shall I commit?" afterwards (implement-feedback rule).
- **Always ask** when the change is destructive or irreversible: `delete_pages`, deleting groups of elements, `find_and_replace_text` whose string can match several places, anything on a design the user did not create.
- Never say "saved" before `commit` returned success.

## 4. Reading a transaction payload

```
richtexts[]  {page_index, element_id, regions[{type:"character", text}], containerElement{type:"TEXT"|"SHAPE", position{top,left}, dimension{width,height}}}
fills[]      {type:"image", asset_id, page_index, editable, alt_text?, containerElement{type:"RECT", position, dimension}, element_id}
pages[]      {page_id, page_number, dimension{1920x1080}, is_responsive, is_empty, is_editable}
```

- Group a page's elements by `page_index`; sort by `position.top` then `left` to see the reading order and the grid.
- A SHAPE with `regions: []` is decoration (rule, card, bar); a SHAPE **with** regions is a box with text (diagram node). A TEXT is free text.
- `regions` are text **runs**. Never join them naively: a run may end with `\n`, and joining fuses words ("patternfor"). Read raw runs before reporting a typo.
- Ids: `pageId-groupId-childId` for grouped elements. See section 6 for the delete trap.
- **Evidence rule** (official `get-design-feedback`): colours and font families are **not** in the payload. Never state a hex or font name as fact; judge colour from the thumbnail and say "appears". Position, size and text are reliable.
- `fills[].editable:false` means the asset is a locked part of the theme (frame art, rails); do not plan around replacing it.

## 5. Operations cookbook

All coordinates are slide pixels (1920x1080). `top`/`left` are relative to the page.

```json
{ "type": "replace_text", "element_id": "...", "text": "line 1\nline 2" }
{ "type": "find_and_replace_text", "element_id": "...", "find_text": "phát triển", "replace_text": "phổ biến" }
{ "type": "format_text", "element_id": "...", "formatting": { "font_size": 38, "font_weight": "bold", "text_align": "start", "color": "#0F2740", "line_height": 1.3 } }
{ "type": "position_element", "element_id": "...", "top": 380, "left": 130 }
{ "type": "resize_element", "element_id": "...", "width": 1500 }                       // TEXT: never pass height (auto)
{ "type": "insert_fill", "page_id": "PB...", "asset_type": "image", "asset_id": "MA...", "alt_text": "...", "top": 230, "left": 140, "width": 1600, "height": 760 }
{ "type": "update_fill", "element_id": "...", "asset_type": "image", "asset_id": "MA...", "alt_text": "..." }
{ "type": "delete_element", "element_id": "pageId-groupId" }                           // GROUP id, see below
{ "type": "update_title", "title": "..." }
```

Behaviour notes:

- `replace_text` replaces the whole element's text; `\n` makes a new line, which is how a label becomes two lines. On the single-style boxes used in this session the existing formatting was kept. **For mixed-style text** (a headline with a coloured span) prefer `find_and_replace_text`, which preserves per-run formatting, because another source reports that `replace_text` flattens the element to one style (carousel-builder; `[U]` not re-tested here). `format_text` always applies to the **whole element**: a single word cannot be recoloured.
- `format_text.font_size` is **absolute px** (1-800), also on grouped child ids. There is **no font-family** option: consistency comes from scale, weight, alignment and colour only.
- `format_text` knobs: font_size, text_align (start|center|end), color, font_weight (normal|bold), font_style, decoration, strikethrough, link, list_level, list_marker, line_height (0.5-2.5).
- Enlarging text grows the box downward; shrinking leaves the box. After a size change **re-position** anything beneath (verified: slide 3 definition block needed `position_element` after 44 -> 52 px).
- `insert_fill` lands **above** everything already on the page. That is how an opaque, background-coloured image covers leftover decoration that cannot be deleted (arrows, lines are not enumerated).
- `insert_fill` needs `alt_text`; this is the only place alt text can be written. No operation writes alt text on existing fills.
- `update_autofill_field` works on fixed-page designs only and is for brand-template tagging; ignore it for decks.

## 6. Group ids and un-deletable decoration

- `delete_element` on a **child id** inside a group reports success and does **nothing**. Pass the common prefix `pageId-groupId` (the first two dash-separated parts) to delete the whole group, then verify by re-reading `richtexts` that the labels are gone **before** committing.
- Decorative lines/arrows may not appear in `richtexts` or `fills` at all, so they cannot be targeted. Cover them with an opaque `insert_fill` PNG whose background equals the slide colour (sample the thumbnail, e.g. `#F7F8FA`).
- If a whole page is structurally wrong, cancel and rebuild the page via `copy-design` of a good slide plus `merge-designs`, not by patching (design-director: cancel the transaction when the layout is structurally compromised).

## 7. Typography pass (the "font bigger" job)

1. Declare the pass and the target scale (see `03-visual-system.md`): slide title 52, section label 40-44, card title 38-44, body 34-38, caption/support 30-34 on a 1920x1080 slide. Never go below 30 px for anything that must be read, and avoid a 3rd weight.
2. Build ONE batch of `format_text` ops keyed by role (title / card title / body / caption), not by page; roles keep the deck consistent.
3. Estimate wrap before sending (heuristic, calibrate against the first render): chars per line ~= `box_width / (0.53 * font_px)` for regular Vietnamese text and `/ (0.56 * font_px)` for bold; lines x `font_px` x 1.3 must fit the space before the next element.
4. Where a box is too narrow, `resize_element` width (never height on TEXT) or shorten the text with `replace_text`; do **not** shrink below the floor.
5. Where a connector label or card title wraps unevenly across siblings, force the same line count on all siblings (`\n`), or put all siblings on one line by shortening.
6. Commit, then **render every page** (not just the ones you touched) and build a contact sheet (`scripts/contact_sheet.py`). Typical regressions: connector label clipped by a neighbour box, one card title wrapping, a number badge drifting off its circle, a bottom half left empty after the block grew.
7. A second pass is normal. Expect 2 rounds for a 15-slide deck.

## 8. Alignment and spacing edits

- Fix a **grid once** (see `03-visual-system.md`): left margin 130, title top 76, accent rule top 176 and width 90, content starts >= 290, right margin 130, 8-px spacing step. Any element whose `left` or `top` differs from its siblings by more than ~6 px is an alignment bug: compute the target from the majority and `position_element` it.
- Vertically balance sparse slides by moving the whole block, not one element (definition slide: three elements moved together, 380 / 640 / 712).
- Do not centre-align everything: left-aligned text with a consistent left edge reads as designed.

## 9. Responsive pages

`pages[].is_responsive == true` allows only `update_title`, `replace_text`, `update_fill`, `delete_element`, `find_and_replace_text`. Check before every `perform-editing-operations`; if a requested op is outside the set, do not call, say so, and offer: (a) `replace_text` only, (b) rebuild the page by `copy-design` of a fixed-page slide, (c) manual step for the user. Decks produced by `create-design` have been fixed-page (`is_responsive:false`) in all tests.

## 10. Failure ladder

1. `start-editing-transaction` fails with a 503 / "Failed to load design manipulation output" / timeout: **retry once after 15-30 s**. Earlier (2026-11-06) the 503 cleared by itself; on 2026-11-07 it **persisted for 35+ minutes across two designs and ~8 attempts** while read tools, `copy-design`, `merge-designs` and `export-design` kept working, so it is not a scope or design problem and may not be short-lived. After the second failure stop hammering it: switch to read-only/no-transaction work (below), tell the user, and try once more later.
2. Open the transaction earlier in the flow and keep operations in one batch.
3. Try a smaller copy (`copy-design` with a page subset) to prove the path.
4. **Work around without a transaction**: review through `export-design` PNG per page + `get-design-content`; restructure with `copy-design` + `merge-designs`; deliver PDF/PPTX. These cannot change text/format/media: for those, give the user per-slide text and exact manual steps (see the manual-changes checklist in `07-delivery.md`) and say plainly that text edits are blocked.
5. A commit that returns an error discards everything: reopen and redo. Never claim the edit landed.

## 11. Pre-commit checklist

- [ ] every touched page rendered and **looked at** (images shown to the user)
- [ ] no leftover labels from a deleted group (re-read `richtexts`)
- [ ] repeated components (cards, rows, connectors) have identical line counts and baselines
- [ ] nothing outside a 130 px left/right margin; nothing overlapping
- [ ] terminology matches the approved outline (`scripts/text_diff.py`)
- [ ] body >= 34 px, support text >= 30 px, no text under 28 px except a slide-number or source tag
- [ ] backup exists when more than ~3 pages changed
