# 03 - Visual system: type, colour, grid, density, diagrams, anti-slop

One canvas, one unit: **everything below is in px on the 1920x1080 slide** (that is what `format_text`, `position_element`, `resize_element` and `insert_fill` use).
Sources disagree by ~1.5x because they mix pt and px (20 pt body, 24 px body, 26 pt body ...). Conversion if you meet pt in a source: PowerPoint's 13.333 in-wide slide gives **1 pt = 2 px at 1920 wide**
(20 pt body = 40 px); a 20-in reading gives 1.33 px/pt. This skill resolves the conflict with the user's own measured preference (classroom, back row): **body 34-38 px, titles ~52-56 px**.
Sources merged: power-design (20 numeric rules), SlideSpeak/Phlegonlabs/huashu/present-now (type, grid, density), academic-pptx and Geongyu (academic scale), medical (adaptive tiers, image area),
minorun (figure and dark-mode rules), lecture-slides (Layout Doctrine from 151 complaints), design-director (grid, anti-slop), lesson-designer (Vietnamese system), vstorm and anthropics (slop lists),
visualise and CHART (diagram and chart numbers).

## 1. Type system

### 1.1 Roles (default scale, talk mode)

| Role | px | Weight | Notes |
|---|---:|---|---|
| Cover title | 72-96 | bold | one to two lines; only place all-caps is tolerable |
| Slide title (action title) | **52-60** | bold | <= 2 lines; <= ~57 chars fit one line at 52 bold in a 1660 box |
| Lead sentence / definition | 46-52 | semibold | one sentence, <= 2 lines |
| Section label / card title | 40-44 | bold | repeated cards must share size and line count |
| **Body** | **34-38** | regular | the classroom floor; never < 32 |
| Support / caption | 30-34 | regular, muted | never < 28 |
| Diagram labels (in uploaded PNG) | title 40-46, caption 30-34 | bold / regular | at final placed size |
| Source / footnote / slide tag | 26-28 | regular, muted | absolute floor 24; shorten the text instead of going lower |
| Number badge | 56-72 | bold | only when the items are a real sequence |
| Hero number | 120-200 | bold | with a baseline ("37%, trung bình ngành 22%") |

Rules:

- **Tiers differ by >= 1.2x** (lesson-designer: >= 1.3x; power: headline:body 2-4 for 24-px bodies; at 36-px bodies the practical ceiling is ~1.5-1.6x, so add weight/colour to separate tiers). Do not use steps of only 10-20%.
- **<= 4 type sizes on a slide, <= 6 in the deck.** Sizes are integers; round, then re-check the floor.
- **One family** is ideal; **<= 2** (display + body) is the limit. `format_text` has **no font-family**, so the family is whatever the generated theme uses: confirm it on the first render and say so. Hierarchy comes from size, weight, colour and alignment only.
- **Weights 400/500/600/700.** No 100-300 for body (vanishes under projection).
- **Leading**: body 1.3-1.5 (Vietnamese diacritics want >= 1.3), subhead 1.25-1.4, display 1.0-1.2. `line_height` accepts 0.5-2.5.
- **Measure**: <= 60 characters for body, <= 30 for display. Use `resize_element width` to shorten lines, not smaller type.
- **Alignment**: left-align body (centre only a title, a big number, a conclusion). Left edges stay constant across the deck.
- **No all-caps for labels or body**; no tracking (Canva cannot set it; shouting is the result). All-caps cover title and <= 3-word diagram node labels are the only tolerated uses; check diacritic stacking (Ế, Ộ) does not clip.
- **No faux italic** and no underline for emphasis. **Bold first use of a new term** in running text (and accent it); otherwise one emphasis per slide, one per 2-3 body slides.
- **Never shrink to fit.** The overflow repair order is: (1) remove duplication, (2) change layout/width, (3) split across slides, (4) shorten the words keeping the meaning (compare old and new sentence). Only then reduce size, and never below the floor.

### 1.2 Density-adaptive tiers (medical, adapted)

| Register | Content | Body px | Notes |
|---|---|---:|---|
| sparse (definition, hero, divider) | <= 3 lines | 40-48 | whitespace is the message |
| medium (typical) | 4-8 lines | 34-38 | the default |
| dense (table, comparison, document mode) | 9+ lines | 30-32 | floor 28; move detail to the appendix before shrinking |

Adjacent slides stay within +/- 4 px body unless the register changes on purpose.

### 1.3 Vietnamese specifics

- Fonts must cover Latin Extended / Vietnamese (the generator's theme font did on all tests; confirm diacritics in every thumbnail: tone marks over circumflex/horn letters are the first to clip). Vietnamese-safe families seen in sources: Montserrat, Open Sans, Roboto, Nunito, Inter, Noto Sans. Because the family cannot be changed through the API, **choose it at generation time** by naming a type character in the brief, then verify.
- Expect Vietnamese to run **10-25% longer** than the English you may be thinking in, and one token is one syllable: keep bullets <= 12 syllable-words and titles <= 65 characters.
- Use real Vietnamese quotation and citation conventions on slides (see `09-education-playbooks.md`).
- Avoid long unbroken strings and hyphenation; break at meaning boundaries with `\n`.

## 2. Colour system

**Token architecture** (SlideSpeak tokens, smallest schema that still distinguishes a deck): `ground` (page, card, ink: near-black, never pure #000), `signal` (ONE accent + its darker sibling), `support` (muted grey for secondary text, hairline rule colour).

- **60-30-10**: ~60% dominant ground, ~30% secondary, ~10% accent (accent measures 5-15% of pixels; < 2% means no focal accent). **One accent per slide and per deck.** More than 3 chromatic colours is a violation; a categorical set may reach 5-6 only in a chart.
- **Contrast** (WCAG): body >= 4.5:1, large text (>= 24 px, or >= 18.66 px bold) >= 3:1, graphical marks >= 3:1. **Design for 7:1** because projectors wash out 30-50% of contrast. Compute with `scripts/contrast.py`. Muted grey support text on `#F7F8FA` must be >= 4.5:1 (`#5A6978` = 5.3:1 passes; `#9AA5B1` = 2.4:1 fails).
- **Never encode meaning in hue alone** (~8% of men are red/green deficient): pair with a shape, label, weight or position.
- **Neutral ground + one saturated signal** is the structure that survived every comparison; the hex is secondary. Avoid the default clusters listed in section 6 (cream + terracotta + serif; near-black + acid green; SaaS card kit).
- **Derive, do not pick from a menu**: sample (subject's own material: an engraving's blue ink, a manuscript's ochre; the user's reference image) -> converge (2-3 chromatics + a neutral ramp; hue >= 60 deg or lightness >= 0.3 apart) -> argue in one sentence why this palette belongs to this subject. Chroma bands as a mental target: grounds 0.01-0.04, brand/accent 0.08-0.15, small points 0.15-0.22.
- **Dark decks**: choose by luminance ratio against black (minorun): heading/lines 10-12, solid fill with white text 6-7, hero box 4.5-5.5, supplementary box 2.5-3, secondary box ~1.5 (invisible if used as a callout). A large fill reads brighter than thin text of the same colour: raise text/line colour 1-2 steps. Fix tone (lightness/saturation) before hue.
- **Chart palettes** (colourblind-safe): categorical `#4E79A7 #F28E2B #E15759 #76B7B2 #59A14F #EDC948`; sequential `#EFF3FF #BDD7E7 #6BAED6 #3182BD #08519C`; diverging `#B2182B #EF8A62 #FDDBC7 #F7F7F7 #D1E5F0 #67A9CF #2166AC`.
- **Backgrounds cannot be changed after generation**: put the ground colour in the brief. Decoration that cannot be deleted can be covered by an opaque `insert_fill` PNG whose background equals the slide colour.
- Cultural context: the same hue carries different meaning (ink-and-paper vs temple red/ochre vs SaaS blue). For philosophy/humanities prefer ink, paper and one restrained accent.

The deck built in this skill's session used: ink `#0F2740`, accent `#1B4F72` / mid `#4A90C2`, soft `#E3EDF5`, muted `#5A6978`, paper `#F7F8FA` (sampled from the thumbnail). Reuse as a reference, not a default.

## 3. Grid, spacing, density registers

**Page geometry on 1920x1080** (consistent across four scaling conventions in the sources):

| Zone | Value |
|---|---|
| Left / right margin | **130** (minimum safe zone 96 = 5% of width; use 154 if front-row cropping is possible) |
| Title | top **76**, left **130**, width **1660** (action title <= 2 lines) |
| Accent rule under title | **avoid** (see anti-slop); if the theme has one, it sits at top 176, width 90, height 8 and is deletable |
| Content block | from top **~290** to bottom **~980**, i.e. ~1660 x ~690-860 |
| Bottom reserve | >= 100 |

- **8-px spacing step**: every margin, gap and offset is a multiple of 8 (4 inside tiny details). Gaps by relationship: label + value 2-8; sibling cards 24-32; different topic groups 48-64; an isolated claim 64-96. Between-group gap >= 2x within-group gap.
- **Alignment is the cheapest quality signal**: every element aligns to the left margin, a column edge or another element. A deviation of more than ~6 px from siblings is a bug: `position_element` the outlier to the modal value (`scripts/deck_audit.py` finds them).
- **12-column grid** (96-130 margins, 24-32 gutters) for mental layout; spans 4/6/8/12 cover everything. Asymmetry by default (40:60, 35:65, 43:57); **50:50 only for a true A/B comparison** (thesis/antithesis, before/after).
- **Whitespace is a margin, not a hole**: the question is "is the empty space calm or lost?", not a percentage. Information slides ~25-40% empty, covers/quotes >= 60%. A sparse slide has a **bounded content island** (a content-sized cluster with fixed gaps) vertically balanced; never stretch content to the edges, never leave one quadrant empty while another is crammed.
- **Fix sparse pages by changing the layout or adding the missing example/diagram, not by padding** (lecture-slides: kill or merge thin pages; "add words" is not the answer).
- **Cards**: equal width and height, padding >= 24, gap >= 24, content aligned inside; same line count in sibling titles.
- **Edge safe zone**: nothing inside 96 px of any edge (title chrome excepted).
- **Rhythm** (deck level): no 3 consecutive slides of the same form; no 5 consecutive text slides; no 6 consecutive figure slides of one type; 4-6 archetypes per deck, >= 5 distinct per 10 slides; chrome (logo, art band, footer) only on cover and closing.

### Geometry sheet (measured on the deck built here; reuse to align clones)

| Archetype | Elements |
|---|---|
| Definition | lead sentence left 130 top ~380 width 1450 (46-52 px); support lines left 130, tops ~640 and ~712 (34-38 px) |
| Three-up | columns at left 130 / 685 / 1240, width 440-470, number badge top 320, title top 440, body top 520; hairline dividers at left 647 and 1202 |
| Cards (3) | cards left 130 / 685 / 1240, top 310, 490 x 470; inner padding 35; number top 350, title top 470, body top 640 |
| Rows (table) | row left 130 width 1660, heights 150-170, stacked from top 285-290 with 10-20 gap; label left 170-175, value left 630-745 |
| Chain (3 boxes) | boxes 430 x 190 at left 130 / 720 / 1310, top ~470; arrow labels between at top ~450 (two lines, 24-28 px); captions top ~700 (30-34 px) |
| Custom diagram | PNG 1600 x 760 at left 140, top 230 |
| Cover band | art 1700 x 494 at left 110, top 586 |

## 4. Slide archetypes (one job each) and their budgets

| Archetype | Words | Visual | Rule |
|---|---:|---|---|
| Cover | <= 12 | art band or one image | title + one credits line; no agenda text |
| Agenda | <= 25 | 4 numbered rows, grid | orientation for graders; never more than 5 rows |
| Definition / thesis | <= 40 | one sentence, huge | support lines add *why*, not synonyms |
| Three-up / cards | <= 40 | 3 equal columns | items are the same kind; numbers only for a real order |
| Comparison table | <= 45 | 2-3 columns x 3-6 rows | one highlighted row; no empty header cell; <= 6 rows |
| Chain / flow | <= 35 | 3-5 boxes + arrows | each arrow labelled with the transformation |
| Cycle / spiral / matrix / timeline | <= 20 | custom PNG | labels 1-3 words; the claim is the title |
| Example | <= 40 | chain + "why it fits" line | name, steps, link to the concept |
| Quote | <= 30 | one line + attribution | quotes only from real sources |
| Metric | <= 15 | one hero number + baseline | no three-equal-number slides |
| Summary / takeaways | <= 40 | 3 numbered rows | stays up during Q&A |
| Closing | <= 12 | art band | takeaway or ask; thanks line allowed; never a bare "Thank you" |
| Sources / backup | any | small | >= 24 px |

**One idea per slide.** A slide with two headline-worthy claims, two equal-weight charts or two accent moments is split.

## 5. Visual hierarchy tests (run on the thumbnail)

- **One focal point**: exactly one element is >= 1.5x the area of the next, or the only saturated element, or isolated by >= 48 px more whitespace. Place it in the top-left quadrant or the first ~30% of the height (F-pattern for text, Z for image-led).
- **One-second glance**: close eyes, open a random slide; the first thing you see must be the point.
- **Squint test** (blur the thumbnail): the hierarchy survives.
- **B&W test**: desaturated, the contrast still separates ground, text and accent.
- **Show/tell split**: the title tells the claim, the visual shows the structure; they must not repeat each other (thumbnail-design rule).
- **De-templating test**: "if a stranger can name the template, keep going." If three consecutive slides share the same grid and treatment, it is a template tell (design-independence check).

## 6. Anti-slop veto list (merged: frontend-design, huashu, vstorm, SlideSpeak, lesson-designer, design-director, anthropics pptx)

Fail the slide when you see any of these. Many are generator defaults you can delete (SHAPEs are enumerated) or forbid in the brief.

1. **Accent line / colour bar under titles** and decorative **edge stripes or single-side borders** on cards (the two loudest AI tells; the generator adds a title rule by default: the deck built here had one on every content slide - delete the SHAPEs at ~top 176, width 90, or forbid in the brief).
2. **Uppercase / tracked micro-labels** and mid-dot meta rows ("A · B · C"), "WORD - fragment" labels, "->" appended to links.
3. **Numbering 01/02/03 when the content is not a sequence** (parallel properties are not steps; use bullets or no marker).
4. **Centre-aligned body text**; centre-aligning everything.
5. **5+ bullets**, walls of text, a slide that could be a paragraph; 6x6 style slides.
6. **Gradients, drop shadows, 3D, glassy cards, blobs, Memphis confetti, corner swooshes, generic network meshes** used as filler. At most one elevation level per deck and only if the theme has it.
7. **Same soft-shadow rounded card repeated** with no relationship between cards ("SaaS card kit"); "three big numbers" with no relation.
8. **Cream/beige default ground + serif + terracotta** or **near-black + acid accent** chosen by default (acceptable only when derived from the subject and argued).
9. **Stock clichés**: handshakes, headsets, lightbulbs, magnifying glass, gears, smiling-at-camera, clip-art, emoji as icons. **Hard rule for this user: no emoji or pictographic symbol anywhere in the deck** - not in titles, points, labels, captions, diagram labels, alt text or notes; `plan_check.py` and `deck_audit.py` reject them.
10. **Decorative icons** on academic slides; **decorative images** that carry no information (the honesty test: remove the image; if nothing is lost it was decoration).
11. **Template chrome on every slide**: logo or footer repeated on interior slides (cover and closing only unless the institution requires it).
12. **"Questions?" / bare "Thank you" / "Let's dive in" / agenda as filler** openers and closers in a talk that is not required to have one.
13. **Reasoning traces or private words on slides**: "[NEEDS SOURCE]", "Fig3a_crop", "this slide should emphasise", internal IDs, agent self-commentary.
14. **Content slop**: filler openers/closers, empty adjectives ("significantly improved" with no number), fake precision (73%, 4.2x) without a source or `minh hoạ` label, three-point symmetry in every section, uniform heading grammar. Em-dash budget: <= 2 per 500 words, none in visible titles.
15. **Diagram sins**: sub-labels under box names, prose inside the figure, arrow through a box, floating labels, one arrow meaning two things, more than 4-5 nodes unsplit, decorative blobs behind nodes.
16. **Template smell**: three consecutive slides on one grid; every slide the same layout; every title the same grammar and length.

Restraint (huashu): spend boldness in one place; one detail at 120%, the rest at 80%; every decoration answers "if I remove it does the viewer lose information?"

## 7. Media

- **Media is the protagonist** (lecture-slides E1): on a slide with an image or diagram, the media takes >= ~60% of the slide area (>= 80% of body height when paired with a text column) and the text column shrinks to <= 1/3 of the width. If there is more text, delete words or add a slide; never widen the text column.
- **Never distort or crop**: placed image aspect = source aspect within 0.1%; contain-fit; cards in a row share height, widths differ. If a panel is unreadable at slide size, crop that panel deliberately and label it ("Fig. X, panel B").
- **Real figures only** in academic decks: crop, scale, align, annotate lightly; never regenerate a micrograph, spectrum, table or chart with a generator.
- **Text over images** needs a 40-70% scrim, or a solid panel with >= 24 px padding, or a text shadow; re-measure contrast at ~9 sample points, >= 4.5:1 everywhere. Captions go below or beside figures, not over them.
- **Photo vs illustration vs diagram**: photo for emotion, place, person, artefact; flat/geometric illustration for abstract concepts; diagram for relationships; icon only to reinforce a label. Never hand-draw a person or object in vector.
- **Image resolution**: >= 150 DPI at displayed size (>= 1920 px wide for full-bleed).
- **Alt text**: only writable on `insert_fill`; write what the picture *shows* and, for a diagram, the takeaway.
- **No duplicate images** across slides (cross-reference by slide number).
- Engraving / manuscript styles: keep the user's own art whole; one art band bookends the deck.

## 8. Diagrams and charts

### 8.1 Choose by the relation, not by the chart name

| Relation | Visual |
|---|---|
| identity / definition | a sentence, not a chart |
| sequence, transformation | chain with labelled arrows (<= 5 nodes) |
| cycle, negation of negation, spiral | `diagrams.py spiral|cycle`; one node marked "current" |
| 2-variable positioning | 2x2 matrix: uniform pale cells, identical chips, one highlighted quadrant, axis labels outside |
| hierarchy, levels | pyramid |
| overlap, inclusion | Venn (2-3 sets) |
| change over time | timeline (narrative phases) or one line chart |
| comparison of quantities | bars from zero |
| parts of a whole (<= 5) | 100% stacked bar or donut (60% cut-out); pie only <= 5 slices |
| one core number | metric: hero number + baseline + meaning |

Golden bans: no pie above 5, no 3-D, dual axis only for logically related units, <= 7 lines per chart (filter or cut), **bars start at zero**, no gradient fills on data, <= 4 horizontal gridlines at ~50% opacity, direct labels instead of legends, <= 5 series. Chart title states the conclusion (a verb or comparison). A number with no baseline is an incomplete slide. Sometimes the honest answer is "this is not a chart".

### 8.2 Construction numbers (visualise, minorun, Phlegonlabs)

- Nodes: <= 4-5 per diagram; more means overview + sub-flows or a build-up across 3-5 slides, one element at a time.
- Gaps between boxes >= 60 (scaled to slide px: 90-160 on a 1600-wide diagram); box padding >= 24; text-to-edge >= 14; arrowhead ~18 px with shaft >= 3x head; labels >= 10 px from arrows.
- Labels: box name inside; **no sub-labels**, no prose in the figure; every label belongs to a box or a leader line. Label size >= 28 px at final placement.
- Geometry preservation: the arrangement is the argument (triad, spiral, matrix). If labels do not fit, shorten them or split the figure; never compress until proportions mislead.
- Do not over-simplify: keep the figure's individuality (timelines, bar counts, branching, one hero number); delete fine text, not shape.
- One diagram per slide, figure-first (heading + one lead line) or text-first (figure illustration-sized); never both.
- Hierarchy by fill (solid hero, dark fill, outline, pale zone), not by border weight. Match figure surfaces to the slide ground.
- A circular flow is drawn as one circle, not separate curves. Draw out-of-scope parts pale.
- Render diagrams with `scripts/diagrams.py` at the final slide size (`06`).

## 9. Accessibility inside Canva (state the limits)

- Possible: contrast (computed), redundant encoding, large type, alt text on inserted fills, a clean PDF export.
- Not possible via this MCP: alt text on existing images, reading order, tags. Say so; do not imply compliance.
- Projector check: view the exported PDF at 25-50% zoom; all body text still readable; nothing relies on a pale grey.

## 10. Numbers cheat sheet (1920x1080)

title 52-60 | body 34-38 (floor 32) | support 30-34 (floor 28) | tag 26-28 (floor 24) | tier ratio >= 1.2 | <= 4 sizes/slide, <= 6/deck | leading 1.3-1.5 | measure <= 60 chars |
margins 130 (min 96) | title top 76 | content from 290 | 8-px step | related <= 24, unrelated >= 48 | contrast 4.5 (target 7) | accent 5-15% of pixels, 1 per slide | words/slide 25 / 40 / 75 |
bullets <= 3-4, <= 12 words | nodes <= 5 | 1 emphasis per slide | image aspect error <= 0.1% | rhythm: no 3 same, no 5 text in a row.
