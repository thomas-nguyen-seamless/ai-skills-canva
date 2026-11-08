# 02 - Outline, brief and generation (`create-design`)

Verified live 2026-11-06/07: 3 sections -> exactly 3 slides, 14 sections -> exactly 14, all 1920x1080, `is_responsive:false`. Sources merged: official `generate-deck` / `branded-presentation` /
`classroom-helper` brief schema, rifater field notes (put every string in the brief; screen text, not thumbnails), lesson-designer 8-field contract, design-director (plan before paint),
huashu (lock grammar early), carousel-builder (character budgets), our own regeneration experience.

## 1. Preconditions (stop if any is false)

- Plan exists on screen and passed `scripts/plan_check.py` with 0 errors (`01`).
- Terminology sheet and mode token are fixed.
- Stance (palette, type character, image language, density register) is written.
- **Quota awareness (corrected 2026-11-07)**: `create-design` **does** draw on the same AI-credit quota as `generate-image`. It worked on 2026-11-06 and failed on 2026-11-07 with a synchronous `{"status":"failed","failure":{"code":"quota_exceeded","message":"User has exceeded their credit quota"}}` (no `job_id`; `mcpMeta` `com.canva/aiCreditQuotaError`: `used_percentage:100`, `resets_at:1796083200` = 2026-12-01 00:00 UTC). A failed generation returns instantly, so there is nothing to poll: **branch on the first response**: no `job_id` and `status:"failed"` -> go to section 8 (no-credit mode). Do not retry in a loop.
- Each regeneration is a full job and costs credits: plan for **<= 2 generations** of a deck, then repair in place. Probe cheaply first when a deck matters: `get-logged-in-account-details` does not show credits, so the first `create-design` response is the probe.

## 2. The call

```json
{
 "brief": "<see section 3>",
 "format": "Presentation (16:9)",
 "outline": { "sections": [ { "title": "...", "description": "...", "points": ["...", "..."] } ] },
 "user_intent": "one line stating the goal"
}
```

- **`format` must include the orientation.** A format name without it resolves to a square design. Never omit it for a deck.
- **Never omit `outline`** for a real deck: without it Canva invents the structure, the main cause of unusable output. **One section = one slide, in order** (verified).
- `create-design` **cannot** apply a brand kit or brand template (`08`). It does not take `brand_kit_id`.
- Always pass `user_intent` (<= 255 chars).

### Poll the job (verified contract)

1. Response: `{ job_id, status:"pending", continuation_token, polling_policy:{ wait_seconds:15, instructions } }`. Wait **at least `wait_seconds`** (15) before the first poll; polling earlier returns the same answer.
2. `get-create-design-async-job { job_id, continuation_token }`. Pass the token from the **most recent** response; if a response carries none, reuse the last one (observed: the token stayed valid across 5 polls and the completed response carried none).
3. Statuses seen: `pending` / `in_progress` -> keep waiting; **`completed`** (not `success`) -> `design:{ id, url, edit_url }`; `failed` -> read the error, do not blindly resubmit.
4. Timings seen: 3 slides about 1 poll (15-30 s); 14 slides about 5 polls (about 75 s). A long deck can time out once and succeed on an identical retry: retry once **without** changing the brief.
5. When `design.print.is_printable` is true and you reply in text only, mention the print link; never say a design cannot be printed.
6. Store `design_id`, `url`, job id in the plan folder. `edit_url`/`view_url` returned by other tools are expiring JWT links; `canva.link/...` short links and `canva.com/design/<id>` are durable.

## 3. The brief (what the generator reads besides the outline)

Open with one line that blocks the document-degradation failure (official `classroom-helper` / `generate-deck`):

> `Bài thuyết trình đúng <N> slide, định dạng slide 16:9 nhiều trang, không phải poster, flyer hay tài liệu một trang.`

Then, in this order (each 1-3 lines):

1. **Subject, audience, purpose, language**: "Triết học Mác - Lênin, quy luật phủ định của phủ định; khán giả: giảng viên và sinh viên; mục tiêu: giải thích khái niệm, nội dung, ý nghĩa, kèm ví dụ; tiếng Việt có dấu đầy đủ, thuật ngữ nhất quán".
2. **Mode and narrative stance**: "chế độ talk (<= 40 từ/slide, <= 4 gạch đầu dòng), tiết lộ dần, kết bằng slide takeaway".
3. **Design stance** (5 lines): ground colour, ONE accent, type character, image language, density register.
4. **Avoid list (emoji is a hard ban: no emoji anywhere, in any field)** (the merged anti-slop veto list, section 6 of `03`): "không 3D, không gradient, không đổ bóng, không clip-art, không ảnh stock, tuyệt đối không emoji hay biểu tượng pictograph, không gạch chân/vạch màu dưới tiêu đề, không viền một cạnh, không căn giữa toàn bộ, không chữ in hoa trừ tiêu đề bìa".
5. **Type and layout hints**: "chữ lớn, tiêu đề ngắn một dòng, tối đa 3 ý mỗi slide, lề rộng, mọi slide cùng lưới, tiêu đề cùng vị trí".
6. **Visual vocabulary per slide type**: the sentence that tells the generator to draw chains, tables, cards **natively** where possible and to leave a large empty area where you will insert a custom diagram.
7. **Terminology**: the approved terms, spelled exactly.

Lock the grammar early (huashu): if the stakes are high, generate a **2-slide probe** (cover + one content slide) with the same brief, inspect, then run the full deck.

## 4. The outline schema (each section = one slide)

```json
{
 "title": "Mỗi vòng xoáy lặp lại điểm xuất phát nhưng ở trình độ cao hơn",
 "description": "<role> + <visual: native chain|table|cards | large empty area for a custom diagram> + <layout register: editorial|balanced|data-dense> + <anything the generator must NOT draw>",
 "points": ["<= 12 words", "<= 12 words", "<= 12 words"]
}
```

Rules:

- **Title** = action title (a claim, <= 65 chars, 1-2 lines). The generator may paraphrase it; you will diff and fix.
- **Put every string you will ever need into the outline.** No operation inserts a new text element, so footers, credits, source lines, captions, slide labels, numbers and closing text must exist now. Put credit lines in the cover's `points`; put the source/caption as the final point; put the thanks line in the closing section.
- **Description carries visual direction** (the generator's habit is to become a document otherwise): name the visual type per slide. Examples that worked: "ba cột bằng nhau, mỗi cột một tính chất: tiêu đề đậm + một dòng"; "bảng so sánh 3 hàng x 2 cột, hàng cuối làm nổi bật"; "chuỗi ba khối bằng nhau nối bằng mũi tên, chú thích ngắn dưới mỗi khối".
- **Diagram slides** (spiral, cycle, matrix, timeline, pyramid, venn, bars): describe `một tiêu đề và một vùng trống lớn phía dưới, không vẽ minh hoạ, không ảnh`, then insert the PNG yourself (`06`). Asking the generator to draw a spiral gave a scribble that had to be replaced.
- **No text baked into generated art**: curriculum-critical words must be real text.
- **Points are telegraphic**, <= 12 words, parallel, no full paragraphs. Width of the target box is a constraint: predict wraps with `scripts/fit_check.py`.
- Section order = slide order = plan order. Do not add sections that are not in the approved plan.

## 5. Screen the result before anyone sees it (never trust the thumbnail alone)

Order (cheap to expensive):

1. **Page count and order**: `get-design { design_id }` -> `page_count == N`.
2. **Text diff**: `get-design-content { design_id, content_types:["richtexts"] }` -> save to `generated.txt` -> `python3 scripts/text_diff.py plan.json generated.txt`. Fix every MISSING and every swapped term. Elements of one slide are separated by newlines and runs by nothing: do not infer a typo from a fused word.
3. **Transaction inspect** (`start-editing-transaction`): `pages[]` (all fixed-page?), `richtexts[]` and `fills[]` per page; note theme art that is locked (`editable:false`).
4. **Thumbnails**: `get-design-thumbnail` per page inside the same transaction, **show every image**; build a contact sheet (`scripts/contact_sheet.py`). `get-design-pages` fills only page 1.
5. Cancel the transaction (inspection only) unless you proceed to fixes in it.
6. Walk the rubric in `04-review-and-qa.md`. Typical first-pass defects seen: generator-chosen accent rule under every title; all-caps node labels; numbered 01/02/03 where the items are not a sequence; invented credit/date text; over-small body (~28 px); a swapped doctrinal term; a scribbled "diagram".

## 6. Regenerate or repair? (recovery playbook for a bad generated deck)

| Defect | Action |
|---|---|
| A few strings wrong or paraphrased | `replace_text` / `find_and_replace_text` in place |
| Terminology swapped | fix in place, then diff again |
| Wrong page order or one slide missing/extra | `merge-designs` move/insert/delete (`06`) |
| Text too small / spacing uneven | declared typography/alignment pass (`05`) |
| One slide structurally wrong | clone a donor slide (`copy-design` + retext + `merge-designs`), delete the bad page (ask first) |
| Theme wrong (palette, fonts, generator look) | regenerate with a tighter stance and avoid list (max 2 generations); if still wrong switch strategy: pick the best generated slides as donors |
| Generator ignored the outline (page count off, sections merged) | tighten the outline descriptions, regenerate once; never "negative-constraint" prompts (they can fail the whole job with `design_generation_error`) |
| Candidate looks right but text is garbled | the text defect is cheaper to fix than regenerating |

Do not regenerate to fix text; do not repair around a wrong theme.

## 7. After generation, always

- Share the `edit_url` (short link) and say how many slides came back vs planned.
- Record in `deck-rules.md` any new learned preference.
- Move straight to review (`04`); do not describe the deck as finished at this point.

## 8. No-credit mode (when `create-design` / `generate-image` return `quota_exceeded`)

Verified 2026-11-07 with the quota at 100% (resets 2026-12-01 00:00 UTC, `is_admin:true`): these tools still **worked**: `copy-design` (3 pages -> new design), `merge-designs` (`move_pages` -> success), `get-design`, `get-design-content`, `get-export-formats`, `export-design` (PDF and per-page PNG), `create-upload-url` + POST, `resize-design` / `import-design-from-url` `[U]` (not re-tested). `create-design` and `generate-image` failed. `start-editing-transaction` was failing with 503 at the same time (separate cause; see `10`).

So a new deck can be built **without credits** by recombination of existing designs (minorun's "reuse and derive" discipline):

1. **Pick donors**: the user's best existing deck(s) (`search-designs`) or the deck built earlier in the session. Read donor text and page list (`get-design-content`; `get-design-pages` for page 1).
2. `copy-design { design_id, page_numbers }` for the donor pages you need -> a working design (the original is untouched).
3. Order and combine with `merge-designs` (`insert_pages` from several donors, `move_pages`, `delete_pages` with approval); **read titles back** after every merge.
4. **Retext** with a transaction (`replace_text` on every element) - this needs `start-editing-transaction`; if that is down, you cannot change text: say so and deliver the structure (the page set) plus the exact per-page text and steps as a manual checklist (`07` s.5).
5. Diagrams: `diagrams.py` -> `create-upload-url` -> `post_upload.sh` -> `insert_fill` (needs a transaction).
6. Review without a transaction: export PNG per page (`export-design { format:{type:"png", width:960, height:540} }`; verified 960x540 per page) and view the images; `get-design-content` for text; `scripts/contact_sheet.py` for a sheet. Deliver with PDF/PPTX export.

Rules: tell the user the credit state and the reset date once; never retry generation; never present a recombined deck as generated; keep honest status (`DRAFT - VERIFICATION INCOMPLETE` when you could not run transaction-only checks).
