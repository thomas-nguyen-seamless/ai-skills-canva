# 10 - Troubleshooting and the verified quirks catalogue

Evidence tags: **[V]** verified live on this mount (2026-11-06/07); **[S]** reported by an independent source and consistent with the tool contracts (not re-tested here);
**[U]** unverified, treat as a hypothesis. Sources: rifaterdemsahin canva-mcp notebook (105 files), canva-creator gotchas, carousel-builder, academic-poster gotcha table, canva-2 tool reference,
official skills, TerminalSkills, our own session.

## 1. Symptom -> cause -> fix

| Symptom | Likely cause | Fix |
|---|---|---|
| `start-editing-transaction` returns "Failed to load design manipulation output. Status: '503'" | upstream Canva problem **[V]**: cleared by itself on 2026-11-06; on 2026-11-07 it persisted 35+ min over two designs and ~8 attempts while `get-design-content`, `copy-design`, `merge-designs`, `export-design` worked | wait 15-30 s and retry once; stop hammering; work without a transaction (PNG export for review, `copy-design`/`merge-designs` for structure); tell the user text/format/media edits are blocked; retry later |
| `delete_element` succeeded but the label is still there | grouped child id **[V]** | delete the `pageId-groupId` prefix, then re-read `richtexts` before commit |
| Decorative line/arrow cannot be found or deleted | not enumerated as text or fill **[V]** | cover with an opaque, background-matched `insert_fill` PNG |
| Fused words like "patternfor" in `get-design-content` | text run ends with `\n` or runs are joined naively **[V]** | read raw `regions`; do not "fix" |
| Pages come back in the wrong order after `merge-designs` | insert order reversed **[V]** | read titles back, `move_pages` |
| Terminology differs from the outline | generator paraphrases and can swap terms **[V]** | `text_diff.py`, fix with `replace_text`/`find_and_replace_text` |
| Diagram came back as a scribble/garbled labels | asked the generator to draw a curve/diagram **[V]** | request a title + empty area; insert a custom PNG (`06`) |
| `create-design` or `generate-image` -> `quota_exceeded` / `credit_quota_exceeded`, `used_percentage:100`, `resets_at` | **AI-credit quota shared by both tools** **[V]** (2026-11-07: `create-design` returned the failure synchronously, no `job_id`; reset 2026-12-01 00:00 UTC) | stop retrying; no-credit mode (`02` s.8): recombine existing decks with `copy-design` + `merge-designs`; user art, local diagrams, public images |
| `export-design` PNG/PDF returns URLs | works under exhausted quota and with transactions down **[V]** (PNG 960x540 per page when `width`/`height` given) | use as the review substitute for thumbnails and for delivery |
| second POST to the same upload URL -> `403 forbidden` | single-use URL **[V]** | `create-upload-url` again |
| `create-design` card says square design | format without orientation **[V per tool doc]** | `format:"Presentation (16:9)"` |
| `get-design-pages` thumbnails empty for pages 2+ | only page 1 is filled **[V]** | per-page `get-design-thumbnail` inside a transaction |
| `get-design-thumbnail` fails or stale | needs an open `transaction_id` **[V]**; thumbnails go stale/expire **[S]** | open a transaction first; export PNG for anything durable |
| `edit_url` link stopped working | API `edit_url`/`view_url` are expiring JWT links **[S]** | store `canva.link/...` or `canva.com/design/<id>`; resolve fresh via `get-design` |
| Upload POST fails / "already used" | upload URL is single-use and short-lived **[V]** | call `create-upload-url` again; never retry a used URL |
| `insert_fill` image covers the wrong things | inserted fills land on top of existing elements **[V]** | intentional for covers; otherwise delete the old art first |
| New text appears 16 px black in the heading font | `add_text`-style flows in other MCPs **[S]**; not available here | there is no add-text op here; use existing boxes |
| `update_fill` zooms the image 1.2-4x | frame-fit behaviour **[S]** | prefer `insert_fill` (cover-fit) and delete the old; keep frame effects only if you need them |
| `resize-design` shifted blocks ~+130 px | layout reflow on resize **[S]** | re-review every page, `position_element` back |
| Free plan: `resize-design` or autofill errors | plan gate **[S]** | state the gate; do not retry |
| 403 `Missing scopes: [x]` | token lacks a scope **[S]** | disconnect and reconnect the connector to refresh the token |
| "Access Restricted by Team Admin" at consent | Canva Team setting **[S]** | team admin must allow the app (`settings/apps-and-integrations`) |
| `Missing scopes: [brandkit:read]` or `[brandtemplate:content:write]` | scope not granted **[S per tool docs]** | reconnect |
| `invalid client ID` | wrong endpoint or unpublished app **[S]** | use the right endpoint (`00`) |
| Transaction response huge | dense deck **[V]** | work from the saved JSON (`/tmp/richtexts.json`), not by re-reading output |
| Commit "succeeded" but content unchanged | wrong transaction or no ops applied **[S]** | check `updated_at > created_at` and re-read content |
| A merge/import produced fewer pages than asked | incomplete structure op **[S]** | treat as failure; page count check; redo |

## 2. Verified and reported quirks by area

### Generation
- **[V]** 1 outline section -> 1 slide; `format` with orientation required; async job status terminal is `completed`; text is paraphrased.
- **[V]** `create-design` **is** drawn from the AI-credit quota (corrected 2026-11-07; it worked on 11-06 and returned `quota_exceeded` synchronously on 11-07).
- **[S]** Over-constraining a prompt with many negatives can fail the job (`design_generation_error`). Prefer positive stance + an avoid list of <= 10 items.
- **[S]** Long decks can time out once and succeed on an identical retry.
- **[S]** `infographic` type tends to fabricate statistics instead of rendering a literal list; do not use it for decks.
- **[S]** Opening a preview in a browser may materialise a design in the account (legacy candidate flow).
- **[S]** Generated candidates often drop/duplicate/garble labels: screen **text**, not thumbnails.
- **[S]** A success job can still carry placeholders (empty image slot -> cloud-and-hills landscape): look at pixels.

### Editing
- **[V]** `format_text` px absolute; works on grouped child ids; no font family; applies to the **whole element**.
- **[S]** `find_and_replace_text` preserves per-run formatting; `replace_text` flattens a mixed-style element to one style (carousel-builder). Use `find_and_replace_text` on headlines with a coloured span; `replace_text` on single-style boxes. (Not re-tested here: the deck built in this session had single-style boxes.)
- **[S]** `update_fill` preserves frame effects (glow/shadow); delete + `insert_fill` loses them.
- **[V]** Up to ~75 operations succeeded in one `perform-editing-operations` call; academic-poster recommends <= 15 per batch to localise failure **[S]**: for risky batches use <= 15-20 and verify between.
- **[S]** `position_element`/`resize_element` only on fixed pages; check `is_responsive`.
- **[S]** Element ids exist only inside a transaction and differ per copy; never cache them across transactions.
- **[S]** Forcing a header into another column with `position_element` can orphan it from its body; use `text_align` instead.
- **[V]** Uncommitted drafts are lost; a failed commit loses all.
- **[S]** Per-op results come back in `edit_operation_results` with `status`; check the count, not just call success (not seen in this mount's responses, which return the page state).

### Structure and files
- **[V]** `merge-designs` operations are sequential and 1-based against the running state; `delete_pages` is permanent; each call needs approval of the exact operations.
- **[S]** Pages have no settable name; keep a page-name -> number map in your notes.
- **[V]** `copy-design` accepts `page_numbers`.
- **[S]** `import-design-from-url` refuses local paths and needs public HTTPS; import always creates a **new** design; PPTX groups are flattened on import; raster-backed PPTX has no editable text.
- **[S]** `upload-asset-from-url` needs a public HTTPS URL, one asset per call.

### Previews and URLs
- **[S]** `design.canva.ai` thumbnails expire in minutes; edit/view URLs from the API expire; designs made via API appear under Projects, not Home/Recents.
- **[V]** `get-design-thumbnail` needs a transaction; show every image you fetch (tool contract).

### Limits and quotas
- **[S]** Rate limits per user per minute: create/copy/start/commit/cancel/resize/export/import 20, perform 50, reads 100, upload-from-url 30, default 300; exports 75 per 5 min per document and 500 per day; second quota error -> stop and ask.
- **[S]** Free tier ~20 advanced-AI uses per month vs ~200 on Pro/EDU, reset on the 1st 00:00 UTC; probe entitlements with `list-brand-kits` (empty list is not a failure).

## 3. Operational checklists

**Before every transaction**: backup if > ~3 pages change; open it early; keep the `pages` array; plan one batch.
**After every commit**: render all pages, show images, re-run `text_diff.py` and `deck_audit.py`, confirm `updated_at`.
**When a tool errors twice**: stop, say what failed, give the manual fallback; never loop and never invent a success.
**Never**: claim a font change, a notes write, an animation, a page rename, a deletion of a design, or a verification you did not run.
