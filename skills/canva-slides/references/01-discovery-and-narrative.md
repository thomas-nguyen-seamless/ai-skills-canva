# 01 - Discovery, narrative and the slide plan (everything decided BEFORE `create-design`)

The plan is the contract. Structure cannot be repaired after generation: no page can be added in a transaction, no text box inserted, and `create-design`
paraphrases what you give it. A bad plan costs a regeneration; a good plan costs minutes. Sources merged: academic-pptx (SCR/spine, action titles, ghost-deck, timing,
defence playbook), minorun slide-story (hooks, crossheads, concept 3-piece set, 7-step body, timing units), power-design (mode token, word budgets), pitch-deck-mastery
and YC (12-slide arc, 3 vertebrae), canva-ppt-lesson-designer (challenge-before-acting, 8-field slide contract, lesson map), Nathanielguo and AI272 (timing),
official `branded-presentation` / `generate-deck` / `classroom-helper` (brief schema, document-degradation warning), consultant (hypothesis/answer first/so-what/pp vs %).

## 1. Intake: challenge before acting

Mandatory criteria: **(1) subject + source material, (2) audience and setting (course, lecturer, seminar, defence), (3) talk length in minutes, (4) language, (5) deliverables (slides / + notes / + Q&A), (6) visual direction or a reference image the user likes.**

- Missing **>= 2**: do not guess. Push back **once** with a pre-filled sample the user can answer in one line:
  `Chủ đề: ...; môn/lớp: ...; thời lượng: ... phút; số slide mong muốn: ...; phong cách: học thuật, nền sáng, chữ lớn; có ví dụ minh hoạ: ...`
- Missing **exactly 1**: pick a sensible default, say it in one line, continue.
- Never ask for what a tool or file already tells you; never open with "paste the plan or describe the topic" (official `classroom-helper`).
- If the user gives a plan, **respect its sequence and vocabulary**; flag each addition ("thêm ví dụ X").
- When the user supplies a picture they like (e.g. an engraving band), it is the style anchor: skip style probes, reuse the art on cover + closing (`06`).

### Durable preference file (`deck-rules.md`) - read first, append on every correction

The highest-leverage mechanism found (lecture-slides' 151 solved complaints; academic-poster's `poster-rules.md`): **record the user's corrections so the next run satisfies them on the first draft.**

1. Look for `deck-rules.md` in the user's working folder for the deck (ask where files go once; default `~/Documents/slides/<deck>/`). Template: `templates/deck-rules.md`.
2. Read it before planning; obey it as defaults.
3. Whenever the user says "bigger", "misaligned", "too empty", "more examples", "use my picture", append one dated line: the complaint, the measured fix, the rule.
4. Seeded rules for this user (observed 2026-11): Vietnamese; body 34-38 px and titles ~52 px on 1920x1080; consistent fonts and aligned format; real diagrams, not decorative art; many worked examples; rebuild as a new deck and keep the original; use the user's own engraving band on cover and closing; never idle-pad with AI stock imagery.

## 2. Source material and content integrity

Doctrinal and factual accuracy is the highest-severity failure mode (the generator once swapped "phổ biến" for "phát triển").

1. **Source ladder**: the user's textbook passages / notes > the user's original deck > anything fetched later (flag `[verify]`). Never fill gaps from memory silently.
2. **Terminology sheet** (`templates/` or the plan): the approved terms and exact formulations, plus banned mistranslations ("We say ___, never ___"). Example: the three properties of the negation of the negation are khách quan, kế thừa, phổ biến.
3. **Lesson/course map** (lesson-designer): when the course has a syllabus, keep a small map file: chapter -> knowledge units -> emphasis -> real-life hook -> visual idea. Content of every slide must trace to a unit.
4. **Content ledger** (beatdeck/medical): for a rebuild, list every source slide as `kept / merged / cut` with the reason. Deletion is a decision, never an accident. Zero omissions of source facts unless cut on purpose and listed.
5. **Never fabricate**: no invented quotes, numbers, citations, sources or "from the log". Illustrative numbers are labelled `ví dụ minh hoạ`. A misattributed quote on a slide is misinformation with nice typography.
6. **Percent vs percentage points**, absolute vs relative change, dates and units: check each against the source (consultant; academic QA gate).
7. Add **at least one honest caveat** or limit of the claim (minorun; academic Discussion).

## 3. Choose the mode token (one per deck, never mixed)

| Mode | Use | Visible words per slide | Bullets | Notes |
|---|---|---|---|---|
| `presenter` | big room, image-led, keynote | <= 25 | <= 3 | speaker carries the content |
| `talk` (**default for coursework**) | class presentation, seminar | <= 40 | <= 4 (<= 12 words each) | slide + speaker both carry content |
| `document` | read as PDF handout, thesis appendix | <= 75 | <= 6 | dense but hierarchical; 20-px-equivalent floors still apply |

Bullets are a fallback: prefer one statement, a diagram, a table or an example chain. Never paste paragraphs.

## 4. Choose the spine (and the narrative stance)

Pick **one** spine, say it in one sentence ("spine sentence"): if you cannot, the deck is not ready.

| Spine | Shape | Use |
|---|---|---|
| **SCR** | Situation -> Complication -> Resolution | defence, argument-driven talks |
| **Funnel + Answer** | broad context -> gap -> approach -> findings -> implications | academic/research |
| **Answer first** | conclusion, then support | grant panels, executives, time-pressed audiences |
| **Concept deck** (default for philosophy/coursework) | hook -> concept 3-piece set -> mechanism (one diagram) -> examples -> methodological meaning -> caveat -> takeaway | explaining a law or theory |
| **Lesson spine** | opener -> objectives -> prior knowledge -> content -> example/practice -> summary -> closing/assignment | teaching a class |
| **Investor 12** | title, problem, solution, why now, market, product, traction, model, competition, team, financials, ask | fundraising only |
| **3 vertebrae** | insight -> solution -> proof, must survive every slide | compression check for any deck |

**Concept 3-piece set** (minorun): (1) *what is X* - one-line definition (+ etymology breakdown when it helps); (2) *why it matters* - before vs after; (3) *put crudely, it is Y* - the one-liner students remember. Order: abstract -> concrete -> metaphor, and the slide after a metaphor must derive the point from it.

**Hook** (never open with a definition): empathy ("ai cũng từng thấy..."), a provocative question, a news hook, or a personal status line; then **two audience questions** whose second thins the hands.

**Narrative stance is audience-conditional** (resolving the answer-first vs withhold-the-answer contradiction): answer-first for executives, panels, investors; progressive disclosure for teaching, conference talks and defences. Declare it in the brief and hold it deck-wide. For a lecturer-graded coursework deck: keep a **short agenda slide** (graders expect orientation), disclose the *answer* progressively inside sections, end on a **takeaway slide that stays up during Q&A** (never end on "Thank you" alone; the closing slide may carry a thanks line plus the takeaway).

**Crossheads** (decks >= 10 slides): a divider that carries the audience's inner-voice question, answered by the very next slide; one line only; max 2 in a row; one every 3-6 body slides; an unanswered crosshead is deleted. Use dividers only when the deck has >= 3 real parts.

**Staging devices** (use 2-3, never zero): build-up diagram across slides; pre-empt a misunderstanding; rebut an expected objection; etymology/name trivia; one honest caveat slide; a personal coinage for a real experience.

## 5. Slide count and time

Rules of thumb (pick the model by deck type; do not mix models in one estimate):

| Deck type | Pace | 10 min | 15 min | 20 min | 45 min |
|---|---|---|---|---|---|
| Academic / argumentative (academic-pptx) | <= 1 content slide per minute | 8-10 | 12-14 | 15-18 | 30-40 |
| Lecture / teaching (lesson-designer, vstorm) | ~1 per 1.5-2 min | 6-7 | 8-10 | 10-13 | 22-30 |
| Defence (each slide carries an argument) | ~1 per 2-3 min | 4-5 | 6-8 | 8-10 | 15-22 |
| Fast demo / lightning (minorun) | 16-30 s per body slide; cover and crossheads 8 s | ~35 total at 10 min | | | |

Time planning facts:

- Finish **1-2 min under** the slot (academic) and up to ~5 min under on-site; plan the main script to **~90%** of the slot and subtract a known Q&A block first.
- Per-slide-type seconds (Nathanielguo): cover 15-30; section divider 10-20; simple conclusion 30-60; ordinary content 45-90; chart 60-120; process 60-120; core solution 90-180; case/example 90-180; summary 60-120; appendix 0. Bounded modifiers: text density 0.85/1.0/1.15, chart complexity 1.0/1.15/1.3, key slide 1.2-1.5. Never reward clutter with time.
- Mark **2 cut triggers** at crossheads ("if past minute N here, skip slide k"); never cut crossheads.
- `plan_check.py` flags decks outside 0.7-3 min per content slide and errors when a deck is clearly too long. Recompute at four checkpoints: structure fixed, slide count +/-5, before delivery, the day before.
- Slide count is a function of time, not of source length: backup slides (appendix) hold the rest and cost no time.

## 6. The per-slide record (one row per slide; this is also the `create-design` outline)

| Field | Content | Rule |
|---|---|---|
| `n`, `role` | cover, agenda, definition, three-up, comparison, chain, diagram, quote, example, summary, sources, closing, backup | pick from the archetype library (`06`) |
| **title** | an **action title**: a full-sentence claim, <= 65 chars, <= 2 lines | **ghost-deck test**: titles alone must carry the whole argument |
| **claim / what the audience must understand** | one sentence | one job per slide; if it needs "and", split |
| **points** | <= mode budget, each <= 12 words | telegraphic is fine |
| **visual** | kind (definition, chain, cycle, table, matrix...) + native or image | every slide has a visual element; title and visual must not repeat each other |
| **evidence / example** | what proves it; source | cite on the slide (small); invented numbers labelled illustrative |
| **notes seed** | 2-5 sentences or the transition | notes live in a sidecar file (`07`) |
| **time** | seconds | from the table above |

Page-type contracts (0frost0): *definition* -> the audience can restate it in their own words (failure: a quote with no reading); *three-up* -> three parallel items of the same kind (failure: items of different kinds); *comparison* -> the difference that matters (failure: attribute lists with no verdict); *example* -> why this case is an instance of the law (failure: a story with no link back); *diagram* -> the relation the words cannot show (failure: decoration); *summary* -> what to remember (failure: a new idea); *limitations* -> where it breaks (failure: only strengths).

## 7. Examples: plan them like a feature

For concept decks the examples carry the grade. Plan **>= 3-4**, from different domains (e.g. nature, society, thought/technology/science), each as: *name -> 3-step chain -> one sentence on why it instantiates the law -> source if factual*.

- Choose cases that would not make sense without the concept; prefer ones the lecturer will recognise from the course.
- Every chain shows the *change that carries over* (what was kept) and the *change that is new*, so the example proves the concept rather than decorating it.
- Put the link back to the concept in an editable caption (not baked into an image).

## 8. Substitute for the outline-approval widget

No widget exists in this MCP. Gate in the chat instead:

1. Print the plan as a table (`# | role | action title | visual | time`) plus the spine sentence, mode token, minutes and the terminology list.
2. Run `scripts/plan_check.py` first; fix every ERROR, resolve or accept every WARN.
3. Decks > 10 slides, or any deck for grading/defence: ask **once** ("Chốt kế hoạch này chứ?") before spending a generation. Short or low-stakes decks: state the plan and proceed.
4. If the user edits the outline, re-lint, then show a diff of titles only.
5. Never call `create-design` before the plan exists on screen and has passed the lint.

## 9. Style direction (derive, do not pick from a menu)

Menus cause sameness (huashu, SlideSpeak). Derive the look from the subject:

- **Anchor**: a user reference (image, existing deck) > the subject's own material (engraving, manuscript, diagrams) > a stated stance.
- Write a **5-line design stance** in the plan: palette (ground + one accent), type character, image language, density register, what to avoid.
- If the user has no preference and the deck matters: produce **<= 3 short probes** (2-3 slides each with `create-design`, costs generations), show the thumbnails, let them pick, quote their words into `deck-rules.md`. Add options, not bans.
- Details (palette construction, type scale, grid) are in `03-visual-system.md`; the generation brief that carries the stance is in `02-outline-and-generation.md`.

## 10. Plan artifacts to produce

- `plan.json` (sections + mode + minutes) - machine-checked by `plan_check.py`.
- `plan.md` - the human table plus spine, stance, terminology sheet.
- `deck-rules.md` - updated with anything learned.
- Keep them next to the deck; the plan is also the input to `text_diff.py` after generation.
