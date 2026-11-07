# 06 - Structure, archetypes, diagrams and image assets

Sources merged: official `resize-for-social-media` rule ladder, `design-translation` clone idea, `classroom-helper` visual-integrity rules, `canva-product-imagery`
image facts (canva-sdks, Apache-2.0); 10x "duplicate, never blank"; design-director data-viz minimalism; social `infographic-and-data-viz` (CHART); live tests.

## 1. Structure tools (page level, not transactions)

| Goal | Tool | Notes |
|---|---|---|
| Duplicate a slide or a whole deck | `copy-design { design_id, page_numbers? }` | creates a NEW design; source untouched; no reflow. Use instead of `resize-design` at identical size (official clone trick is obsolete). |
| Insert slides from another design | `merge-designs { type:"modify_existing_design", design_id, operations:[{type:"insert_pages", source:{type:"design", design_id, page_numbers}, after_page_number}] }` | `after_page_number: 0` = front; omit = append. Same `design_id` comes back. |
| Reorder | `merge-designs ... { type:"move_pages", from_page_numbers:[13], to_after_page_number:11 }` | page numbers refer to the structure **after the previous operation** |
| Delete slides | `merge-designs ... { type:"delete_pages", page_numbers }` | **permanent**; ask first, name the slides |
| Build a new deck from pages | `merge-designs { type:"create_new_design", title, operations:[insert_pages...] }` | only `insert_pages` allowed here |
| Other size | `resize-design { design_id, design_type:{type:"preset", name:"presentation"|"whiteboard"} or {type:"custom", width, height} }` | new design; Pro feature (free = limited trial); max ~25 MP; **always re-review**, reflow is not a finished layout |

Rules:

- The tool contract says each `merge-designs` call needs explicit user approval of the **exact** operations. Tell the user the operations in one line, then call.
- **Inserted order can come back reversed** (verified: inserting clone pages `[1,2]` produced example 4 before example 3). After every merge: read every page title in order (`start-editing-transaction` -> `richtexts` where `top == 76`, or `get-design-content`), compare with the plan, fix with `move_pages`.
- Never create a blank slide. A blank page inherits no theme, and text boxes cannot be added. **Always duplicate a donor slide** (10x `canva-presentation`).

## 2. Slide archetype library (the deck's "templates")

Treat 6-8 slides of the deck as donors. Every new slide is a clone of the nearest donor with new text.

| Archetype | Donor looks like | Use for |
|---|---|---|
| Cover | dark band, title, one-line credits, art band | opening, closing (bookend) |
| Agenda | 2x2 or 1x4 numbered rows | slide 2 |
| Definition / thesis | one large sentence + 2 support lines | a core concept |
| Three-up | 3 numbered columns or cards (title + 1 line) | properties, criteria, steps |
| Comparison table | 3 rows x 2 columns, one highlighted row | types, before/after |
| Chain / flow | 3 boxes + arrows + captions | examples, processes |
| Diagram (custom image) | one uploaded PNG, title only | spiral, cycle, matrix, timeline |
| Quote | one line, attribution caption | primary-source citations |
| Summary / takeaways | 3 numbered rows | end of a section |
| Sources | small text list | citations |

Clone-and-retext recipe (verified, produces perfectly style-matched slides):

1. `copy-design { design_id, page_numbers:[donor pages] }` -> clone design.
2. `start-editing-transaction` on the clone; list `richtexts` for each page; `replace_text` every text (use `\n` for 2-line labels); commit.
3. `merge-designs insert_pages` the clone pages into the main deck at the right position.
4. Read titles back; fix order; render; the new pages should be indistinguishable from the old.

## 3. Choosing a visual for a slide

| Content | Visual | Native or image |
|---|---|---|
| 1 definition | big sentence, whitespace | native text |
| 3 parallel items | numbered columns / cards | native (ask `create-design` for it in the outline description) |
| 2-column comparison | table rows | native |
| Process A -> B -> C, example chains | boxes + arrows + captions | native chain donor; or `diagrams.py chain` |
| Cycle, spiral, loop, curve | custom PNG (`diagrams.py cycle|spiral`) | image |
| 2x2 relationship | `diagrams.py matrix` | image |
| History / stages over time | `diagrams.py timeline` | image |
| Hierarchy, levels | `diagrams.py pyramid` | image |
| Quantity comparison | `diagrams.py bars` (zero baseline) | image |
| Overlap / inclusion | `diagrams.py venn` | image |
| Quote | one line + attribution | native text |

Rules (CHART + design-director + classroom-helper):

- A slide title and its visual must **not repeat each other**: title states the claim, the visual shows the structure.
- Title = takeaway ("Mỗi vòng xoáy ở trình độ cao hơn"), not a topic label ("Đường xoáy ốc").
- Honest charts: bars start at zero, no 3D, no dual axis, direct labels instead of legends, one accent + muted greys, source line. Sometimes the honest answer is "this is not a chart" - use a stat slide (one huge number + one line).
- **Visual integrity** (official `classroom-helper`): never rely on text baked into generated images; curriculum-critical wording (definitions, terms, numbers, dates, quotes) lives in **editable slide text**. Diagram PNG labels may name the stages (1-3 words) because the user can re-render them, but the claim sentence must also exist as editable text on the slide or in the notes. Tell the user diagram labels are image, not text.
- Plan for human swap-in: leave a clean, image-light layout where a vetted photo can go.
- Each example slide: example name + 3-step chain + one sentence that states *why* it illustrates the law (the "so what"). Put the link back to the concept in the caption, not in the diagram.

## 4. Diagram pipeline (custom PNG -> slide)

Why: no operation adds shapes or text boxes, so curves and diagrams have to be images.

1. **Write the spec** (`scripts/diagrams.py --example KIND > spec.json`, edit text, keep labels 1-3 words, Vietnamese diacritics render with Arial).
2. **Match the slide**: `bg` = the slide's background colour (sample a thumbnail pixel; `#F7F8FA` in the deck built here), palette = deck palette (`ink`, `accent`, `mid`, `soft`, `muted`).
3. **Render at the final size**: `size:[w,h]` = the pixel box you will place. 1 image px = 1 slide px, so `title_px 40+` and `body_px 30+` land at classroom size. Typical: 1600x760 at left 140, top 230 (leaves title zone clear).
4. `uv run --with pillow python scripts/diagrams.py spec.json out.png`, then **look at it** (`read out.png`). Reject: overlapping labels, text under 28 px, crossings, clipped edges.
5. **Upload** (single-use URL, raw bytes):
   - `create-upload-url {}` -> `{ uploadUrl }` (camelCase)
   - `bash scripts/post_upload.sh "<uploadUrl>" out.png` -> `{ "mediaId": "MA..." }`
   - On any failure fetch a **new** URL; never retry a used one. Upload each asset just before the page that needs it (official `bulk-create` rule: failures stay local).
6. **Place** in one transaction: delete the old art/labels (group ids!), `insert_fill` with `alt_text` describing the structure, `top/left/width/height` exactly the PNG size. Re-read `richtexts`: no stale labels left. Commit. Render the page.
7. Keep the spec JSON next to the deck (the user's folder) so a label change is a 1-minute re-render + `update_fill`.

## 5. Image sourcing ladder (in order)

1. The user's own attachments and slides (crop, never redraw): scale a screenshot to real pixels before cropping (displayed width != file width), crop with Pillow, keep aspect, upload. Reuse one art band on cover and closing slide as bookends (verified with the classical philosopher engraving, placed top 586 / left 110 / 1700x494).
2. A locally drawn diagram (section 4).
3. `upload-asset-from-url { url, name }` for a **public HTTPS** image (public-domain / Commons). Not for local or private files; never push local files to a third-party host to obtain a URL.
4. `generate-image { prompt, aspectRatio, imageReferences? }` - can be slow and can fail with `credit_quota_exceeded`.
5. Omit the visual and keep the slide typographic. A clean slide beats a wrong picture.

`generate-image` facts: prompt is the user's own wording (do not paraphrase when they supply one); `aspectRatio` is an enum (`LANDSCAPE_16_9`, `SQUARE_1_1`, `PORTRAIT_9_16`, ...), exact ratio can also go in the prompt; reference images must be uploaded first and passed as `{type:"MEDIA", id}`; the result needs `get-generate-image-job` polling unless a widget does it. Ask for decorative imagery only (engraving, texture, icon), **never** labelled diagrams, readable text, maps, charts, specific real people or exact facts - those are exactly what generators corrupt (official `classroom-helper`).

**Quota failure**: response `quota_exceeded` / `credit_quota_exceeded`, `used_percentage: 100`, `resets_at` epoch (observed reset 2026-12-01 00:00 UTC), `is_admin:true`. The failure is **synchronous** (no job id). Do **not** retry in a loop. Tell the user the date, then use rungs 1, 2, 3, 5. **`create-design` shares this quota** (it failed with the same code on 2026-11-07 although it had worked on 2026-11-06), so a quota-exhausted account also needs the no-credit deck path (`02` section 8). Credit-free tools verified: `copy-design`, `merge-designs`, `export-design`, `get-design-content`, `create-upload-url`.

**Quota-free art via omp's own `generate_image` (verified 2026-11-07)**: it bills the user's Google/OpenAI/OpenRouter accounts, not Canva credits. Needs `generate_image.enabled: true` (`cfg://generate_image/enabled`, ask first) and is called by writing JSON to `xd://generate_image` (`subject`, `style`, `scene`, `composition`, `aspect_ratio:"16:9"`, `model`). `google-antigravity/gemini-3-pro-image` returned a clean one-colour copperplate engraving of three rice-growth vignettes with no text. Save the returned `/var/folders/.../omp-image-*.jpg`, **view it**, crop with Pillow if needed, then `create-upload-url` -> `scripts/post_upload.sh` -> `insert_fill` (needs a transaction). Same rules as any generator: decorative art only, never labelled diagrams, maps or exact facts; request "no text anywhere".

## 6. Translation / bilingual copies (official `design-translation`, adapted)

1. `copy-design` (not resize) -> clone.
2. Transaction on the clone; `replace_text` every text element in **one** batch; keep proper nouns, preserve `\n`; append the language to the title.
3. **Overflow pass**: expansion is the risk. Vietnamese is roughly 10-25% longer than English for the same content; apply the chars-per-line heuristic in `05-editing-operations.md` and shorten up front.
4. Review every page; commit.

## 7. Resize and variants

Use the five-rule ladder from official `resize-for-social-media`: exact pixels given -> use only those; platform + placement -> lookup; ratio only -> ratio set; "all channels" with no sizes -> default set without asking; "common formats" -> ratio set. De-duplicate near-identical sizes (1200x627 / 1200x628 / 1200x630 -> create 627 once). For decks the relevant sizes are 1920x1080 (16:9 presentation), 1024x768 (4:3), A4 landscape for a handout (export as PDF instead when possible). Name outputs `<title> - <variant>`. `resize-design` is parallel-safe (independent new designs).

## 8. Import (documents -> deck)

`import-design-from-url { url, name, intended_design_type }` converts a **public HTTPS** PDF / PPTX / Keynote / Word / Markdown / HTML into a design. For non-interactive HTML the tool schema says each page element needs `data-document-role="page"`, with optional `data-label` (page title) and `data-speaker-notes` (presenter notes). `[UNVERIFIED]` - we have not tested it and it requires a public URL the **user** controls (the tool forbids uploading local/private files to third-party hosting to manufacture a URL). If the user has such hosting, this is the only route to **speaker notes inside a Canva deck**.
