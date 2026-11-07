# 07 - Delivery: export, notes, rehearsal, hand-off, feedback rounds

Sources merged: official `presentation-time-fitting`, `implement-feedback`, `resize-for-social-media`, `classroom-helper` hand-off honesty (canva-sdks, Apache-2.0);
TerminalSkills `canva` (limits, URL lifetimes, "jobs are not results"); 10x `canva-export`; design-director export standards; live tests.

## 1. Export

1. `get-export-formats { design_id }` -> which formats and which pages. Only request a format it reported.
2. `export-design { design_id, format:{ type, ... } }`:

| Need | type | Options worth setting |
|---|---|---|
| Show in the room / email | `pdf` | omit `pages` for all; `size` only matters for paper (a4/a3/letter/legal); `export_quality:"pro"` if the plan allows |
| Lecturer wants an editable copy | `pptx` | check the result opens; fonts may substitute |
| Page-by-page proof, review without a transaction, or images for a doc | `png` | `lossless:true` (default), `as_single_image:false`; `width`/`height` are honoured (960x540 returned one image per page, verified) and credit-free |
| Handout | `pdf` (+ say that Canva notes pages are not exported) |

MP4/GIF/CSV are not deck outputs. A deck without `pdf` **and** `pptx` is not delivered (design-director/10x consensus: PDF for the room, PPTX for handoff, PNG for review).

3. The result is a **download URL, valid ~24 h** (TerminalSkills). Download it at once to a named file, e.g.
 `curl -sSL -o "$HOME/Documents/<deck>.pdf" "<url>"`, then verify: file size > 0, page count equals the slide count
 (`uv run --with pypdf python -c "import pypdf,sys;print(len(pypdf.PdfReader(sys.argv[1]).pages))" file.pdf`).
4. Never store signed URLs. Thumbnails expire in ~15 min; `edit_url`/`view_url` last ~30 days. Hand humans the **edit link**, not a thumbnail URL.
5. Throttles: exports 75 per 5 min per user per document, 500 per 24 h. Do not loop exports.
6. Exports are asynchronous behind the tool: treat "accepted" as not-yet-done until a URL arrives; on `failed` read the error and do not blindly resubmit (`license_required` -> an asset in the deck needs a licence: replace it).

## 2. Presenter notes

- `get-presenter-notes { design_id, pages? }` is **read-only**. There is **no operation** that writes notes (`perform-editing-operations` has none), so the official `presentation-time-fitting` cannot complete its write-back step here. Do not invent an operation; say so.
- Deliver notes as a separate artifact: a markdown file per deck (`<deck>-speaker-notes.md`) **and** the same text in chat, grouped by slide (the official fallback). Include for each slide: time budget, 2-5 sentences to say, the transition sentence, and any definition to read verbatim.
- Only way to get notes **inside** Canva: `import-design-from-url` with HTML `data-speaker-notes` (see `06-structure-and-assets.md` section 8, `[UNVERIFIED]`, needs a user-hosted public URL). Otherwise the user pastes notes manually: give them slide-numbered blocks that are ready to paste.

### Time budget (planning-stage arithmetic, official `presentation-time-fitting`)

- English pace ~150 words/min is the published guide; treat as guidance, not a cap.
- Vietnamese is written one syllable per token, so a token count over-states duration compared with English words. `[INFERENCE]` plan with ~150-190 tokens per minute at presentation pace, then **calibrate from one timed rehearsal** and rescale.
- `minutes per content slide = total minutes / content slides`; target tokens per slide = minutes per slide x pace. Typical bands: 1-2.5 min per content slide (below 0.7 min = too many slides; above 3 min = add an example or a diagram).
- If the target is impossible for the slide count, say so and cut slides **before** generation rather than after: the structure tools can delete pages, but each deletion needs approval.

## 3. Q&A and defence preparation

For coursework, thesis defence or seminar, produce (in the notes file, not on slides; full method in `09-education-playbooks.md` section 4):

1. The one-sentence spine of the talk and the three claims that carry it.
2. Five to ten likely questions, typed (motivation, novelty, method validity, figure interpretation, controls, mechanism, fair comparison, stability, limitations, transferable insight; for a concept deck: definition, counter-example, scope, "so what", source), each as `slide | question | safe answer (<= 3 sentences) | source | caution`.
3. **Claim risk level -> verb**: low (directly stated in the source) "cho thấy / chỉ ra"; medium (supported + interpreted) "ủng hộ / phù hợp với"; high (proposed, conditional) "gợi ý / có thể / theo quan điểm của ...". High-risk claims need backup support or an explicit limitation.
4. The two strongest objections and the reply; check **percent vs percentage points** and absolute vs relative change.
5. **Backup slides** for the likeliest questions, appended after the conclusion with `merge-designs` (they cost no talk time) and labelled "Phụ lục A: ...".
6. Terminology sheet (approved terms, mistranslations to avoid): the generator once swapped "Phổ biến" for "Phát triển"; the sheet is the guard.
7. Drill: 60-90 s per answer; start with a concrete detail, not theory.

## 4. Rehearsal checklist (hand to the user)

- [ ] Read slide 1 aloud in 20 s; each content slide <= the budget; total within 90% of the slot (leave Q&A room).
- [ ] One-second glance test: close your eyes, open a random slide, can you state its point?
- [ ] Back-of-room test: view the exported PDF at 50% zoom on a laptop; every body line readable.
- [ ] Open the PDF on the presentation machine, not just the dev machine; fonts and diagrams intact.
- [ ] Keep the PPTX as a backup and the notes file on paper or a phone.

## 5. Hand-off message (template)

```
Deck: <title> - <N> slides 16:9 Edit link: <edit_url>
Delivered: PDF <path>, PPTX <path>, notes <path>
Changes this round: <slide list, one line each>
What is image vs text: <diagram slides: labels are part of the image (re-render to change)>
Needs your decision: <open questions, max 3>
Could not do via the API (manual): <checklist, see below>
Unverified: generated visuals and any facts on them are drafts until you check them
Backup: <backup design link>
```

### Manual-changes checklist (official `implement-feedback` shape)

For each thing the API cannot do, emit one block:

```
Slide <n>: <what to change>
 Requested by: <person or "you">
 Why manual: <API limit, e.g. cannot change font family / background / add text box / write notes>
 -> Steps: <exact editor clicks>
```

Do not apologise for API limits and do not over-explain them: state the limit once, give the steps.

## 6. Feedback rounds (comments -> changes)

Adapted from official `implement-feedback`:

1. `list-comments { design_id }`; for every thread with replies `list-replies { design_id, comment_id }`. Comments carry **no page id**: map each thread to a slide by quoting its text against `get-design-content` per page, and say the mapping.
2. Triage into **Actionable**, **Manual only**, **Resolved/positive**. Be generous: "make the title punchier" is actionable, not ambiguous. Ask only when two reviewers contradict or a comment points at something not in the deck.
3. Present the plan once (this is the single approval; see `05-editing-operations.md` approval gate), then take a backup (`copy-design`).
4. One transaction, one batch, render affected pages, commit.
5. `reply-to-comment { design_id, comment_id, message_plaintext }` on every thread: what was done, or what remains and why. Finish with the manual checklist.
6. Keep a round log (`round N: fixed A, B; pending C`) so round N+1 re-verifies only what changed.

## 7. Filing

Optional: `create-folder { name, parent_folder_id:"root" }` then `move-item-to-folder { item_id, to_folder_id }` for the deck, backup and resized variants. `search-designs { query, ownership, sort_by, design_types:["presentation"] }` finds decks by title; **never** call it when you already hold a design id.

## 8. Definition of done (a deck is delivered when ALL are true)

- [ ] plan passed `plan_check.py` with zero errors
- [ ] generated text diffed against the plan; terminology fixed
- [ ] every page rendered and looked at after the last edit
- [ ] repeated components aligned; body >= 34 px; no text clipped
- [ ] 16:9, one font system, one accent, <= 3 type styles + a caption style
- [ ] diagrams uploaded with alt text; key claims also exist as editable text
- [ ] PDF + PPTX exported, downloaded, page count verified
- [ ] speaker-notes file and Q&A sheet delivered
- [ ] hand-off message sent with edit link, backup link, manual checklist, unverified warning
