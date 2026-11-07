# 09 - Education playbooks (Vietnamese university coursework, lessons, defences)

This is the part no source covered well: **Vietnamese academic register, coursework rubrics, doctrinal accuracy, group decks**. Sources merged: canva-ppt-lesson-designer (Vietnamese lesson system, lesson map,
8-field contract, 6 layouts), academic-pptx and bushiAgoni (defence, Q&A, claim risk), minorun (concept 3-piece set, crossheads), consultant (answer first, so-what, pp vs %), talk-like-ted (drills),
canva-prompt-creator (Vietnamese-safe fonts, "1-6-6"), medical (content integrity), plus this user's observed feedback (2026-11). Items marked **[ask]** need the user's course material;
**[verify]** needs checking against the course text before it goes on a slide. Never invent bibliographic details, page numbers, quotations or exam criteria.

## 1. Pick the playbook

| Situation | Playbook | Mode | Spine |
|---|---|---|---|
| Explain a law / concept (Triết học Mác – Lênin, lý luận chính trị, kinh tế học...) | A. Concept lecture | `talk` | concept deck |
| Teach a class period (GDPT, tiết học) | B. Lesson | `talk` | lesson spine |
| Thesis, seminar, research defence | C. Defence | `talk`/`document` | SCR or funnel + answer |
| Report on a paper or chapter | D. Literature report | `talk` | SCR |
| Group assignment (several authors) | E. Team deck | `talk` | whichever fits + merge workflow |

Always ask for the **course rubric / lecturer's criteria** [ask]. If none: use the generic mapping in section 8.

## 2. Playbook A - Concept lecture (the deck type built in this skill's session)

Spine: **hook -> concept 3-piece set -> mechanism (one diagram) -> properties -> examples from different domains -> methodological meaning -> honest caveat -> takeaway**.

Suggested 14-16 slides for a 15-minute talk (adjust with `plan_check.py`):

| # | Role | Action title pattern | Visual |
|---|---|---|---|
| 1 | cover | law name | art band (user's own) |
| 2 | agenda | "Bốn phần giúp ta hiểu quy luật" | 4 numbered rows |
| 3 | hook / question | a real-life question the audience has | one sentence |
| 4 | definition | "X là ..." (exact textbook formulation [verify]) | huge sentence + 2 support lines |
| 5 | properties | "X có ba tính chất" | three-up (no 01/02/03 unless a sequence) |
| 6 | types / contrast | "Khác với Y và Z ở chỗ ..." | comparison table, highlighted row |
| 7 | mechanism | "Hai lần phủ định hoàn thành một chu kỳ" | chain A -> not-A -> A' |
| 8 | mechanism visual | "Phát triển có dạng đường xoáy ốc" | spiral PNG |
| 9 | cycle | "Mỗi chu kỳ khởi đầu một chu kỳ mới" | cycle PNG |
| 10-13 | examples (3-4) | "Ví dụ: <case>" | chain + why-it-fits caption |
| 14 | methodological meaning (1) | "Nhận thức: ..." | numbered rows |
| 15 | methodological meaning (2) | "Thái độ thực tiễn: ..." | cards |
| 16 | takeaway + closing | 3 takeaways, thanks line | art band |

Rules specific to doctrine:

1. **Content comes from the course text** (lesson/course map): definition, properties, formulations exactly as taught. Terminology sheet is mandatory; run `text_diff.py` after every generation and after every edit pass.
2. Keep the **standard Vietnamese forms** of terms; do not translate back and forth, do not transliterate (e.g. phủ định biện chứng, kế thừa, khuynh hướng phát triển, đường xoáy ốc). A swapped term is a Severity-1 defect.
3. **Contrast concepts precisely** (biện chứng vs siêu hình): each side gets one line stating the *effect on development*, not synonyms.
4. **Examples carry the grade.** Plan 3-4 from different domains; each as `name -> 3-step chain -> why it instantiates the law` and what is preserved vs new. Candidate pool (use only those the course text supports [verify]): nature (grain -> plant -> grains; egg -> larva -> pupa -> butterfly), society (social formations in sequence), thought/science (a theory challenged and superseded, keeping what remains valid), technology (valves -> transistors -> integrated circuits), mathematics (signs: positive -> negative -> positive). Prefer examples the lecturer already used in the course; avoid examples that only illustrate a negation without a *negation of the negation* (one step is not the law).
5. Show the **limits**: the spiral is not a straight line; temporary regress happens; the new is weak at first and needs protection (methodological meaning). Add one honest caveat slide.
6. **Slide with a diagram has the claim as the editable title**; the PNG labels name stages only (`06`).

## 3. Playbook B - Lesson (teach a class period)

Derive slide count from class time (lesson-designer): 20-30 min -> 6-8 slides; 35-45 min -> 8-12; 60 min -> 12-18. Spine: opener -> objectives -> prior knowledge -> content groups -> example/practice -> summary -> closing/assignment.

Challenge-before-acting criteria: **subject, grade, lesson/topic, slide count, class duration, style**. Missing 2+ -> push back with a filled sample; exactly 1 -> default and state it.

Per-slide **8-field contract** (machine-checkable): purpose | main content | layout | image keywords (>= 5 English keyword clusters of 2-6 words; image + icon + shape groups) | video suggestion | colour and font | interaction (question to ask) | teacher notes (misconception, check for understanding, timing). One knowledge unit per slide, each traceable to the lesson map; **1-6-6** (1 idea, <= 6 lines, <= 6 words per line) is the lesson-designer's cap for projected slides; this skill's `talk` mode (<= 4 bullets, <= 12 words) is the working default.

Six layouts cover a lesson: Cover, Single concept, Process, Comparison, Big number, Quote; a 6-14-slide deck uses 5-6 of them. Subject accent colours are allowed (one accent per slide). Minimum projected type in the source is 24 pt (= 48 px under the 2 px/pt mapping); this skill's floor is stricter in px (body >= 34).

## 4. Playbook C - Thesis / seminar defence

From academic-pptx (assembled; the source has no dedicated section):

1. Structured-argument mode. **Research question on its own slide** by slide 2-3.
2. Spine: SCR (Situation -> Complication -> Resolution). Methods only as much as the committee needs to judge validity; the rest to the appendix.
3. **Action titles** on every content slide; ghost-deck test passes.
4. One exhibit per results slide; annotate the key finding on it (callout, shaded region, focal colour). Real figures only; rebuild figures at slide size with labels >= 28 px.
5. **State the main limitation yourself** in Discussion (pre-empts the objection).
6. **Conclusions slide stays on screen through Q&A**; contact/QR on it; references slide before the appendix.
7. Timing: <= 1 content slide per minute for argumentative decks, finish 1-2 min under; mark 2 cut triggers.
8. **Backup slides** are first-class: one per anticipated question, labelled "Phụ lục A: ...", `merge-designs` appends them at the end at no time cost.

### Q&A preparation (bushiAgoni, adapted)

Ten question types to prepare for: motivation, novelty, method validity, figure interpretation, controls, mechanism, fair comparison, stability/reproducibility, limitations, transferable insight. Template per question: `slide | likely question | safe answer | source support | caution`.

**Claim risk levels -> verbs**: *low* (directly measured/quoted): "cho thấy / chỉ ra"; *medium* (supported + interpretation): "ủng hộ / phù hợp với"; *high* (proposed, mechanistic, conditional): "gợi ý / có thể / theo quan điểm của ...". High-risk claims need backup support or an explicit limitation. Check **percent vs percentage points** and absolute vs relative change before they reach a slide (consultant).

Drill: 60-90 seconds per answer; open with a concrete detail, not theory; one sentence + three points; one number that survives 10 minutes (talk-like-ted).

## 5. Playbook D - Literature report

One page per claim; **real figures only** (crop, scale, label; never regenerate a chart or table); tables > ~8 rows go to backup (highlight this work + 2-4 comparison rows); > 4 equally important panels split across slides; keep scale bars; annotations never cover data. For a 10-15 minute coursework talk use 12-16 main slides + 4-8 backup; 20+ only for a full paper report.

## 6. Vietnamese register, rhetoric and conventions

- **Language lock**: one output language (Vietnamese) for slides and notes; keep technical terms canonical; never mix grammar. English only for search keywords or when the course uses an English term (gloss it once).
- Academic, neutral, active voice; short sentences; no marketing language, no filler openers ("Trong xã hội ngày nay...", "Hãy cùng khám phá...").
- **Address** in the opening of the *script* (not the slide): "Kính thưa thầy cô và các bạn, ..." then the hook. Close with the takeaway, then "Em/Nhóm em xin cảm ơn thầy cô và các bạn đã lắng nghe" (verbally; the closing slide may carry a thanks line plus the takeaway).
- Titles: sentence case, claims, <= 65 characters; no all-caps; no trailing full stops; avoid colons that split a title in two.
- **Quotation slide**: the quote verbatim, in quotation marks, attribution line below in the support size (<= 3 lines); quotes only from the course text or source [verify]; never fabricate or tidy.
- **Citations**: small source line at the bottom-left (>= 26 px): `(Nguồn: <tác giả/cơ quan>, <tên tài liệu>, <NXB>, <năm>)` and a references slide before the appendix. The pattern is fixed; **the content is the user's [ask]**: never invent author names, editions, years or page numbers. For classical texts quote the edition the course uses.
- Numbers: use the Vietnamese decimal comma consistently in prose if the course does; otherwise use one convention deck-wide. Dates `dd/mm/yyyy`.
- **Speaking pace for notes**: start at ~140 words per minute `[INFERENCE]` and calibrate with one timed rehearsal (`07`). Notes: signals not scripts, 150-300 characters per slide for a 1-2 minute slide is a good band to start; no "Slide này cho thấy".

## 7. Playbook E - Team deck (several authors)

1. **One style, one owner**: the first author builds the donor deck (cover, agenda, 6-8 archetypes); everyone else clones those donors (`copy-design` + `replace_text`), never their own template.
2. **Slide ownership table** (who owns which slides and which terms); the terminology sheet is shared.
3. Combine with `merge-designs { type:"create_new_design", operations:[insert_pages ...] }` from each member's design; **read titles back and fix order** (inserts can come back reversed); run `deck_audit.py` for alignment drift between authors.
4. Normalise with a single declared typography pass (`05`) so type sizes match across authors.
5. One person runs the final review (`04`) and the export (`07`). Rehearse the hand-offs between speakers: a hand-off is a transition sentence in the notes.

## 8. Generic rubric mapping (use when the lecturer gives none; replace with the real rubric [ask])

| Typical criterion | Where it is scored | What to show |
|---|---|---|
| Content accuracy | terminology, definitions, examples | zero drift (`text_diff.py`), sources on slides |
| Structure and logic | ghost-deck test, spine | titles tell the argument |
| Visual quality | hierarchy, consistency, readability | `deck_audit.py`, contrast, big type |
| Examples and application | example slides | 3-4 sourced examples with "why it fits" |
| Presentation / delivery | timing, notes, rehearsal | timed run, notes file |
| Q&A | backup slides, drills | question sheet with risk-level verbs |
| Teamwork (groups) | ownership table, seamless style | single style, clean hand-offs |

## 9. Pre-flight for a class deck (tick before generating)

- [ ] Rubric or lecturer criteria obtained (or generic mapping accepted)
- [ ] Source text in hand (definitions copied exactly); terminology sheet written
- [ ] Slot length known; slide count computed; Q&A time reserved
- [ ] Examples chosen from the course text; each tied to a domain
- [ ] User's own images collected (art band, figures); no generated facts planned
- [ ] `deck-rules.md` read; new corrections appended after review
