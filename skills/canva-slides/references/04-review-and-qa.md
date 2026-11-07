# 04 - Review and QA (render, look, score, fix, re-run)

No DOM, no computed styles: Canva exposes text, positions, sizes and **per-page thumbnails inside a transaction**. So review is **eyes on images plus a few scripted checks**, with an honest report of
what was and was not checked. Sources merged: official `get-design-feedback` (7 lenses, evidence rule), `brand-check` (Can't verify), sunbigfly review playbook (P0/P1/P2, two rounds, rollback),
Geongyu (6 gates, statuses, wording gate), medical (3-layer QA, re-run whole layer), minorun (deletion audit, deck-level metrics, honest verification), power-design (21-line checklist),
YuliangXiu (thumbnail wall, Layout Doctrine), anthropics (visual QA on fresh images, reader testing), pitchdeck-pro (scored verdict), academic-poster (5 lenses, finding schema).

## 1. Principles (read once)

1. **Never claim a check you did not run.** Report each gate as `PASS`, `FAIL` or `NOT_RUN`. A contact sheet does not prove small labels are readable; say exactly what you looked at.
2. **Evidence rule**: payload gives text, positions, sizes. It does **not** give colours or fonts. Judge those from the thumbnail and write "appears". Never state a hex or font as fact unless a tool returned it.
3. **Look at fresh renders**, after every edit (after staring at your own ops you see what you expect, not what rendered). **Overflow first**: it is the most common and most visible defect.
4. **Minimum two rounds**; round 1 may never finalise. From round 2 re-check the previous report item by item.
5. **One page's criticism is an instruction to check every page** for the same condition: list them all, fix, re-run to zero.
6. **After any fix re-run the whole QA layer**, not only the failed check; no manual overrides.
7. **If the same P0/P1 survives two rounds, stop patching and roll back to planning** (change layout, density or slide allocation).
8. Inspect a slide **with its neighbours** (problems appear in sequence); wording fixes and structure fixes are separate passes.
9. Thumbnails can be stale or expired: use in-transaction thumbnails for review; export a PNG/PDF for anything the user keeps.

## 2. Procedure

| Step | Action | Tool |
|---|---|---|
| 1 | Structure: page count == plan, order == plan, all `is_responsive:false` | `get-design`, transaction `pages[]` |
| 2 | Content integrity: diff plan vs generated text; swapped terms | `get-design-content` -> `scripts/text_diff.py` |
| 3 | Plan lint (if not already) | `scripts/plan_check.py` |
| 4 | Deck audit: alignment, margins, overlaps, per-slide words, duplicates | dump `richtexts` -> `scripts/deck_audit.py` |
| 5 | Render every page (thumbnails inside one transaction), **show every image**, build a contact sheet | `get-design-thumbnail`, `scripts/contact_sheet.py` |
| 6 | Three-pass scan per page (below) | eyes |
| 7 | Reader test with a cold agent (optional but recommended for graded decks) | subagent |
| 8 | Score (section 5), list findings by severity, set the release status |
| 9 | Fix in one declared pass (`05`), commit, re-render everything, re-run steps 2-6 |
| 10 | Export PDF/PPTX, verify page count and open the PDF at 50% zoom (`07`) | `export-design` |

### Three-pass scan (per page, from the rendered image)

1. **Border patrol**: four corners, four edges, footer band. Anything clipped, anything within ~30 px of the frame, any text cut by its own box or by a neighbour.
2. **Depth scan**: title zone, focus zone, support zone; overlaps and stacking; image integrity (aspect, sharp); leftover decoration or labels from a deleted element; diacritics (tone marks clipped at the top of a line).
3. **Whole-page impression**: one-second focus test; squint test; "does this look designed or default?"; same grid as the previous page?; difference from the previous page (rhythm).

### Review without a transaction (when `start-editing-transaction` is down; verified 2026-11-07)

`export-design { design_id, format:{ type:"png", width:960, height:540 } }` returns one URL per page (status `success`; 960x540 per page confirmed). Download them, write `page<TAB>path` lines and run `scripts/contact_sheet.py`; read text with `get-design-content`; page count from `get-design`. You can still run gates 1-3 and the visual pass, but **not** `deck_audit.py` (it needs `richtexts` geometry from a transaction): record `deck-audit: NOT_RUN` and the release status `DRAFT - VERIFICATION INCOMPLETE`. Exported PNGs also work for anything you hand to the user.

### Lenses (seven official + five for course decks)

Official: visual hierarchy, layout and spacing, copy and messaging, consistency, readability and contrast, accessibility, fit for purpose. Course-deck lenses (adapted from the poster review): **outsider** (can a classmate who missed the lecture follow it?), **projector** (back-row legibility at 25-50% zoom), **wording** (terms, fidelity, no reasoning traces), **rubric** (what the grader scores: accuracy, structure, visuals, examples, delivery), **design** (the anti-slop list). Skip a lens that does not apply and say so.

### Reader test (anthropics doc-coauthoring, adapted)

Give a fresh agent **only the slide titles** and ask it to reconstruct the argument (ghost-deck test). Then give it the thumbnails and ask what each slide is *for*. Wherever it stalls or answers wrongly, the slide is the defect.

## 3. Hard fails (block delivery regardless of score)

1. Source fact missing, altered, or a **doctrinal term swapped** by the generator.
2. **Fabricated** quote, number, source or "from the log"; invented credit/date text.
3. **Placeholder** text or art left in (`lorem`, `[insert]`, `<Project Name>`, "Click to add", Canva's cloud-and-hills placeholder landscape, grey rectangles).
4. **Overflow, clipping or overlap** of text; text over busy imagery without a scrim.
5. Any required text **below the floor** (body < 32 px, support < 28, tag < 24).
6. Wrong **order**, missing or duplicated slide, orphaned divider.
7. **Contrast** below 4.5:1 for body (3:1 large) or meaning carried by hue only.
8. A **diagram label unreadable** at slide size, or a diagram that misrepresents the concept (proportions compressed until they mislead).
9. A visual the user did not agree to that is **unverified generated art** presented as fact.
10. A claim of "saved", "verified" or "exported" that the tools did not confirm.

## 4. Severity-ordered checklist (1920x1080 values)

**Severity 1 - blocking (content truth, legibility, structure)**
- [ ] Every planned title/point present and exact (`text_diff.py` = 0 MISSING); terminology matches the sheet
- [ ] No fabricated quotes/numbers; illustrative values labelled; sources shown for borrowed figures
- [ ] No placeholders, reasoning traces ("[NEEDS SOURCE]", "this slide should..."), private words, file names
- [ ] No overflow/clipping/overlap; nothing within 96 px of an edge (title chrome excepted)
- [ ] Body >= 32 px (target 34-38), support >= 28, tag >= 24; no text in an image carries a required definition
- [ ] One idea per slide; no slide with two headlines
- [ ] Page order and count correct; cross-references (slide/figure numbers) correct
- [ ] Contrast >= 4.5:1 body / 3:1 large; never hue-only
- [ ] No unverified visuals asserted as fact; images undistorted

**Severity 2 - major (comprehension and hierarchy)**
- [ ] **Ghost-deck test** passes (titles alone tell the argument); titles are claims, <= 65 chars
- [ ] One focal point per slide (>= 1.5x next element, or the only saturated one)
- [ ] <= 4 type sizes per slide, <= 6 per deck; tier ratio >= 1.2; weights 400-700
- [ ] Bullets <= 3-4 (<= 12 words), words <= mode budget (25/40/75)
- [ ] Repeated components identical: card widths/heights, line counts, number-badge alignment
- [ ] Alignment: left edges, title position, column tops identical across slides (`deck_audit.py` outliers = 0)
- [ ] Diagrams: <= 5 nodes, labels >= 28 px at final size, no sub-labels, no prose inside, arrows single-meaning
- [ ] Charts: bars from zero, <= 5 series, <= 7 lines, direct labels, title = conclusion
- [ ] Crossheads answered by the next slide; <= 2 in a row; none unanswered
- [ ] Deck rhythm: no 3 same-form in a row, no 5 text slides in a row
- [ ] One emphasis per slide; accent <= 15% of pixels and one hue
- [ ] Examples: >= 2-4, each shows what carries over and what is new, each linked back in editable text
- [ ] Timing model run; landing time inside the slot (`01`)

**Severity 3 - quality (craft)**
- [ ] 8-px spacing consistent; proximity (related <= 24, unrelated >= 48)
- [ ] No orphan one-word last lines; breaks at meaning
- [ ] Heading grammar varied; no pattern repeated 3+ times; no uniform title length
- [ ] No accent rule under titles, no edge stripes, no gradients/shadows/3D, no emoji, no all-caps labels, no centred body
- [ ] Number badges only where there is a sequence
- [ ] No duplicate images; illustration count modest; art only where it carries information
- [ ] Tables <= 6 rows, one highlighted row, no empty header cell
- [ ] Chrome (logo/art band) only on cover and closing

**Severity 4 - polish**: consistent punctuation and date format; no em-dash overuse (<= 2 per 500 words, none in titles); consistent casing; page numbers if the theme provides them; no flashing; appendix slides clearly labelled.

**Severity 5 - packaging**: PDF and PPTX exported and opened; page count verified; filename `<Type>_<Topic>_<YYYY-MM-DD>`; notes file and Q&A sheet delivered; backup and edit links shared; `updated_at` of the design is later than `created_at` after the last commit (cheap proof a commit landed).

## 5. Scoring and release status

Score out of 100 (adapted from the 10-dimension academic rubric and the weighted Phlegonlabs rubric):

| Dimension | Points | What 10/10 looks like |
|---|---:|---|
| Argument and structure | 20 | spine clear, ghost-deck passes, one job per slide |
| Accuracy and terminology | 20 | zero drift, sources shown, caveat present |
| Examples and visuals carry the idea | 15 | 2-4 relevant examples, diagrams show relations |
| Hierarchy and consistency | 15 | one system, aligned, same line counts, rhythm |
| Readability | 15 | back-row legible, contrast, diacritics intact |
| Delivery readiness | 10 | timing fits, notes + Q&A prepared |
| Packaging and accessibility limits stated | 5 | exported, verified, limits disclosed |

Ship at **>= 85** with **no dimension below 60% of its weight**. Bands: 90-100 ready; 80-89 strong with fixes; 70-79 usable draft; < 70 do not present. A hard fail overrides the score.

**Release status** (set by the reviewing agent, never by a script):
`READY` | `DRAFT - FIXES REQUIRED` | `DRAFT - VERIFICATION INCOMPLETE` (state which gates were `NOT_RUN`).

## 6. Wording gate (visible text and notes)

- Concrete over abstract: numbers, names, cases instead of "significantly improved".
- **No reasoning traces or private words** on slides ("[ghi chu: ...]", "ket qua kiem tra", file names, internal IDs, self-coined abbreviations without expansion).
- Newcomer-readable, not childish; define a term at first use; expand acronyms once.
- Notes never start with "Slide này cho thấy / this slide shows / we can see / as shown"; state the claim.
- Heading grammar varies (claims, labels, questions) across the deck; measure repetition: three headings in a row with the same pattern is a machine tell.
- Quotes only from real artifacts; keep wording; never tidy a quote.
- Mark every unverified generated fact `[verify]` until the user confirms it.

## 7. Deck-level audit (script)

`scripts/deck_audit.py` takes the transaction's `richtexts` JSON and reports, per deck: title position outliers (top/left versus the modal value), left-edge drift of body text, text boxes outside the 96-px safe zone or past the page, TEXT-vs-TEXT overlaps, bottom overflow (`top + height > 1080`), word counts per slide against the mode budget, duplicate titles, and heading-length monotony. It cannot see colour or font, so it complements the visual pass, never replaces it.

How to dump the JSON (eval):

```js
const tx = parse(await tool.mcp__canva_start_editing_transaction({design_id}));
await write('/tmp/richtexts.json', JSON.stringify(tx.richtexts));
await tool.mcp__canva_cancel_editing_transaction({transaction_id: tx.transaction.transaction_id});
```

## 8. Report format (deliver this, not an essay)

```
## Review - "<title>" (<N> slides) Status: <READY|DRAFT - FIXES REQUIRED|DRAFT - VERIFICATION INCOMPLETE> Score: <n>/100
Gates: structure PASS | text-diff PASS | audit PASS | render PASS (all 16 pages viewed) | export NOT_RUN | reader-test NOT_RUN
### Top priorities (max 5)
1. <slide n> [P0] <what> - evidence: <thumbnail/box> - fix: <op>
### Page by page (one block per page with findings, severity High/Med/Low, concrete fix)
### What is working (2-4 items; keeps the critique usable)
### Not verified / manual (what the API cannot do or you could not check)
### Round log (round k: fixed A,B; pending C)
```

Finding schema when fan-out is used: `{slide, severity, lens, box:[x,y,w,h] (px), problem, fix_op}`; merge findings on the same box (+/- 20 px) with the same problem into one.

## 9. Reviewing a deck you did not build

Read-only until the user says "fix". Use a **cancelled** transaction for inspection. Optional: leave per-page comments with `comment-on-design` **only if the user asks** (comments are visible to everyone with access). Never edit the original: copy first (`05`).
