# Cluster 04 — Slide craft for academic and pitch storytelling

**Reader:** SlideCraftAcademic · **Date:** 2026-11-07 · **Target:** one Canva-MCP slide skill (SKILL.md + references)
**Sources:** markdown/JSON clones under `/tmp/skills-src` (`.git` excluded). All paths below are relative to `/tmp/skills-src`.

**Method.** All non-`.git` markdown/JSON in the eight repos was read, with two disclosed exceptions handled structurally rather than line-read: (a) the 72 `brands/*/brand-style.md` files in power-design — headings, colour rows and token blocks across all 72, plus an accent-row audit (8 files have no accent row) and a check that two schema generations coexist; their prose is boilerplate permutations of one schema; (b) the 22 Marp examples in robonuggets — slide-block split, CSS tokens, headings and representative bodies; 20 of them are 3–4-page specimens with no CSS classes (all inline styles), so line-reading adds no rules beyond `SKILL.md`. Claims are tagged with the file and the nearest heading; line numbers are given where the repo is small enough for them to stay stable. Where a repo references a file that is not in the clone, that is called out — the clones are **sparse/partial** (markdown + JSON only; no `LICENSE`, no `theme/`, no `tools/`, no HTML templates, no scripts).

**License facts (recorded, not acted on).** No repo in this cluster contains a `LICENSE` file in the clone. Licenses below are what the repo *states*. `academic-pptx-skill` is contradictory: its README says MIT, its SKILL.md front-matter says `license: Proprietary. LICENSE.txt has complete terms`, and no LICENSE.txt is present.

---

## Inventory

| Skill (repo dir) | Repo path | License (as stated; no LICENSE file in clone) | What it is, in one sentence | Verdict |
|---|---|---|---|---|
| academic-pptx-skill (Gabberflast) | `Gabberflast_academic-pptx-skill/` | **Conflicting**: README "MIT"; `SKILL.md` front-matter "Proprietary. LICENSE.txt has complete terms" | Content-and-structure rulebook that overrides "design-forward" defaults for conference/seminar/thesis/grant decks, with a companion per-slide PptxGenJS pattern file. | **A−** — the best argument-architecture material in the cluster (action titles, ghost-deck test, exhibit discipline, deck architecture, timing), but the design half is thin and its own two files disagree. |
| power-design (ItsssssJack) | `ItsssssJack_power-design/` | README "MIT — see LICENSE" (absent) | Brand DNA + codified-rulebook generator for HTML decks and sites; the deck half is a 20-rule numeric field manual with sources. | **A** — the single most reusable artifact here: 20 rules with hard numbers, a numbers cheat sheet, and a contradiction-resolution table. Medium (HTML) does not transfer. |
| medical-ppt-designer-skill (yushengchen519-cmd) | `yushengchen519-cmd_medical-ppt-designer-skill/` | README "MIT — see LICENSE" (absent) | Methodology for medical academic decks: template fidelity, content integrity, density-adaptive typography, image-first layouts, three-layer QA. | **A−** — content-integrity policy, adaptive type tiers, image-size floors and the three-layer QA are directly transferable; "template is sacred" is unreachable in Canva. |
| pitch-deck-mastery-skill (Stevekaplanai) | `Stevekaplanai_pitch-deck-mastery-skill/` | README "MIT" (absent) | 12-slide investor narrative + stage adjustments + review checklist, backed by a directory of 10 external resources to fetch. | **B** — strong content framework and review gates; no production guidance at all, and the resource list is a 2024-era link farm. |
| yc-pitch-deck-max (josezuma) | `josezuma_yc-pitch-deck-max/` | README/SKILL/manifest "MIT" (absent) | Claims a 10-skill YC deck system (content, design, PPTX/HTML/Marp, audit, investor Q-bank). | **C** — a **thin wrapper**: manifest lists 10 skills but only `.claude/skills/create/SKILL.md` exists; `scripts/`, `references/design.md` are missing; CI runs nonexistent scripts. Two ideas survive (3 vertebrae, founder interview). |
| beautiful-hackathon-slides (Esther2524) | `Esther2524_beautiful-hackathon-slides/` | README "MIT" (absent) | 9-phase process for distinctive hackathon/Demo-Day decks: clarify → curate 5 of 13 visual styles → build → PLAN.md → iterate → narrated video → submit. | **A−** — the best *process* discipline in the cluster (context files, visual option previews, narration budget); HTML-only output, and its `assets/*.html`, `preset-samples/` are absent from the clone. |
| minorun-marp-skill (minorun365) | `minorun365_minorun-marp-skill/` | README "Apache License 2.0" (LICENSE absent; bundled illustrations explicitly excluded) | Three Japanese sub-skills — story (`slide-story`), figures (`slide-figures`), dark-theme design balance (`slide-design-dark`) — distilled from years of the author's own speaker decks, with measured thresholds and PDF/SVG check scripts. | **A** — the most *craft-dense* material in the cluster: crosshead theory, "don't reveal the answer", measured timing units, luminance ladders, figure-integrity rules. Marp/PDF tooling does not transfer, the rules do. |
| marp-slides (robonuggets) | `robonuggets_marp-slides/` | README "MIT" (absent) | Marp component cookbook: theme variables, dashboard cards, SVG chart recipes, icon paths, 22 "reference decks". | **C+** — useful component/chart vocabulary and font-pairing table, but 20 of the 22 "decks" are 3–4-page style specimens (the other two are 17 and 21 pages); no narrative, no QA, no density model beyond 8 rules. |

**Clone gaps that affect this reading** (verified by `ls`): Esther `assets/style-preview-template.html`, `assets/live-demo-template.html`, `assets/preset-samples/`; minorun `theme/`, `tools/`; josezuma `scripts/`, `references/design.md`; power-design `principles/images/`; medical `LICENSE`; every repo's `LICENSE`. The prose describes these as central, so the notes below judge only what is present.

---

## Skill: academic-pptx-skill

### Purpose

Governs **content, argument structure and design standards** for any deck where the audience will evaluate reasoning and evidence — conference papers, seminar talks, thesis defences, grant briefings, lab meetings, policy briefings (`SKILL.md` front-matter and "How This Skill Works"). It explicitly delegates file mechanics (pptxgenjs/editing/QA) to a separate PPTX skill and says to read both before writing any code.

Two modes (`SKILL.md` §Step 1):
- **Structured Argument** — the default. Priority order is stated verbatim as: argument structure → data → layout → aesthetics.
- **Visual / Narrative** — public engagement, science communication, lay funding panels, keynotes; visual storytelling wins but argument still matters.
- Rule of thumb: if the user mentions a paper, study, dataset, thesis, grant or conference, assume Structured Argument.

### The prescribed process (numbered, from `SKILL.md` §Step 1–4 and `content_guidelines.md`)

1. **Classify the deck type** (Structured Argument vs Visual/Narrative) before planning a single slide; when in doubt choose Structured Argument.
2. **Produce a slide-by-slide outline** containing, for each slide, the title, the action title and the exhibit type; confirm the outline with the user if the deck exceeds 10 slides or the content is complex.
3. **Do not build until the outline is agreed** — the outline is the contract.
4. **Run the ghost-deck test on the outline**: read only the action titles in sequence; they must tell the whole argument. If they don't, repair the titles or the structure first.
5. **Apply the academic design standards**: white content backgrounds, one sans-serif face, ≤3 colours, the specified type scale, left-aligned body, a single grid with ≥0.5 in margins, figure-left/interpretation-right.
6. **Build the deck** using the PPTX skill, following `slide_patterns.md` for per-slide-type structure.
7. **Run two QA passes**: technical QA from the PPTX skill (content extraction via markitdown, visual QA from rendered slide images, a fix-and-verify loop that repeats until a full pass produces no new issues) and then the academic checklist.
8. **Deliver**: conclusions slide on screen, references slide before the appendix, contact/QR on the final slide.

### Argument structure (numbered, from `content_guidelines.md` §1)

1. **Lead with the research question** — state the central question or claim explicitly by slide 2 or 3 at the latest; never bury it.
2. **Choose one narrative spine and keep it**:
   - **SCR** — Situation (what was known) → Complication (what is missing/broken/contested) → Resolution (your contribution).
   - **Funnel + Answer** — broad context → specific gap → approach → findings → implications.
   - **Answer First** — conclusion first, then support; reserved for senior or time-pressured audiences (grant panels, advisory boards, short talks).
3. **One argument per presentation** — pick the claim that can be made convincingly in the slot; everything else goes to the appendix.
4. **One job per slide** — if a slide is doing two things, split it.
5. **Flow test** — each title should make the next one feel like a natural consequence; a slide that could sit anywhere without loss is misplaced or dispensable.

### Action titles (the core mechanic)

- Every content-slide title is a **complete sentence stating the takeaway**, never a topic label (`content_guidelines.md` §2).
- Worked conversions: "Results" → "Treatment effect is significant across all three cohorts"; "Data" → "Dataset covers 40 years of county-level panel data"; "Methodology" → "Regression discontinuity exploits a sharp funding threshold".
- **Ghost-deck test**: titles alone must carry the argument.
- Length: **1–2 lines**; if more is needed the point is not sharp enough.
- Type: **24–28 pt, bold**; readable from the back of the room.
- Titles are mirrored by chart titles in practice — the power-design rule "chart title = conclusion, not topic" is the same idea applied one level down.

### Exhibit discipline (numbered, from §3)

1. **One exhibit per slide** (one chart, table, diagram, equation block or map).
2. **Earn its place** — cover the exhibit and read the title: if the title still stands alone, the exhibit is decorative; cover the title and look at the exhibit: if the takeaway is not obvious, the annotation is too weak.
3. **Annotate the key finding on the chart** — call-out arrow/label, shaded region, text annotation ("↑ 23% above baseline") or a different colour on the focal series; do not make the room hunt.
4. **Self-sufficient slide test** — someone reading the slide as a handout or PDF must get the point without narration.
5. **Figure left, interpretation right** (~5.5 in / ~3.5 in in the 10 in-wide pattern), matching left-to-right reading order.
6. **Prefer graphs to tables** for trend/comparison/distribution; reserve tables for exact-value comparisons.
7. **Rebuild figures from the paper** — paper figures are print-resolution with small type; rebuild at presentation size with **axis labels ≥16 pt**.
8. **Do not include an exhibit you will not discuss** — undiscussed material moves to the appendix.

### Text, citation and accessibility rules

- **Body text ≈40 words maximum per content slide**; more means the slide does too much or the material belongs in an appendix/handout.
- **3–5 bullets typical; >5 is a warning sign**; one idea per bullet; telegraphic style is explicitly allowed ("Intervention reduced costs by 23% (p < 0.01)").
- **Body 20 pt floor** — a floor, not a target; if text must be smaller to fit, remove content until it fits at 20 pt.
- Bold for first-use key terms, inline labels ("Note:", "Limitation:") and the focal finding; italics for statistical notation, species names, titles — never decoration.
- **Cite on the slide**: every borrowed claim/figure/dataset gets an in-slide citation at the bottom in **12–14 pt muted**; field-standard format (Author, Year) or footnote/superscript; oral attribution before the citation appears; figure captions directly beneath the figure.
- **References slide**: complete citations for everything cited, immediately before the appendix.
- Accessibility: **≥20 pt body, ≥24 pt titles**, high contrast, never colour alone, alt text on figures if circulated as PDF; define acronyms on first use; avoid idioms for international audiences.

### Deck architecture (required order, §6)

1. **Title** — full title framed as statement or question; authors, affiliations, venue, date.
2. **Motivation / Context (1–2)** — why the problem matters; SCR's Situation and Complication.
3. **Research Question / Hypothesis (1)** — its own slide, stated precisely; "this slide must exist".
4. **Methods (1–2)** — only what the audience needs to evaluate the findings (identification strategy, sample, variables; or data sources and analytical approach).
5. **Results (n)** — one finding per slide, one exhibit, action title states the finding, key result annotated.
6. **Discussion / Implications (1–2)** — interpret, reconnect to the opening question, state the main limitation directly to pre-empt the objection.
7. **Conclusions (1)** — 2–4 takeaways; **stays on screen through Q&A**; do not follow it with "Thank You" or a blank.
8. **Contact / Next steps** — email or URL, QR/short link to slides or preprint, "work in progress — feedback welcome" if apt.
9. **References** — complete, consistently formatted.
10. **Appendix** — pre-built Q&A slides, robustness/sensitivity, extra data, derivations; each labelled ("Appendix A: Robustness Checks").

### Timing and slot management (§7)

- **Maximum one slide per minute.** 10-minute talk → **8–10 content slides**; 15 min → **12–14**; 20 min → **15–18**; 45-minute seminar → **30–40**.
- Rehearse aloud; finish **1–2 minutes under** time; overrunning at a conference is described as "a significant professional misstep".
- Mark in advance which slides to cut; prioritise research question, key result, conclusions; compress methods and context first.
- Q&A: anticipate the **3–5 most likely questions** and pre-build an appendix slide for each; invite "questions or feedback" rather than "any questions".
- End on conclusions with that slide already on screen.

### Thesis-defence guidance (honest note)

The repo has **no dedicated thesis-defence section** — "thesis defense" appears only as a trigger and as an example of Structured Argument. The defence playbook is therefore an assembly of existing rules, and should be presented as such in the merged skill:

1. Use Structured Argument mode (thesis defences are named explicitly in `SKILL.md` triggers and mode list).
2. Research question gets its own slide by slide 2–3.
3. Methods limited to what the committee needs to judge validity; everything else to the appendix.
4. Discussion must state the main limitation directly.
5. Conclusions slide stays up during the viva/Q&A; committee questions map to pre-built appendix slides (the skill's own examples: "why not use X method?", "how does this compare to Y?", "what about endogeneity?", "is the sample representative?").
6. Strict time discipline; 1–2 minutes of slack; know the cut list.
7. References slide before the appendix; contact/QR last.

### Design standards and the concrete pattern file

`SKILL.md` §Step 3: white background on content slides; one sans-serif face (Arial/Calibri/Helvetica); **max three colours** — dark navy `1F4E79` primary, mid-blue `2E75B6` accent, white/off-white ground; **no gradients, no decorative icons, no accent lines under titles, no full-bleed images on content slides**; left-align body, centre only titles and axis labels; consistent grid with **≥0.5 in margins**; 16:9 default.

`slide_patterns.md` "Global Defaults" fixes the numbers (10 × 5.625 in canvas):

| Token | Value |
|---|---|
| Background / primary / accent | `#FFFFFF` / `#1F4E79` / `#2E75B6` |
| Body / muted / rule | `#2D2D2D` / `#777777` / `#CCCCCC` |
| Highlight callout | `#FFF2CC` (use sparingly) |
| Type scale | title 26, section header 22, body 20, chart label 16, citation 13 |
| Margin | 0.5 in minimum |
| Breadcrumb bar | 0.28 in tall, 10 pt labels, for talks >15 min |
| Section dividers | required for decks >15 slides |
| Appendix label | 14 pt muted italic |

### Unique ideas

- **The ghost-deck test** as a *pre-build* gate, not a post-hoc check — it is applied twice (outline and finished deck).
- **Exhibit "cover test" in both directions** (title without exhibit, exhibit without title) to prove the exhibit earns its place.
- **One job per slide** phrased as an argumentative role, not a content count.
- **Appendix as pre-built Q&A ordnance**, keyed to the 3–5 anticipated questions.
- **Contact/QR on the conclusions slide** rather than a throwaway final slide.
- **Cut-list marking** (small corner indicator) so the presenter can shorten live.

### Pitfalls it warns about (§9 table)

Topic labels as titles; presenting the whole paper; reading slides aloud; evidence with no "so what"; uncited borrowed figures; body under 20 pt; inconsistent formatting; slides you won't discuss; overrunning; ending on "Thank You"; burying the research question; missing references slide.

### What is outdated, wrong, or impossible against our MCP

| Prescribed | Status in our Canva MCP | Adaptation |
|---|---|---|
| PptxGenJS coordinates, shapes, addText boxes (`slide_patterns.md` throughout) | No code path; no new text boxes; no shape creation | Convert to *target element roles* + `perform-editing-operations` on existing elements; delete/cover what cannot be edited |
| "Single font face (Arial/Calibri/Helvetica)" | `format_text` has **no font-family** | Lock the family at `create-design` time; if the generated deck uses several families, either accept or regenerate |
| Navy title-slide background, accent rules, divider bars, breadcrumb bars | No background-change op; no shape creation; no page-number op | Use the generated template's own title treatment; breadcrumbs/division markers are impossible unless baked into the generated design |
| Add a References slide / appendix section | No page-add op; `merge-designs` can insert pages from another design | Generate appendix/reference pages as a separate design (or via `copy-design` of an existing page) and merge; verify order (known reversal bug) |
| 12–14 pt citations | Achievable | Apply `format_text` size/colour; but 12–14 pt on a 1920×1080 canvas is far below the classroom floor — see Contradictions |
| Presenter notes / narration | `get-presenter-notes` is **read-only** | Deliver narration as a sidecar markdown (see Esther, minorun) |
| Content QA via markitdown | No local file | Use `get-design-content` (read-only text extraction) as the equivalent |

---

## Skill: power-design

### Purpose and workflow

Produces brand-native HTML — either a **deck** (fixed 16:9) or a **website** (fluid) — from two inputs: brand DNA and a codified rulebook. Deck path (`SKILL.md` "Path A"):

1. **Establish the medium** (deck vs site) before anything else.
2. **Establish the brand**: paste a URL (Firecrawl `branding` scrape), pick from the 72-brand library, or use a neutral house style. Minimum viable extract is six values: background, foreground, accent, display font, radius, one voice sample (`lib/extract-brand.md`).
3. **Ask for the deck brief**: headline + 3–5 key points + audience — "that's enough".
4. **Confirm logo placement once** — default is a small wordmark bottom-left, ~24 px tall, inside the 5 % safe zone, on every slide.
5. **Read both** `principles/design-principles.md` (all 20 rules, described as non-negotiable) and the chosen brand file.
6. **Emit a single self-contained HTML file**, then run the 21-item pre-emit checklist.
7. **Open it in the browser** and iterate in natural conversation.

### The 20 codified slide principles (complete numbered list, with thresholds)

Source: `principles/design-principles.md` "TL;DR — The 20 Rules That Matter Most for Slides" (lines 8–31), expanded in §1–§11 and tabulated in Appendix A.

1. **One idea per slide** — one headline of **≤10 words** plus at most one supporting block; a second headline means split. (Reynolds; Duarte)
2. **Glanceable in ≤3 seconds** — the single message must land in three seconds; otherwise simplify or split. (Duarte; NN/g)
3. **At most 7 ± 2 visual chunks, ideal 3–5** — group with proximity into 3–5 super-chunks; the stricter Cowan limit (≈4) is recommended for slides, so a 6-bullet list is a violation. (Miller 1956; Cowan 2001)
4. **Whitespace ≥40 %** of slide pixels on information slides; **≥60 %** on hero/title/section slides; **≥70 %** on quote slides. (Refactoring UI; Presentation Zen)
5. **Edge safe zone = 5 % of width on every side** — **≥96 px** at 1920×1080; no text, logo or focal element inside it. Raise to **8 % (154 px)** if front rows may crop the projection. (Broadcast title-safe; Apple HIG)
6. **One modular type ratio**, chosen once: **1.200, 1.250, 1.333 (default), 1.414, 1.500 or 1.618**; every size derives from it, no ad-hoc sizes. Default 1.333 on a 20 px base yields 20 / 27 / 36 / 48 / 64 / 85 / 113, rounded to 20 / 28 / 36 / 48 / 64 / 84 / 112. (Tschichold; Bringhurst; Brown)
7. **≤4 type sizes per slide, ≤6 per deck** — display, subhead, body, caption; reject any size outside the token array. (Refactoring UI; Müller-Brockmann)
8. **Body ≥24 px on screen, ≥28 pt for projection; title ≥48 px; caption floor 18 px**; footer/source **14–16 px at 50–60 % opacity**. Concretely: projected body ≈ **37 px** at 1920×1080. (Reynolds; Duarte; AAP)
9. **Line-height 1.4–1.6 body, 1.25–1.4 subhead, 1.0–1.2 display**; formula `1.5 − (px − 16) × 0.005` clamped to [1.0, 1.6]. (Butterick; Bringhurst)
10. **Line length ≤60 characters body (ideal 45–60), ≤30 characters display** (`max-width: 60ch` / `30ch`). (Bringhurst; Butterick)
11. **WCAG contrast**: body **4.5:1** (AAA 7:1), large text **3:1** (AAA 4.5:1), UI/graphical **3:1**; design at 7:1 because projectors wash out 30–50 %. (WCAG 2.2)
12. **60-30-10 colour split** — 60 % dominant (usually neutral ground), 30 % secondary, 10 % accent; accent should measure **5–15 %** of pixels; <2 % means no focal accent. (Itten; Refactoring UI)
13. **One accent per slide** (and one per deck) — multiple accents means no accent. (Tufte's smallest effective difference; Schoger)
14. **Never encode meaning in hue alone** — pair colour with shape, label, icon, weight or position; ~8 % of men have red-green colour blindness. (WCAG 1.4.1; Brewer)
15. **8-pt spacing grid** — every margin/padding/gap is a multiple of 8 (4 permitted inside icons); scale **4, 8, 12, 16, 24, 32, 40, 48, 64, 80, 96, 128, 160, 192, 256**. (Jackson; Material)
16. **One 12-column grid, 24–32 px gutters, 96 px outer margin** at 1920×1080 — column ≈117 px; common spans 4/6/8/12; everything snaps, sub-4 px misalignment is snapped. (Müller-Brockmann)
17. **Proximity: related ≤16 px apart, unrelated ≥48 px apart**, and the between-group gap must be **≥2×** the within-group gap. (Wertheimer; Williams)
18. **Data-ink ratio ≥80 %** — no 3D, no gradients on data, no drop shadows on bars, **≤4 horizontal gridlines at 50 % opacity**, no redundant legends, direct labels preferred. (Tufte 1983)
19. **F-pattern for text, Z-pattern for image-led slides** — headline + key visual in the top band; most important element in the top-left quadrant or the first **30 %** of slide height. Mirror for RTL. (NN/g 2006–2023)
20. **Pick one mode per deck and never mix** — *presenter mode*: **≤15 words/slide** (rejects >25), image-led; *document mode*: dense but hierarchical (rejects >75 words or a slide with no headline). (Tufte vs Reynolds synthesis)

Supporting principles that the 20 summarise, with extra numbers worth importing:

- **Fitts (slides)**: dominant focal element **≥25 % of slide area or ≥3×** the next element; interactive targets ≥44×44 px.
- **Focal point**: exactly one per slide; **≥1.5× the area** of the next largest, or the only saturated element, or isolated by **≥48 px** more whitespace.
- **Scale hierarchy**: headline:body ratio **2.0–4.0**; subhead:body **1.25–1.5**; avoid size steps of only 10–20 %.
- **Weights**: allowed 400/500/600/700 (+800/900 display); ban 100–300 for body (they vanish under projection).
- **Symmetry**: if the two side margins differ by **≤5 %** of width, snap to true centre; otherwise force **≥15 %** asymmetry — the near-symmetric middle is the failure.
- **Figure/ground on images**: scrim **40–70 %** opacity, or text shadow ≥2 px/30 %, or move text to a solid zone; re-measure contrast at **9 sample points**, ≥4.5:1 everywhere.
- **Cards**: padding ≥24 px, gap ≥24 px.
- **Icons**: sizes ∈ {16, 20, 24, 32, 40, 48, 64, 96}; inline icons = 1 em; never <16 px.
- **Charts**: **≤5 series** per chart, beyond that small multiples; chart title must contain a verb or comparison.
- **Word budgets**: title slide ≤10; section divider ≤8; content presenter ≤25; content document ≤75; quote ≤30; closing ≤10; **≤3 bullets, ≤8 words per bullet**.
- **Split triggers**: over budget; more than one headline-worthy claim; >5 chunks after grouping; two equal-weight charts; more than one accent moment.
- **Hick**: ≤1 call-to-action and ≤1 decision per slide; visible options ≤3 (pricing: 3 tiers, middle highlighted, scaled 1.05×).
- **Animation**: transitions ≤300 ms, no flashes >3/s.
- **Mayer's multimedia rules**: coherence (every element earns its place), signalling (1 accent + 1 weight emphasis per slide), redundancy (notes ≠ on-screen text verbatim), spatial contiguity (**label-to-target ≤32 px**), temporal contiguity, modality.
- **Williams CRAP**: contrast (size ≥1.5×, weight ≥200 apart, colour ≥3:1), repetition, alignment, proximity.

### The pre-emit checklist

`SKILL.md` "Pre-emit checklist (slides)" restates all 20 as one-line gates plus **#21: brand logo on every slide unless opted out**. It is the most directly reusable artifact in the repo — a 21-line pass/fail gate that maps cleanly onto a programmatic review of a Canva deck (each line becomes a check on text length, size tokens, spacing values, accent count, chart type).

### Unique ideas

- **Refuses unmeasurable rules.** The document's opening states that rules resisting measurement were rewritten as concrete checks — this is why it is the best merge source: every line is testable.
- **Mode as a deck-level token** (`presenter` / `document`) that changes every downstream budget (words, density, contrast target, split triggers).
- **A contradiction-resolution table** (§13) that adjudicates Tufte vs Reynolds, 6×6 vs no bullets, golden ratio vs 8-pt grid, symmetry vs asymmetry, brand saturation vs WCAG, Krug vs Tufte.
- **A numbers cheat sheet** (Appendix A, ~75 values) that can be lifted almost wholesale into a skill appendix.
- **Brand extraction with a six-value minimum** and a documented white-fill-SVG-logo bug (`lib/extract-brand.md`).
- **72 brand systems** (verified: 72 directories, `brands/_template.md` schema) — but two schema generations coexist and **8 files have no "Accent" row**, so a consumer must not assume uniform keys.

### Pitfalls it names

Purple-gradient heroes; six-bullet slides; drop-shadowed bars; centred-everything; multiple accents; ad-hoc spacing; paragraphs; mixing presenter/document mode; omitting the logo. Internal tension: §1 signal-to-noise bans "logos repeated on every interior slide (footer logo only on title + closing)" while `SKILL.md` default #21 puts the logo on every slide.

### What is outdated, wrong, or impossible against our MCP

| Prescribed | Status | Adaptation |
|---|---|---|
| Emit HTML/CSS (the entire output contract) | We emit a Canva design | Keep the rules as **brief text + review rubric**; translate CSS numbers (px, ch, em) into Canva px/weight/colour |
| Brand DNA via Firecrawl, 72 brand files | Our account has **zero brand kits/templates**; no Firecrawl in the MCP | Use the brand library as a *palette source* only; inject colours via `format_text`/`update_fill`; palette must be chosen before `create-design` because backgrounds cannot change later |
| Logo on every slide, positioned bottom-left | No shape insertion; logo requires upload + per-page positioning; `insert_fill` sits above existing elements | Upload a logo once (`create-upload-url`) only if the user supplies one; otherwise omit and say why |
| Custom web fonts, weights 800/900 | No font-family op; weight set is limited to the existing runs | Treat weight/colour/size as the only hierarchy levers |
| Hairlines, divider rules, cards, gradients | No shape creation | Use existing template shapes; otherwise bake diagrams/rules into uploaded images |
| Page count flexibility, section dividers | No page add/remove outside `merge-designs` | Generate the intended page count in `create-design`; build divider/appendix pages as a separate design and merge |
| 60 % background share | Background cannot be changed after generation | Front-load the ground colour in the `create-design` brief |

---

## Skill: medical-ppt-designer-skill

### Purpose

A methodology for medical academic decks (case reports, grand rounds, journal club, research, teaching) whose central claim is that **medical content integrity must coexist with professional design** (`README.md`). It positions itself explicitly against general-purpose slide defaults (one idea, minimal text, big whitespace), which it says are right for marketing and wrong for medicine.

### Seven-phase workflow (`README.md`, `docs/DESIGN_PHILOSOPHY.md`)

1. **Template analysis** — inventory masters, fonts, colours, placeholders *before* any generation; never redesign the template.
2. **Content extraction** — extract and preserve all clinical content from the source, exact terminology, measurements, dates.
3. **Layout planning** — choose layouts from content shape (image count, grouping), not aesthetics; produce a slide-by-slide outline.
4. **Slide generation** — apply the prompt library and layout patterns, using adaptive typography per slide density.
5. **Designer review** — self-review against the 8 principles, reporting pass/fail per principle with slide numbers.
6. **Medical QA** — verify zero content loss and clinical accuracy against source.
7. **Final submission** — file integrity, visual inspection at 100 %, cross-references, naming, multi-platform testing.

The case study (`docs/CASE_STUDY_ORTHODONTICS.md`) reports that adding phases 1 and 3 cut iteration rounds from **~8 to ~2**, and that **2–3 refinement passes** were still needed after first generation.

### The 8 permanent principles, in priority order (`docs/DESIGN_PRINCIPLES.md`)

1. **Content integrity first** — every piece of source information appears in the final deck unless a human clinician removes it; zero omissions; enforced by source-vs-slide comparison.
2. **Template fidelity** — always inherit, never redesign: backgrounds, logo position/size, colour scheme, masters, footers, aspect ratio are untouchable; only editable content regions change.
3. **Adaptive typography** — font size responds to content volume, never the reverse; never one fixed size across all slides; sizes must fall inside the density tier's range.
4. **Canvas utilisation** — allocate **~60 % primary content, ~25 % supporting, ~15 % breathing room**; a slide with 40 % blank while content is crammed in a corner has failed.
5. **Visual balance** — distribute weight across the horizontal axis; no slide with everything on one side; consistent margins.
6. **Medical images first** — images are evidence: place them first, flow text around them, never shrink them to fit more text; images **≈60 % of slide area** when present (**≥50 %** enforced).
7. **One visual focus per slide** — one primary visual (a 2×2 grid of related images can be one composite focus); two stories = two slides; test: state the main point in one sentence.
8. **Professional academic style** — no clip art/stock/irrelevant icons, no animated transitions, no non-standard fonts, no saturated colours outside the palette, no emoji, no marketing language; test: could the slide appear in a journal without embarrassment?

**Conflict hierarchy** (stated explicitly, highest first): Content Integrity → Template Fidelity → Medical Images First → One Visual Focus → Canvas Utilisation → Visual Balance → Adaptive Typography → Professional Academic Style. Worked example: shrink type before splitting content, but never delete content to keep one slide.

### Adaptive typography (`docs/TYPOGRAPHY_GUIDELINES.md`)

Classify every slide before choosing sizes:

| Density | Trigger | Title | Subtitle | Body | Labels/captions |
|---|---|---|---|---|---|
| Sparse | ≤3 body lines, 0–1 image | 32–36 pt | 24–28 | 30–34 | 18–22 |
| Medium | 4–8 lines, 1–2 images | 28–32 | 22–26 | 24–28 | 16–20 |
| Dense | 9+ lines, multiple images or complex table | 24–28 | 20–24 | 20–22 | 14–18 |

**Absolute floors**: title 24 pt, body 18 pt, figure labels 14 pt, table text 12 pt, citations 10 pt. **Line spacing**: title 1.0–1.15×, body 1.15–1.3×, bullets 1.3–1.5×, captions 1.0×. **Alignment**: title per template (usually left), body left, captions centred under figures, citations left/bottom. **Consistency**: adjacent slides within **±2 pt**. Fonts: template-native first; otherwise one sans-serif family for both title and body; avoid serif on screen; CJK needs a bilingual-capable face (Microsoft YaHei, Source Han Sans, Noto Sans CJK).

### Layout decision flow (`docs/LAYOUT_GUIDELINES.md`)

| Images | Layout |
|---|---|
| 0 | Text layout; multi-column when content has natural groups; never stack 4+ distinct topics in one vertical column |
| 1 | Portrait/narrow → text beside at **60/40**; landscape → full-width or centred with caption below; panoramic (aspect ≥2:1) → full-width, no side text |
| 2 | Equal → 50/50; primary+secondary → hero **60 %** left / **40 %** right; timeline → left-right with arrows/numbers |
| 3 | One dominant → hero top **60 % width** + 2 below; equal → 3 columns; sequence → 3 across |
| 4 | 2×2 grid, equal size and spacing |
| 5–6 | 2×3 or 3×2 grid |
| 7+ | Split across slides — never shrink to thumbnails |

**Spacing standard**: slide margins **0.3 in minimum, 0.5 in target**; image↔text **0.2 / 0.3 in**; image↔image **0.15 / 0.2 in**; text block↔text block **0.2 / 0.3 in**; consistent within a slide and across the deck.

**Prohibited layouts**: Word-style vertical stacking (title → image → text → image), thumbnail grids, floating images (every image edge must align to something).

### Image rules (`docs/IMAGE_LAYOUT_GUIDELINES.md`)

- **The 60 % rule**: images collectively occupy **≈60 % of usable slide area (±10 %)**.
- Minimum sizes by type: radiograph/CT/MRI **3.0×2.0 in (20 %)**; clinical photo **2.5×2.0 (15 %)**; chart **3.5×2.5 (25 %)**; pathology **2.5×2.0 (15 %)**; treatment diagram **3.0×2.5 (25 %)**.
- Minimum per count: 1 image **50 %** of slide; 2 → **30 %** each; 3 → hero **35 %**, supporting **20 %** each; 4 → **15 %** each; 5–6 → **12 %** each.
- **Never** duplicate an image across slides (cross-reference by slide number instead), shrink to fit, float, or overlay text (captions below/beside; only labels that are part of the image are allowed).
- Before/after pairs equal size side by side; sequences equal size left-to-right; panoramic full width with caption and no side text; different modalities same size for fair comparison.
- Quality: **≥150 DPI at display size**; no pixelation or stretching.

### Content-integrity policy (`docs/CONTENT_INTEGRITY.md`)

**Prime directive**: medical content must never be deleted, truncated, summarised or rewritten for visual reasons.

Allowed: font size within the tiers; line spacing 1.0–1.5×; text-box size (must contain all text); reflow across columns; image size/position within constraints; splitting content across slides (each self-contained); reordering only where clinical logic permits.

Prohibited for visual reasons: removing discussion/differential/treatment/follow-up/conclusions; summarising without permission; simplifying terminology; dropping negative findings; merging distinct clinical sections; replacing sentences with bullets; deleting a table/chart; removing complications or adverse events.

When content does not fit, the order is: **add slides** → split dense slides → move supplementary material to appendix. A 20-slide complete deck beats a 12-slide incomplete one. The reviewer's test: "If an attending physician reviewed these slides against the chart, would anything be missing?"

### Three-layer QA (`docs/QA_CHECKLIST.md`, `checklists/`)

- **Layer 1 — Medical QA**: completeness by section (chief complaint, HPI, PMH, examination, auxiliary exams, diagnosis + differential, treatment plan/process, follow-up/outcomes, discussion, conclusions); accuracy (demographics, dates, measurements/units, exact terminology, drug names/doses, imaging findings, lab values with reference ranges); clinical logic (diagnosis follows evidence, treatment addresses diagnosis, plausible differential, appropriate follow-up, no contradictions). Red flags are automatic fails: missing diagnosis/treatment/discussion/conclusions, PHI exposure, diagnosis unsupported by evidence, dangerous recommendation, internal contradiction.
- **Layer 2 — Design QA**: template compliance; typography tiers and floors; layout pattern matches image count; canvas utilisation; balance; image minimums/duplicates/quality; spacing/alignment; professional style; table and chart specifics.
- **Layer 3 — Submission QA**: file opens, all slides render, expected vs actual count, no broken links, size <50 MB; every slide at 100 % zoom with no overflow/overlap/pixelation; no placeholders or AI-instruction remnants; cross-references correct; filename convention `{Type}_{Topic}_{Date}.pptx`; multi-platform (PowerPoint 2016+, WPS, LibreOffice); notes/handouts; delivery package.
- **Failure protocol**: document failure → fix with the relevant prompt → **re-run the entire QA layer**, not just the failed check → proceed only when all pass; no manual overrides.

### The nine documented failure modes (`docs/COMMON_FAILURES.md`)

1. Deleting content to fit → reduce type within tiers, split slides, widen boxes; never delete.
2. Fixed font sizes → adaptive tiers; never put a fixed size in a generation prompt.
3. Thumbnail figures (1.5–2.0 in radiographs) → minimum sizes, 60 % target, split.
4. Duplicate figures → each image once, cross-reference by slide number, comparison slide for A/B.
5. Large blank regions (30–50 % blank while content crams a corner) → resize boxes, multi-column; target **≤25 % unused** on content slides.
6. Unbalanced layouts → distribute across the horizontal axis, centre text vertically against images.
7. Word-style vertical stacking → grids, text beside images.
8. Unofficial backgrounds → never replace; adjust text colour or add a subtle text background.
9. Ignoring the departmental template → template analysis first; if no template was provided, **ask**.

### Unique ideas

- **Density-adaptive typography** (three tiers with ranges and a ±2 pt neighbour tolerance) — a direct answer to "one fixed size fits all" failure.
- **A ranked conflict hierarchy** among design principles with a worked resolution, so contradictions are adjudicated rather than argued.
- **A content-deletion prohibition with an audit procedure** and an explicit overflow ladder that ends in "add slides".
- **Image-area percentages per image count**, not just "make images big".
- **Failure catalogue with cause → fix → prevention**, each entry traceable to a real project.
- **Re-run the whole QA layer** after any fix — a discipline no other skill in the cluster states.

### Pitfalls

Its own philosophy warns that the model will default to simplification, minimalism and bullet reduction; that templates will be ignored unless analysis is forced first; and that shrinking type is the tempting wrong fix. It also warns against adding rules without failure data ("principle bloat").

### What is outdated, wrong, or impossible against our MCP

| Prescribed | Status | Adaptation |
|---|---|---|
| Departmental `.potx`/`.pptx` template fidelity | No template import except brand templates; **zero brand templates** in the account | Apply the *spirit*: if the user supplies an existing Canva design, `copy-design` it and only edit content; never restyle an inherited design |
| Master slides, placeholders, aspect-ratio control | No master/placeholder ops | Express as "reuse an existing design" or "accept the generated template" |
| Add slides freely | No page add except `merge-designs` | Plan page count at generation; merge extra pages from a second design |
| Image minimum sizes in inches / % area | Achievable-ish: `resize_element` + `position_element` per image | Compute target px from the 1920×1080 canvas (60 % ≈ 1,244,160 px² total) and verify by thumbnail |
| `python-pptx` generation pipeline | Not applicable | Use prompt-library *language* as the `create-design` brief and the QA layers as review passes |
| Per-slide speaker notes | Read-only | Sidecar script |

---

## Skill: pitch-deck-mastery

### Purpose

A content framework for investor decks, "informed by patterns from the world's best startup decks", with a companion database of 10 external resources to fetch via `web_fetch` (`SKILL.md`; `references/resources.md`).

### Process it prescribes

1. **Identify the stage** — pre-seed, seed, Series A, Series B+.
2. **Fetch relevant examples** from the appropriate resource (URLs in `references/resources.md`).
3. **Apply the 12-slide framework**, adjusted for stage.
4. **Review against the checklist** (must-pass, strength signals, common mistakes).
5. **Point the user at real decks** in their industry/stage.

### The 12-slide framework (`SKILL.md` "The Standard Pitch Deck Structure")

| # | Slide | Purpose | Question answered |
|---|---|---|---|
| 1 | Title | brand + one-liner | What is this company? |
| 2 | Problem | pain point with evidence | Why does this matter? |
| 3 | Solution | product/approach | How do you solve it? |
| 4 | Why Now | timing and tailwinds | Why now? |
| 5 | Market Size | TAM → SAM → SOM | How big is the opportunity? |
| 6 | Product | demo/screenshots | What does it look like? |
| 7 | Traction | metrics, growth | Is it working? |
| 8 | Business Model | revenue, pricing, unit economics | How do you make money? |
| 9 | Competition | positioning matrix | Why will you win? |
| 10 | Team | founders + key hires | Can you execute? |
| 11 | Financials | projections, use of funds | What do you need? |
| 12 | Ask | amount, terms, next steps | What are you asking for? |

Stage adjustments (same file):

| Stage | Emphasise | Minimise | Deck length |
|---|---|---|---|
| Pre-seed | Problem, Solution, Team, Why Now | Financials, Competition | **8–10** |
| Seed | Traction, Product, Market Size | detailed financials | **10–12** |
| Series A | Traction, Unit economics, GTM | Problem (brief) | **12–15** |
| Series B+ | Metrics, Financials, Expansion | Problem, Solution (brief) | **15–20** |

### Rules (verbatim categories)

**Content**: one idea per slide; lead with the headline (takeaway, not label); show don't tell; quantify everything ("large market" → "$47B market"); **no bullet over 10 words**.
**Visual**: **max 3 fonts** (headings, body, accents); **2–3 brand colours + 1 accent**; whitespace signals clear thinking; respect left-to-right/top-to-bottom reading; charts over tables unless precision matters.
**Narrative**: Problem → Solution arc; credibility stacking; end with momentum (the Ask should feel inevitable); the "So what?" test on every slide.

**Deck review checklist** — Must-pass (instant rejection): clear one-liner; specific quantified problem; solution tied to problem; credible sourced market size; team credentials; clear ask with use of funds. Strength signals: traction curve, named customers/logos, unit economics, honest competitive positioning, genuine "why now" insight, consistent visual identity. Common mistakes: wall-of-text, unsourced market claims, "no competition", vanity metrics, **>15 slides at seed**, generic team bios.

**Slide-by-slide writing tips worth importing**: the one-liner must pass the "mom test"; problem in human terms then quantified ("X people face Y problem, costing Z"); solution leads with outcome, one visual, **max 3 differentiators**; five valid "why now" triggers (regulatory change, technology inflection, behaviour shift, market failure, cost-curve crossing); **bottom-up market sizing** ("X customers × $Y/year = SAM", not "$X billion"); traction metrics by stage (pre-seed: waitlist/LOIs/pilots; seed: MRR, growth rate, retention; A: revenue, NDR, CAC/LTV); competition as a **2×2 on two customer-relevant axes**, not a feature checklist you win; team as name/photo/title/one credential line; **3-year** financial projection with stated assumptions and a use-of-funds breakdown; ask with instrument, milestones, timeline and contact.

### Unique ideas

- **Stage-conditional deck length and emphasis** — a single table that changes the outline for four audiences.
- **"The deck is the last thing you should build"** (resource 8, Foundational) — prep before slides.
- **Failed-deck analysis as a resource** — the #1 failure pattern named as vague problem statements.
- **The 2×2 competition matrix** with a warning against feature checklists where you win everything.
- The review checklist's split into *must-pass / strength signals / mistakes* is a usable severity model.

### Pitfalls / weaknesses

No production guidance (font sizes, grids, image handling); the resource list is a link farm with 2024-era notes and will rot; the 10-word bullet rule is stricter than every other skill; **internal inconsistency on seed length** ("10–12" in the stage table vs "no more than 15" in the mistakes list).

### Against our MCP

Nothing here is tool-specific, so it ports as **content** into the `create-design` brief and as a review rubric. It cannot supply the deck's visuals; screenshots/logos must come from the user (`create-upload-url`/`upload-asset-from-url`) and a 2×2 matrix must be authored as an image.

---

## Skill: yc-pitch-deck-max

### Purpose and claim

Claims to be a "super-skill" covering content framework (Kevin Hale / Geoff Ralston), design system, and production (PPTX/HTML/Marp), with 30+ styles and an audit mode (`README.md`, `.claude/skills/create/SKILL.md`).

### Create-mode process (`create/SKILL.md`)

1. **Choose mode** — CREATE (new deck) or REVIEW (audit an existing one); ask which if ambiguous.
2. **Founder interview — all 10 questions in ONE message**: what it does (plain sentence); who the customer is (specific); the problem; why now; traction; market size (push bottom-up); team's unfair advantage; ask/stage; brand colour (default YC Klein Blue `#002FA7`); logo file (PNG/SVG, top-right on every slide).
3. **Identify the 3 vertebrae** — the three most memorable facts that make an investor afraid to miss the deal (e.g. "40 % MoM growth with zero paid acquisition", "ex-CTO of Stripe", "$2B TAM with 3 competitors").
4. **Build the 12 standard slides** under the **billboard rule**: ~**7 words** in the headline, one idea per slide, conclusion written explicitly.
5. **Apply the design system** (below).
6. **Generate** via PPTX (PptxGenJS), HTML (React/Vite/Framer Motion) or Marp.

**Review mode** goes slide by slide with ✅/❌/🔧 and seven red flags: headline >10 words; no numbers; jargon; too many bullets; missing comparison; team without credentials; ask without use of funds.

### The 3-vertebrae framework (`README.md`)

| # | Vertebra | Purpose | Investor reaction |
|---|---|---|---|
| 1 | The Insight | you understand something others don't | "I see the pattern" |
| 2 | The Solution | you're the right team to act | "They have the right approach" |
| 3 | The Proof | traction de-risks the bet | "This is real" |

This is the most portable narrative compression in the cluster: three sentences that must survive every slide.

### Design system numbers (`create/SKILL.md` §Step 4)

- Principles: **legible** (large type, high contrast on white; back-row test), **simple** (one idea, billboard not essay, ~7-word headline), **obvious** (conclusion explicit, understood in 3 seconds).
- Palette: white `#FFFFFF`; headline `#1A1A1A`; body `#4A4A4A`; accent Klein Blue `#002FA7`; secondary light gray `#E8E8E8`.
- Type: headlines **36–48 pt bold**; body **18–24 pt**; metric numbers **48–72 pt**, accent-coloured; Helvetica Neue or Inter.
- Layout: content area **80 % of slide width**, centred; logo top-right, **max 60 px** tall; numbers full-bleed/centred; footer page number, subtle gray.

### Repo state — the decisive finding

- `.claude-plugin/manifest.json` declares **10 skills** (`create, content, design, pptx, html, marp, audit, investor, charts, story`); only `.claude/skills/create/SKILL.md` exists in the clone.
- `create/SKILL.md` points to `references/design.md` — absent.
- `AGENTS.md`, `FAQ.md`, `README.md` and `CI` all reference `scripts/generate.py` / `scripts/audit.py` / `cli/yc-pitch-deck-max` — **absent**; the CI workflow would fail.
- `references/content-framework.md` is present and useful; `pitch-deck-plan.json` is a 12-title stub.

Verdict: **thin wrapper with broken links**. Keep the interview protocol, the 3 vertebrae, the red-flag list and the numeric design defaults; ignore the production claims.

### Against our MCP

The 10-question interview and 3-vertebrae compression are excellent **upstream** of `create-design`; the design numbers (36–48 pt headline) need re-basing to the 1920×1080 canvas; the PPTX/HTML/Marp paths are unusable.

---

## Skill: beautiful-hackathon-slides

### Purpose

A 9-phase process for hackathon/Demo-Day decks that "stand out" — explicitly rejecting the default black-console-screenshot demo and generic AI aesthetics (`SKILL.md` "What Makes This Different").

### The 9 phases (`references/workflow-phases.md`)

Each phase has inputs, outputs and exit criteria; the file states "do not skip phases".

1. **Phase 0 — Discover**: read linked context, listen, no designing. Exit: summarise the project in one sentence.
2. **Phase 1 — Clarify**: first ask for an existing project description/README/pitch doc and derive answers from it; then ask only the blocking questions, all in one message (**Q1** event + video length; **Q2** product name + who it helps do what; **Q3** audience technicality; **Q4** existing brand colours/logo/mascot; **Q5** the impression judges should leave with; **Q6** live-demo plan: embed video / build an animated demo / skip / both). Defer team, narrator, recording tools, stack and per-slide detail to the phase where they matter. Anti-patterns: asking "what style do you want?", asking about colours or fonts in words, peppering with 10+ questions.
3. **Phase 2 — Preview (show, don't tell)**: curate **5 of 13** style presets with the **5-2-2-1** rule (2 impression-aligned, 2 theme-aligned, 1 wildcard), cross-check that no two share a primary display font, that the set covers light+dark and sans+serif+mono, that Warm Editorial and Friendly Casual are not both chosen (both use Fraunces); generate **5 preview files of 3 sample slides each** (title/hero, problem, demo placeholder); copy each preset's exact `@import` + `:root` block verbatim; run the Font Sanity Check; open all five side by side and explain the curation.
4. **Phase 3 — Build**: delete the unchosen previews; apply the chosen preset's fonts verbatim; pick the emoji logo; ask for team info; insert a video placeholder or run **step 5b** for an animated demo; apply the impression mapping to slide emphasis; build a single-file HTML deck with the seven core patterns; **10–14 slides, default 12**; use `var(--font-display/body)`, never hardcoded families; run Font Sanity Check again.
5. **Phase 4 — Document**: write `PLAN.md` (context, style, slide-by-slide timing, video points, team) — but only *after* style selection.
6. **Phase 5 — Iterate**: apply the iteration-pattern lookup; refresh the browser after each edit; update PLAN.md only on significant changes (slide add/remove/reorder, style pivot, length change, major restructure, team change); after **3+ iterations on the same slide**, suggest moving on; if slides change after narration, mark affected sections stale and regenerate only those.
7. **Phase 6 — Narrate**: ask narrator type; **1–4 sentences per slide**; budget **≈170 words per minute** of AI TTS (2 min ≈340 words, 3 ≈510, 4 ≈680, 5 ≈850); include per-slide counts, a runtime table, tool recommendations and pronunciation notes; tone "smart friend explaining a cool project".
8. **Phase 7 — Integrate**: ask recording/assembly tools; replace placeholders with `<video>` or keep them for post-production compositing.
9. **Phase 8 — Submit**: confirm the submission format (video file / URL / video+description / source zip / deployed URL); final checklist (plays end-to-end in a fresh player, runtime within limit, no leaked placeholders, no secrets or private info visible, audio clean, descriptive filename).

**Non-linear paths**: 5→2 (style was wrong: 2–3 targeted new previews, not 5), 5→6 (scripts go stale), 4→6 (script first, plan later). Explicit "what not to do": 0→3 (skipping 1–2 guarantees generic output), 6 before 5, 8 without testing.

### Build rules and numeric thresholds

- **Distinctiveness**: commit to one aesthetic direction; distinctive typography (explicitly **not Inter, Roboto or Arial**); character/narrative where possible; reserve demo space; provide a narration script.
- **Slide patterns** (`references/slide-patterns.md`): title/hero; problem split **55–60 / 40–45**; solution as a three-step pipeline; use-case **2×2** narrative grid + **~280 px** sidebar; flow diagram **5–7** boxes with identical width and min-height; architecture diagram with cloud-service styling and a "deployed" badge; video placeholder **16:9**, dashed accent border, **70–75 % viewport, max 960 px**; card grid **3×2** is most readable, descriptions **8–15 words**; team 2×2 (or 1×4), 3×2 for 5–6, 4×2 for 7–8, split for 9+; optional composable visual, mascot card, quote split.
- **Global styling requirements**: navigation dots, slide counter, key hint, arrow-key navigation, click halves, staggered entry animations, consistent uppercase section label with a thin coloured line.
- **Emoji logo**: one primary emoji per deck, **2–5 supporting max**, consistent family, avoid 💡🚀⭐✨💎⚡ and generic 🎯🎨🧠📊; hex badge for refined styles, oversized raw emoji for playful, bracketed mono for terminal styles; never rotate the logo emoji.
- **Style presets** (13, each with an exact font block): Warm Editorial (Fraunces + Outfit), Cyber Terminal (Syne + JetBrains Mono + DM Sans), Citrus Punch (Bricolage Grotesque + Plus Jakarta), Electric Dusk (Manrope), Pastel Chapters (Nunito), Crafted Tactile (Caveat + Space Grotesk + DM Mono), Studio Electric (Barlow 900 + IBM Plex Mono), Moody Nocturnal (DM Serif Display italic + Inter + JetBrains Mono), Kawaii Retro (Big Shoulders + Albert Sans + Press Start 2P), Friendly Casual (Fraunces italic + Bricolage), Lo-Fi Underground (Bebas Neue + Caveat + Space Grotesk), Bold Poster (Shrikhand + Libre Baskerville), Architectural Grid (Newsreader + Hanken Grotesk + DM Mono).
- **Colour priority** (a genuinely novel rule): preset archetype first → negative preferences **100 %** respected → theme context → positive preferences **weak** (honour in 2–3 of 5) → variety and contrast. Users' stated colour is "a hypothesis, not a requirement".
- **Per-script type discipline**: display weight **800** default; import weights 400/500/600/700/800; import italics if used; the `font-family` name must match the `@import` or the browser silently falls back; always use CSS variables.
- **Multi-language**: Latin display fonts do not render CJK/Arabic; swap to Noto Sans/Serif SC/TC/JP/KR/Arabic while keeping the aesthetic direction and palette.
- **Narration**: ≈170 wpm; per-slide 10–40 s in the template.
- **Video**: MP4/H.264, 16:9, **≥1920×1080**, **30 fps** (60 OK), muted or clean mic, 30–60 s typical, **<50 MB per clip**, **<200 MB total**; relative paths only.
- **Animated demo** (when there is no recording): **15–25 s** loop, always a **final reveal beat**, inherit the deck's CSS variables, one archetype per slide, no mandatory clicking; choose from six archetypes (Split Narrative, Pipeline Walk, Before/After Morph, Dashboard Fill-In, Network Graph Grow, Map Heatbloom), recommend **2–3 not 6**, ask **3 elicitation questions**.
- **Density**: "if a slide has more than ~50 words of prose, it's too much for 25 seconds of narration" (`references/iteration-patterns.md` "This slide has too much text").

### Unique ideas

- **Show-don't-tell style selection** with generated previews instead of adjectives — the single best idea for a design-uncertain user.
- **5-2-2-1 curation** and the anti-paralysis principle (never show 13 options; never dump 6 archetypes).
- **Context outlives the conversation** (`PLAN.md`, `narration-script.md`) — directly relevant because our MCP cannot write presenter notes.
- **Impression → emphasis mapping** (technically impressive ⇒ architecture and pipeline get detail; beautifully designed ⇒ title animation and spacing precision; solves a real problem ⇒ problem slide and use case; creative/bold ⇒ unconventional layouts).
- **Iteration lookup table** keyed to the user's phrasing ("fonts too small" → bump 15–25 %; "text cut off" → nowrap → column ratio → shorten → reduce size, in that order; "cards different heights" → min-height; "too much text" → <15 words per bullet).
- **Narration as a first-class deliverable** with a words-per-minute budget and pronunciation guide.
- **Submission packaging** (secrets visible in recordings, descriptive filename, fresh-player test) — a delivery checklist no other skill has.

### Pitfalls it warns about

All five previews using the same font (silent `@import`/`font-family` mismatch); re-declaring fonts/colours inside a demo slide; no final reveal in an animation; animation >30 s; showing all 13 presets; generating PLAN.md before style selection; iterating >3 times on one slide; writing narration before slides are stable; submitting without end-to-end playback.

### Against our MCP

No HTML, CSS, fonts, animations, navigation chrome or video embedding. Transferable: phase discipline, clarify-before-build, visual option previews (as **three-page sample designs** generated with `create-design`, then discarded), PLAN.md sidecar, narration sidecar, density targets, and the submission checklist.

---

## Skill: minorun-marp-skill

Three sub-skills, all derived from the author's own decks and all unusually specific. Japanese; rules paraphrased below with numbers preserved.

**Process the three sub-skills add up to** (synthesised from the three files — no single file states it as a list):

1. **Fix the brief from the organiser's page** — official title, abstract, slot length, audience; read one of the speaker's own past decks before designing anything (`slide-story` "着手の順序").
2. **Agree the argument in words**, then the storyboard skeleton, then the page-unique artifact for each page; choose format last (`slide-story` same).
3. **Write the story** — hook, two audience questions, crossheads, 7-step body, CTA ending; check for withheld answers, emphasis budget and heading-style variety (`slide-story`).
4. **Draw the figures** — decide figure-first vs text-first, split mechanisms across 3–5 slides, strip sub-labels and annotation prose, keep the figure's individuality, then implement with the SVG numbers (`slide-figures`).
5. **Set the visual system** — theme sizes, measured margins, luminance ladder, settled table/code/callout designs, rhythm (`slide-design-dark`).
6. **Export and inspect** — mechanical checks first (margins <60 px, gaps <36 px, figure text <16 pt, SVG box-fit/contrast, line breaks), then every page by eye at ≥150 dpi; report the checks actually run (`slide-design-dark` / `slide-figures` "書き出したら検査する").

### `slide-story` — narrative and editorial rules

**Starting order** (its opening section): 1) check the organiser's announcement page for the official title, abstract and slot length — do not reuse the proposal text; 2) read one of the speaker's own past decks as a physical artifact; 3) agree in words what must be conveyed, to whom, and where the surprise is; 4) agree the storyboard skeleton; 5) decide the page-unique content (diagram, concrete example, real screenshot, number) for each page; 6) only then choose the format. Explicitly refuses pouring content into a template's slots, and refuses borrowing the organiser's template structure (match only aspect ratio, logo, typeface).

**Hook rules**: never start from a definition — in a survey of the author's 21 most-used decks, **not one** started with a definition. Four hook types: empathy/voicing the audience's frustration; a provocative quiz; a news hook; a personal status update. After self-introduction, open with **two audience questions**, the second one thinning the raised hands ("do you use it?" → "do you build with it?"), which becomes the entry to the body.

**Crossheads (中扉) = the audience's inner voice**: a divider page carries the question the audience is actually thinking, and the very next slide must answer it. Rules: one line only (no sub-line, chapter label or number); never two in a row beyond **2 consecutive slides**; place one every **3–6 body slides**; when joining two decks, put a paired question at the seam; a comprehension-check question does not signal a topic change. An unanswered crosshead is deleted.

**Concept introduction is a 3-piece set**: (1) "what is X?" — one-line definition plus etymology decomposition; (2) "why is it good?" — before vs after; (3) "put crudely, it's Y" — the killer one-liner, with precision pushed to a footnote. Explanation order is abstract → concrete → metaphor; after a metaphor, the next slide must derive the product from it.

**Body order (7 steps)**: concrete example first ("here's something you can build") → limits of the current way → mechanism (one diagram) → how to build it → sticking points (a table of options vs problems) → what solves them → next step. Keep claim and example adjacent; mark throwaway examples with "for example" and keep the essential message higher.

**Ending**: do not build a summary slide; land on a call-to-action crosshead and finish on a full-bleed image of the book/announcement. Do not put "thank you" immediately before a promo slide (two closing slides cancel each other). CTA multipliers may be exaggerated; advertising is placed openly as a form.

**Do not reveal the answer first** (its most distinctive rule): adding information one step at a time lowers cognitive load. Therefore: no agenda slide, no "today I'll cover these three", no preview of conclusions; once a question is posed, the answer opens over subsequent slides, never inside the same slide; before adding a slide, check it isn't a summary of later material; no "overview/map/loop diagram" at the start. A single through-line is fine in the design notes, not on slides — slides carry one discovery at a time.

**Staging (演出)** — put at least **2–3** of these in a deck, never zero: build-up diagrams split across slides; a fake ending then a reversal (only if the speaker's real story supports it); speech-bubble dramatisation; emotional exclamation; pre-empting a misunderstanding; rapid rebuttal of expected objections; name-etymology trivia; **at least one honest caveat slide**; a personal coinage for a real experience. With 3+ chapters, re-show a correspondence table or step bar at chapter boundaries.

**Use cases and proper nouns**: choose only use cases that would collapse without the product's specific strength (speed, cheapness, parallelism); load published implementations and numbers with sources; write problem slides in the audience's own tool context (tool name, the exact request, the shape of the desired answer); proper nouns and numbers must be explainable by the speaker — put the paper's identity next to its title and a market reference next to a price/score, or split the slide; for non-engineers, replace command names with what they do; never put the speaker's local configuration counts on slides; gloss jargon at first use (e.g. latency = response delay) and expand acronyms.

**One-slide information budget** (table): one heading + **3–4 body lines**, nothing more; heading = one claim sentence, understandable the instant the page turns; body = 3–4 bullets of 1–2 sentences, one level deep, split at 4 lines; **emphasis 1 per slide**, **1 per 2–3 body slides** across the deck; avoid heavy use of em-dashes and full-width colons; **one diagram per slide, large** (a diagram-only slide with the same heading is allowed); tables **2–3 columns**; heading on **one line**. On a figure-led slide, text is heading + one lead line only; adding two lines under a figure shrinks the figure and crowds the text. On a text-led slide the figure is illustration-sized. Do not annotate what the eye can see; the test is "can you tell from the screen, or does it change the audience's decision today?"

**First-use emphasis (separate allowance)**: a newly taught term or feature name gets bold + accent colour at first appearance in running text; not in headings, tables, speech bubbles, and not on second mention; when two terms are introduced as a contrast, colour both; treat all terms of a kind identically; don't colour the expanded form in parentheses; don't also wrap in quotation marks.

**Heading style must be mixed**: uniform polite style or uniform plain style reads as machine-written. Per-page roles map to heading forms:

| Page role | Heading form |
|---|---|
| Figure/code/screenshot is the star | short noun-phrase label, 3–6 characters |
| Claim, realisation | plain-style declarative |
| Surprise, good news, turn | "!" |
| Audience inner voice | colloquial monologue |
| Rebuttal, promo, close | polite style |
| Lead into next slide | cut off mid-sentence |
| Term introduction | descriptive phrase + the term |
| Crosshead question | "…?" |

**Measured heading metrics** (from two hand-made decks of 57–58 slides): slides containing "!" **7–20 %** (1 % when wrong); containing "?" **10–15 %** (7 % when wrong); polite style **10–12 %** (1 % when wrong); shortest heading **3–6 characters** (when wrong, every heading is 15–24 characters). Also count repeated patterns: two-part comma-then-short headings, conjunction-led headings, colon headings — **3+ in a row** is a signature of machine tidying. Similarly, in body text watch the "if X, then Y" conditional-comma-consequence pattern: **3 in one slide** means mix declaratives, noun phrases and questions. A checker script (`tools/check-ai-smell.py`) is referenced but absent from the clone.

**Quote boxes and speech bubbles**: quotes and "actual prompts" may only come from real logs — inventing a plausible line and presenting it as said is fabrication; if there is no real artifact, rewrite the slide so it no longer claims "actual"; keep the original wording, do not tidy the ending, and do not add "from the actual log" on the slide. Never put an aphorism in a coloured quote box — only concrete steps, numbers, examples and real prompts. A speech bubble must not restate the slide's conclusion; put a concrete personal aside that isn't in the bullets. Do not put a bubble tail on expository text with no speaker — use a rounded box for explanation and reserve tails for real utterances. Colour boxes by role (quote/example: pale ground + border; punchline: solid theme colour with reversed text).

**Conclusion boxes**: at most **2 of any 5 consecutive pages**; never mid-body (text continuing below the box kills its conclusiveness); prefer a diagram or plain body text; supplementary coloured columns limited to a few places and never directly under a bubble or table.

**Reuse and derivation** (strong production discipline): when a past deck covers the same theme, build by recombination — copy content, order and wording verbatim; do not split pairs that only make sense together; only three edits are allowed: updating stale facts, minimal venue-specific joins, and slide-level cuts for time. If unsure what to cut, present candidates as **blocks including 2–3 neighbouring slides as images**, not titles and summaries. Do not raid previously cut slides as "fleshing out" candidates. When adding a slide, first search past decks for an existing artifact (headings then PDF page-by-page — image-only slides don't appear in text search); copy the structure, not an enhanced version. When moving a standard slide between decks, list every deck containing it and copy from the most recently corrected version. Short versions are made by cutting from **one newest canonical deck**, never by stitching usable slides from several decks. When reusing for a different audience, build a table of every slide against "can this audience do this with the tools they already have?" (columns: number, heading, assumed tool, whether the tool has appeared) and move prerequisite slides after the tool introduction rather than deleting them. After inserting into an existing deck, re-count three things across old and new: emphasis ratio (check the lower bound, not just the upper), duplicate examples (grep proper nouns), and runtime.

**Revision protocol**: before fixing one slide, view it with **2–3 neighbours as images** — problems appear in sequence, not per page. Never let the same form run **3 slides** in a row (three tables, three same-position boxes). Don't change one slide's component design to make it stand out — vary column count and arrangement instead. Don't shrink type to fix crowding; the fix order is (1) remove duplication, (2) create space with layout, (3) split across neighbouring slides. Shortening must not change meaning — compare the new sentence with the original and confirm it says the same thing. Deleting text alone is not "fixing crowding": the freed lower half must be re-used for the slide's role (bigger definition, bigger code). When fixing a cramped figure, delete fine text but keep the figure's individuality (timeline, bar counts, branching, illustration). Wording fixes: apply one recommendation directly and show before/after. Structure/design fixes: don't touch the original — show 2–3 directional proposals (with the recommended one first) as images rendered from a working copy, each with a one-line statement of the page's role, then edit after agreement. When a heading is criticised, rebuild from "what is this slide for", not by swapping the criticised word. Never silently delete a slide called "floating"; find where it belongs in the canonical flow and move it, or ask first. When deleting or merging, list every element on the page (body, box, note, bubble, footnote) and state what is moved and what is discarded; after deletion, check the diff for lines not in the list. When merging two slides, do not stuff the deleted slide's prose into diagram boxes — one short label per box, with the explanation in one body line or spoken.

**Lecture / hands-on decks** (a distinct mode): every participant action that needs a screen gets its own step slide with a real screenshot; step slides start with a **1–2 line lead sentence** saying why, then numbered steps; don't give click instructions outside numbered steps (screenshots and arrows own that); step wording must match the on-screen label exactly, in the audience's UI language; don't rely on "look at my screen"; don't put the instructor's own actions or venue logistics on slides; keep the request phrasing consistent across the deck; never show a prompt bubble without a one-line lead-in; body-slide headings should be **labels** ("the scenario for today's hands-on"), not the first sentence of the explanation — action-style claim headings are for crossheads only; put a crosshead before each theme change; put a real screen slide right after introducing a tool; draw the whole mechanism in one diagram; don't assume a comparison target that hasn't been introduced; put security caveats after the convenience story, not in the middle; for a paper slide, show page 1 with a small bibliographic caption and keep the body in the audience's language; one term per concept for the whole lecture; put an overview sentence before and after an inner-voice slide; use the organiser's official course title on the cover, and for internal formal events use company/role/real name with no social handle. Wording: polite style for lecture body, noun-phrase for short bullets, no sudden casual imperative, crossheads addressing the audience in polite style but list-type crossheads in plain style; no comma in newly written headings; no full-width-space two-part headings; avoid nominalised verbs ("write-down" → "leave a note"); avoid vague abstract verbs for results/effects — name the concrete action; don't stack short clipped verbs for mechanism explanations; notes start with "※"; no underlining for emphasis.

**Title patterns**: titles that get read relieve the reader's fear of being behind — "gentle introduction to X", "a gentle review of X", "still in time!", "too late to ask!?" — teach from above only after reassuring.

**Timing model** (measured, not guessed): compute landing time at four checkpoints — when the structure is fixed, when slide count changes by **5+**, before submission, and the day before. Unit cost is per **body slide**; crossheads and the cover are counted at **8 s** each. Body count = total − crossheads − cover. Demos and Q&A are fixed blocks added on top (a live demo adds **0.5 min** for screen switching and waiting). Measured per-body-slide costs:

| Venue | Seconds per body slide |
|---|---|
| 5-minute LT | ~30 |
| 10-minute LT | ~16 (average across all slides, crossheads included; ~35 slides) |
| ~15-minute short slot, screenshot-heavy | ~29 |
| Developer conference (~40 min) | ~37 |
| Online stream, general audience (~40 min) | ~37 |
| Expo / non-engineers | ~46 |

Short slots have lower unit cost because introductions and restatements disappear; never apply a 45-minute unit cost to a 20-minute slot. Aim **~5 minutes under** for on-site talks; if the margin is only ~3 minutes, offer 2–3 cut candidates. For online events with Q&A in a separate block, design to the full slot. Pick **up to 2 cut triggers** at crossheads ("if we pass this crosshead after N minutes, skip this slide"), never cut crossheads. Record one line of actuals after each talk. For hands-on sessions, add up per-slide speaking time **plus per-action waiting time** (open settings, save, upload, wait for generation, check result, help stragglers), assume you proceed when about half the room responds, and overlap talkable slides with generation waits.

**Inspection (検品)** — a 10-item list: no slide over 1 heading + 3–4 lines; no heading that is merely an item name; no slide with 2+ figures; no slide with 2+ emphases and not more than half of body slides carrying emphasis; the slide after each crosshead answers it; no previews, summaries or overview-first leaks; the AI-smell checker returns 0 on rewritten slides; inserted slides match the existing emphasis ratio and examples; revised slides checked against neighbours; in lecture decks, no heading immediately followed by a table or figure, and every participant action covered by a step slide.

### `slide-design-dark` — measured visual balance

- Theme sizes: body **26 pt**, h1 **36 pt**, crosshead **44 pt**, cover **52 pt**.
- **Measure before adjusting**: extract line positions from the PDF (`mutool draw -F stext`); filled shapes don't appear in text extraction, so rasterise pages. Horizontal positions align to slide centre or the body's left edge, never outside the body margins; vertical positions sit at the midpoint of the gap between body bottom and slide bottom, recomputed per slide. Elements at least **30 px** apart. Margin pairs differing by a few px (167 vs 168, 60 vs 65) are balanced; the difference *is* the correction. PDF coordinates are 960×540 while CSS is 1280×720 — multiply by **0.75**.
- **Vertical rules**: body starts directly under the heading even if the page then has empty space below — do not widen the heading-body gap to fake centring; fill space with paragraph breaks or a bottom-right illustration/box. Figure-led pages get **~36 px above** and **~44 px below**; if a figure/table has empty space below, equalise top and bottom gaps and correct any **>6 px** difference with `position: relative; top: <half the difference>`. Marp's `section` is `display:block`, so `margin:auto 0` does not centre; tables need `display:table; width:auto; margin:<top> auto 0`. Body paragraphs **≤3 lines**. **Never shrink font** to fit — break at meaning or cut words. Don't place a box that repeats the heading directly under it; send boxes to the page bottom. Kill one-word orphan lines.
- **Colour by luminance ratio against black**, not by feel:

| Use | Ratio vs black |
|---|---|
| Heading, line, frame | **10–12** |
| Solid fill carrying white text | **6–7** |
| Hero figure box (white text) | **4.5–5.5** |
| Supplementary box in body | **2.5–3.0** |
| Secondary box inside a figure | **~1.5** |

  Reference: cyan `#00c4e4` = 10.0, pure yellow `#ffff00` = 19.6; a heading colour below 10 looks sunken. A body callout must not use the 1.5 secondary value (it merges with the ground): the author's `#2f2f37` (1.58) sank, `#555561` (2.86) stood up. The ceiling is set by the emphasis colour placed inside: yellow emphasis requires ground-to-yellow ≥6. White-on-fill has its own floor: **3.0** against white for large bold (~25 pt), **4.0+** for small in-figure text (17–19 px). The same colour reads brighter as a large fill and darker as thin text — raise text/line colours **1–2 steps** above the fill colour. Conflicts between two colours are usually **tone (lightness/saturation)**, not hue: match tone first, separate hue last (hue carries meaning — yellow→green reads "success"). Create contrast by **lowering everything except the hero** rather than adding colours, in **doubling steps 21 → 10 → 6 → 3**; steps within 1.5× are invisible. Projected headers stop at ~10; below 7 is unreadable because projectors lift black.
- **Brand colours**: take hex values from the product's CSS/docs; raise lightness for text, darken fills and reverse white text, and allow the brand colour unfiltered only on the cover band. When deriving a dark deck from a light one, don't machine-replace figure colours — rebuild figures as dark-grey panels (`#2c2c35`→`#18181e`, border `#3c3c46`) with white text and one dark-teal hero (`#00788c`).
- **Show candidates on real pages**: render the same page once per candidate and tile them **2×2**; test on both an emphasis-heavy page and a figure-heavy page. Do the same for fonts (cover + bullets + table pages).
- **Bulk colour replacement**: don't use "exclude this colour" searches (a line containing both target and excluded colour is skipped); search for the exact colours being replaced and verify the old colour count is 0 afterwards, including SVGs.
- **Emphasis**: 1 per slide, 1 per 2–3 body slides; keep only part punchlines (pillar names, closing lines, key numbers), not convenient phrases; a consistently filled table column counts as one; when three numbers are shown, colour only the one that leads to the next slide; don't use bold inside table cells (the theme's grey cell kills yellow).
- **Settled designs**: tables with **no fill, hairlines only**, header 18 pt muted with letter-spacing and a bottom rule, body 22 pt, first column white bold nowrap, **≤6 rows**, key row shaded `rgba(255,226,120,.16)` for comparison tables of 6+ rows, no footnote under the table. Code in a translucent gradient panel with a 3 px accent top line, **21.5 pt minimum (≈16 pt PDF)**, **≤60 half-width characters per line**, one property per line, panel bottom **≥60 px** from the page bottom. Supplementary box `#555561`, min-width aligned across slides, bottom 64 px (104 px when the body is short), font applied to both `.gbox` and `.gbox p`, centred by `left:0; right:0; margin:0 auto` (not `translateX`, which halves the usable width). Conclusion = solid `#555561` + white bold; quote = no border, 3 px left accent rule; never light fill + dark text on black.
- **Comparison slides**: exactly **two large numbers at 88 pt** with one line below and a thin vertical divider; adding price rows or notes breaks it. **Figure labels sit outside and above the box** (14 px above), boxes contain only content. Screenshots: `![w:720 center]` with `border-radius:14px` rather than `bg right:40%` (which pins to the edge); side-by-side images must share aspect ratio. **Rhythm**: no **5** consecutive text slides, no **6** consecutive same-type figure slides — alternate.
- **Marp traps** (medium-specific but instructive): `**bold**` adjacent to full-width brackets fails (use `<strong>`); a `---` with no blank line before it merges slides or creates a setext heading; slide insertion/deletion scripts must process in **descending** order with assertions; PDF page numbers differ from source because of front-matter; inline `style` on `<img>` is stripped; a raw `<br>` plus a soft line break yields a double break; HTML blocks don't honour Markdown breaks.
- **Post-export inspection**: margins check (content bottom/right gap **<60 px = fail**), gap check (**<36 px = fail** between figures/boxes and adjacent text), figure text (**<16 pt** or **<14 px** from the box edge = fail), SVG box-fit, SVG contrast (**<1.25** = fail), line-break checker. Machine checks cannot see a whole element that failed to render — so also rasterise every page and inspect at **≥150 dpi**; for stacked shapes (bubble tails, arrows, bands) re-render that page at high resolution and zoom **300 %** at the joint. Never report "no breakage on all pages" from a contact sheet; if only a contact sheet was viewed, say exactly that.

### `slide-figures` — diagram and illustration rules

- **Decide figure-first or text-first before drawing.** Figure-first: text limited to heading + one lead line, figure full width. Text-first: figure illustration-sized (**100–330 px wide**) in a corner. Trying to do both shrinks the figure and crowds the text.
- **Split a mechanism diagram across 3–5 slides**, adding one element at a time. If bullet items have hierarchy or branching, convert to a diagram (the test: do you want to draw an arrow or a boundary?); after converting, remove the conclusion box (the figure is now the star).
- **Step slides**: two columns from the start (text left, real screenshot right), left column width fixed in **px, not %** (percent breaks words mid-token), breaks inserted by hand at meaning boundaries; right frame absolutely positioned to match the text height; screenshots shown at native size, cropped only on request and never inside the requested edge (window chrome and sidebar tell the audience which screen); pressed targets boxed and numbered with arrows; no window shadows or outer frames.
- **Information discipline**: one theme per slide; preconditions, follow-on phases and key-message bands belong to other slides; don't say the same thing in a step heading, icon and arrow; **no sub-label under a box name** ("CDN / delivery entry" is the signature of machine-made diagrams); no annotation prose inside the figure; no explanatory text under arrows or in corners; if more than **4** items sit side by side, wrap related ones in the same pale background — people track about **3** at once.
- **Don't over-simplify**: when de-cramming, delete fine text but keep the figure's individuality — timelines, bar counts, unit charts, 1→6 branching, back-and-forth arrows, one illustration per figure, the hero number. The test: can you name in one word what this figure shows that no other figure does? If not, you over-cut. Don't replace a bespoke figure with a generic three-card or six-box layout; don't recolour one data point in a chart with a non-deck colour.
- **Architecture diagrams**: draw the client (browser/app) as a node — a person-with-arrow-to-cloud erases the screen; don't put role icons inside boxes (then only box-to-box relations are drawable); draw out-of-scope systems in pale grey; draw arrows as implemented (read the permission model and the actual call targets); don't label radial lines along the line (the line will cross the text) — put labels in bands the line doesn't cross; use official icon sets, never similar-looking brand logos or abbreviated产品 names; draw infrastructure as a **base layer under** the things it hosts, with relations drawn on top, and split the base when instances are separate.
- **2×2 matrices**: all four cells the same pale fill, names as identical dark chips; two names in one cell = two chips, not two lines; no corner notes; don't colour-code cells; empty cells stay pale; arrows must contrast with the cells they cross; chip colours must match the deck's other figures (verify with a colour-frequency listing).
- **De-machine the look**: no emoji as icons; people are illustrations, not "user" rounded boxes; one large one-line label per box (no title+subtitle frames); hierarchy by **fill** not border, in four tiers (solid hero, dark fill no border, border only, pale zone); figure surfaces match the slide background; vertical bands/large shapes centre their text vertically; body text and images in split pages align to the top, under the heading — only text inside shapes is vertically centred.
- **SVG implementation numbers**: figure text **≥16 pt** at exported size; if the viewBox is 1000 wide and pasted at `w:1000`, box labels are **19–22 px**; text-to-box-edge **≥14 px**; fix order when it doesn't fit: shorten wording → widen box → raise figure width → raise font size. Measure with `getBBox()` after rendering — character-width estimates (`0.6 × size × count`) are ~20 % off and shrunken screenshots hide a few px of overflow. Arrowheads: `<marker>` defaults to `markerUnits="strokeWidth"` so an 8×4 head on a 4 px stroke is 32 px and swallows a 42 px shaft — set `userSpaceOnUse`, fix the head at ~**18 px**, keep shafts **≥3×** the head, labels **≥10 px** from the arrow. Gradients: a horizontal or vertical stroke with a gradient disappears (zero-width bbox) — use solid strokes and solid text fills (gradient text loses glyph shapes in PDF); for one gradient across several boxes use `userSpaceOnUse` coordinates; bulk colour replacement can rewrite `marker-end:url(#id)` and kill arrowheads. Crop empty bands with `viewBox`. Keep **10 px** between any two elements (**14 px** preferred; 8 px between a label and its sub-line; **6 px** inside a frame) and verify by measuring bounding boxes in the generation script.
- **Illustrations**: the author uses irasutoya; pick the image that depicts the slide's key noun, not the vibe; no "OK sign" filler; positive images only under positive conclusions; no illustration on a page that already has a table/figure/code; in a **49-slide** deck, **6** illustrations was right and **13** was too many; never twice the same image; base position bottom-right, right edge **inside the body margin** (118 px if margins are 96 px); portrait images limited to 100–120 px wide; pair the illustration and any adjacent bubble so they move together; no illustration over a box (borders don't appear in text extraction, so machine checks miss it); real screenshots for products/repos, not illustrations.
- **Reuse across decks**: copy figures from the most recently corrected deck; don't bring icons for services not in this deck's story; don't paste a dark-deck figure onto a light deck (re-build against the target ground; knock out black screenshot margins); when redrawing a speaker's original figure, put it side by side and match stroke weight, colour depth and arrow spacing; a circular flow must be drawn as one circle, not separate curves.

### Unique ideas

- **Crossheads as the audience's inner voice**, with cadence rules (max 2 consecutive, every 3–6 body slides) and an answered-by-next-slide gate.
- **"Don't reveal the answer first"** as a hard editorial rule, including a ban on agenda/summary/overview slides.
- **Measured self-audit**: percentages of "!"/"?"/polite-style headings and minimum heading length, taken from the author's own decks — a rare empirical baseline.
- **Per-body-slide timing units by venue**, with crossheads at 8 s and demos as fixed blocks.
- **Luminance-ratio colour design for dark backgrounds** (10–12 / 6–7 / 4.5–5.5 / 2.5–3 / 1.5), with the "same colour reads brighter as fill" correction.
- **The "delete fine text, keep the shape" rule** for de-cramming figures.
- **A deletion audit** (list every element, then diff) and a **wording-vs-structure review split**.
- **Hands-on timing = speaking time + waiting time per participant action.**
- **Machine + eye verification with an honesty rule**: state which checks were run; never claim full-page visual verification from a contact sheet.

### Pitfalls it warns about

Definition-first openings; template-filling; agenda/summary/preview slides; unanswered crossheads; three crossheads in a row; four-block slides; colour-only figure hierarchy; shrinking type to fit; sub-labels under box names; emoji icons; gradient strokes/text in SVG; arrowheads swallowing shafts; duplicate illustrations; "vibe" illustrations; machine-only verification; claiming verification that wasn't done.

### Against our MCP

| Prescribed | Status | Adaptation |
|---|---|---|
| Marp theme, CSS, `<style scoped>`, SVG inline | No code, no shape creation | Use the *numbers and rules*; render diagrams as PNG/SVG externally and upload via `create-upload-url` |
| Measure PDF margins, gaps, font sizes | No PDF of the deck unless exported | Export via `export-design` and measure the PDF/PNG, or measure from `get-design-thumbnail` pixel inspection |
| Luminance ratios | Computable from hex values we choose | Adopt as a palette-selection rule before generation |
| Crossheads, section dividers | No page add | Generate the intended page count with dividers; or merge pages from a second design |
| Presenter narration | Notes read-only | Sidecar script with the 170 wpm budget |
| Illustration placement at bottom-right 118 px | Achievable for uploaded images via `position_element` | Use it as the default safe position |
| Figure text ≥16 pt | Achievable only if baked into the uploaded image | Bake at export time; verify by thumbnail |

---

## Skill: robonuggets-marp-slides

### Purpose

A Marp component cookbook. `SKILL.md` teaches CSS variables, dashboard components, SVG chart recipes, icon paths and animations; the **22 examples are declared the quality bar** ("read 2–3 examples that match the requested style before generating").

### What it actually contains

**Process it prescribes** (from the core rules and the "Example Decks" section):

1. **Read 2–3 examples matching the requested style before generating** — explicitly "the quality bar"; match their composition, spacing and density.
2. **Pick a theme and a tested font pairing** (Outfit+Raleway for dashboards, DM Serif+DM Sans for editorial, Space Grotesk+IBM Plex Mono for travel/light, etc.).
3. **Compose each slide from the component vocabulary** — heading roles (h3 eyebrow / h1 title / h2 subtitle), metric cards, chart type, layout block.
4. **Keep to the 8 design rules** — one idea, accent for data only, body `#999`/labels `#666`, ≤6 list rows, charts over numbers, relative image paths, preview, per-slide overrides.
5. **Export** to PDF/PPTX/HTML with Marp CLI and check for silent overflow (the source warns "overflow clips silently").

- **Design rules (8)**: one idea per slide (overflow clips silently); h1 white, accent only for data highlights; body `#999`, labels `#666`, never darker than `#555`; **max 6 rows** per list slide; charts over numbers, mix visual types; relative image paths only; always preview; per-slide overrides (`_backgroundColor`, `_header`, `_paginate`, `_footer`).
- **Heading roles**: h1 = title slides (white, extra large, `3em`); h2 = subtitle (grey, thin, `1.3em`); h3 = section label (muted, uppercase, **0.6em**, letter-spacing **0.2em**).
- **Tested font pairings**: Outfit 800 + Raleway 100 (data/dashboard default); DM Serif Display + DM Sans 300 (editorial); Space Grotesk 700 + IBM Plex Mono 300 (travel/light); Sora 700 + Sora 200 (comparisons); Urbanist 800 + Urbanist 100 (music); Plus Jakarta Sans 800 + 200 (retros/team).
- **Theme defaults**: 16:9, **1280×720**; section padding **56 px 72 px** (or 50/70, 60/80, 48/64 in examples); accent `#ff6b1a`; card `#080808`; border `#111`; body `#999`; label `#666`; muted `#555`; status green `#22c55e`, red `#ef4444`, yellow `#f5a623`.
- **Images**: logo header `![w:100]`, hide per slide with `_header: ''`; photo background `brightness:0.15`; split `bg right:35% brightness:0.2 blur:3px`.
- **Dashboard components**: metric card with a 2 px gradient top border, icon + label + big number + trend; status dots (8 px SVG circles); verdict tags; hover rows.
- **Chart recipes with maths**: area/line via polyline+polygon; donut segments as stroked circles with `stroke-dasharray` and accumulating negative `stroke-dashoffset` (r=110 → circumference ≈691; offset = −(pct/100)×691; `rotate(-90 cx cy)`); gauge 0–100 with `stroke-linecap:round`; single-ring donut (r=74 → 465); sparkline 50×16; stacked bar as flex widths; vertical bars with gradient and 3 px top radius; radar polygon.
- **Icons**: 16 px inline, 32 px features, 44 px cards, `stroke-width:1.5`.
- **Animations**: float/glow/blink, stagger with delay, HTML export only.
- **Export**: Marp CLI to PDF/PPTX/HTML; `--pptx-editable` needs LibreOffice.
- **Custom canvas**: `section { width:540px; height:720px; }` in CSS rather than front-matter; portrait = stack and scale down **15–20 %**.

### Verdict on the examples

Split each example on lines that are exactly `---` (front-matter consumes the first two) and count the blocks: **19 of the 22** files are **3-page specimens** (cover + two content pages: coffee, cocktail, board-game, dog-breed, fitness, garden, houseplant, home-gym, kids-party, film-director, apartment, wardrobe, travel, walking-tour, road-trip, recipe, language, comparison, wine-tasting), `marp_hero.md` is 4 pages, `marp_facebook-ads.md` is **17 pages** and `marp_sample.md` is **21 pages**. Every specimen is a single `#` title plus inline-styled flex/SVG components — there are no CSS classes at all. So "22 curated reference decks" overstates it: they are mostly **style specimens**, two of which are deck-shaped. Their value is compositional vocabulary (eyebrow h3 → big h1 → muted h2; KPI card rows; funnel with connector rules; donut with a centre label), not deck structure.

### Unique ideas

- **A named quality bar read before generation** — feed the model 2–3 reference specimens rather than describing style in adjectives (the same instinct as Esther's previews, but simpler).
- **Chart-type vocabulary with the actual trig**, so a reviewer can ask for "a donut with three segments" precisely.
- **Metric-card anatomy** (label / hero number / delta with arrow / accent hairline) — the most reusable visual unit for traction slides.
- **Font-pairing table with tested pairings** by deck genre.

### Pitfalls

The 8 rules are shallow (no hierarchy ratios, no grid, no contrast targets); body `#999` on black is low-contrast by construction; "charts over numbers" is the opposite of the academic "one exhibit, annotate the point"; most examples are component demos, so imitating them yields component collages rather than arguments; no QA beyond "always preview".

### Against our MCP

No HTML/SVG. Transferable: chart-type selection, metric-card composition, icon sizing, padding ratios (56/72 ≈ 7.8 %/10 % of 720/1280), and the "read references first" habit — implemented as attaching **3 reference thumbnails** or naming 3 reference designs in the brief.

---

## Principles catalogue

Deduplicated across all eight skills. "Source" gives the repo file and heading; numbers are as stated by that source.

### A. Narrative frameworks

| # | Framework | Structure | Source |
|---|---|---|---|
| A1 | SCR | Situation → Complication → Resolution | `Gabberflast_academic-pptx-skill/content_guidelines.md` §1 |
| A2 | Funnel + Answer | Broad context → specific gap → approach → findings → implications | same §1 |
| A3 | Answer First | Conclusion first, then support; for senior/time-pressed audiences | same §1 |
| A4 | 12-slide investor arc | Title → Problem → Solution → Why Now → Market → Product → Traction → Model → Competition → Team → Financials → Ask | `Stevekaplanai_pitch-deck-mastery-skill/SKILL.md` |
| A5 | 3 vertebrae | Insight → Solution → Proof | `josezuma_yc-pitch-deck-max/README.md` |
| A6 | 7-step talk body | Concrete example → limits of current way → mechanism (one diagram) → how to build → sticking points table → what solves them → next step | `minorun365_minorun-marp-skill/skills/slide-story/SKILL.md` "本編の運び" |
| A7 | Concept 3-piece set | What is X → why it's good (before/after) → crude one-liner | same, "概念の導入は3点セット" |
| A8 | Hook → two questions | Empathy/quiz/news/status, then two audience questions that thin the hands | same, "つかみは聴衆の現在地から" |
| A9 | 9-phase production | Discover → Clarify → Preview → Build → Document → Iterate → Narrate → Integrate → Submit | `Esther2524_beautiful-hackathon-slides/references/workflow-phases.md` |
| A10 | Crosshead chain | Every section opens with the audience's inner-voice question, answered by the next slide | minorun `slide-story` "セクションの接続" |
| A11 | Problem→Solution arc + credibility stacking + inevitable Ask | Narrative rules | pitch-deck-mastery `SKILL.md` "Narrative Rules" |
| A12 | Title patterns | "gentle introduction", "still in time", "too late to ask" — reassure the reader first | minorun `slide-story` "タイトルの型" |

### B. Slide-count and timing rules

| # | Rule | Threshold | Source |
|---|---|---|---|
| B1 | Max slides per minute | 1 slide/minute | academic `content_guidelines.md` §7 |
| B2 | Talk budgets | 10 min → 8–10 content; 15 → 12–14; 20 → 15–18; 45 → 30–40 | same §7 |
| B3 | Finish under time | 1–2 min under (academic); ~5 min under on-site (minorun) | academic §7; minorun "尺の見積り" |
| B4 | Per-body-slide cost | 5-min LT 30 s; 10-min LT 16 s; 15-min short slot 29 s; 40-min dev conf 37 s; 40-min stream 37 s; expo 46 s; crosshead/cover 8 s; live demo +0.5 min | minorun "尺の見積り" table |
| B5 | Compute timing at 4 checkpoints | structure fixed, slide count ±5, before submission, day before | minorun same |
| B6 | Investor deck length by stage | pre-seed 8–10; seed 10–12; A 12–15; B+ 15–20 | pitch-deck-mastery `SKILL.md` stage table |
| B7 | YC deck | 12 slides | yc `create/SKILL.md` |
| B8 | Hackathon deck | 10–14, default 12 | Esther `workflow-phases.md` Phase 3 |
| B9 | Medical case report | 10–15 slides (case study) | medical `docs/CASE_STUDY_ORTHODONTICS.md` |
| B10 | 10-min LT structure | ~35 slides total | minorun timing table |
| B11 | Narration budget | 170 wpm; 2/3/4/5 min → 340/510/680/850 words; 1–4 sentences per slide | Esther Phase 6 + `assets/narration-script-template.md` |
| B12 | Demo animation length | 15–25 s including a final reveal; never >30 s | Esther `references/live-demo-archetypes.md` "Anti-patterns" |

### C. Type and size rules

| # | Rule | Threshold | Source |
|---|---|---|---|
| C1 | Academic type scale (pt, 16:9) | title 24–28 bold; section 20–22 bold; body 20; chart labels 16–18; citations 12–14 | academic `SKILL.md` §Step 3 table; `slide_patterns.md` |
| C2 | Academic floors | body ≥20 pt; titles ≥24 pt; axis labels ≥16 pt | academic §3, §8 |
| C3 | Power-design screen scale (px, 1920×1080) | body ≥24; title ≥48; caption ≥18; footer 14–16 @ 50–60 % | power `principles/design-principles.md` rules 8, and "Minimum Readable Size" |
| C4 | Projection floor | ≥28 pt body (≈37 px at 1920×1080); subtitle "old rule" 24 pt only for close viewing | power §9 "Minimum Type Size for Projection" |
| C5 | Type sizes per slide/deck | ≤4 per slide, ≤6 per deck | power rule 7 |
| C6 | Modular scale | one ratio of 1.200/1.250/1.333/1.414/1.500/1.618; default 1.333 | power rule 6 |
| C7 | Hierarchy ratios | headline:body 2.0–4.0; subhead:body 1.25–1.5; avoid 10–20 % steps; primary ≥2× secondary, secondary ≥1.5× tertiary | power §2 |
| C8 | Line height | body 1.4–1.6; subhead 1.25–1.4; display 1.0–1.2 (0.95 allowed very large); medical title 1.0–1.15, body 1.15–1.3, bullets 1.3–1.5, captions 1.0 | power rule 9; medical `TYPOGRAPHY_GUIDELINES.md` |
| C9 | Line length | body ≤60 ch (ideal 45–60); display ≤30 ch | power rule 10 |
| C10 | Tracking | display −0.01 to −0.02 em; all-caps +0.05 to +0.1 em | power §4 |
| C11 | Font families | academic 1; power ≤2 (serif+sans or different superfamilies); pitch ≤3; robonuggets tested pairs of 2; minorun theme = display + body | academic §3; power §4; pitch `SKILL.md`; minorun `slide-design-dark` |
| C12 | Weight floors | no 100–300 for body (vanishes under projection); allowed 400/500/600/700 (+800/900 display); display default 800 in hackathon presets | power §2; Esther `style-presets.md` "Critical: Font Weight Matters" |
| C13 | Medical adaptive tiers | sparse 32–36/30–34/18–22; medium 28–32/24–28/16–20; dense 24–28/20–22/14–18 (title/body/label) | medical `TYPOGRAPHY_GUIDELINES.md` |
| C14 | Medical absolute floors | title 24, body 18, figure label 14, table 12, citation 10 pt; adjacent slides within ±2 pt | same |
| C15 | YC deck numeric type | headline 36–48 pt; body 18–24 pt; metrics 48–72 pt | yc `create/SKILL.md` |
| C16 | Minorun dark theme | body 26, h1 36, crosshead 44, cover 52 pt | minorun `slide-design-dark` "テーマの基本" |
| C17 | Code blocks | ≥21.5 pt (≈16 pt PDF); ≤60 half-width chars per line; one property per line | minorun `slide-design-dark` "コード" |
| C18 | Figure text | ≥16 pt at exported size; ≥14 px from box edge; labels 19–22 px when viewBox 1000 pasted at 1000 | minorun `slide-figures` "文字サイズ" |
| C19 | Robonuggets heading roles | h1 3em, h2 1.3em, h3 0.6em with 0.2em tracking | `robonuggets_marp-slides/SKILL.md` |
| C20 | Orphan/widow | kill any one-word last line; break at punctuation/meaning by hand | minorun `slide-design-dark` "縦のバランス" |

**Unit warning.** These skills mix `pt` and `px` on a 1920×1080 canvas with no conversion stated. Two mappings are possible — PowerPoint's 13.333 in-wide slide gives **2 px per pt** (20 pt = 40 px), while treating the canvas as 20 in wide at 96 dpi gives **1.333 px per pt** (20 pt ≈ 27 px). `[INFERENCE]` — neither is stated by any source. The merged skill should pick one explicitly; see Contradictions #3 and Gaps #1.

### D. Colour rules

| # | Rule | Threshold | Source |
|---|---|---|---|
| D1 | Academic palette | white ground; ≤3 colours; navy `1F4E79`, mid-blue `2E75B6`, highlight `FFF2CC` | academic `SKILL.md` §3; `slide_patterns.md` |
| D2 | Pitch palette | 2–3 brand colours + 1 accent | pitch-deck-mastery "Visual Rules" |
| D3 | 60-30-10 | 60 dominant / 30 secondary / 10 accent; accent 5–15 % of pixels; <2 % = no accent | power rule 12 |
| D4 | Accent count | 1 per slide, 1 per deck; emphasis 1 per slide and 1 per 2–3 body slides | power rule 13; minorun `slide-story` "1スライドの情報量"; `slide-design-dark` "強調" |
| D5 | Contrast | body 4.5:1, large 3:1, UI 3:1; aim 7:1 for projection; text-over-image ≥4.5:1 at 9 points | power rule 11 + §10 |
| D6 | Never hue alone | pair with shape/label/icon/weight; ~8 % of men red-green | power rule 14 |
| D7 | Dark-mode luminance ratio vs black | headings/lines 10–12; solid fills 6–7; hero box 4.5–5.5; body callout 2.5–3; secondary box ~1.5 | minorun `slide-design-dark` "配色" |
| D8 | Dark-mode contrast steps | double the steps 21 → 10 → 6 → 3; ≤1.5× is invisible; projected header ≤10, never <7 | same |
| D9 | Same colour, fill vs text | a large fill reads brighter, thin text darker; raise text/line colours 1–2 steps | same |
| D10 | Tone before hue | fix lightness/saturation mismatch before moving hue (hue carries meaning) | same |
| D11 | Brand colour use | text: raise lightness; fills: darken + white text; only the cover band may use it raw | same |
| D12 | Colour scheme types | monochromatic / analogous (≤30°) / complementary (180°) / split-complementary (150°/210°) / triadic (120°); never mix schemes | power §5 |
| D13 | Template palette | medical: use template colours only, never introduce new colours | medical `DESIGN_PRINCIPLES.md` #2, `TEMPLATE_INHERITANCE.md` |
| D14 | User colour preference | archetype first; negatives 100 %; theme context moderate; positives 2–3 of 5; variety last | Esther `style-presets.md` "Color Priority" |
| D15 | Status colours | green `#22c55e` active / yellow `#f5a623` learning / red `#ef4444` paused; never hue-only | robonuggets `SKILL.md` |

### E. Density and word budgets

| # | Rule | Threshold | Source |
|---|---|---|---|
| E1 | Words per content slide | academic ~40; power presenter ≤25 / document ≤75; hackathon ≤50 prose; YC billboard ~7-word headline | academic §4; power rule 20 + §11; Esther `iteration-patterns.md`; yc `create/SKILL.md` |
| E2 | Bullets | 3–5 typical (academic); ≤3 bullets and ≤8 words (power); 3–4 × 1–2 sentences (minorun); 6×6 rule explicitly rejected | academic §4; power §8; minorun `slide-story` table |
| E3 | Chunks | ≤7 ± 2, ideal 3–5; Cowan ≈4 for slides; group >5 into ≤5 super-chunks | power rule 3 + §1 |
| E4 | Slide structure (talk mode) | 1 heading + 3–4 body lines; heading 1 line; 1 figure; table 2–3 columns | minorun `slide-story` "1スライドの情報量" |
| E5 | Medical density | sparse ≤3 lines; medium 4–8; dense 9+; dense still allowed at 20–22 pt | medical `TYPOGRAPHY_GUIDELINES.md` |
| E6 | Image share | 60 % of slide area ±10 % when images present; ≥50 % enforced; per-count minimums 50/30/35/15/12 % | medical `IMAGE_LAYOUT_GUIDELINES.md` |
| E7 | Canvas allocation | 60 % primary / 25 % supporting / 15 % breathing; ≤25 % unused on content slides (>30 % = QA fail) | medical `DESIGN_PRINCIPLES.md` #4, `COMMON_FAILURES.md` #5, `QA_CHECKLIST.md` |
| E8 | Hackathon card copy | 8–15 words per card; ≤6 cards in a 3×2; flow boxes 5–7 | Esther `slide-patterns.md` patterns 5, 8 |
| E9 | Pitch bullets | ≤10 words per bullet | pitch-deck-mastery "Content Rules" |
| E10 | Comparison slides | exactly 2 numbers at 88 pt + 1 line + a divider | minorun `slide-design-dark` "比較のスライド" |

### F. Layout, spacing and grid

| # | Rule | Threshold | Source |
|---|---|---|---|
| F1 | Edge safe zone | 5 % of width (≥96 px at 1920); 8 % (154 px) if front-row cropping | power rule 5 + §7 |
| F2 | 8-pt spacing | all spacing multiples of 8 (4 for icons); scale 4–256 | power rule 15 |
| F3 | Grid | 12 columns, 24–32 px gutters, 96 px margins; col ≈117 px; snap sub-4 px | power rule 16 + §6 |
| F4 | Proximity | related ≤16 px; unrelated ≥48 px; between-group ≥2× within-group | power rule 17 + §3 |
| F5 | Whitespace | ≥40 % content, ≥60 % hero, ≥70 % quote | power rule 4 + §6 |
| F6 | Academic margins | ≥0.5 in (0.5 in = 96 px at 1920) | academic §3 |
| F7 | Medical margins | ≥0.3 in, target 0.5 in; image↔text 0.2–0.3 in; image↔image 0.15–0.2 in; text↔text 0.2–0.3 in | medical `LAYOUT_GUIDELINES.md` |
| F8 | Minorun gaps | elements ≥30 px; figure top ~36 px / bottom ~44 px; content bottom/right ≥60 px; figure↔text ≥36 px; text↔box edge ≥14 px | minorun `slide-design-dark` |
| F9 | Illustration inset | right edge inside the body margin (118 px when margins are 96 px) | minorun `slide-figures` "入れる数と位置" |
| F10 | Reading pattern | F for text, Z for image-led; key element in top-left quadrant / first 30 % of height | power rule 19 |
| F11 | Symmetry | snap if side margins differ ≤5 %; else ≥15 % asymmetry | power §3 |
| F12 | Cards | padding ≥24 px, gap ≥24 px | power §3 |
| F13 | Golden ratio | 38 % / 62 % only for hero splits (8-pt grid is the daily driver) | power §6 |
| F14 | YC content area | 80 % of slide width, centred | yc `create/SKILL.md` |
| F15 | Robonuggets padding | 56/72 px typical (≈7.8 % / 10 % of a 1280×720 canvas) | `robonuggets_marp-slides/SKILL.md` |
| F16 | Rhythm | no 3 consecutive same-form slides; no 5 consecutive text slides; no 6 same-type figure slides | minorun `slide-story` "前後の枚と並べて見る"; `slide-design-dark` "見せ方のリズム" |

### G. Diagram and figure rules

| # | Rule | Threshold | Source |
|---|---|---|---|
| G1 | One exhibit/figure per slide | 1; a diagram-only page with the same heading is allowed | academic §3; minorun `slide-story` |
| G2 | Figure-first vs text-first | figure-first = figure full width + heading + 1 lead line; text-first = illustration 100–330 px | minorun `slide-figures` "描く前に決めること" |
| G3 | Build-up | split a mechanism figure across 3–5 slides, one element at a time | minorun same; `slide-story` "演出" |
| G4 | Figure text | ≥16 pt exported; ≥14 px to edge; 19–22 px at viewBox 1000 | minorun `slide-figures` |
| G5 | Label placement | box name outside/above (14 px); no sub-labels; no prose annotations; labels ≥10 px from arrows | minorun same; `slide-design-dark` "図のラベル" |
| G6 | Element count | ≤3–4 parallel items before grouping; people track ~3 | minorun `slide-figures` "情報量の規律" |
| G7 | Arrows | head 18 px fixed, shaft ≥3× head, no line-through-label | minorun `slide-figures` "矢印" |
| G8 | Architecture | draw client nodes; real boundaries only; out-of-scope pale; arrows as implemented; official icons; infrastructure as a base layer | minorun `slide-figures` "構成図" |
| G9 | 2×2 matrix | uniform pale cells, identical chips, no corner notes, no cell colour coding, arrows contrasting | minorun `slide-figures` "2軸の図" |
| G10 | De-machine | no emoji icons; people as illustrations; one-line labels; hierarchy by fill (4 tiers); surfaces match the slide ground | minorun `slide-figures` "機械っぽさを消す" |
| G11 | Don't over-simplify | keep timelines, branching, bar counts, one illustration, hero number; delete only fine text | minorun `slide-figures` "削りすぎない" |
| G12 | Figure choice | photo for emotion/authenticity; illustration for abstract concepts; diagram for relationships; icon only to reinforce a label | power §10 "Photo vs Illustration vs Diagram" |
| G13 | Icon sizes | 16/20/24/32/40/48/64/96; inline = 1 em; never <16 px | power §10; robonuggets 16/32/44 |
| G14 | Full-bleed vs framed | full-bleed when the image is the message (no padding); framed when it supports (50–66 % width, inside grid) | power §10 |
| G15 | Text over image | scrim 40–70 %, or shadow ≥2 px/30 %, or solid panel ≥24 px padding; re-measure 9 points ≥4.5:1 | power §10; §3 figure/ground |
| G16 | Medical image minimums | radiograph 3.0×2.0 in (20 %); clinical 2.5×2.0 (15 %); chart 3.5×2.5 (25 %); pathology 2.5×2.0 (15 %); diagram 3.0×2.5 (25 %) | medical `IMAGE_LAYOUT_GUIDELINES.md` |
| G17 | No duplicate figures | one appearance per image; cross-reference by slide number; A/B on a comparison slide | medical `COMMON_FAILURES.md` #4 |
| G18 | No text over medical images | captions below/beside; only labels that are part of the image | medical `IMAGE_LAYOUT_GUIDELINES.md` "Never Do This" |
| G19 | Illustration count | ~1 per 8 slides (6 in a 49-slide deck); never twice the same; only on text-only pages | minorun `slide-figures` "入れる数と位置" |
| G20 | Figure–text adjacency | spatial contiguity ≤32 px label-to-target; claim and example adjacent | power §8; minorun `slide-story` "本編の運び" |

### H. Data-visualisation rules

| # | Rule | Threshold | Source |
|---|---|---|---|
| H1 | Data-ink ratio | ≥80 %; no 3D/gradients on data/shadows on bars | power rule 18 + §11 |
| H2 | Gridlines | ≤4 horizontal at 50 % opacity; axis labels only at relevant ticks; direct labels over legends | power §11 |
| H3 | Series count | ≤5 per chart, else small multiples | power §11 |
| H4 | Chart title | conclusion with a verb/comparison, not a noun phrase | power §11 |
| H5 | Annotate the key finding | arrow, shaded region, text annotation or focal colour | academic §3 |
| H6 | Graphs vs tables | graph for trend/comparison/distribution; table for exact values; 2–3-column tables in talks; medical dense tables allowed at ≥12 pt | academic §3; minorun `slide-story`; medical `TYPOGRAPHY_GUIDELINES.md` |
| H7 | Table styling (dark) | no fill, hairline rules only, header 18 pt muted, body 22 pt, first column white bold, ≤6 rows, key row shaded, no footnote | minorun `slide-design-dark` "表" |
| H8 | Table structure | no empty header cell; hierarchy 4 columns into 2 groups; don't place a third column in a 2-way comparison | minorun `slide-story` "箱と表" |
| H9 | Chart type menu | line/area, donut/pie (dasharray maths), gauge, donut ring, sparkline, stacked bar, vertical bars, radar | robonuggets `SKILL.md` "SVG Charts" |
| H10 | Metric card anatomy | eyebrow label + hero number (2 em, 800) + delta with arrow + 2 px accent hairline | robonuggets `SKILL.md` "Metric Card" |
| H11 | Medical chart QA | axes labelled, units shown, legend readable, data labels clear, colours from template | medical `checklists/design_review.md` |
| H12 | Number formatting | 3 numbers → colour only the one that leads onward; comparison = 2 numbers at 88 pt | minorun `slide-design-dark` "強調", "比較" |

### I. Imagery, iconography and branding

| # | Rule | Threshold | Source |
|---|---|---|---|
| I1 | No decorative icons | academic and medical forbid decorative icons, clip art, stock photos | academic §3; medical `DESIGN_PRINCIPLES.md` #8 |
| I2 | Logo discipline | power default: logo every slide, 24 px tall, bottom-left, inside the 5 % zone; YC: top-right ≤60 px; hackathon: logo emoji once | power `SKILL.md`; yc; Esther |
| I3 | Emoji logo | 1 primary + 2–5 supporting; avoid 💡🚀⭐✨💎⚡; consistent family | Esther `slide-patterns.md` "Rules to prevent emoji chaos" |
| I4 | No emoji in medical/academic | professional/academic style bans emoji and casual punctuation | medical `DESIGN_PRINCIPLES.md` #8; academic §3 |
| I5 | Illustration selection | depict the slide's key noun, not the vibe; positive images only under positive conclusions | minorun `slide-figures` "選び方" |
| I6 | Real screenshots for products | screenshots for products/repos, illustrations for concepts | minorun `slide-figures` "選び方" |
| I7 | Image quality | ≥150 DPI at display size; no pixelation/stretch | medical `checklists/design_review.md` |
| I8 | White-fill SVG logos | recolour before use on light ground | power `lib/extract-brand.md` |

### J. Verification and QA rules

Consolidated into the final checklist below. The distinctive *meta*-rules worth stating separately:

| # | Rule | Source |
|---|---|---|
| J1 | Re-run the **entire** QA layer after any fix, not just the failed check; no manual overrides | medical `docs/QA_CHECKLIST.md` "QA Failure Protocol" |
| J2 | One page's criticism is an instruction to check **all** pages for the same condition; report the list, then fix, then re-run to zero | minorun `slide-design-dark` "書き出したら検査する" |
| J3 | Machine checks only measure elements that exist; a fully missing element is invisible to them — visual inspection is mandatory | minorun `slide-design-dark` / `slide-figures` |
| J4 | Never claim visual verification that wasn't done; distinguish "contact sheet reviewed" from "every page at ≥150 dpi" | minorun `slide-design-dark` "機械検査のあとに" |
| J5 | Ghost-deck test before building and after building | academic `SKILL.md` §2, §Step 4 |
| J6 | Content audit against source before design review; zero omissions | medical `CONTENT_INTEGRITY.md` |
| J7 | Cross-reference audit after any reorder (slide numbers, figure numbers, table numbers) | medical `checklists/submission_checklist.md` |
| J8 | End-to-end playback test in a fresh player before submission | Esther `workflow-phases.md` Phase 8 |
| J9 | After inserting pages into an existing deck, re-count emphasis ratio, duplicate examples and runtime | minorun `slide-story` "既存のデッキへ足したら" |
| J10 | Count heading style metrics across the whole deck (not per page) to catch machine monotony | minorun `slide-story` "全見出しを並べて数える" |

---

## Merge recommendations

| Idea | Source skill(s) | Keep / adapt / drop | Why | Where it belongs |
|---|---|---|---|---|
| Action titles + ghost-deck test | academic | **keep** | The strongest single content gate; testable with `get-design-content` by concatenating page titles | plan, review |
| Research-question-on-its-own-slide | academic | **keep** | Forces the deck to have a thesis; cheap to enforce | plan |
| One argument / one job per slide | academic, power rule 1, pitch | **keep** | Universal, and the root cause of most bad decks | plan, review |
| SCR / Funnel / Answer-First spine choice | academic | **adapt** | Keep as a single "pick a spine" question; Answer-First conflicts with minorun's withholding rule — make it an explicit audience choice | plan |
| 12-slide investor arc | pitch-deck-mastery, yc | **keep** (as a preset) | Battle-tested for fundraising; not for academic talks | plan (template) |
| 3 vertebrae | yc | **keep** | Three sentences that must survive every slide; excellent pre-flight compression | plan |
| Crossheads as audience inner voice + cadence | minorun | **keep** | Gives a deck its forward motion; cadence rules prevent overuse | structure, plan |
| "Don't reveal the answer first" | minorun | **adapt** | Right for talks and teaching; wrong for executive/grant audiences who want the answer up front — gate on audience type | plan, review |
| Hook types + two audience questions | minorun | **keep** | Solves the "definition-first" opening that kills most student decks | plan |
| Concept 3-piece set (what / why / crude summary) | minorun | **keep** | Directly applicable to explaining a philosophical or technical concept | plan, structure |
| 7-step talk body | minorun | **keep** | Concrete-before-abstract ordering; fits coursework explanations | plan |
| 20 codified slide rules with numbers | power-design | **keep** | The review rubric the skill will run on every page | review (core) |
| Numbers cheat sheet | power-design | **keep** | Becomes the skill's `references/thresholds.md` | reference |
| Mode token (presenter vs document) | power-design | **adapt** | In Canva, document mode is a real deliverable (exported PDF); presenter mode is the classroom case | plan |
| 8-pt grid, 12-col grid, safe zone | power-design | **adapt** | Cannot set a grid in Canva, but can *judge* alignment and margins from thumbnails and can position elements to 8-pt multiples | review, edit |
| 40/60/70 % whitespace | power-design | **adapt** | Measure from exported PNGs; conflicts with medical density — mode-dependent | review |
| 60-30-10 + single accent | power-design | **keep** | Works on any medium; accent count is checkable via `get-design-content` colours | plan, review |
| WCAG contrast ladder + 7:1 projection target | power-design | **keep** | Projector washout is real in classrooms; computable from hex values | plan, visuals |
| Dark-mode luminance-ratio design | minorun | **keep** | The only rigorous dark-palette method found; applies whenever the deck is dark | visuals |
| Density-adaptive typography tiers | medical | **keep** | Solves the "one fixed size" failure; combine with power's floors | plan, edit |
| Content-integrity policy + audit | medical | **keep** | Especially relevant when `create-design` paraphrases and can swap doctrinal terms | plan, review |
| Explicit overflow ladder (dedupe → layout → split → add slides) | medical, minorun | **keep** | Gives the agent a deterministic repair order instead of shrinking type | edit |
| Three-layer QA → merged severity checklist | medical (+ all) | **adapt** | Merge into one severity-ordered list (below); keep the re-run-whole-layer rule | review |
| Image-area rule (60 %, per-count minimums) | medical | **adapt** | Convert inches to px; use as a visual QA heuristic on thumbnails | visuals, review |
| Figure information discipline (no sub-labels, ≤3–4 items, split across 3–5 slides) | minorun | **keep** | The best diagram guidance in the cluster; directly improves "strong visuals" | visuals |
| SVG implementation numbers (16 pt, 14 px, 18 px heads, no gradient text) | minorun | **adapt** | Only relevant if we author SVG before upload; still valuable as a spec for the diagram author | visuals |
| Chart type menu + donut maths | robonuggets | **adapt** | Use as the vocabulary for diagram briefs; not as code | visuals |
| Metric card anatomy | robonuggets | **keep** | Best single visual unit for traction/results slides | visuals |
| 35-slide/10-min timing model + venue units | minorun | **keep** | Far more accurate than 1 slide/minute for short talks | plan, delivery |
| 1 slide/minute + 1–2 min under | academic | **keep** (as the conservative default) | Simple and safe for academic talks | plan |
| Narration script with 170 wpm budget | Esther | **keep** | Compensates for read-only presenter notes | delivery (sidecar) |
| PLAN.md context file | Esther | **keep** | Long Canva sessions lose context; a durable outline is the fix | plan |
| Show-don't-tell style previews (5 curated, 3 pages each) | Esther | **adapt** | In Canva: generate 3 short sample designs, export thumbnails, let the user pick; then build the real deck | plan, visuals |
| 5-2-2-1 curation | Esther | **drop** (mostly) | Requires a 13-preset pool; we have no preset library. Keep the anti-paralysis principle (≤3 options) | plan |
| Style preset pool (13 with font blocks) | Esther | **adapt** | Keep as a *naming vocabulary* for aesthetic directions; font blocks are unusable (no font-family op) | visuals |
| Global nav chrome (dots, counter, arrows) | Esther | **drop** | Impossible in Canva; the presenter app supplies navigation | delivery |
| Animated demo archetypes | Esther | **drop** | No animation ops; the equivalent is a static diagram sequence across pages | visuals |
| Video embedding | Esther | **drop** | Canva can host video, but MCP editing cannot insert it; user must do it in the editor | delivery |
| Submission/export checklist | Esther, medical | **keep** | Export format, filename, size, playback test | delivery |
| Template fidelity | medical | **adapt** | No templates, but "never restyle an inherited design" is the transferable rule | plan, edit |
| Reuse-and-derive discipline (copy verbatim, 3 allowed edits, one canonical base) | minorun | **keep** | Directly applicable to iterating a Canva deck across sessions | edit, structure |
| Deletion audit (list elements, diff after) | minorun | **adapt** | With `get-design-content` we can diff text before/after; pair with group-id delete | edit |
| Wording-fix vs structure-fix review split | minorun | **keep** | Prevents unreviewed structural churn | edit |
| Emphasis budget (1/slide, 1 per 2–3 body slides) | minorun, power | **keep** | Checkable by counting coloured/bold runs | review |
| Heading-style mixing + measured metrics | minorun | **adapt** | Language-specific (Japanese polite/plain). Generalise to "vary heading grammar; count repetition" and set per-language baselines | review |
| Quote-only-from-real-logs | minorun | **keep** | Anti-fabrication rule; critical for academic integrity | review |
| "At least one honest caveat" | minorun | **keep** | Improves academic credibility | plan |
| Professional/academic style bans (no clip art, no emoji, no marketing language) | medical, academic | **keep** for academic mode | Audience-appropriate; conflicts with hackathon mode | review |
| Brand extraction (Firecrawl, 6 values) | power | **drop** tool, **keep** the 6-value minimum | No Firecrawl/brand kits; still the right minimum palette spec | plan, visuals |
| 72-brand library | power | **adapt** | Use as hex references only; schemas are inconsistent (8 lack an accent row) | visuals (reference) |
| Marp/HTML/PptxGenJS/python-pptx code | all | **drop** | Wrong medium; keep only the numbers and structures | — |
| Robonuggets component recipes | robonuggets | **drop** code, **keep** chart vocabulary | Components can't be inserted; chart types can be briefed | visuals |

---

## Contradictions

1. **Answer first vs withhold the answer.** Academic Option C ("lead with the conclusion") and pitch-deck-mastery ("lead with the headline") vs minorun's hard rule ("do not reveal the answer first; no agenda, no summary, no overview"). **Recommendation:** make it audience-conditional, not a house rule. Grant panels, executive reviews and investor decks get answer-first; teaching, conference talks and thesis defences get progressive disclosure. State the choice in the brief and enforce it deck-wide (power-design's "one mode per deck" logic).

2. **Density: sparse vs dense.** Academic caps content at ~40 words and 20 pt; power-design caps presenter mode at 25 words; minorun caps at 1 heading + 3–4 lines; medical explicitly allows 9+ lines and 20–22 pt on a "dense" slide and calls simplification a failure mode. **Recommendation:** adopt a **three-mode token** — `presenter` (≤25 words), `talk` (≤40 words, minorun's 3–4 lines), `document` (medical density, ≤75 words, 20 pt floor). The medical position is right for case reports and handouts; it is wrong for a projected classroom talk. Do not average them.

3. **Point sizes vs pixel sizes on a 1920×1080 canvas.** Academic says body 20 pt; power says body 24 px; YC says body 18–24 pt and headline 36–48 pt; minorun says body 26 pt; our own verified experience is that body **34–38 px** and titles **~52 px** are readable in a classroom. With PowerPoint's 13.333 in-wide slide, 20 pt = **40 px**; with a 20 in-wide reading, 20 pt ≈ **27 px**. `[INFERENCE]` — no source states the mapping. **Recommendation:** define the skill's canonical unit as **px on the 1920×1080 canvas** (because that is what Canva exposes): body ≥34 px, titles 52–64 px, secondary 26–28 px, captions ≥24 px, absolute floor 24 px. Note in a footnote that this corresponds to roughly 17–19 pt under the PowerPoint mapping and ~26–28 pt under the 20-inch mapping, so users who think in pt should not be surprised. One caveat from power-design that survives either mapping: **aim for 7:1 contrast because projectors wash out 30–50 %**.

4. **Font count.** Academic: one face. Power: ≤2. Pitch: ≤3. Minorun's theme: 2 (display + body). Robonuggets: 2. **Recommendation:** one family is ideal and is all Canva can guarantee (no family op); if the generated design uses two, accept them but enforce one weight/size hierarchy scheme. Never claim font consistency we cannot verify — check weight/size/colour consistency instead.

5. **White space: ≥40 % empty vs ≤25–30 % unused.** Power-design mandates ≥40 % empty on information slides; medical treats 30–50 % blank while content is cramped as a failure and targets ≤25 % unused. **Recommendation:** they measure different things — *empty pixels* vs *unused canvas while content is crammed*. State the medical version as the rule ("no quadrant empty while another is crowded") and the power version as a *hero/title* target (≥60 % on covers). On content slides, allow 25–40 % empty.

6. **Summary slide: required vs forbidden.** Academic requires a Conclusions slide that stays up during Q&A; minorun forbids summary slides and ends on a call to action. **Recommendation:** academic/defence mode keeps Conclusions (it is the Q&A anchor); talk/pitch mode ends on the CTA or the Ask. Never end on "Thank You".

7. **Action titles vs label headings.** Academic mandates a complete-sentence action title on every content slide; minorun says body slides in lectures should use short **labels** and reserves claim-style headings for crossheads; pitch-deck-mastery wants takeaway headlines. **Recommendation:** action titles for argument-driven decks (academic, investor), labels for instructional/step decks. Detect mode, then enforce one convention for the whole deck.

8. **Slide count per minute.** Academic: max 1 slide/minute (10 min → 8–10 content slides). Minorun: 10-minute LT ≈ **35 slides** total at ~16 s per slide. **Recommendation:** use academic's budget for argumentative academic talks (each slide carries evidence), minorun's unit costs for demo/teaching talks (many fast slides, crossheads at 8 s). Do not mix the two models in one estimate.

9. **Bullets.** Pitch allows them freely (≤10 words); power rejects the 6×6 rule and prefers ≤3 bullets or none; minorun allows 3–4; academic allows 3–5 as "orientation cues". **Recommendation:** bullets are a fallback in every source except academic; cap at 3–4 in talk mode, allow 3–5 in academic document mode, and prefer a diagram or a single statement.

10. **Decorative imagery.** Academic and medical ban decorative icons, stock photos, clip art and emoji. Esther and minorun use illustrations, mascots and emoji logos heavily. **Recommendation:** tie to audience. Academic/medical/institutional → no decoration. Hackathon/consumer/teaching → illustration allowed under minorun's rules (depicts the key noun, count ≈1 per 8 slides, no duplicates). Never mix both in one deck.

11. **Template fidelity vs design freedom.** Medical says the institutional template is sacred and the designer is a "precision instrument, not a creative director"; power-design and Esther start from brand DNA and a chosen aesthetic. **Recommendation:** if the user supplies an existing deck/template, medical's rule wins (copy-design, edit content only). If starting from scratch, power/Esther win (choose the aesthetic first). Make this the first question after "what is the deck for?".

12. **Logo on every slide.** Power's `SKILL.md` default (#21) puts the logo on every slide; its own §1 signal-to-noise rule says footer logos belong on title and closing only. **Recommendation:** logo on cover + closing, plus a small mark on interior slides only if the user's institution requires it. This also reduces Canva work.

13. **"Charts over tables" vs "prefer graphs" vs medical tables.** Pitch and robonuggets favour charts; academic prefers graphs but explicitly reserves tables for exact values; medical treats tables as first-class evidence (with ≥12 pt text). **Recommendation:** graph for trend/comparison, table for exact values; academic and minorun both cap it at one exhibit per slide (pitch and robonuggets don't address exhibit count, so they don't override that cap).

14. **Academic-pptx internal contradiction.** `SKILL.md` says "No accent lines under titles — use whitespace instead", while `slide_patterns.md` draws a 0.025 in rule under every content title in code. **Recommendation:** follow the prose (no rules); the pattern file is older implementation detail. Note this when harvesting the file so the skill doesn't import both.

15. **Power-design internal contradiction.** Fitts's Law says the dominant element must occupy ≥25 % of slide area **or be ≥3×** larger, while the Focal Point principle and Appendix A say **≥1.5× the area**. **Recommendation:** use 1.5× area (or "the only saturated element", or "+48 px isolation") — 3× is unachievable with a headline over body text at the recommended 2–4 ratio.

---

## Gaps

What a complete Canva slide workflow needs that **none** of these eight skills covers:

1. **A unit contract.** No source states how its pt/px numbers map onto a 1920×1080 Canva canvas, and they disagree by ~1.5×. The merged skill must define one unit (px recommended) and give a conversion footnote.
2. **The Canva operation layer.** Every source targets another medium (PptxGenJS, python-pptx, HTML, Marp). Missing: the exact op sequence for each edit (`replace_text` vs `find_and_replace_text`, `update_title`, `format_text` on runs), the transaction protocol (start → operate → inspect thumbnails → commit), what to do when an op no-ops (grouped child ids), and rollback (`cancel-editing-transaction`).
3. **Page generation strategy.** No source covers generating a deck whose page count and page roles are fixed in advance, nor how to add/replace a page later. `merge-designs` is the only lever and it has a known reversed-insert bug; no source warns about it.
4. **Typography without font-family control.** Every typography rule in the cluster assumes you can choose the face; we cannot. Missing: a font-agnostic hierarchy system (size ratio + weight + colour + alignment), a diagnostic for "the generated template uses 3 families", and a decision rule for regenerate-vs-accept.
5. **Colour without a brand kit.** Power-design's brand extraction and Esther's presets both assume you can define the palette. We have zero brand kits and no background-change op, so the palette must be chosen *before* generation and then applied only to text and existing fills. Missing: a palette-derivation procedure from a hex list, a contrast pre-check, and a rule for covering unwanted template decoration with background-matched `insert_fill`.
6. **Diagram authoring pipeline.** Minorun's figure rules are the best in the cluster but assume SVG in the deck. We need: brief → external render (SVG/PNG) → `create-upload-url` → insert as image → position/resize → verify. Missing: image sizing maths for the 1920×1080 canvas, how to guarantee ≥16 pt label size after scaling, and how to replace a diagram later (no z-order control).
7. **Text-diff verification against source.** Medical's content audit is manual; `create-design` paraphrases and can swap doctrinal terms. Missing: a procedure to extract text (`get-design-content`), diff it against the source outline, and flag every semantic change (a prior verified session on a Vietnamese philosophy deck had the generator substitute "phát triển" for a required term — `[prior verified session]`, not re-run here).
8. **Presenter notes.** `get-presenter-notes` is read-only. Esther's narration script and minorun's talk timing are the right material, but no source defines a sidecar file format that pairs with an exported PDF, nor how to keep it in sync when pages change.
9. **Accessibility inside Canva.** No alt-text op, no reading-order control, no contrast checker in the tool. Missing: a pre-generation accessibility brief and a post-export manual check.
10. **CJK / Vietnamese typography in Canva.** Esther documents Noto fallbacks for CJK; nothing covers Vietnamese diacritics at large sizes (line-height and clipping risks), which is the actual use case here.
11. **Deck-level consistency audit.** Only minorun measures across pages (heading metrics, emphasis ratio, rhythm). Missing: a scripted audit over `get-design-content` for size drift, colour drift, heading-length monotony, duplicate examples and repeated layouts.
12. **Cost and quota awareness.** `generate-image` can fail with `credit_quota_exceeded`; no source discusses quotas, retries, or fallback to uploads/stock.
13. **Comment-based review.** `comment-on-design`/`list-comments` exist and no skill uses them; a review workflow that leaves per-page comments would beat a chat summary.
14. **Responsive pages.** The MCP exposes `resize-design` and responsive pages accept only a restricted op set; no source addresses what breaks and what to do.
15. **Narration timing vs slide count for non-English text.** 170 wpm is an English TTS figure; Vietnamese narration runs at a different rate. Needs a measured local baseline.

---

## Unified QA checklist (severity-ordered, deduplicated)

Every item below is drawn from at least one source; duplicates across skills are merged. Severity 1 blocks delivery, 2 must be fixed before review sign-off, 3 is a quality pass, 4 is polish, 5 is packaging.

### Severity 1 — Blocking (content truth, legibility, structural integrity)

1. **Zero content omissions against the source** — every section, number, date, unit and diagnosis/term present and exact (`medical/CONTENT_INTEGRITY.md`; case study).
2. **No semantic drift introduced by generation** — paraphrases, swapped doctrinal terms, invented claims checked against the outline (`[INFERENCE]` from our own `create-design` behaviour; academic's content-QA loop).
3. **No fabricated quotes, logs or prompts** — quoted material must come from a real artifact (`minorun slide-story` "引用枠と吹き出し").
4. **No unresolved placeholders** — no `[Click to add…]`, `<Project Name>`, `{placeholder}`, AI-instruction remnants (`medical/submission_checklist.md`; Esther Phase 8).
5. **No overflow, clipping or overlap** — text not cut by its box, no text on images, no shape over text (`medical/submission_checklist.md`; Esther `video-integration` final checklist).
6. **Every body text at or above the legibility floor** — ≥34 px on our canvas (≥20 pt academic / ≥24 px power / ≥18 pt medical dense floor) (`academic §4`; `power rule 8`; `medical TYPOGRAPHY`).
7. **No slide with two headlines or two competing ideas** (`academic §1`; `power rule 1`).
8. **One exhibit per results slide, and the key finding is annotated on it** (`academic §3`).
9. **Every borrowed figure/data point cited on the slide**; references slide exists (`academic §5`, §6).
10. **Cross-references correct** — slide/figure/table numbers, appendix pointers (`medical/submission_checklist.md`).
11. **Correct page order, no duplicated or missing pages, no orphaned divider** (`minorun slide-story` reuse rules; `merge-designs` order check `[INFERENCE]`).
12. **Contrast meets 4.5:1 body / 3:1 large / 3:1 UI, and 7:1 is targeted for projection** (`power rule 11`).
13. **Colour is never the only carrier of meaning** (`power rule 14`; WCAG 1.4.1).
14. **Template/brand fidelity** — no background, logo, palette or master changes in an inherited deck (`medical DESIGN_PRINCIPLES` #2).
15. **Clinical/academic logic intact** — diagnosis follows evidence, no contradictions between slides, limitations stated (`medical checklists/medical_review.md`; academic §6).

### Severity 2 — Major (comprehension and hierarchy)

16. **Ghost-deck test passes** — titles alone tell the argument (`academic §2`).
17. **Each crosshead is answered by the next slide; no more than 2 in a row; one every 3–6 body slides** (`minorun slide-story`).
18. **No preview/agenda/summary leak** if the deck is in withholding mode (`minorun slide-story`).
19. **One primary focal point per slide** — squint test; focal ≥1.5× the next element or the only saturated element (`power §2`, §3).
20. **Chunk count ≤7, ideally 3–5** (`power rule 3`).
21. **Type sizes within the token set** — ≤4 per slide, ≤6 per deck (`power rule 7`).
22. **Hierarchy ratio** — headline:body 2.0–4.0, subhead:body 1.25–1.5 (`power §2`).
23. **Line length ≤60 characters body / ≤30 display** (`power rule 10`).
24. **Line height in range** — body 1.4–1.6, display 1.0–1.2 (`power rule 9`).
25. **Whitespace** — ≥60 % on covers/quotes, 25–40 % empty on content slides with no crowded quadrant (`power rule 4`; `medical DESIGN_PRINCIPLES` #4).
26. **Images occupy ≈60 % of the slide when present, and meet the per-type minimum** (`medical IMAGE_LAYOUT`).
27. **Figure text ≥16 pt and labels ≥14 px from box edges** (`minorun slide-figures`).
28. **No sub-labels, annotation prose or duplicated statements inside diagrams** (`minorun slide-figures` "情報量の規律").
29. **≤5 data series per chart; ≤4 horizontal gridlines; no 3D/shadows/gradient data** (`power §11`).
30. **Chart title states the conclusion, with a verb or comparison** (`power §11`; `academic §2`).
31. **Density within the mode budget** — presenter ≤25 / talk ≤40 / document ≤75 words (`power §11`; `academic §4`; `medical TYPOGRAPHY`).
32. **Bullets ≤3–4 in talk mode, ≤8 words each** (`power §8`; `minorun slide-story`).
33. **No font-family fallback drift** — all runs use one family or a deliberate display/body pair; weights are 400–700 (no 100–300 body) (`power §2`, §4; Esther Font Sanity Check adapted).
34. **Emphasis budget respected** — 1 per slide, 1 per 2–3 body slides; new-term first-use emphasis counted separately (`minorun slide-story`; `power rule 13`).
35. **Deck-level rhythm** — no 3 consecutive same-form slides, no 5 consecutive text slides, no 6 same-type figure slides (`minorun slide-design-dark`).
36. **One mode per deck** — presenter/talk/document, no mixing (`power rule 20`).
37. **Investor/academic must-pass items** — one-liner, quantified problem, sourced market, credentials, clear ask / research question slide, methods, conclusions slide (`pitch-deck-mastery`; `academic §6`).
38. **Timing model run at the four checkpoints; landing time inside the slot** (`minorun slide-story` "尺の見積り").

### Severity 3 — Quality (craft and consistency)

39. **8-pt-consistent spacing** — margins, gaps and element offsets are multiples of 8 or visually consistent (`power rule 15`).
40. **Single alignment grid** — every element aligns to a column edge or another element; no floating images (`power rule 16`; `medical LAYOUT_GUIDELINES`).
41. **Proximity** — related ≤16 px, unrelated ≥48 px, between-group ≥2× within-group (`power rule 17`).
42. **Edge safe zone** — nothing within 5 % of any edge (`power rule 5`).
43. **Medical spacing set** — margins ≥0.3 in, image gaps 0.15–0.2 in, text gaps 0.2–0.3 in (`medical LAYOUT_GUIDELINES`).
44. **Accent share 5–15 % of pixels; no second accent** (`power rule 12`, rule 13).
45. **Heading style varied** — no uniform ending form across the deck; shortest heading noticeably shorter than the longest (`minorun slide-story` "見出しの文体は混ぜる").
46. **No repeated rhetorical pattern 3+ times** (comma-then-short, conjunction-led, colon headings) (`minorun slide-story`).
47. **No duplicate images across slides** (`medical COMMON_FAILURES` #4).
48. **Illustration count ≈1 per 8 slides; none on figure/table/code slides; never repeated** (`minorun slide-figures`).
49. **Figure–text gap ≥36 px; content ≥60 px from bottom/right edges** (`minorun slide-design-dark`).
50. **No one-word last lines; breaks made at meaning boundaries** (`minorun slide-design-dark`).
51. **Tables ≤6 rows, no fill, hairline rules, first column emphasised, no empty header cell, no footnote** (`minorun slide-design-dark`; `minorun slide-story`).
52. **Comparison slides exactly two numbers at large size** (`minorun slide-design-dark`).
53. **Cards equal height and width; grid consistent** (`Esther iteration-patterns`).
54. **Icons from one official set, sized from the allowed ladder, never emoji in academic/medical mode** (`minorun slide-figures`; `power §10`; `medical DESIGN_PRINCIPLES` #8).
55. **Medical adaptive tier consistency** — adjacent slides within ±2 pt (`medical TYPOGRAPHY`).

### Severity 4 — Polish

56. **Punctuation and typography hygiene** — no overuse of em-dashes/full-width colons, no underlining for emphasis, consistent date format (`minorun slide-story`; `medical/submission_checklist.md`).
57. **Title/label casing and tracking consistent**; all-caps labels tracked +0.05–0.1 em (`power §4`).
58. **Caption placement** — below figures, centred, same size across the slide (`medical IMAGE_LAYOUT`).
59. **Page numbers present and sequential where the template provides them** (`medical/submission_checklist.md`).
60. **Transitions/animations none or ≤300 ms, no flashing >3/s** (`power §9`; `medical DESIGN_PRINCIPLES` #8).
61. **No orphan appendix label; appendix slides clearly labelled** (`academic §6`).

### Severity 5 — Packaging and delivery

62. **Export in the requested format(s); confirm with `get-export-formats`** (`[INFERENCE]` from the MCP tool set; `Esther Phase 8`).
63. **Filename convention** `{Type}_{Topic}_{Date}` or descriptive project name (`medical/submission_checklist.md`; Esther Phase 8).
64. **File size within limits** (<50 MB medical; <200 MB for deck+video Esther).
65. **Plays/opens end-to-end in a fresh viewer** (`Esther Phase 8`; `medical/submission_checklist.md`).
66. **Narration/speaker notes delivered as a sidecar if requested** (`[INFERENCE]` — notes are read-only in our MCP; source material from Esther/minorun).
67. **Handout/print check** — readable in greyscale, no content cut by print margins (`medical/submission_checklist.md`).
68. **Report which checks were actually run; never claim visual verification that wasn't performed** (`minorun slide-design-dark` "機械検査のあとに、自分の目で見る").
