# 11 - Native PPTX -> Canva (when Canva MCP cannot generate or edit)

Use when **both** `create-design` (credit quota) and `start-editing-transaction` (503) are down and the user still needs a deck now. Verified end to end on 2026-11-07 with a 20-slide Vietnamese deck. The PPTX is then **imported into Canva by the official Connect REST import API through the Canva CLI** (section below), producing a real Canva design with native, editable text and shapes, without AI credits.

## The official import route (verified 2026-11-07)

Docs: Connect/REST `POST /v1/imports` ("Create design import job", octet-stream body + `Import-Metadata` header, scope `design:content:write`, 20 req/min; `.pptx`, `.ppt`, `.pdf`, `.key`, `.docx`, `.xlsx`, ... listed under "Supported file types") and Canva CLI `canva api design-imports create`. Canva Help "Import PowerPoint presentations": `.pptx/.ppt/.potx`, <= 300 MB, **<= 300 slides, <= 1,400 elements and images per file**; charts, SmartArt, 3D, WordArt are ignored; font matching is best-effort; beta feature.

```sh
npx -y @canva/cli@latest login # user approves in the browser (once; token stays local)
npx -y @canva/cli@latest api users me|profile # confirm WHICH account (it can differ from the MCP account!)
npx -y @canva/cli@latest api design-imports create --file deck.pptx --title "<=50 chars" \
 --mime-type application/vnd.openxmlformats-officedocument.presentationml.presentation
npx -y @canva/cli@latest api design-imports get <jobId> # poll; success -> result.designs[0].id, page_count
npx -y @canva/cli@latest api exports create --design-id <id> --format png --format-width 960 --format-height 540
npx -y @canva/cli@latest api exports get <jobId> # per-page review images
npx -y @canva/cli@latest api exports create --design-id <id> --format pdf # text layer: run verify_text.py on it
```

The MCP `import-design-from-url` needs a public URL and forbids local/generated files; the MCP has no local-file import. The CLI/REST route is the supported one. The imported design lands in the account the CLI is logged into. **Verified 2026-11-07: it is the same account as the MCP** - `api users me` reports `team_user.user_id`/`team_id` (a different id namespace), yet MCP `get-design` and `get-design-content` read the imported design immediately (owner ids match the MCP account). So after a CLI import you can go straight back to MCP tools for text/diff/export.

### What Canva's importer keeps and drops (observed)
- Keeps: text boxes (as real text; Canva's own PDF export contained every planned string), rectangles, preset arrows/ovals, **filled** freeform polygons, pictures, slide background.
- Drops: **shape-internal text insets** (text sits flush at the shape edge) and **paragraph spacing** (`space_after`) -> use a separate text box per paragraph over a plain shape.
- Flattens **freeform strokes to hairlines** -> draw curves as filled ribbon polygons (`ribbon()` in `build_deck.py`).
- Never bake labels into PNGs: user needs editable text. Only pure artwork (engravings) may stay as pictures; say so.
- Each import creates a **new** design; there is no delete or update call (`design-imports` has none), so iterate locally and import once or twice. Old imports must be deleted by the user.

## What is blocked (verified; do not try)
- MCP `import-design-from-url`: its own contract forbids local/generated files and uploading them to third-party hosts to get a URL. Never host the deck on a paste/file site to use it.
- `create-upload-url` + POST of `.pptx` -> `400 Unsupported file format PPTX` (images and PDF are the document types it names).
- No MCP tool inserts text. So the PPTX cannot be pushed into Canva by the agent.

## Pipeline
1. Plan as usual (`01`, `plan_check.py` 0 errors). Put the **textbook ledger** next to it: each slide -> source page (`nguon-doi-chieu.md`). Printed page = PDF page - 1 in the Vietnamese textbook used; check per book.
2. Art: omp `generate_image` (`06` s.5), one subject per call, then `templates/pptx-fallback/prep_assets.py` turns parchment JPGs into **ink-only RGBA PNGs** (local background estimate via `maximum_filter`+`gaussian`, alpha floor 30-40 to kill paper speckle, crop 14% inward to drop plate marks) so art sits on the slide background without yellow rectangles. View every PNG.
3. Diagrams: native shapes (rectangles, `MSO_SHAPE.RIGHT_ARROW`/`DOWN_ARROW`, freeform polylines) so Canva imports editable objects; only the spiral stays a PNG (`diagrams.py spiral`, `label_x` >= 600 on a 1100 px canvas or the longest label clips).
4. Build with `templates/pptx-fallback/build_deck.py` (python-pptx, 1920x1080 px = 13.333x7.5 in, 1 px = 6350 EMU = 0.5 pt, **Arial** so Canva maps the font). Every text box height is **measured with Arial metrics in PIL** and written to `build/layout.json` in richtexts shape so `scripts/deck_audit.py` runs on it. Rules that mattered: cards take height from content; sibling cards share heading-line count; title top 76, left 130; footer 24 px.
5. Render with the real engine: `templates/pptx-fallback/render.sh` (PowerPoint via `osascript`, then PyMuPDF to PNG, then `contact_sheet.py`). Gotchas: `save ... as save as PDF` needs a **`POSIX file` object** (a plain string silently writes nothing); PowerPoint is sandboxed, so write to the project folder through that object, never read from `~/Library/Containers/...` (EPERM); the `read` tool caches images by path, so write review images under a **new filename** each time.
6. Verify: `templates/pptx-fallback/verify_text.py` extracts the **rendered PDF text** and checks every planned title, point and label (whitespace/punctuation normalised) and lists rendered lines the plan does not cover. Text inside PNGs (spiral labels) is checked by eye.
7. Import with the CLI (above), export PNG + PDF from the imported design, rerun `verify_text.py` on Canva's PDF, view the sheet. Hand off: Canva edit link (`https://www.canva.com/design/<id>/edit`), `deck.pptx`, `deck.pdf`, ledger, plan, assets.

## Pitfalls found
- **Never use NBSP to avoid orphan words**: PowerPoint's PDF text layer fuses the neighbours ("phủđịnh"), breaking search and copy. Fix wraps by width/size or an explicit paragraph break.
- Measure with a **0.98 safety factor**; PowerPoint fitted a 1644 px line in a 1660 px box that Canva might wrap, so design for the wrapped height.
- Word budgets: textbook-faithful definitions break the talk budget (<=40). Keep the exact wording, mark the exception in the ledger, do not paraphrase to satisfy a lint.
- Check every example for **source status**: textbook example vs "minh hoạ ngoài giáo trình"; label the latter inside the slide.

## Making the design public (no API; UI only - verified 2026-11-07)

Neither the Connect API nor the MCP has a share/publish operation (`canva api` groups: analytics, assets, autofill, brand-templates, comments, design-imports, designs, exports, folders, generations, image-transformations, merges, resizes, users, webhooks). Do it in the editor UI (browser-skill / bsk): open `/design/<id>/edit` -> **Share** -> **Access level** = "Anyone with the link" -> **Link sharing permission** = "Can view" (default is "Can edit") -> **Copy link**. The copied value is a `https://canva.link/<token>` short link.

Verification facts: the short link and the tokenised path `/design/<id>/<token>/view` open as a **guest** (no sign-in), while the bare `/design/<id>/view` or `/edit` still redirect to `/login`. So hand over the **short link**, never the bare URL. Test the link in a signed-out browser tab before delivering; "Anyone with the link" also exposes the design to anyone the link is forwarded to, so confirm with the user first.

## Proving the design is natively editable (round-trip test, verified 2026-11-07)

Do not guess from screenshots. `canva api exports create --design-id <id> --format pptx`, download, then parse with python-pptx and count `MSO_SHAPE_TYPE`: a native import returns `TEXT_BOX` per text block and `FREEFORM`/`GROUP` for shapes, never one picture per slide. Observed for the 20-slide deck: 199 text boxes, 99 groups, 7 freeforms, 0 pictures per page; fonts came back as `Arial`/`Arial Bold` with sizes preserved relative to the canvas (Canva canvas 1440x810 pt = 20x11.25 in; pt = design px * 0.75, so a 52 px title exports as 39 pt). A PDF export also let us read the text layer to confirm every planned string is real text.

## Updating a deck WITHOUT changing its link (verified 2026-11-07)

Official docs: [Create design merge job](https://www.canva.dev/docs/apps/rest-apis/reference/merges/create-design-merge-job/) (`POST /v1/merges`, preview) takes `type: "modify_existing_design"` + `design_id` and applies `insert_pages` / `move_pages` / `delete_pages` to that design; "When the job completes successfully, the job result includes metadata for the created or updated design" (docs). Scopes `design:content:write` + `design:meta:read`, 100 req/min. **Only one operation per request is supported by default** - multiple operations in one call fail unless Canva enables multi-operation mode. So a page replacement is two jobs:

```sh
# 1) import the new version -> NEW source design id (import always creates a new design)
canva api design-imports create --file deck.pptx --title "..." --mime-type ...pptx
# 2) copy the new pages into the EXISTING design (design id and link stay)
canva api merges create --type modify_existing_design --design-id <TARGET> \
 --operations '[{"type":"insert_pages","source":{"type":"design","design_id":"<NEW>","page_numbers":[1..N]},"after_page_number":0}]'
# 3) delete the old pages, now shifted to N+1 .. 2N
canva api merges create --type modify_existing_design --design-id <TARGET> \
 --operations '[{"type":"delete_pages","page_numbers":[N+1..2N]}]'
canva api merges get <jobId> # poll each job
```

One mode by default (`scripts/update_canva_deck.sh`) - per page, because decks are usually shared:
- `<TARGET_ID> deck.pptx "title" --pages "5,7,12-14"` - replaces **only those 1-based pages**, one insert+delete pair per page. Page count stays constant, so numbering does not drift.
- `<TARGET_ID> deck.pptx "title" --all` - replaces **every** page; only for a deck nobody else edits (wipes manual edits).
- No flag -> the script **refuses to run** (`exit 2`). Never default to an all-pages replace on a shared design.

**Shared-deck rule (collaboration).** If other people edit the same Canva design, never run the all-pages mode: it replaces pages wholesale and destroys their manual edits on every page. Default to `--pages` with only the slides you actually rebuilt, and confirm the page numbers with the user first (they shift when someone adds or deletes a page). A replaced page loses any manual edit made on that page in Canva, so either leave those pages alone or pull the current state back into the build first (export the design as PPTX, rebuild locally from it, then replace only your pages).

Verified 2026-11-07 on the throwaway: replacing page 5 of a 20-page design changed **only** page 5 (1,266 pixels), all other 19 pages exported pixel-identical, and the marker text existed only on page 5.

Verified end to end on a throwaway (`DAHaQreBJVw`): 1 page -> replace with a 20-page PPTX -> `page_count` 20, **same design id**; then a second replacement while the design was shared -> 40 pages -> delete 21-40 -> 20 pages, **same id and the same `canva.link` short link still opened signed-out, 20 pages**. So a full page replacement does NOT change the link and does NOT reset link sharing. Deleting is permanent and there is no undo; every update also leaves one temporary import design behind (no delete API - ask the user to delete it).

