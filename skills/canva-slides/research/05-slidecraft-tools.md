# 05 — Slide-craft tools: cross-ecosystem extraction

Scope: seven repos cloned (markdown/JSON only, sparse checkouts — `scripts/` are usually referenced but absent) under `/tmp/skills-src`. Every claim is cited as `<repo>/<path>:<line or heading>`. Licenses are recorded as facts; all are permissive except Phlegonlabs, which has no license file at all and is therefore unlicensed (all rights reserved by default).

Method: read every `SKILL.md`, every `references/*.md`, every `tokens.json`/`*.json` token file, every layout/block/chart catalogue, every QA playbook, and the design specs. Where a skill is a thin wrapper (a routing table plus links), it is called out in one line and not padded.

---

## Inventory

| Skill / repo | Repo path | License (as found) | What it is, in one sentence | Verdict |
|---|---|---|---|---|
| **huashu-design** (花叔 Design, v3.2.0) | `alchaincyf_huashu-design/` | **MIT** — `LICENSE` ("MIT License, Copyright (c) 2026 alchaincyf"); `package.json:license: "MIT"` | An HTML-first "design studio" skill: art-director persona, mandatory three-direction gate, form-five-questions, colour-derivation protocol, Chinese typography, and HTML→PDF/PPTX delivery chain. | **A** — the deepest taste system in the cluster; process and anti-slop taxonomy are directly transferable. |
| **slide-design-skill** (SlideSpeak) | `SlideSpeak_slide-design-skill/` | **MIT** — `LICENSE` ("Copyright (c) 2026 SlideSpeak") | A deterministic deck *engine*: per-brief token package + slot templates + layout-capacity contracts + code-enforced quality gates (14px floor, no uppercase, occupancy, richness), with declared design-spec docs and a measured McKinsey page anatomy. | **A** — the best engineering model and the only source with measured density targets and a "bounded content island" rule. |
| **ppt-agent-skills** (PPT Agent v4.1) | `sunbigfly_ppt-agent-skills/` | **MIT** — `LICENSE` ("Copyright (c) 2025 sunbigfly") | A 5-stage multi-agent Chinese HTML-deck pipeline (interview → research → outline → style → per-page HTML) with 10 layout families, 14 blocks, 18 chart recipes, and a rigorous P0/P1/P2 render-review loop. | **A for the QA loop and numeric ladder, C for prose** — heavy rhetorical padding, but the P0/P1/P2 protocol and the field-level cheatsheet are gold. |
| **content-skills** (vstorm) | `vstorm-co_content-skills/` | **MIT** — `LICENSE` ("Copyright (c) 2026 Vstorm") | A content-marketing suite; the relevant parts are `content-presentation`, `content-infographic`, `content-audit/slop-detector`, `content-audit/scoring`, `content-image/style-library`, and the brand token JSON. | **B+** — not slide-native, but the AI-slop detector, scoring maths, chart rules and colourblind palette are the most systematic in the cluster. |
| **Powerpoint-fancy-design** | `Phlegonlabs_Powerpoint-fancy-design/` | **NO-LICENSE** — no `LICENSE`/`COPYING` in the git tree (`git ls-tree`), no license field in `package.json` | 1600×900 HTML slides in 10 named visual styles, with a hard 8-role type scale, a pixel safe-zone spec, a 12-prototype layout library and a weighted quality rubric. | **A for the safe zone, type scale and rubric; flag license** — treat as idea-only for reuse, but the numbers are the most explicit of any source. |
| **present-now** | `Taimoorkhan1122_present-now/` | **MIT** — `LICENSE` ("Copyright (c) 2026 taimoorkhan112") | A single-file, clicker-safe interactive HTML deck (1600×900) built by interviewing, scaffolding from a template, dispatching 3–5 slide-writing subagents, then QA-ing every slide in a real browser. | **B+** — thin on visual theory, excellent on authoring contract, timeboxing and overflow QA. |
| **anthropics/skills** — `pptx` | `anthropics_skills/skills/pptx/` | **Apache-2.0** — `LICENSE.txt`; repo README says "Many skills in this repo are open source (Apache 2.0)" | Production PPTX creation/editing reference: pptxgenjs footguns, template surgery rules, palette table, type sizes in pt, and a mandatory render-and-rain-eye QA pass. | **A** — the single best source of "never do this in slides" rules (accent stripes, title underlines, beige defaults) plus real OOXML failure modes. |
| **anthropics/skills** — `canvas-design` | `anthropics_skills/skills/canvas-design/` | **Apache-2.0** — `LICENSE.txt` | Generates a written "design philosophy/manifesto" first, then expresses it as a poster-like PNG/PDF; Bundled 27 OFL fonts in `canvas-fonts/`. | **B** — not a deck skill; valuable for the manifesto-first method, minimal-text stance and the "refine, don't add" final pass. |
| **anthropics/skills** — `theme-factory` | `anthropics_skills/skills/theme-factory/` | **Apache-2.0** — `LICENSE.txt` | A menu of 10 pre-made colour+font themes with a showcase PDF and a pick-then-apply flow. | **C** — a theme menu is precisely the anti-pattern this project must avoid (Huashu and SlideSpeak both ban style menus explicitly). Keep only the theme-file schema. |
| **anthropics/skills** — `brand-guidelines` | `anthropics_skills/skills/brand-guidelines/` | **Apache-2.0** — `LICENSE.txt` | Hard-codes Anthropic's own palette (`#141413`, `#faf9f5`, `#d97757`…) and Poppins/Lora with fallbacks. | **C** — thin wrapper around one brand's hex codes; useful only as an example of a brand token payload. Note the irony: Huashu and `frontend-design` both name this exact palette as the #1 AI tell. |
| **anthropics/skills** — `frontend-design` | `anthropics_skills/skills/frontend-design/` | **Apache-2.0** — `LICENSE.txt` | The canonical statement of the 2026 "AI-generated look" clusters and typographic tells, plus a plan → review-against-brief → build → critique process. | **A** — every anti-slop rule in this cluster either quotes it or reinvents it. |
| **anthropics/skills** — `doc-coauthoring` | `anthropics_skills/skills/doc-coauthoring/` | **No per-skill LICENSE** in the tree; repo README states "many skills in this repo are open source (Apache 2.0)" — treat as Apache-2.0 with that caveat | Three-stage co-authoring workflow for documents: context gathering → refinement/structure (clarify, brainstorm, curate, gap-check, draft) → reader testing with a fresh agent. | **B** — not slide-specific; the "reader testing" stage is a transferable QA idea (predict the audience's questions, then have a cold reader answer them). |

---

## Skill: huashu-design

**Purpose.** Force the agent to behave as a design studio rather than an HTML typist: establish a point of view from the subject's own material, present alternatives, then execute one system consistently. `SKILL.md` §"你是谁" states the bar explicitly — the output should not be recognisable as AI work.

### Prescribed process

1. **Run three cheap diagnostics before anything** (`SKILL.md` §开工三件事): pull the user's recorded taste preferences, read the "appearance ledger" of recent deliverables so this project does not repeat their look, and probe available capability tiers.
2. **Fact-check the subject first** (`SKILL.md` §0 · 事实验证先于假设): anything about a real product/version/event gets a web search and a `product-facts.md` before questions are asked. The recorded failure: asserting a product was unreleased when it had shipped four days earlier, costing two hours.
3. **Start from existing context** (`references/design-context.md` §"什么是 Design Context"): user's design system → their codebase (lift exact hex/px) → live product screenshots → brand assets → competitor references → a named public design system as fallback. Never render high-fidelity from memory.
4. **Brand-asset protocol** (`SKILL.md` §2): five steps (ask → search official channels → download → verify → freeze into `brand-spec.md`), triggered both when designing *for* a brand and when any recognisable product appears in the design.
5. **Three-direction gate** (`references/directions.md` §Phase 4): three logics — best-designer-in-the-world, real same-medium reference, and a "second-hand roulette" pick from the style library — each producing **two** candidates. Six direction cards, six thumbnails at ~480×300, pick the strongest three that are genuinely different, build three full versions, present and **stop**.
6. **Materials before layout** (`references/materials.md` §原则): every direction names its hero material; content-critical images are gathered first; a page about an animal without the animal's image is a failure.
7. **Answer the five form questions per page** (`references/workflow.md` §3): narrative role (hero/transition/data/quote/close), viewing distance (10 cm phone / 1 m laptop / 10 m projector), visual temperature, capacity estimate (three 5-second sketches), and visual motif ("what could only come from this subject?").
8. **Lock grammar on two pages before batching** (`references/modules/deck.md` §做的顺序): for decks ≥5 pages, build the two most structurally different pages (e.g. cover + data), get sign-off, then fill the rest.
9. **Lint and verify**, then deliver HTML → PDF always, PPTX on request (`references/modules/deck.md` §交付链).

### Rules, thresholds, checklists (with sources)

- **Readability floors** — deck body ≥24px (ideal 28–36), labels/annotations/chart ticks ≥16px, titles 60–120px, section titles 80–160px, hero 180–240px, on a 1920×1080 canvas (`references/content-guidelines.md:181-185`; repeated as a hard rule in `references/modules/deck.md:33`).
- **Web**: body ≥14px, labels ≥12px; mobile body 16px; hit targets ≥44×44px (`references/content-guidelines.md` §Scale 规范).
- **Print**: body ≥10pt (≈13.3px), ideal 11–12pt; headlines 18–36pt; captions 8–9pt (`references/content-guidelines.md` §Scale 规范).
- **Long-image (1080 wide, viewed on phone)**: body ≥36px, labels ≥28px on the canvas, because a 1080-wide image lands at ~390pt on a phone (~2.8× downscale) (`references/modules/infographic.md` §体检).
- **Contrast**: body ≥4.5:1, large text ≥3:1 (`references/content-guidelines.md` §对比度).
- **Modular type scale**: ratios 1.2 (dense dashboards) / 1.25 (default web) / 1.333 (editorial) / 1.5 (posters, slides); body 16–18px (CJK 17–18); **more than 5 steps is out of control**; display sizes 3×–8× escape the scale because they are layout elements, not text levels (`references/typography.md` §1).
- **Measure and leading**: Latin 45–75 characters per line, best 66 (`max-width: 65ch`); Chinese 22–38 characters, best 28–32 (`max-width: 36em`). Leading by line length — display 0.95–1.1 (Latin) / 1.1–1.25 (CJK); headings 1.1–1.3 / 1.3–1.4; short body 1.4–1.5 / 1.6–1.7; long body 1.6 / 1.8–2.0; CJK runs ~+0.2 above Latin everywhere (`references/typography.md` §2).
- **Letter-spacing**: CJK body 0 to 0.05em, CJK headings 0, CJK display −0.02 to 0; only **all-caps Latin micro-labels** take 0.08–0.15em (`references/typography.md` §4.5).
- **CJK typographic law** (`references/typography.md` §4.2–4.4): Latin font must come **first** in the `font-family` chain so Han characters fall through; no synthetic italic (`font-synthesis: none`) because browsers shear Han glyphs; replace italic emphasis with weight, highlighter background, a kai (楷) face, or emphasis dots; `line-break: strict` for kinsoku; corner brackets 「」 for quotes.
- **Hierarchy arithmetic**: title must be ≥2.5× body, and the prescribed fix when it is not is **3×** ("body 16px → title 48–64px") (`references/critique-guide.md:55`, `:136`).
- **Spacing system**: 8pt grid, spacing only from 8/16/24/32/48/64px (`references/critique-guide.md:146`).
- **Whitespace**: ≥40% of total area, ≥60% for minimalist directions (`references/critique-guide.md:151`).
- **Colour budget**: at most 1 primary + 1 secondary + 1 accent + greys (`references/critique-guide.md` §3).
- **Craft budget**: at most 2 font families; 3–4 clear hierarchy levels; a single "boldness" element (`references/critique-guide.md` §2, §3).
- **Colour derivation protocol** (`references/design-styles.md:23-62`): (1) sample from brand assets, real photography of the subject, or cultural context; (2) converge to **2–3 chromatic colours + one neutral ramp** written as lightness steps (L 0.15/0.35/0.65/0.92/0.98), separating chromatics by **H ≥60° or L ≥0.3**; (3) argue the palette in one sentence. Chroma bands: large grounds 0.01–0.04, brand/accent 0.08–0.15, small accents 0.15–0.22, >0.25 only for deliberately "born-digital" looks.
- **Deck composition**: at most **4–5 layouts** per deck (`references/slide-decks.md` §2); rotate the *visual protagonist* type page by page across 10 listed kinds (typographic cover, single portrait, group shot, timeline cards, node graph, before/after, UI screenshot in a device frame, half-page pull quote, testimonial grid, closing CTA) (`references/slide-decks.md` §视觉主角必须差异化).
- **Per-page content budget**: one core message + 3–4 supports + one visual protagonist; anything more gets its own page (`references/slide-decks.md` §4).
- **Speaker notes**: 200–400 characters, conversational, one array entry per slide, mark stress and pauses (`references/slide-decks.md` §Speaker Notes).
- **Numbering**: slide numbers are 1-based in labels; humans never say "slide 0" (`references/slide-decks.md` §Slide Labels).
- **Pages must not carry their own page numbers** — chrome owns them, or you get two competing counters (recorded bug: "02/03" over "6/16") (`references/modules/deck.md` §硬规则).

### Unique ideas

- **Gate files as physical checkpoints** (`SKILL.md` §6): `brand-spec.md`, `direction-approved.md` (which must quote the user's own words), `导演稿.md`. "No file = the step did not happen"; a hook can hard-block rendering. This converts soft process into auditable state.
- **"Add options, don't add bans"** (`references/directions.md` §为什么这样做): after banning AI-default look families, all three directions retreated into pale minimalism and the user called it boring. The fix was to police *convergence* (three versions in one family, or repeating the last project) instead of banning families.
- **Appearance ledger**: an external record of what recent deliverables looked like, consulted before generating, so variety is enforced across projects rather than within one.
- **Two-way slop taxonomy**: "appearance families" (warm cream + serif, near-black + one acid accent, broadsheet rules, SaaS card kit) are legitimate choices and only a problem when converged; "template decoration" (all-caps eyebrow above every heading, mid-dot meta strings, "WORD — fragment" labels, monospace micro-data, trailing arrows, one coloured word in a headline) is cheap to delete and should go (`references/content-guidelines.md` §2026 年的 AI 默认外观).
- **Data pages must answer a relational question first** — proportion, change, composition, comparison, scale — instead of defaulting to "three big numbers plus a bar chart" (`references/modules/deck.md` §数据页别默认成…).
- **Capability tiers for imagery** (T0 real images/procedural texture/data-as-image/physical-object mimicry/type-as-image; T1 AI generation; T2 sibling skills), with graceful degradation that never blocks (`references/materials.md` §三档).
- **Honest-image test**: remove the image — if no information is lost, it was decoration (`references/materials.md` §原则 3).
- **Two PPTX routes chosen by the state of the HTML**, never mixed: constraint-compliant HTML from line one, or a rendered-coordinate extractor that preserves a finished visual (`references/modules/deck.md` §交付链).

### Pitfalls it warns about

- Emoji do not render in headless Chromium PDF/screenshot (empty boxes) — use text symbols (`references/slide-decks.md` §1).
- Screenshotting before webfonts paint yields system fallbacks; wait ≥3500 ms or self-host (`references/slide-decks.md` §3).
- Single-file `<deck-stage>` decks: page-level `display` rules override the shadow-DOM hide rule and **all slides render stacked**; counter still says "1/10" (`references/slide-decks.md` §CSS 陷阱).
- 13 pages in a single-file architecture silently lost the overview wall; multi-file is the default for long decks (`references/modules/deck.md` §架构).
- Density overload: a 2×2 grid plus three bottom creeds (7 blocks) was cramped and repetitive; 1×3 restored breathing room (`references/slide-decks.md` §4).
- **Rendering-tool trust ladder** (`references/verification.md` §第 0 条): `qlmanage -t` thumbnails passed four text-overlap bugs that real PowerPoint/WPS showed instantly; LibreOffice drops CJK glyphs on macOS; Keynote-via-AppleScript PDF is trustworthy; the target app is final. Always run a control file through the same renderer to separate tool defects from product defects.
- **Mechanical text diff**: compare source strings to product strings after `re.sub(r'\s+','')` and compare element counts per page — renderers fool the eye, counts do not (`references/verification.md` §第 0 条).

### Outdated / wrong / impossible against our MCP

- Everything built on CSS has no Canva equivalent: `clamp()`, `text-wrap: balance/pretty`, `hanging-punctuation`, `text-spacing-trim`, `font-feature-settings`, `font-size-adjust`, `writing-mode: vertical-rl`, `oklch()`, `color-mix()`, `mask-image`, `clip-path`, backdrop filters. `format_text` exposes only size/weight/style/align/colour/line-height/list-level/list-marker — **no font family, no letter-spacing, no text-transform**.
- The whole HTML architecture layer (multi-file iframes, `<deck-stage>` web component, overview wall, localStorage playback position, keyboard controls) is irrelevant: Canva is the renderer and the player.
- The four `html2pptx` constraints (960×540pt body, all text in `<p>`/`<h*>`, no backgrounds on text tags, no CSS gradients, no web components, no complex SVG) are moot for us, but they are a useful warning that *any* HTML→office conversion loses design.
- `design_lint.py`, `learn.py`, `capabilities.py`, `ref_board.py`, `export_deck_*.mjs`, `verify.py` are referenced but absent from this sparse clone; treat them as described behaviour, not available tooling.
- The advice to "wait 3500ms for fonts" has no analogue — but the underlying lesson (webfonts are a silent failure mode) transfers to Canva's font substitution when a design's font is unavailable.
- Speaker-notes authoring is impossible: `get-presenter-notes` is read-only and there is no write op.

---

## Skill: slide-design-skill (SlideSpeak)

**Purpose.** Separate *style authoring* from *deck filling*: a style package (tokens, chrome, layout grammar, templates) is generated or authored once and frozen; the model only supplies slot text, so two runs of the same brief are visually indistinguishable (`docs/SKILL-FORMAT.md` opening).

### Prescribed process

1. **Capture the brief** including a look signal in any form (free text, "like stripe.com", a brand URL, a moodboard). If there is *zero* style signal, ask exactly one short question (`SKILL.md` §How to use; `CLAUDE.md` §What to actually do).
2. **Derive a bespoke style** silently — tokens, chrome, slide types, layout grammar, image direction. Never surface the machinery or claim a preset (`CLAUDE.md` §NEVER surface internal machinery).
3. **Plan the deck** before generating: `presentationType` (pitch/report/teaching/editorial/keynote/general), `audience`, `register` (punchy/formal/technical/warm/plain), `assetAppetite` (image-led/data-led/balanced), plus a **per-slide density rhythm** whose endpoints are always `editorial` (`docs/specs/2026-06-09-anti-slop-adoption.md` §4).
4. **Fill slot templates** — the model writes text only; the engine draws charts, tables, icons, scrims (`docs/SKILL-FORMAT.md` §components.html).
5. **Validate → render → measure**: style validation, slide-tree validation, content lint, occupancy, richness (`README.md` §Quality gates). "A deck with occupancy flags is not done" (`docs/INTEGRATION.md:156-159`).
6. **Look at every slide** — gates catch geometry, not taste (`meta-generator/GENERATOR.md` §Step 8).

### Rules, thresholds, checklists (with sources)

- **Page is always 1920×1080**; safe area typically **80–128px**, commonly 96 (`meta-generator/GENERATOR.md:61`; `docs/SKILL-FORMAT.md` §tokens.json; every `skills/*/tokens.json` has `"page": {..., "safe": 96}` except training 112, pitch and product-marketing 128, neue-klasse 88, opex 80).
- **Hard type floor: 14px anywhere; body and descriptions run 16–21px** (`docs/SKILL-FORMAT.md:112`). Thin content is set at **17–21px** and centred, never stretched (`docs/SKILL-FORMAT.md:81`).
- **Per-style type scales** (`skills/*/tokens.json`): consulting header 64/44/32/24, body 18/16/14/12; academic 56/42/30/22 and 22/20/18/14; kanagi 76/46/32/24 and 19/17/16/14; neue-klasse 96/54/38/26 and 20/17/15/13; opex 86/42/29/21 and 19/16/14/12.5; pitch 96/72/48/32 and 22/18/16/14; product-marketing 128/80/56/32 and 24/20/18/14; training 72/56/40/28 and 26/22/18/16.
- **Spacing**: unit 4 with scale [4, 8, 12, 16, 24, 32, 48, 64, 96] for editorial/consulting styles; unit 8 with [8, 16, 24, 32, 48, 64, 96, 128, 192] for pitch/product/training.
- **Radius and elevation are style signals**: 0 (academic, kanagi) → 2px (consulting) → 12–16px (pitch, product). Elevation ranges from `none` to `0 16px 64px rgba(0,0,0,0.08)`. Decoration is not a default.
- **Banned, machine-enforced** (`docs/SKILL-FORMAT.md:111-116`): `text-transform: uppercase` and tracked-out caps labels; any CSS font-size <14px; accent-coloured border pinned to a card edge; em-dashes in rendered copy; invented logos or fake product UI; fewer than **three drawn graphic constructs** per package; and as filler — blobs, squiggles, Memphis confetti, corner swooshes, generic network meshes.
- **Bounded Intrinsic Content Island** (`docs/specs/2026-06-04-layout-fit-model.md` §Schicht 2): the main area is a fixed safe-area box; the content island grows to its own height with a declared `max-height`; children may not swallow leftover space via `flex:1`, `space-evenly`, `space-between` or `height:100%`. "Whitespace is a margin around a content-sized cluster, never a gap stretched between rows to fill height."
- **Density is a layout register, never a font knob** (`docs/specs/2026-06-04-layout-fit-model.md` §Prinzipien 4; `docs/specs/2026-06-03-design-variance-brief.md` §M2): `editorial` / `balanced` / `data-dense` change column count, grouping, gap size and element count; type size stays fixed. Three tiers only.
- **Overflow policy** (`docs/specs/2026-06-04-layout-fit-model.md` §5.1): regenerate inside the budget → auto-paginate per the family's continuation policy → flag. Never shrink type.
- **Composition rules per style** (`skills/consulting/layout-grammar.md` §Composition Rules): first slide is cover, last is closing; second slide is an executive summary when the deck has >3 slides; `data-callout` max 2 consecutive; decks >8 slides must contain at least one structural slide (2×2, process flow, comparison table); `section-divider` appears only in decks >12, separating runs of 4–6 content slides.
- **Academic rules** (`skills/academic/layout-grammar.md` §Composition Rules): every result figure/table needs a `source` slot; conference talks (≤12 slides) skip prior work and merge discussion+conclusion; thesis defences (≥25 slides) duplicate prior-work and result-figure types; result slides may use the signal colour only on the highlighted finding.
- **Deck-planning contract** (`docs/specs/2026-06-09-anti-slop-adoption.md` §2): ban filler phrases (elevate, seamless, unlock, leverage, next-gen, revolutionize, game-changing, cutting-edge, world-class, synergy); placeholder names (John/Jane Doe, Acme, Lorem ipsum); generic step labels (Stage N / Phase 0N / Step N); **fake-precise numbers** (`73%`, `4.2x`, `$12.4M`, `10,000+`) unless present in the user's prompt or marked illustrative; eyebrow-overuse when a kicker appears on **more than ⌈slides/3⌉** slides; density monotony when decks >6 slides all share one tier.
- **McKinsey page anatomy** (`docs/specs/2026-06-11-mckinsey-anatomy.md` §1–§3): kicker naming the current section (sentence case, grey, no counter dressing); an **action title that is a full sentence with a verb, max 2 lines**, and all titles read in sequence must reproduce the storyline without any exhibit; every content page carries a SOURCE line with assumptions in a "Note:" above it; numbered footnotes with superscript markers; exhibits are **boxed** with a header band plus a unit line ("$ billions"); default content page is two-panel, exhibit 60–65% plus a boxed drivers panel; annotation callouts with leader lines; values on the data (above bars, inside stacked segments, at line ends); no gridline forests; legends as compact swatch rows; closing pages state requirements, not "thank you".
- **Measured density targets** (`docs/specs/2026-06-11-mckinsey-anatomy.md` §Counted reference density spec) — counted with `pdftotext`, not estimated:

  | metric | median content page | standard exhibit | dense exhibit (1–3 per deck) |
  |---|---|---|---|
  | tokens | ~100 | 80–160 | 150–195 |
  | text lines | ~35 | 30–60 | 60–90 |
  | numerals | ~20 | 15–45 | 70–112 |

  Hard floors: data slides ≥80 tokens and ≥20 numerals; deck median across content pages ≥90 tokens. Structural sources of that density: **6–18 y-axis tick labels per chart**, x labels on every period (14 labels, no thinning below ~16), a value on every bar (10–14), multi-panel pages (3 exhibits side by side or 2 stacked), in-chart series labels with CAGR notes, dashed reference line with a right-edge marker value, an actual/forecast divider with zone labels, annotation callouts, an embedded mini-table beside the chart, and a matrix with a value in every cell plus badge summary rows (49 cells + 14 badges).
- **Rubric** (`skills/consulting/SKILL.md` §Density, §Visual System): one main claim per content slide supported by 3–5 evidence bullets; "no slide is half-empty"; the signal colour may be used only for callout strips, the title-slide bar, and the underline beneath section numbers; rules are 1px `#D4D0CB`; big numbers 96–128px serif at weight 600; **no icons** — use a number or a rule.

### Unique ideas

- **Layout contracts with capacity in the grammar** (`docs/specs/2026-06-04-layout-fit-model.md` §Schicht 1): each slot declares `kind` (line/prose/items/stat/table/chart/media) and `{min, ideal, max}` in its natural unit, plus headline char maxima (~90 chars) and an overflow policy. Validation and prompting read the same source.
- **Richness gate measured on the DOM** (`docs/SKILL-FORMAT.md` §components.html): every directive stamps `data-visual-event`, each slide root carries `data-family`, and floors are per family — typographic families pass on one event (oversized display type counts), data families need more. It measures event density, never colour saturation, so an austere monochrome deck still passes.
- **Moodboard intake on rotated colour axes** (`CLAUDE.md` §Moodboard step): generate two boards deliberately rotated onto different unexpected colour axes, let the user pick, then extract palette/material/lighting. The recorded failure: hand-written moodboard prompts return the genre cliché every time ("premium chocolate" → beige + espresso).
- **Image-subject monotony lint**: if every slide's background prompt redraws one motif, a lint rule flags it (`CLAUDE.md` §Moodboard step).
- **Two references per direction must diverge in structure**, not skin: spine family + slide-type set + a signature structural move (`CLAUDE.md` §Rendered decks…).
- **Versioned iteration convention**: every full pass is a new `Vn/` folder, patches are `V3.1`; never overwrite (`CLAUDE.md`).
- **"A harness is necessary but not sufficient"**: the fit harness passed 16/16 while visual review still found floating sparse slides and wrong fixture separators (`docs/specs/2026-06-03-design-variance-brief.md` §M2 REDO).

### Pitfalls it warns about

- Underflow is as bad as overflow: distributing 3–5 lines across ~700px produced slides that "float in white space and look lost" (`docs/specs/2026-06-04-layout-fit-model.md` §1).
- Font shrinking to fit creates text walls — explicitly rejected after a failed iteration (`docs/specs/2026-06-03-design-variance-brief.md` §M2).
- A reference defines "good" only for its own presentation type; McKinsey density is wrong for an editorial deck (`docs/specs/…variance-brief.md` §M2 corrected core model).
- **Budget drift**: declared capacities drift from real CSS as templates evolve, so prompts, validator and renderer disagree; keep budgets in the same grammar, derive prompt excerpts from one source, keep min/typical/max fixtures, and feed measured capacity back into the grammar (`docs/specs/2026-06-04-layout-fit-model.md` §9).
- Template slots ≠ source items: if the template shows 4 team members and you have 3, delete the whole group including its image, then check for orphaned visuals (`anthropics_skills/skills/pptx/SKILL.md` §"Template slots ≠ source items" — same class of bug).

### Outdated / wrong / impossible against our MCP

- The engine assumes it can author HTML/CSS and SVG; Canva's `perform-editing-operations` can only restyle *existing* elements. There is no `text-transform`, no letter-spacing, no clamp, no `@container`, no `text-wrap`, no per-element CSS.
- **Layout re-selection is impossible**: we cannot swap a template or choose a "higher-capacity variant" — `merge-designs` can insert/remove/move whole pages, and `create-design` can regenerate, but there is no within-page re-layout.
- The occupancy/richness gates read the DOM. Canva has no DOM; the only measurement channel is a **per-page thumbnail inside an editing transaction**. Any gate must become a visual-review checklist.
- Charts are engine-drawn. Canva has **no chart creation op** — charts must come from the generated design or be uploaded as images (`create-upload-url`), which makes every chart rule a *pre-generation* instruction or an image-authoring step.
- 14px floor and 1920×1080 are compatible with our canvas; the rest of the token layer is not addressable.
- `search-brand-templates` and `list-brand-kits` both return empty on our account, so the brand-package path has no data to work with.

---

## Skill: ppt-agent-skills (PPT Agent v4.1)

**Purpose.** A staged, multi-agent production line for Chinese HTML decks: interview → research/source compression → outline → global style lock → per-page planning+HTML+review → export. It is as much a workflow discipline as a design skill.

### Prescribed process

1. **P0 interview** — one structured round, answers normalised into `requirements-interview.txt`; manual-audit checkpoints declared up front (`SKILL.md` §4 P0).
2. **P1 branch** — research (web) vs local-source compression, chosen by the user, never both.
3. **P2 research synthesis** — a research subagent produces `search.txt` + `search-brief.txt`.
4. **P3 outline** — with an explicit density contract: `density_bias`, `density_curve`, per-page density window (`SKILL.md` §6.1 P3).
5. **P3.5 style lock** — a `style.json` with `mood_keywords`, `design_soul`, `variation_strategy`, `decoration_dna` (`references/styles/runtime-style-rules.md` §2).
6. **P4 per-page pipeline** — planning (JSON) → HTML → review → PNG; one page per agent, pages run in parallel; each page passes `planning_validator` + `visual_qa.py` (`SKILL.md` §4 P4.NN).
7. **P5 export** — preview, PNG-based and SVG-based PPTX, delivery manifest.

### Rules, thresholds, checklists (with sources)

- **Canvas** (`references/design-runtime/design-specs.md` §A): fixed 1280×720, overflow hidden; title zone at 40px left, y 20–70, max height 50px; content padding 40px starting at y=80, usable **1200×580**; footer inside the bottom 40px, height 20px.
- **Type ladder** (`references/design-runtime/design-specs.md` §A): H0 cover 48–160px/900 (push for ≥80), H1 26–32/700, H2 16–20/700, body 13–14/400 with line-height 1.8, caption 9–12 at 0.4–0.6 opacity, overline 10–12 with 2–4px tracking, Data-Hero 64–120/900 at 0.85–1.0 leading, Data-Sub 28–40/800. **Per-page max/min size ratio should be ≥5×** (`design-specs.md:112`).
- **Spacing as emotion** (`design-specs.md` §A): number+annotation 2–4px; sibling cards 16–20px; different topic areas 32–48px; isolated core claim 48–80px padding.
- **Fill-rate targets by page type** (`design-specs.md` §A 留白与视觉焦点): cover 40–55%, section 25–40%, standard content 60–75%, data-dense 70–80%, closing 35–50%.
- **Colour rhythm**: 60/30/10 ground/surface/accent; **at most 2 accents per page**; 2–3 decorative devices per page (`design-specs.md` §C).
- **Depth**: five layers (background, texture 0.03–0.08 opacity, content, elevated, focal), **at least 3 active per page** (`design-specs.md` §A 五层景深架构).
- **Composition anchors**: rule-of-thirds intersections at (427,240), (853,240), (427,480), (853,480) on the 1280×720 canvas; dead centre is the most boring position (`design-specs.md` §A 构图锚点).
- **Card styles** (`references/blocks/card-styles.md`): ≥2 styles per page; `accent` and `elevated` **max 1 each per page**; `transparent` for quotes/timelines/diagrams that already carry their own skeleton.
- **Decoration density tiers** (`references/design-runtime/data-type-decoration-mapping.md` §装饰密度分级): minimal 0–1 T + 0–1 W; low 1–2 + 1–2; medium 2–3 + 2–3; generous 2–3 T + up to 4 W. Multi-type pages: union and de-dupe, **T ≤3 and W ≤3**, take the *lowest* density among the types (`§多数据类型组合规则`).
- **Layout library** (`references/layouts/README.md`): 10 gravity-field families (single focus, symmetric, asymmetric 6:4, three-column, primary-secondary, hero-top, mixed grid, L-shape, T-shape, waterfall); use 4–6 per deck; three consecutive pages with the same layout is a warning sign.
- **Chart minimum content contract** (`references/charts/runtime-chart-rules.md` §4): a metric page must state value + meaning + baseline/trend; a comparison page must state the objects + dimension + direction (+ a management read); a trend page needs axis + direction + turning point; a progress page needs current + target + remainder.
- **Chart failure modes** (`runtime-chart-rules.md` §6): corner-chart (a "data page" whose chart is a small corner ornament), single-KPI island (one big number with no baseline/trend/explanation), chart with no takeaway, support chart degenerating into decoration, and material/decoration taking over the reading path.
- **QA protocol** (`references/playbooks/step4/page-review-playbook.md`): three scan passes (border patrol → content-depth scan → whole-page impression); severity P0/P1/P2; **minimum 2 rounds, first round may never FINALIZE**; archive every round's screenshots to `REVIEW_DIR/roundX/`; from round 2 read only the newest screenshot and tick off the previous report item by item; if the same P0/P1 survives two rounds, **roll back to planning** and change at least one of density label/contract/layout hint/card allocation rather than nudging 5px.
- **P0 list** (page-review-playbook §Part B): content clipped by canvas; `transform: scale()` hacks; >40% of the canvas empty; unreadable core text (<2:1 contrast or <10px); a planning card missing from the HTML; severe overlap/stacking; pixel-level clipping from missing `border-box` or too-tight line-height; broken or distorted images (missing `object-fit: cover`).
- **P1 list**: truncated text, uneven gaps (standardise `gap: 16–24px`), decoration above text in z-order, no focal point, hard-coded hex values, data numbers the same size as body (fix: +8–12px and weight 700), line-height <1.4 (fix: 1.6–1.8 body, 1.2–1.3 headings), and **design-independence failure** — three consecutive pages with the same grid/card count/style (a template tell).
- **P2 polish**: inconsistent radii, missing signature move, font fallback to Times/Songti, flat cards, title/body gap <4px (fix ≥6px), "webpage feel" instead of "deck feel".

### Unique ideas

- **The severity ladder with hard gate semantics** — P0 is a no-go even if everything else is beautiful, and the protocol explicitly forbids "I changed the CSS so it should be fine" as evidence.
- **Round-scoped screenshot archive** so the reviewer can prove a fix landed in pixels rather than in reasoning.
- **Rollback-to-planning tripwire**: two failed rounds on the same defect class means the skeleton is wrong, not the spacing.
- **Style as a field contract** (`style.json`) with a `design_soul` that must describe the *system's judgement criteria*, not a page composition, and a `variation_strategy` that must name both what may vary and what may not.
- **Decor density as a tier tied to data type**, with an explicit union/de-dupe algorithm and a "take the lowest tier" rule.
- **A `resource_rationale` obligation**: if a page departs from the mapping table, the planner must write the spatial reasoning down, which makes deviation auditable rather than accidental.

### Pitfalls it warns about

- The orchestration itself is a failure surface: the skill spends enormous prose on "main agent may not write artifacts", subagent isolation, model/effort pinning, RUN/STATUS/FINALIZE protocol. That is agent-harness plumbing, not slide craft — most of it should not be copied.
- Rhetorical inflation is a real cost: the same rule is stated three times in three registers, and directives such as "you are a tyrant of the visual canvas" add no executable information.
- `gradient text`, `text-transform: uppercase` with `letter-spacing: 2px` overlines, and `border-left: 4px accent` (P1-4) are all recommended here and all banned by stronger sources — see Contradictions.

### Outdated / wrong / impossible against our MCP

- 1280×720 is not our canvas; every px value needs ×1.5 to land on 1920×1080 (see the normalisation table in the catalogue).
- The whole per-page HTML/CSS remediation guide (clip-path, mask-image, backdrop-filter, `-webkit-line-clamp`, `display:none !important`) has no Canva analogue: we cannot add CSS, only restyle existing elements.
- `visual_qa.py`, `html2png.py`, `planning_validator.py`, `resource_loader.py` are absent from the clone and unobtainable in Canva.
- Multi-agent orchestration with a shared filesystem does not map onto Canva MCP; a single agent with an editing transaction is the real unit of work.
- PPTX export via PNG/SVG is exactly what we must *not* do — our deck is native Canva.

---

## Skill: content-skills (vstorm) — presentation, infographic, audit, image

**Purpose.** A content-marketing suite; the slide-relevant parts are the presentation generator, the infographic design principles, the AI-slop detector with a scoring rubric, and the image style library. Not slide-native, but the most *systematic* anti-slop and chart-rule source in the cluster.

### Prescribed process (presentation)

1. **Read brand context** (`brand/BRAND.md`, `VISUAL.md`, `VOICE.md`); if missing, ask for colour/font/tone before proceeding — "do not generate a deck with default blue-and-white styling" (`skills/content-presentation/SKILL.md` §Step 1).
2. **3–5 clarifying questions**, but skip any already answered: length, audience, purpose, available data, delivery context (`§Step 2`). Length benchmarks are stated per type: pitch 10–15, conference 30–40, sales 12–18.
3. **Recommend a framework** with a one-sentence rationale (Slidev/Reveal/Spectacle/raw HTML) and let the user override (`§Step 3`).
4. **Emit the narrative outline before any slide code**, with slide number, working title, and one-line purpose; mark where the arc shifts (`§Step 4`).
5. **Wait for explicit approval of the structure** (`§Step 5`).
6. **Generate slide by slide** with content, speaker notes (talking points, timing cues, transition phrase, interaction cue) and design notes (`§Step 6`).

### Rules, thresholds, checklists (with sources)

- **One idea per slide, non-negotiable**; the test is "can you state the purpose in one sentence without *and*?" (`skills/content-presentation/SKILL.md` §One Idea Per Slide).
- **Never more than two font sizes on one slide; one accent colour per slide; one mode (dark or light) per deck** (`§Design Principles`).
- **Banned slide patterns** (`§Anti-Slop Rules for Slides`): "Let's dive in" as a title; an agenda slide; 5+ bullets ("bullet-pocalypse"); stock-photo defaults; "Questions?" as the last slide; a "Thank you" slide; a wall of text; orphan slides with no narrative connection.
- **Narrative arc and pacing** (`skills/content-presentation/presentation-narrative.md` §Pacing Guidance): hook/problem → solution → evidence → CTA, with time budgets 1/2/1.5/0.5 min for a 5-minute talk, 4/8/6/2 for 20 minutes, 8/16/12/4 for 40 minutes. Slides per minute: dense 1 per 2–3 min, standard 1 per 1–2 min, impact slides 1 per 15–30 s, dividers 1 per 5–10 s.
- **Slide patterns with hard caps** (`skills/content-presentation/slide-patterns.md`): comparison columns ≤5 points each and equal counts; code ≤15 lines with 2–4 highlighted at a time; images 60–70% of the slide; quotes ≤3 sentences; pie/donut ≤5 segments; team grid ≤6 people (2×2 or 3×2); timelines 4–8 points (horizontal for 4–6).
- **Chart selection** (`slide-patterns.md` §Chart / Data; expanded in `skills/content-infographic/design-principles.md`): bar = categories; line = change over time; pie/donut = parts of a whole, sparingly, max 5; scatter = correlation. Never 3D, never dual y-axes, never Excel screenshots, never chartjunk.
- **Chart craft rules** (`content-infographic/design-principles.md` §Chart-Specific Principles): y-axis starts at zero; horizontal bars when labels exceed 3 words; sort bars by value unless there is a natural order; bar gap 40–60% of bar width; ≤3–4 lines per line chart; direct labels instead of legends; donut for a centre total; annotate the line, not a detached legend; trend line only when the relationship is meaningful.
- **Data honesty** (`design-principles.md` §Data-Ink Ratio, §Common Mistakes): no truncated axes, no inconsistent intervals, no dual axes with different scales; forecast in dashed/light, historical solid/dark; every chart needs a source and a title that states the insight.
- **Infographic type hierarchy — exactly three levels** (`design-principles.md` §Typography Hierarchy): title 24–32px/700, label 14–18px/400–600, caption 10–13px/400; one family; **at most two weights**; left-align by default; web minimum 10px, print minimum 8pt; descriptive text ≤50–60 characters (no paragraphs).
- **Colour**: ≤5–6 distinct colours per infographic; Tableau-10 categorical palette (`#4E79A7, #F28E2B, #E15759, #76B7B2, #59A14F, #EDC948`); sequential `#EFF3FF→#08519C`; diverging `#B2182B… #2166AC`; **never colour alone** — pair with pattern, shape, label or position (`design-principles.md` §Colorblind-Safe Palettes); red/green never the only differentiator (~8% of men).
- **Whitespace ladder**: sections 40–60px, related items 15–25px, label→data 5–10px; margins for a 1200×800 canvas: 30–50px top, 50–80px sides, 30–50px bottom, 20–40px internal (`§Whitespace`).
- **Contrast**: body 4.5:1, large text (24px+, or 18px bold) 3:1, chart elements 3:1 against neighbours (`§Accessibility`).
- **Slop scoring** (`skills/content-audit/slop-detector.md` §Severity Levels; `skills/content-audit/scoring.md` §Dimension 1): critical −8 first / −5 repeat, warning −3/−2, info −1/−0.5; **em-dash abuse flagged above 2 per 500 words**; passive voice banded at <15% / 15–30% / >30%; paragraph-length uniformity flagged when **>60% of paragraphs sit within 15% of the mean word count**; the "three-point pattern" (every section has exactly three sub-points) is itself a tell.
- **Composite rubric** (`scoring.md` §Overall Composite Score): text content = 0.60 × content quality + 0.40 × voice; visual content = 0.40 + 0.30 + 0.30 (content/voice/visual). Anti-slop, readability, hook strength and structure each weigh 25% of content quality.

### Unique ideas

- **The slop detector is a list of *strings*, not adjectives** — dozens of exact openers, filler phrases, transitions, metaphors, vocabulary tells, and closers, each with a fix. That is directly implementable as a pre-flight text scan.
- **Structural tells** (paragraph uniformity, sentence-length standard deviation, three-point pattern) — slop detected in *shape*, not vocabulary. Sentence-length variety scored by standard deviation: ≥8 = 100, 6–7 = 85, 4–5 = 70, 2–3 = 50, 0–1 = 30.
- **Accessibility as a hard constraint on charts** (title/desc/role on SVG, colour + another channel, contrast bands).
- **Framework selection as an explicit decision with rationale**, and length benchmarks tied to deck type.

### Pitfalls it warns about

- "Do not generate a deck with default blue-and-white styling" — the fallback palette is the failure mode.
- Screenshotting charts, fonts too small to fit more code, images as decoration, multiple CTAs, quotes from yourself.
- Voice/brand files missing → cap the voice-consistency score at 70 and say so (`scoring.md` §Dimension 2).

### Outdated / wrong / impossible against our MCP

- Framework choice (Slidev/Reveal/Spectacle/raw HTML) is irrelevant — Canva is the renderer.
- Speaker notes are written here as first-class content; in Canva they can only be read, so notes must ship as a side file.
- 1200px slide width, 10px minimum type, SVG `<title>/<desc>` accessibility — none addressable through `format_text` or any editing op.
- "Never more than two font sizes on one slide" conflicts with every other source's 4–8 role hierarchy; treat it as a heuristic for simple marketing slides only.

---

## Skill: Powerpoint-fancy-design (Phlegonlabs)

**Purpose.** Produce 1600×900 HTML slides in one of ten named styles, with an unusually explicit pixel contract (safe zone, eight typographic roles, twelve layout prototypes) and a weighted delivery rubric. No license file — record facts, do not copy assets.

### Prescribed process

1. **Identify topic, audience, deliverable**; a Markdown document's `Page X` sections map one-to-one onto slides (`SKILL.md` §Workflow 1–2).
2. **Read the style selector**, recommend **2–3** styles (never all ten), each with name, one-line visual description, and best-fit content (`§Style Selection`).
3. **Confirm `background_mode`** — `paper` default; `white` only for styles that support it (`§Background Modes`).
4. **Read layout rules → review checklist → (for client/public) rubric → layout prototypes**.
5. **Classify each slide's content role** (cover/chronology/comparison/metric/thesis/synthesis/closing) and pick a prototype; never repeat the prototype on consecutive slides (`references/layout-prototypes.md` §Content Role Classification).
6. **Enforce the safe zone**: all primary content inside `y=108…804` (`references/safe-zone.md`).
7. **Generate one HTML file per slide** at fixed 1600×900, static HTML/CSS/inline SVG only, no JS (`SKILL.md` §HTML Rules).
8. **Mandatory second-pass review of every slide** before delivery (`§Mandatory HTML Review`).

### Rules, thresholds, checklists (with sources)

- **Eight typographic roles with hard minimums** (`references/presentation-layout-rules.md` §Typography Scale):

  | Role | EN min | CN min |
  |---|---|---|
  | Display title / hero number | 44px | 40px |
  | Section heading | 28px | 28px |
  | Body | 22px | 24px |
  | Table header | 20px | 22px |
  | Table cell | 18px | 20px |
  | Support copy | 18px | 20px |
  | Label / caption | 16px | 18px |
  | Page number (chrome only) | 14px | 14px |

  CJK is **+2px** for body through label because stroke density reduces apparent size at projection distance; the display title CN floor is *lower* (40 vs 44) because Chinese titles are shorter and each glyph is wider (`§Chinese offset`).
- **Safe zone** (`references/safe-zone.md` §Safe Zone Geometry): canvas 1600×900; top reserved 0–96px; content 108–804px (height **696px**); bottom reserved 804–900px; side edges via `--edge`, usually **92–108px**. If content overflows, do not enlarge the frame — cut content, split the slide, or rebuild hierarchy.
- **Chrome modes**: `bookend` (labels on cover and closing only — default), `all`, `none`; chrome is 14px uppercase at `letter-spacing: 0.18em`, top 28px / bottom 24px (`SKILL.md` §Chrome Labels; `references/safe-zone.md` §Chrome Modes).
- **Layout diversity** (`references/layout-prototypes.md` §Diversity Rules): no prototype twice in a row; **a 10-slide deck uses ≥5 distinct prototypes**; when content is ambiguous, prefer the family not recently used.
- **Cover whitespace rule** (`layout-prototypes.md` §Style-Specific Cover Prototypes): the last direct live child of the layout root must have its bottom at **≥60% of the main frame height**; a cover leaving the lower 40% empty is a layout failure.
- **Dense content**: ≤6 primary ideas per slide, else split; prefer 3–6 major points (`references/presentation-layout-rules.md` §Dense Content Rules; `SKILL.md` §Tables And Text-Heavy Content).
- **Tables**: ≤4 columns; header ≥20/22px bold; cells ≥18/20px; prefer comparison cards, highlighted row groups, metric cards or column blocks; use a real table only when row-column lookup is the point (`presentation-layout-rules.md` §Table Typography, §Table Rules).
- **Geometry preservation** (`references/geometry-preserve.md`): for org charts, architecture diagrams, process maps, strict tables — preserve the structural skeleton, use explicit tracks/coordinates/bounded box sizes, never let text length dictate box sizes, never `align-content: stretch` or uncontrolled `grid-auto-rows`.
- **Style A concrete system** (`styles/style_a.md`): negative space ≥50%; **3 colours + neutral greys**; asymmetric splits 40:60 / 55:35 / 43:57, **never 50:50**; dividers 1px at 6% opacity; 1–3 decorative elements at 0.04–0.12 opacity; palette `--bg #f0ebe2`, `--ink #2a2a30`, `--accent #b85038`; display 88–110px (EN) / 42–48px (CN); giant numbers 140–180px; **forbidden**: pure black, fluorescent orange, purple, gradients, glow/soft shadow, emoji, rounded pills, 50:50 columns, thick arrows, 3D.
- **Delivery rubric** (`references/presentation-quality-rubric.md`): weights Narrative 20, Style/scenario fit 15, Brand fidelity 15, Visual hierarchy 15, Readability 15, Data/diagram clarity 10, Cross-slide pacing 5, Delivery readiness 5; pass = **≥85/100 with no category below 60% of its weight**; hard fails include projection contrast below threshold, more than two competing focal points, weak headline/body hierarchy, unapproved style for the scenario, missing brand lockups, dark-theme projector safety unmet.
- **Review checklist** (`references/html-review-checklist.md`): overlap, clipping, type below minimums, awkward line breaks, decoration fighting content, tables redesigned, padding, deliberate alignment, style still intact, all content inside the main frame, nothing in chrome zones except allowed labels, geometry preserved, HTML/PNG/PPT geometry consistent, text remains the first readable layer.

### Unique ideas

- **Pixel safe zone with a stated reason for each band** — the top band is chrome, the bottom band is footer/page number, and the content frame never moves when chrome toggles.
- **The CN/EN offset table with an explanation**, rather than a single global minimum — stroke density vs character width are handled differently for titles and body.
- **Content-role-first layout selection** (seven roles × twelve prototypes × ten styles matrix), plus an explicit diversity quota.
- **A weighted rubric with a "no weak category" clause**, which prevents a deck from passing on narrative while being unreadable.
- **Background modes as a constrained product decision** (`paper` vs `white`, with styles that must refuse `white` because they are dark-native).

### Pitfalls it warns about

- "Do not shrink text just to preserve the first layout idea."
- "Do not collapse box-and-arrow diagrams into generic cards when relative box sizes carry meaning."
- "Do not normalise all styles toward the same density."
- Chrome labels are the thinnest excuse for decoration: they exist on bookends only by default, and the content frame is fixed regardless.

### Outdated / wrong / impossible against our MCP

- 1600×900 canvas: ours is 1920×1080, so every px value scales ×1.2 (see catalogue).
- `--edge`, CSS custom properties, SVG noise textures, `mix-blend-mode` grain animation, crop marks, `clip-path`, `backdrop-filter` — none are editable in Canva.
- 10 named styles + a style menu is the exact "theme menu" anti-pattern; keep the *style-definition schema* (palette / type roles / allowed devices / forbidden list / checklist) and drop the menu.
- Uppercase tracked chrome (`letter-spacing: 0.18em`, `text-transform: uppercase`) cannot be produced: no letter-spacing, no text-transform.

---

## Skill: present-now

**Purpose.** Turn a subject into a deck the user can present today: one self-contained `deck.html` on a 1600×900 canvas, clicker-safe, with step reveals, tabs, speaker notes and a presenter window. The value here is the **authoring contract** and the **overflow QA harness**, not visual theory.

### Prescribed process

1. **Interview**, at most two rounds of up to four questions, recommended option first: audience, the one takeaway, must-show items (multi-select), format (slides / slides+demo cue / slides+recorded demo); round two settles tensions, timebox, location, look (`SKILL.md` §1).
2. **Recon** the subject just enough to name, for every must-show item, the file or section that proves it (`§2`).
3. **Plan** at "about one slide per minute" following hook → problem → idea (doubles as agenda) → one section per pillar (concept then concrete) → payoff → what changes → close; per slide decide file, id, kicker, a headline with one `<em>` accent phrase, content, at most one interaction, and a notes time; notes times sum to the timebox (`§3`).
4. **Scaffold** from the template, fill every placeholder, verify none remain (`§4`).
5. **Dispatch 3–5 chunks of 2–3 consecutive slides** to parallel subagents that share a source area, each given the authoring contract plus its own paths (`§5`).
6. **Build and QA**; `qa.sh` prints one line per slide (`ok`, or the elements leaving the content box and the click that caused it), saves screenshots with all steps revealed, and lists console errors (`§6`).
7. **Hand off** with keys, slide list, times, and an explicit "what was not verified" list (`§7`).

### Rules, thresholds, checklists (with sources)

- **Canvas and content box**: fixed 1600×900; padding 88px top / 120px sides / 96px bottom; content box **1360×716px** (x 120–1480, y 88–804) (`template/AUTHORING.md:53-57`).
- **Type**: body ≥21px; code ≥19px, ≤8 lines per block, ~60 characters wide (`template/AUTHORING.md:57`).
- **Text budget**: one idea per slide, **≤40 words of visible text** excluding code/interactive data (`template/AUTHORING.md:58`).
- **Notes**: `<aside class="notes">` is required on every slide; 3–6 short sentences plus a transition line into the next slide (`template/AUTHORING.md` §Fragment shape).
- **Themes**: five (`editorial` default, `terminal`, `swiss`, `midnight`, `sage`), each a `:root` token block; brand override sets `--accent` and `--accent-soft` (same hue at ~15% over paper) and must clear **4.5:1 against `--paper` because kickers are small accent text** (`references/themes.md` §Brand).
- **Failure table worth memorising** (`SKILL.md` §6): content overlapping the element below because a grid with `fr` rows grows in an auto-height container (fix: give the grid a definite height, push trailing content with `.mt-auto`); a card holding only a label (fix: drop the card, keep the label); screenshots at an odd size because another process drove the shared browser.

### Unique ideas

- **One slide per minute** as the planning constant, with notes times summing to the timebox — a concrete answer to "how many slides?".
- **Interaction chosen by purpose**, not decoration: tabs for compare/before-after/categories; step reveal for sequences; explore for maps/hubs; simulator for cause-and-effect.
- **Overflow measured per interactive state**, not just at rest — the tallest state of every panel must fit.
- **Chunked subagents by source area** so each writer researches one region rather than the whole corpus.
- **Theme as a token block appended before `</style>`** — a minimal, auditable way to parameterise a deck.

### Pitfalls it warns about

- A grid with `fr` rows inside an auto-height container grows to its content and overlaps what follows.
- Slide-scoped active styles can shadow the shell's `code` styling; scope overrides under the slide id.
- Screenshots taken while another process drives the shared browser come out at the wrong size.
- Step reveals fire on the same tick as a hash change and get reset; navigate in one call, reveal in the next.

### Outdated / wrong / impossible against our MCP

- Everything is HTML/CSS: `var(--token)`, `:root`, `<aside>`, `<script>`, `data-tabs`, `aria-selected`. Canva offers none of it.
- 1600×900 → 1920×1080 at ×1.2 (body 21px → 25.2px; content box 1360×716 → 1632×859).
- Interactive tabs/step reveals have no Canva analogue (Canva supports its own page transitions, not our step logic).
- The 40-word budget is aggressive for a lecture deck but useful as a *prose* target; a technical slide may legitimately exceed it if the extra words are data labels.

---

## Skill: anthropics `pptx`

**Purpose.** Reliability engineering for PowerPoint files — create with pptxgenjs, edit via OOXML surgery, validate, and visually QA. The design section is short but contains the cluster's sharpest negative rules.

### Prescribed process

1. **Choose the path by task**: create → pptxgenjs script; edit/template → unzip → edit `ppt/slides/slideN.xml` → zip; read → `markitdown` for text, `thumbnail.py` for a labelled layout grid (`SKILL.md` §table at top).
2. **Pick layouts from the template** with the thumbnail grid before writing content, and vary them (`§Editing existing decks and templates`).
3. **Do all structural work (add/delete/reorder) before editing content**; `add_slide.py` copies verbatim, and `clean.py` deletes anything missing from `<p:sldIdLst>`.
4. **Create** with a content-informed palette and a single repeating visual motif; **every slide needs a visual element** (`§Design Ideas`).
5. **Validate** with `scripts/office/validate.py`, passing `--original` for template-derived decks so inherited XSD errors are baselined (`§File QA`).
6. **Visual QA**: convert to images (`soffice` → pdf → `pdftoppm -r 150`) and **inspect every slide**, checking text overflow first (`§Visual QA`).

### Rules, thresholds, checklists (with sources)

- **Type sizes** (`SKILL.md:139-143`): slide title 36–44pt bold; section header 20–24pt bold; body 14–16pt; captions 10–12pt muted. On a 13.333×7.5in canvas (960×540pt) that maps to **2px per pt** at 1920×1080: title 72–88px, section 40–48px, body 28–32px, caption 20–24px.
- **Spacing** (`SKILL.md:146-148`): margins ≥0.5in (=72px at 1920 scale); 0.3–0.5in between content blocks (=43–72px); consistent gaps, never random.
- **Palette discipline** (`§Color Palettes`, `§Before Starting`): one colour dominates **60–70%** of visual weight, with 1–2 supporting tones and one sharp accent; never equal weight; ten named palettes supplied as *inspiration*, with the explicit instruction not to default to generic blue.
- **Dark/light sandwich**: dark backgrounds for title and conclusion, light for content — or commit to dark throughout.
- **Fonts** (`§Typography`): safe list that renders true-to-width in QA *and* ships with Office — Arial, Calibri, Cambria, Times New Roman, Courier New, Bookman Old Style, Century Schoolbook. QA-unreliable (substitute has different metrics): Georgia, Trebuchet, Impact, Arial Black, Garamond, Consolas, Palatino. **Never default to Aptos.** If the user asks for an unreliable font, add ~10% slack and don't trust the preview's fit.
- **Hard "avoid" list** (`§Avoid`):
  - **NEVER use accent lines under titles** — "a hallmark of AI-generated slides".
  - **NEVER add decorative colour bars or accent stripes** — header/footer bars, vertical sidebar stripes, thin stripes along a card edge, single-side borders. "If you want to set a card apart, use a subtle background tint, a drop shadow, or an icon."
  - Don't repeat the same layout; don't centre body text; don't skimp on size contrast (title 36pt+ vs body 14–16pt); don't default to blue; don't mix spacing randomly; don't style one slide and leave the rest plain; don't create text-only slides; don't forget text-box padding (`margin: 0` when aligning to a shape); don't use low-contrast elements.
  - **Don't default to cream/beige backgrounds** when none is specified — name-and-shame list: `F5F5DC`, `FAF0E6`, `FAEBD7`, `FFF8E1`.
- **QA defects, in priority order** (`§Visual QA`): text overflow or cut-off **first**; then overlapping elements; footers colliding with content; gaps <0.3in; uneven gaps; margins <0.5in; misaligned columns; low-contrast text; template decoration mispositioned after text replacement; low-contrast icons; text boxes too narrow; leftover placeholders.

### Unique ideas

- **The only source that names the two most common AI slide tells as absolute prohibitions**: accent lines under titles and decorative edge stripes. Every other skill either recommends them (sunbigfly P1-4) or ignores them.
- **Font metrology for QA**: distinguish fonts whose substitutes have compatible widths from those that don't, so you know when the preview's overflow check is a lie.
- **Structural-before-content ordering** for template surgery, with the reason (duplication clones edited content; cleanup deletes unregistered slides).
- **Template slots ≠ source items**: delete the whole group of an unused template item, not just its text.

### Pitfalls it warns about

- pptxgenjs: `pres.layout` must be set before adding slides (default is 10×5.625in, and coordinates past the edge are silently written outside the slide); hex colours must be 6 digits with no `#`; option objects are mutated in place; negative shadow offsets corrupt the file; `letterSpacing` is ignored (use `charSpacing`); literal `•` double-bullets; `rectRadius` only on rounded rectangles; no gradient fills; stacked-bar `dataLabelPosition: outEnd` corrupts the file; combo charts need both `valAxes` and `catAxes`.
- PowerPoint discards charts that reference undeclared axis ids yet opens the file with no error — so a "valid" file can lose data silently.
- `xml.etree` round-tripping OOXML corrupts namespace prefixes.

### Outdated / wrong / impossible against our MCP

- We never touch OOXML. The value is entirely in the design rules, the QA ordering, and the failure taxonomy.
- pt-based sizes require conversion; see the normalisation table.
- The "safe font" concept does map usefully onto Canva: a design whose font is unavailable on the presenting machine will substitute, so font choice must be pre-generation and conservative, and typography QA is a visual check, not a code check.
- `export-design` can produce PPTX/PDF, but there is no validate/repair loop for it.

---

## Skill: anthropics `canvas-design`

**Purpose.** Not a deck skill. It writes a **design philosophy** (a 4–6 paragraph manifesto naming an aesthetic movement) and then expresses it on a single poster-like canvas, 90% visual / 10% text (`SKILL.md` §DESIGN PHILOSOPHY CREATION).

Process worth stealing: name the movement (1–2 words) → articulate 4–6 paragraphs spanning space/form, colour/material, scale/rhythm, composition/balance, hierarchy → identify the "subtle reference" the audience will feel but not be told → express it → **refine, don't add** ("if the instinct is to draw a new shape, stop and ask how to make what is already here more of a piece of art").

Rules: text is minimal and visual-first; "nothing falls off the page and nothing overlaps; every element has breathing room" (`§CANVAS CREATION`); the multi-page option treats page one as a spread in a coffee-table book, each subsequent page a distinct twist.

Why it matters here: it is the purest statement of the "concept before execution" principle that Huashu's rubric scores at the top (`references/critique-guide.md` §0) and that every slide skill in this cluster lacks. Its weakness is the opposite: no numbers, no grid, no delivery constraints, and a heavy "repeat that this took countless hours" prompt incantation that adds no executable instruction.

Against our MCP: nothing is executable except the manifesto text itself, which is a legitimate pre-step for `create-design`'s `user_intent`/`brief`.

---

## Skill: anthropics `frontend-design`

**Purpose.** The canonical anti-default brief. Everything in the Visual craft catalogue's anti-slop section traces back here.

Rules (verbatim-worthy, `SKILL.md` §Process):

1. warm cream background (near `#F4F1EA`) + high-contrast serif display + terracotta/warm-clay accent (often near `#D97757`);
2. near-black background with a single bright acid-green or vermilion accent;
3. broadsheet layout — hairline rules, zero border-radius, dense newspaper columns;
4. the SaaS-card kit — identical rounded cards, one radius for everything, the same soft grey shadow `rgba(0,0,0,.1)`, gradient washes as decoration;
5. template chrome regardless of subject — a tracked-out ALL-CAPS eyebrow above every heading; meta strings joined with middle dots ("A · B · C"); "WORD — fragment" labels with a spaced em dash; tinted near-black (`#0B0B0B`, `#111`) standing in for black; monospace for small data labels; a "→" appended to link and button text.

Plus three typographic defaults: **accenting a single word in a headline** (italic/bold/colour), **all caps for labels**, and **unnecessary labels above content**.

Prescriptive core: subject matter determines the visual language ("a design for a toy for girls aged 8–11 will be very aesthetically different from a dashboard for financial analysts"); one or two typefaces, clearly distinct if two; line lengths **<80 characters**, serif body gets slightly more leading than sans; structural devices (outlines, borders, numbering, eyebrows, dividers) must **encode information** — numbered markers only if the content genuinely is a sequence; motion only when it answers a user action; "spend your boldness in one place"; Chanel's "remove one accessory".

Its two-pass method is directly portable: write a compact token plan (4–6 named hex values, typefaces and roles, layout concept with ASCII wireframes, alignment decision, principles), then **review that plan against the brief** and revise anything that would be produced for any similar page, saying what changed and why — before writing a single slide.

Against our MCP: the design-plan artifact is the executable part; CSS selectors, motion and responsiveness are not.

---

## Skill: anthropics `theme-factory` and `brand-guidelines`

Thin wrappers, one line each. `theme-factory` is a ten-item theme menu (Ocean Depths … Midnight Galaxy) shown as a PDF, then applied; the menu is the anti-pattern our skill must avoid, so keep only (a) the idea of a theme file carrying palette + font pairing + a one-line "fits", and (b) "if none fit, generate a new theme, show it for review, then apply". `brand-guidelines` is one brand's hex codes and two font families with fallbacks; its only transferable content is the *shape* of a brand payload (dark/light/mid/light-grey + 3 accents; heading font vs body font with explicit fallbacks; headings ≥24pt get the display face).

---

## Skill: anthropics `doc-coauthoring`

Not slide-specific, but stage 3 is the best QA idea in the cluster that no slide skill has: **reader testing** — predict the questions a real reader will ask, have a cold sub-agent read the artifact and answer them, then fix the places where it stalls or answers wrong (`skills/doc-coauthoring/SKILL.md` §Stage 3). For a deck, the equivalent is: give a fresh agent only the slide titles and ask it to reconstruct the argument; then give it the rendered thumbnails and ask what each slide is for. Anything it cannot answer is a hierarchy or storyline defect. Stage 2's sequence (clarifying questions → brainstorm → **curate** → gap check → draft → iterative refinement) is also a cleaner articulation of "generate options before converging" than Huashu's.

---

## Merge recommendations

| Idea | Source(s) | Keep / adapt / drop | Why | Where it belongs |
|---|---|---|---|---|
| Three-direction gate (6 candidates → 3 thumbnails → 3 drafts → stop) | huashu `directions.md` §Phase 4–6 | **Adapt** | Proven against a real user who rejected both "templated" and "too safe"; but Canva cannot produce cheap HTML thumbnails — generate three *pages* via `create-design` or three page-sets via `copy-design` | plan |
| Gate files / quoted approval (`direction-approved.md`) | huashu `SKILL.md` §6 | **Adapt** | Prevents silent skipping; record the user's exact words when they choose | plan |
| Five form questions per page (role, distance, temperature, capacity, motif) | huashu `workflow.md` §3 | **Keep** | The cheapest defence against generic layout; "motif" is the only question that forces subject-specific form | plan |
| Lock grammar on 2 showcase pages before batching | huashu `modules/deck.md` §做的顺序 | **Keep** | Turns a 13-page rework into a 2-page rework | plan → generate |
| Appearance ledger (don't repeat recent looks) | huashu `SKILL.md` §开工三件事 | **Adapt** | In a single-user Canva workflow, a local note of the last N decks' palettes/layouts is enough | plan |
| "Add options, don't add bans" | huashu `directions.md` §为什么这样做 | **Keep** | Banning look families produced boring decks; police convergence instead | plan / review |
| Colour derivation: sample → converge → argue | huashu `design-styles.md:23-62` | **Keep** | The single best anti-arbitrary-palette device, and it survives Canva because colours *are* editable | plan → edit |
| oklch chroma bands (0.01–0.04 ground, 0.08–0.15 brand, 0.15–0.22 accent) | huashu `design-styles.md` §印刷色质感 | **Adapt** | Canva edits hex, not oklch; use the bands as a mental target and pick hexes that sit there | plan |
| CJK/Vietnamese fallback-chain and no-faux-italic rules | huashu `typography.md` §4.2–4.4 | **Adapt** | Font family is locked in Canva; the rule becomes "choose a template whose font supports the language, and never rely on italic for emphasis" | plan |
| Modular type scale with 4 ratios and a 5-step ceiling | huashu `typography.md` §1 | **Keep** (as derivation) | Explains *why* the numbers are what they are; useful when a deck needs a non-standard scale | plan |
| Line-length and leading table (65ch / 36em; leading by line length) | huashu `typography.md` §2 | **Adapt** | No `max-width` in Canva, but text-box width *is* adjustable via `resize_element`; leading is editable via `line_height` | edit |
| Type floor: 24/16/60–120 at 1920×1080 | huashu `content-guidelines.md:181-185` | **Keep** | The cleanest expression of the classroom constraint; matches anthropics pt conversion (28–32px body) | plan / review |
| Eight-role type scale with EN/CN offsets | Phlegonlabs `presentation-layout-rules.md` | **Keep**, normalised ×1.2 | Most complete role set; converts cleanly and the offset logic transfers to Vietnamese diacritics | plan |
| 14px absolute floor + "never shrink to fit" | SlideSpeak `SKILL-FORMAT.md:112`; Phlegonlabs §Fancy Style Exception | **Keep** | Universal, enforceable as a review check | review / edit |
| Bounded content island (content-sized cluster, no `space-between` stretching) | SlideSpeak `layout-fit-model.md` §Schicht 2 | **Keep** | Diagnoses both underflow and overflow with one rule; in Canva it becomes "don't stretch a sparse page; add content or change template" | plan → review |
| Density as layout register (editorial/balanced/data-dense), never font scaling | SlideSpeak `layout-fit-model.md` §Prinzipien 4 | **Keep** | The most important correction in the whole cluster | plan |
| Occupancy / richness gates | SlideSpeak `README.md` §Quality gates | **Adapt** | No DOM to measure; convert to a thumbnail checklist (empty band > 40%, hollow card, single text block floating) | review |
| Measured density targets (tokens/lines/numerals) | SlideSpeak `mckinsey-anatomy.md` §Counted spec | **Keep** for data decks | Only source with counted, reproducible targets; use as a floor for data slides, not a global rule | plan / review |
| Action titles (full-sentence claim, ≤2 lines) + title-only storyline test | SlideSpeak `mckinsey-anatomy.md` §1 | **Keep** | The single highest-leverage content rule; the test is free | plan / review |
| Boxed exhibits with header band + unit line; SOURCE line; numbered footnotes | SlideSpeak `mckinsey-anatomy.md` §1–2 | **Adapt** | Canva can restyle existing text/shapes but cannot add boxes or footnotes; achievable only by choosing a template that already has them | plan (template choice) |
| Chart annotation callouts with leader lines; values on data | SlideSpeak `mckinsey-anatomy.md` §2 | **Drop** for Canva | No element creation; only possible if baked into an uploaded image | visuals (image authoring) |
| Layout contracts with slot capacity `{min, ideal, max}` | SlideSpeak `layout-fit-model.md` §Schicht 1 | **Adapt** | Becomes a pre-generation outline contract: each page declares its slot content counts before design | plan |
| Composition rules (cover first, exec summary second, max 2 data slides in a row, ≥1 structural slide after 8) | SlideSpeak `skills/consulting/layout-grammar.md` | **Keep** | Deck-level rhythm rules that survive any renderer | structure |
| Content-role-first layout choice + prototype diversity quota (≥5 per 10 slides, never consecutive) | Phlegonlabs `layout-prototypes.md`; sunbigfly `layouts/README.md` | **Keep** | The clearest formalisation of "vary the layout" | structure / plan |
| Visual-protagonist rotation list (10 kinds) | huashu `slide-decks.md` §视觉主角必须差异化 | **Keep** | Prevents 13 pages of "heading + screenshot" | structure / visuals |
| Safe zone with fixed content frame (108/96 on 1600×900) | Phlegonlabs `safe-zone.md` | **Adapt** ×1.2 | Canva pages have no explicit safe zone, but the *rule* (top ~130px, bottom ~115px reserved on 1920) is a review check | review |
| Chrome only on bookends | Phlegonlabs `safe-zone.md` §Chrome Modes | **Keep** | Kills the duplicate-page-number class of bug | structure |
| Fill-rate targets by page type (cover 40–55%, content 60–75%, data 70–80%) | sunbigfly `design-specs.md` §留白与视觉焦点 | **Adapt** | Useful as an eyeball metric on thumbnails; do not turn into a hard gate | review |
| Five-layer depth with ≥3 active | sunbigfly `design-specs.md` §五层景深 | **Drop** | Needs `position:absolute` and z-index; not expressible in Canva | — |
| 60-30-10 colour rhythm | sunbigfly `design-specs.md` §C; vstorm `content-infographic/design-principles.md`; anthropics pptx §Color Palettes | **Keep** | Three independent sources agree; enforceable as "one dominant, one support, one accent" | plan / review |
| Colour token architecture: ground(page/card/ink) + signal(primary/subtle) + support(muted/rule) | SlideSpeak `skills/*/tokens.json` | **Keep** | The smallest schema that still produces a distinctive deck; maps to Canva's fill/text colours | plan |
| Max 5–6 colours; colourblind-safe categorical palette; never colour alone | vstorm `design-principles.md` §Color Usage, §Colorblind-Safe Palettes | **Keep** | Accessibility + anti-chaos in one rule | visuals |
| P0/P1/P2 severity ladder with "no FINALIZE on round 1" and rollback-to-planning after 2 failed rounds | sunbigfly `page-review-playbook.md` §Part B–E | **Keep** | The most rigorous QA protocol in the cluster, and renderer-agnostic | review |
| Round-scoped screenshot archive, review only the newest image | sunbigfly `page-review-playbook.md` §Part A-0 | **Adapt** | Canva gives per-page thumbnails inside a transaction; save them per round | review |
| Render-then-inspect ladder (thumbnail ≠ render; control-file experiment) | huashu `verification.md` §第 0 条 | **Adapt** | In Canva the "renderer" is the Canva renderer + PDF export; still verify both | review / export |
| Mechanical text diff (strip whitespace, compare, count elements) | huashu `verification.md` §第 0 条 | **Adapt** | `get-design-content` gives text; compare it against the source outline to catch paraphrase drift | review |
| Paragraph-corruption trap: regions/runs must be parsed raw | (learned, not in these sources) | **Keep** | Joining runs invents typos; relevant to `get-design-content` | review |
| Overflow measured per interactive state | present-now `SKILL.md` §6 | **Adapt** | Canva has no interactive states, but "tallest state" maps to "longest line after text replacement" | review |
| One slide per minute; notes times sum to timebox | present-now `SKILL.md` §3 | **Keep** | Instant answer to "how many slides?" | plan / delivery |
| ≤40 words visible per slide | present-now `AUTHORING.md:58` | **Adapt** | Right for talks, wrong for a data/lecture deck; use as a default with a documented exception for tables and quotes | plan |
| Narrative arc + time allocation table | vstorm `presentation-narrative.md` §Pacing Guidance | **Keep** | Turns "how long is each section" into arithmetic | structure |
| Banned-pattern list (no agenda slide, no "Questions?", no "Thank you", no bullet-pocalypse) | vstorm `content-presentation/SKILL.md` §Anti-Slop; huashu deck module (closing = requirements) | **Keep** | Cheap, specific, and testable | review |
| AI-slop string lists + structural tells | vstorm `slop-detector.md`; anthropics `frontend-design.md` §Process | **Keep** | Directly implementable as a pre-flight text scan | review |
| Em-dash budget (>2 per 500 words) | vstorm `slop-detector.md` §Category 7; SlideSpeak hard ban | **Adapt** | Ban in visible copy, since em dashes are also a typographic hazard in Vietnamese/Latin | review |
| No uppercase/tracked labels anywhere | SlideSpeak `SKILL-FORMAT.md:111`; anthropics `frontend-design.md` §Process | **Keep** | Two independent sources, and Canva cannot produce tracking anyway | review |
| No accent stripes / no title underlines / no single-side borders | anthropics `pptx/SKILL.md` §Avoid | **Keep** | The two loudest AI tells; both are also hard to remove once a template has them | plan (template choice) / review |
| No cream/beige default grounds | anthropics `pptx/SKILL.md` §Avoid; huashu `content-guidelines.md` §2026 | **Keep** | Prevents the "Claude look"; note the tension with "appearance family is not a crime" (Huashu) — resolve as "chosen, not defaulted" | plan |
| Image decision rules (gradient/abstract → generate; person/product/building → ask) | SlideSpeak `skills/consulting/image-style.md` §Decision Rules | **Keep** | Clear policy for a tool that can generate but often cannot (credit quota) | visuals |
| Prompt recipe: subject + style + mood + technical | vstorm `content-image/SKILL.md` §Prompt Structure | **Keep** | The most reusable image-prompt skeleton; add "no text, no logos" | visuals |
| Negative-prompt library + stock-photo clichés | vstorm `content-image/style-library/editorial.md`; SlideSpeak `skills/consulting/image-style.md` §Negative prompt | **Keep** | Handshakes, headsets, lightbulbs, magnifying glasses | visuals |
| Image budget / spend guard | SlideSpeak `README.md` §Quality gates | **Adapt** | Our real constraint is `credit_quota_exceeded`; check before promising imagery | visuals |
| Moodboard as an image-first style anchor | SlideSpeak `CLAUDE.md` §Moodboard step | **Adapt** | Two boards on rotated colour axes; but generation may be unavailable, so allow a reference-image path | plan |
| "Every slide needs a visual element" | anthropics `pptx/SKILL.md` §For Each Slide | **Keep** | Simple, memorable, and true for a lecture audience | structure |
| Geometry preservation for frameworks/org charts/process maps | Phlegonlabs `geometry-preserve.md` | **Keep** | Most relevant rule for a philosophy course's diagrams (the triad, the negation spiral) | visuals |
| Design-independence check (3 consecutive pages sharing one grid = template tell) | sunbigfly `page-review-playbook.md` P1-9 | **Keep** | Catches the failure that survives all numeric checks | review |
| Style-fidelity rule: don't normalise every style to the same density | Phlegonlabs `SKILL.md` §Style Fidelity; SlideSpeak `SKILL.md` §Style is discovered | **Keep** | Protects a quiet style from being "filled in" | review |
| Manifesto-first (design philosophy before layout) | anthropics `canvas-design.md` §DESIGN PHILOSOPHY CREATION | **Adapt** | Compress to a 5-line "design stance" inside the plan, not a 6-paragraph document | plan |
| Plan → review-plan-against-brief → build → critique | anthropics `frontend-design.md` §Process | **Keep** | The step most agents skip; costs one message and prevents the generic default | plan |
| Reader testing with a cold agent | anthropics `doc-coauthoring.md` §Stage 3 | **Keep** | Best available substitute for usability testing of a deck | review |
| Theme menu / style catalogue | theme-factory; Phlegonlabs 10 styles; SlideSpeak 8 packages | **Drop** | Both Huashu and SlideSpeak explicitly identify menus as the source of sameness; keep one style *derivation* method and one style *schema* | — |
| pptxgenjs / OOXML / html2pptx constraint stacks | anthropics pptx; huashu `editable-pptx.md` | **Drop** | We never emit HTML or OOXML | — |
| Multi-agent orchestration protocols | sunbigfly `SKILL.md` §2.2; present-now §5 | **Drop** (mostly) | Useful only as "chunk long decks by source area"; the RUN/STATUS/FINALIZE machinery is harness-specific | — |

---

## Contradictions

1. **Uppercase tracked micro-labels.** Phlegonlabs uses `text-transform: uppercase` with `letter-spacing: 0.18em` for chrome and sunbigfly prescribes a 10px/2px-tracking overline on content pages. SlideSpeak bans uppercase *anywhere* (`SKILL-FORMAT.md:111`), and `frontend-design` lists all-caps labels as the second typographic tell. **Recommend SlideSpeak/frontend-design.** All-caps tracked eyebrows are the most recognisable generated-deck signature, and Canva cannot set letter-spacing anyway, so an attempt would look like plain shouting.

2. **Accent stripes on cards.** sunbigfly's P1-4 fix explicitly prescribes `border-left: 4px solid var(--accent-1)` to establish hierarchy; huashu's old-slop list names the same device (`border-radius: 12px; border-left: 4px solid …`) as "the typical signature of an AI-generated card"; anthropics pptx says never, including "single-side borders on rectangles"; SlideSpeak makes it a validation failure. **Recommend the ban.** It is a three-to-one vote and the device carries no information.

3. **Shadows and depth.** sunbigfly recommends four-layer shadows ("4 layers is 5× better than 1") and calls flat cards a P2 defect; huashu's SaaS-card-kit tell is precisely "the same soft grey shadow under each card"; anthropics pptx allows a drop shadow as a card differentiator but its palettes and style anchors are mostly flat; SlideSpeak's consulting style uses `0 1px 0` at most. **Recommend: at most one elevation level per deck, and only where the template's language already has it.** In Canva we cannot author shadows at all — the template decides.

4. **Density philosophy.** sunbigfly treats a large empty band as a P0 (">40% of the canvas with no content or decoration") and sets fill targets of 60–80%; SlideSpeak's core correction is that whitespace is a margin around a content-sized cluster and "no slide is half-empty" is replaced by "sparse should look calm, not lost"; huashu says keep cutting until the whitespace makes you uncomfortable. **Recommend SlideSpeak + huashu.** A page that is 40% empty because the content is one sentence is correct; a page that is 40% empty because content was dropped is a defect. The review question is "is the empty space a margin or a hole?", not "what percentage is filled?".

5. **"Three big numbers" data pages.** anthropics pptx suggests large stat callouts (60–72pt) and vstorm's stat-card pattern says one stat per slide with no chart; huashu calls "three big numbers + bar chart" the template answer to every data page; SlideSpeak's density spec demands 80–160 tokens and 15–45 numerals on an exhibit page. **Recommend huashu + SlideSpeak, differentiated by deck type:** a motivational/lecture page may carry one dominant number with a baseline ("37%, industry average 22%" — vstorm's own context rule), while a data/report page must carry a real exhibit. The failure is three equal cards with no relationship between them.

6. **Title-to-body ratio.** huashu requires ≥2.5× and recommends 3×; sunbigfly wants a **≥5× max/min ratio per page**; Phlegonlabs' role table implies ~2× (44 vs 22) across 8 distinct roles; SlideSpeak's token scales give 64/18 ≈ 3.5× at the top but body steps of only 1.1–1.2×. **Recommend 3× title:body as the default, 5× as the "hero page" mode.** A 5× ratio on every page forces either a giant title or unreadably small body; reserve it for covers and single-number pages.

7. **50/50 columns.** Phlegonlabs style A forbids 50:50 and prescribes 40:60/55:35/43:57; sunbigfly's symmetric layout is explicitly 1fr 1fr; SlideSpeak's two-panel default is 60–65/35–40. **Recommend asymmetry by default, symmetry only for genuine A/B comparisons** (before/after, pros/cons) where equal visual weight is the message. A philosophy "thesis vs antithesis" page is a legitimate 50/50; a "main argument + supporting evidence" page is not.

8. **Slide count and pacing.** vstorm gives 1 slide per 1–2 minutes for standard slides and 1 per 2–3 minutes for dense ones; present-now says about one slide per minute; the SlideSpeak academic grammar treats a ≤12-slide talk as its own mode (skip prior work) and a ≥25-slide defence as another (duplicate prior-work and result types). **Recommend a rule keyed to deck type**, not a single constant: lecture/teaching ~1 slide per 1.5–2 minutes, pitch ~1 per 45–60 seconds, defence ~1 per 2–3 minutes (because each page carries an argument). For a 15-minute course presentation that lands at 8–10 content pages plus cover/section/closing.

9. **Section dividers.** SlideSpeak's consulting grammar allows them only in decks >12 slides; huashu uses full-bleed dividers as a core rhythm device in decks of any length. **Recommend: dividers only when the deck has ≥3 genuine parts**, regardless of page count; a 9-page deck with three movements earns two dividers, a 14-page deck with one argument earns none.

10. **Style menus.** theme-factory ships ten themes and Phlegonlabs ten styles, both with a "pick one" flow; huashu (`SKILL.md` §三方向门) and SlideSpeak (`CLAUDE.md` §The product has NO selectable styles) both treat a menu as the root cause of sameness. **Recommend the derivation path**, with the style catalogue demoted to internal reference material — which is exactly what SlideSpeak does with its own `skills/` folder.

11. **Speaker notes.** vstorm treats notes as first-class content with timing and transition phrases; huashu says don't add them unless asked; Canva cannot write them. **Recommend: always produce notes, but as a separate deliverable** (a chat block or exported file keyed to slide numbers), because the presentation still needs a script and the deck cannot hold one.

12. **Image sourcing.** huashu bans SVG illustration of people/objects and prefers real or generated photography; vstorm's flat-illustration style is *designed* for exactly those subjects and recommends vector abstraction. **Recommend subject-dependent:** photographs for real places, people, artefacts and products; flat/geometric diagrams for abstract relations; never a "hand-drawn" SVG of a person.

---

## Gaps

1. **No chart or diagram authoring path.** Every source assumes it can draw a chart (SVG, pptxgenjs `addChart`, HTML divs). Canva MCP has no chart op, no shape creation, no connector creation. The skill must therefore (a) put chart *intent* into the `create-design` outline so the generator draws one, or (b) author the chart as an image and upload it (`create-upload-url`), or (c) reuse shapes that already exist on a template page and only restyle/position them. None of the studied skills covers this decision, and it is the single largest functional gap for a data-heavy lecture.

2. **No DOM, therefore no measurement.** Every QA protocol in the cluster ultimately measures geometry (overflow, gap, occupancy, contrast). Canva exposes only per-page thumbnails inside a transaction and read-back text. A complete skill needs a *visual* gate list designed for eyes-on-thumbnails, plus a discipline of rendering at a known size and comparing against a checklist — not a percentage.

3. **No typography control beyond size/weight/italic/align/colour/line-height.** No family, tracking, case, features, hyphenation, or text-box auto-fit. All the type-scale *derivation* rules survive, but the enforcement mechanism is "choose the right template up front", which none of the sources discusses because they all control CSS.

4. **No page creation, deletion, or in-page re-layout.** `merge-designs` can insert/remove/move pages and `copy-design` can clone; `create-design` regenerates. There is no "make this page a 3-column layout". The skill needs an explicit escalation ladder: restyle → replace text → swap page via merge → regenerate page → regenerate deck.

5. **No presenter-notes write, no alt-text write, no comment-to-slide mapping.** Accessibility and delivery-readiness therefore become external artifacts. No source covers producing a notes/alt-text sidecar that stays in sync with slide numbers.

6. **No content-verification loop.** Huashu fact-checks the subject; SlideSpeak marks illustrative numbers; vstorm forbids unsourced figures. None describes verifying the *final rendered deck* against the source outline for dropped or paraphrased content — and Canva's `create-design` is known to paraphrase. A diff step (`get-design-content` vs the approved outline) is required and is not described anywhere.

7. **No cost/quota model.** SlideSpeak has a FAL spend guard; nobody models a credit-quota failure (our `generate-image` can hard-fail at 100% quota). The skill needs a plan-B that does not depend on image generation: typographic covers, procedural diagrams uploaded as PNG, or user-supplied imagery.

8. **No collaborative/versioning model.** SlideSpeak versions folders (`V1`, `V2`, `V3.1`) and never overwrites; Canva has no delete-design tool, so the equivalent is `copy-design` before destructive work plus a naming convention. No source describes this.

9. **No multi-language typographic QA for Vietnamese.** The CJK chapters are excellent but Vietnamese is a Latin script with stacked diacritics: it needs generous leading (the CJK-style bump), fonts with full Latin Extended coverage, and care that all-caps/tracking does not break diacritic stacking. Nothing in the cluster covers it, and it is the user's actual language.

10. **No "presentation delivery" skill.** Timing, transitions, clicker behaviour, what to say while a dense chart is on screen, Q&A handling — present-now touches notes and keys, vstorm touches pacing, but nobody covers rehearsal or the live failure modes (font substitution on the venue laptop, projector contrast, 4:3 letterboxing).

11. **No rubric for a *course* deck.** Phlegonlabs' rubric targets client/public delivery; SlideSpeak's targets consulting. A university presentation is judged on argument clarity, doctrinal accuracy, example quality, and whether the audience can read the back row. The cluster has the ingredients but no assembled rubric.

12. **No recovery playbook for a bad generated deck.** Every source assumes generation is competent and only needs polish. The realistic case — `create-design` produced an unusable skeleton — needs a decision tree: regenerate with a tighter outline, copy a page from a reference design, or rebuild page-by-page via merge.

---

## Visual craft catalogue

All numbers below are as stated by the source, then normalised to a **1920×1080** canvas so they can be compared and used. Conversion factors: 1600×900 → ×1.2; 1280×720 → ×1.5; a 13.333×7.5in PowerPoint slide is 960×540pt, so **1pt = 2px** at 1920 wide.

### 1. Type scales

**1.1 The role table (normalised to 1920×1080)**

| Role | Source value | @1920 | Source |
|---|---|---|---|
| Body (deck, HTML) | ≥24px, ideal 28–36 | 24–36 | huashu `content-guidelines.md:181-185` |
| Body (deck, pt) | 14–16pt | 28–32 | anthropics `pptx/SKILL.md:141` |
| Body (1600 canvas) | ≥22px EN / 24px CN | 26.4 / 28.8 | Phlegonlabs `presentation-layout-rules.md` |
| Body (1600 canvas) | ≥21px | 25.2 | present-now `AUTHORING.md:57` |
| Body (1280 canvas) | 13–14px | 19.5–21 | sunbigfly `design-specs.md` §A |
| Body (engine token) | 16–21px | 16–21 | SlideSpeak `SKILL-FORMAT.md:112` |
| Absolute floor | 14px | 14 | SlideSpeak `SKILL-FORMAT.md:112` |
| Label / caption | ≥16px | 16 | huashu `content-guidelines.md:185` |
| Label (1600) | ≥16px EN / 18px CN | 19.2 / 21.6 | Phlegonlabs |
| Caption (pt) | 10–12pt | 20–24 | anthropics `pptx/SKILL.md:143` |
| Title | 60–120px | 60–120 | huashu `content-guidelines.md:183` |
| Section title | 80–160px | 80–160 | huashu |
| Title (pt) | 36–44pt | 72–88 | anthropics |
| Display (1600) | 44px EN / 40px CN | 52.8 / 48 | Phlegonlabs |
| H1 (1280) | 26–32px | 39–48 | sunbigfly |
| Hero / display | 180–240px | 180–240 | huashu |
| Giant number (1600) | 140–180px | 168–216 | Phlegonlabs `styles/style_a.md` |
| Data hero (1280) | 64–120px | 96–180 | sunbigfly |

**Consensus.** Body sits in **24–32px** on 1920×1080, and the sources that run lower (sunbigfly 19.5–21, SlideSpeak 16–21) are writing for close-viewing report decks, not a lecture hall. For a classroom, adopt **body 28–34px, absolute floor 24px, labels ≥18px, titles 60–88px, hero 120–200px**, which is Huashu's scale tightened by the anthropics pt conversion. The user's own learned preference (body 34–38px, titles 52px on a 1920 deck) sits at the top of the body band and should be honoured.

**1.2 Scale construction.** Do not pick numbers; pick a ratio and derive. 1.2 for dense/dashboard, 1.25 default, 1.333 editorial, 1.5 for posters and slides (`huashu typography.md` §1). Body 16–18px is the anchor; caption 12–13; small 14; h3 ≈1.25×; h2 ≈1.56×; h1 ≈1.95×; display 3×–8× **off-scale** because it is a layout element (`references/typography.md` §1 table). More than **5 steps** is hierarchy inflation; more than **6 sizes** is the same problem stated differently (`typography.md` §1; `critique-guide.md` §3). Per-page max/min ratio ≥**5×** is a tension target for expressive pages (`sunbigfly design-specs.md:112`), not a global law. Title:body ≥**2.5×**, target **3×** (`huashu critique-guide.md:55,136`).

**1.3 Leading and measure.** Leading is a function of line length, not a constant: Latin display 0.95–1.1, headings 1.1–1.3, short body 1.4–1.5, long body 1.6; CJK runs +0.2 throughout (display 1.1–1.25, headings 1.3–1.4, short 1.6–1.7, long 1.8–2.0) (`huashu typography.md` §2). Measure: Latin 45–75 characters, best 66 (`max-width: 65ch`); CJK 22–38 characters, best 28–32 (`36em`) (`typography.md` §2). frontend-design sets the Latin ceiling at **<80 characters** and gives serif body slightly more leading than sans (`anthropics frontend-design.md` §Design principles). Body line-height 1.6–1.8 with headings 1.2–1.3 is the operational pair (`sunbigfly page-review-playbook.md` P1-8).

**1.4 Tracking.** Only all-caps Latin micro-labels take positive tracking, 0.08–0.15em (`huashu typography.md` §4.5); CJK never uses negative display tracking ("Han is a full-width design; negative tracking makes strokes collide") (`§4.5`); display Latin tightens −0.02em (`vstorm styles/typography.json` h1) — but since half the cluster bans caps labels outright and Canva cannot set tracking, the safe rule is **zero tracking, sentence case**.

**1.5 Numbers.** Tabular figures for any column or table (`font-variant-numeric: tabular-nums`), slashed zero where 0/O confuse (`huashu typography.md` §4.2, §6; `sunbigfly charts/kpi.md` §关键规则). This is a font-feature rule with no Canva control — it becomes "choose a font whose default figures are tabular, or avoid numeric columns".

**1.6 Language offsets.** CJK body is set **+2px** above Latin at the same role because stroke density lowers apparent size (`Phlegonlabs presentation-layout-rules.md` §Chinese offset); the display title floor is *lower* for Chinese (40 vs 44 at 1600) because each glyph is wider and titles are shorter (`§Chinese offset`). Vietnamese has the opposite problem — narrow diacritic stacks — so it wants the **leading bump** of the CJK rules without the size bump.

### 2. Colour system construction

**2.1 The token architecture that survived review** (SlideSpeak `skills/*/tokens.json`):

```
ground:  page (warm off-white / white), card, ink (near-black, never #000)
signal:  primary, subtle (the accent and its darker sibling)
support: muted (body-secondary grey), rule (hairline divider)
```

Each style then varies only the values: academic `#F5F1E8 / #0F4C5C`; consulting `#F7F5F2 / #C8102E`; kanagi `#EFEAE2 / #B5402A`; neue-klasse `#FFFFFF / #0066B1`; opex `#FFFFFF / #1F4E79`; pitch `#FAFAF8 / #2563EB`; product `#FFFFFF / #5B21B6`; training `#FFFCF7 / #0F766E`. Note that **all eight are neutral grounds with one saturated signal** — the structural insight is "neutral ground, one signal, greys for everything else", not the specific hexes.

**2.2 Derivation order** (Huashu): sample (brand asset → real image of the subject → cultural context) → converge (2–3 chromatics + one neutral ramp; H ≥60° or L ≥0.3 apart) → argue in one sentence (`design-styles.md:23-62`). The chroma bands: 0.01–0.04 for large grounds, 0.08–0.15 for the brand/accent, 0.15–0.22 for small points, >0.25 only for deliberately synthetic styles (`design-styles.md` §印刷色质感). The reason given is physical: print inks sit inside a narrower gamut, and lower chroma reads as "printed" rather than "screen" (`§印刷色质感`).

**2.3 Proportions.** 60/30/10 ground/surface/accent (`sunbigfly design-specs.md` §C; `vstorm content-infographic/design-principles.md` §Color Usage; anthropics pptx §Color Palettes as "one colour dominates 60–70%, 1–2 supporting, one sharp accent"). At most **2 accents per page** (`sunbigfly`), at most **1 accent per slide** for marketing decks (`vstorm content-presentation/SKILL.md` §Design Principles), and accent may only touch numbers, icons, chips or filled surfaces — never a card edge (`SlideSpeak SKILL-FORMAT.md:113`; anthropics pptx §Avoid).

**2.4 Palette size.** ≤5–6 distinct colours in an infographic (`vstorm design-principles.md` §Maximum Palette); 3 main colours + neutrals for Swiss editorial (`Phlegonlabs styles/style_a.md` §Design Philosophy); 1 primary + 1 secondary + 1 accent + grey (`huashu critique-guide.md` §3). Beyond that, group categories into "Other" or use a single-hue sequential ramp (`vstorm`).

**2.5 Contrast.** Body 4.5:1, large text 3:1 (`huashu content-guidelines.md` §对比度; `vstorm design-principles.md` §Contrast); chart elements 3:1 against neighbours and background (`vstorm`); for a brand accent used in small text, check it against the paper at 4.5:1 (`Taimoorkhan1122_present-now/references/themes.md` §Brand).

**2.6 Accessibility.** Never colour alone — pair with pattern, shape, label or position (`vstorm design-principles.md` §Colorblind-Safe Palettes); red/green never the only differentiator (~8% of men affected); categorical palette: `#4E79A7 #F28E2B #E15759 #76B7B2 #59A14F #EDC948`; sequential `#EFF3FF #BDD7E7 #6BAED6 #3182BD #08519C`; diverging `#B2182B #EF8A62 #FDDBC7 #F7F7F7 #D1E5F0 #67A9CF #2166AC` (`§Colorblind-Safe Palettes`).

**2.7 Cultural context.** The same hue means different things: vermilion vs cola red; indigo vs SaaS blue; matcha vs terminal green; cream paper vs lab white (`huashu design-styles.md` §文化语境速查). For a Vietnamese philosophy deck, the useful axis is "ink-and-paper against temple red/ochre", not "tech blue".

### 3. Grid, margins, spacing, density

**3.1 Canvas and safe area.**

| Source | Canvas | Margins / safe zone | Content box |
|---|---|---|---|
| huashu | 1920×1080 | body padding ~120px in the template example | — |
| SlideSpeak | 1920×1080 | safe 80–128px, usually 96 | 1728×888 at 96 |
| Phlegonlabs | 1600×900 | edges 92–108, top band 96, bottom band 96 | 108→804 = **696px** tall |
| present-now | 1600×900 | 88 top / 120 sides / 96 bottom | **1360×716** |
| sunbigfly | 1280×720 | 40px sides, title y20–70, footer 40 | **1200×580** |
| anthropics pptx | 960×540pt | ≥0.5in | — |

Normalised: a 1920×1080 slide wants **a 96–130px side margin, a ~110px top band, a ~100px bottom band, and a content block roughly 1650×860**. That is a consistent design across four scaling conventions and is the number to enforce in thumbnails.

**3.2 Spacing scale.** 4px unit with [4, 8, 12, 16, 24, 32, 48, 64, 96] (`SlideSpeak tokens.json`) or 8px unit with [8, 16, 24, 32, 48, 64, 96, 128, 192] (`pitch`, `product-marketing`, `training`). 8pt grid with only 8/16/24/32/48/64 is the simplest defensible system (`huashu critique-guide.md:146`). 12-column grid with 24px gutter and 24px margins (`vstorm styles/layouts.json` §grid). Content gaps by relationship: number + annotation 2–4px; sibling cards 16–20px; different topic areas 32–48px; isolated claim 48–80px (`sunbigfly design-specs.md` §间距是情绪变量). Three-tier whitespace must be **monotonic**: micro < meso < macro, or hierarchy collapses (`sunbigfly composition.md` §留白的三个层级).

**3.3 Density budget.** Fill-rate targets on 1280×720: cover 40–55%, section 25–40%, content 60–75%, data 70–80%, closing 35–50% (`sunbigfly design-specs.md` §留白与视觉焦点). Whitespace ≥40% of area, ≥60% for minimalist (`huashu critique-guide.md:151`). Role-level content budget: 1 core + 3–4 supports + 1 visual protagonist (`huashu slide-decks.md` §4); ≤6 primary ideas per slide (`Phlegonlabs presentation-layout-rules.md` §Dense Content Rules); one main claim + 3–5 evidence bullets (`SlideSpeak skills/consulting/SKILL.md` §Density); ≤40 words of visible text for a talk deck (`present-now AUTHORING.md:58`).

These are not contradictory if read as different registers: **a slide's density is a property of its job** (cover / argument / exhibit), not of the deck. SlideSpeak's three-tier `editorial / balanced / data-dense` register, chosen per slide, is the operational synthesis (`layout-fit-model.md` §Prinzipien 4).

**3.4 Layout families and rotation.** 10 gravity-field families (single focus, symmetric, asymmetric 6:4, three-column, primary-secondary, hero-top, mixed grid, L-shape, T-shape, waterfall) with a rule to use 4–6 per deck (`sunbigfly layouts/README.md`); 12 prototypes with ≥5 per 10 slides and never consecutive (`Phlegonlabs layout-prototypes.md` §Diversity Rules); at most 4–5 layouts per deck (`huashu slide-decks.md` §2); 5–12 slide types per style package (`SlideSpeak meta-generator/GENERATOR.md` §Step 5). The synthesis: **4–6 structural archetypes, none repeated on adjacent pages, with the choice driven by content role** (cover / chronology / comparison / metric / thesis / synthesis / closing).

**3.5 Composition devices.** Rule-of-thirds intersections are the strong points (`sunbigfly design-specs.md` §构图锚点); dead centre is the weakest position; Z-path for standard content, F-path for lists, focus-radiating for single claims (`§构图锚点与视觉动线`). Five-layer depth with ≥3 layers active (`§五层景深架构`) — but see the Canva flag below. Asymmetry 40:60 / 55:35 / 43:57 instead of 50:50 (`Phlegonlabs styles/style_a.md` §Layout Rules).

### 4. Diagram and chart selection

**4.1 Choose by the relation the data expresses, not by chart type** (`huashu modules/deck.md` §数据页…): proportion → scaled object or area; change → a curve or timeline; composition → an exploded whole; comparison → left/right opposition; scale → one giant object against a familiar reference. The same rule, stated as a matrix, is the most complete in the cluster (`sunbigfly charts/runtime-chart-rules.md` §2):

| Data feature | Chart | Rule |
|---|---|---|
| Percentage / completion | progress bar / ring | progress bar when several indicators sit side by side |
| Two-item difference | comparison bar | must highlight the gap, not just the values |
| Change over time | sparkline / timeline | sparkline for small trends, timeline for narrative phases |
| Many indicators to scan | metric row | each item's explanation must be short |
| One core metric | KPI card | only if it carries the page's main conclusion |
| Composition | waffle / stacked bar / treemap | treemap when there is hierarchy |
| Multi-dimension capability | radar | only 3–5 dimensions, all genuinely important |
| Rating | rating indicator | must carry a judgement, not decorate |
| Funnel/conversion | funnel | only when stage loss is the point |

Cross-checked against vstorm: bar = categories, line = time, pie ≤5 segments, scatter = correlation; **never 3D, never dual y-axes, never Excel screenshots** (`content-presentation/slide-patterns.md` §Chart / Data; `content-infographic/design-principles.md` §Chart-Specific Principles).

**4.2 Chart craft, counted.** Y-axis starts at zero (`vstorm`); horizontal bars when labels exceed 3 words; sort by value unless natural order; bar gap 40–60% of bar width; ≤3–4 lines per line chart; direct labels over legends; donut with centre total; annotate key points on the line (`vstorm`). At the high-density end: **6–18 y-tick labels**, x labels on every period (14 labels, no thinning below ~16), a value on every bar (10–14), in-chart series labels with CAGR notes, a dashed reference line with a right-edge marker value, an actual/forecast divider with zone labels, annotation callouts with leader lines, and an embedded mini-table beside the chart (`SlideSpeak mckinsey-anatomy.md` §Counted spec). Every chart needs a **title that states the insight**, not the chart type (`vstorm`; `SlideSpeak mckinsey-anatomy.md` §1 action titles).

**4.3 Minimum content contract.** Metric page: value + meaning + baseline/trend. Comparison: objects + dimension + direction (+ a management read). Trend: axis + direction + turning point. Progress: current + target + remainder (`sunbigfly runtime-chart-rules.md` §4). A single number with no baseline is an incomplete slide (`§4`; `vstorm design-principles.md` §Stephen Few: "37%" is worse than "37% (industry average 22%)"; "a number with a trend is 10× more informative than a static number").

**4.4 Diagram types.** Five sub-types with an intended visual character: pyramid (bottom broad, top sharp — hierarchy), flowchart (curves over right angles to imply flow), hub-spoke (one dominant centre, arms of varying weight), layers (depth through colour ramps, inter-layer lines), cycle (nodes on a trajectory, one node marked "current") (`sunbigfly blocks/diagram.md` §子类型的灵动设计思维). Matrix: 2×2 with one **highlighted** quadrant at ~15% accent tint, others at ≤5%, axis labels 12px tracked like instrument plates, and a deliberate asymmetry so the highlight quadrant reads heavier (`blocks/matrix-chart.md` §设计灵魂).

**4.5 Geometry discipline.** For org charts, system maps, process maps, strict tables: preserve the skeleton, use explicit tracks and bounded box sizes, never let text length drive box size, never `align-content: stretch` (`Phlegonlabs geometry-preserve.md`). If labels do not fit, shorten them or split the figure — never compress until proportions mislead (`§Layout Rules`). This is the single most important rule for a philosophy deck's triad/spiral diagrams: the *arrangement* is the argument.

### 5. Image and illustration rules

**5.1 Decide by subject, not by style mood.**

| Subject | Approach | Source |
|---|---|---|
| gradient / abstract / background / texture | AI-generate by default | SlideSpeak `skills/consulting/image-style.md` §Decision Rules |
| architecture / interior / landscape / nature | AI-generate by default | ibid. |
| person / product / building / location / object | ask the user: AI or stock | ibid. |
| concept / scene / situation | ask | ibid. |
| real place, artefact, person, animal | real photograph; never a hand-drawn SVG | huashu `materials.md` §原则 4 |
| abstract relation, system, hierarchy | diagram, not illustration | sunbigfly `blocks/diagram.md` |
| data | the data itself as image, not a decorative icon set | huashu `materials.md` T0 |

**5.2 The honesty test.** Remove the image — if no information is lost, it was decoration (`huashu materials.md` §原则 3). A grey rectangle labelled "image 1200×800" is better than a bad SVG illustration (`huashu content-guidelines.md` §SVG 画 imagery). Never stock "inspiration" imagery (`materials.md` §原则 3).

**5.3 Prompt recipe.** Subject + style + mood + technical spec, with the subject specific enough that "two different artists would produce recognisably similar images" (`vstorm content-image/SKILL.md` §Prompt Structure). Technical: 16:9 hero, 1:1 social, 4:5 portrait, 3:2 blog (`§4`). Negative prompts for the recurring stock clichés: handshakes, headsets, jumping people, charts on laptops, magnifying glasses, lightbulbs, gears, smiling-at-camera (`SlideSpeak consulting/image-style.md` §Negative prompt; `vstorm style-library/editorial.md` §Negative Prompt Elements).

**5.4 Style library characteristics.** Editorial: natural window light, shallow-to-medium depth of field (f/2–f/4 equivalent), 35–85mm, muted desaturated grading, candid framing, subtle grain (`vstorm style-library/editorial.md` §Key Characteristics). Flat illustration: 3–5 colours maximum, no shadows or gradients, geometric simplification, flat or simple isometric perspective, consistent line weight (`style-library/flat-illustration.md` §Key Characteristics). Use flat illustration only where photography would be too heavy and realism is not required.

**5.5 Brand and legal guard.** No brand names, logos, trademarks, identifiable products or named buildings in prompts or stock queries (`SlideSpeak consulting/image-style.md` §Brand-Asset-Constraint; `docs/SKILL-FORMAT.md` §image-style.md). Real logos must be fetched, not invented (`huashu brand-asset-protocol.md`).

**5.6 Consistency across a deck.** One visual language, a different figure per slide — never one reference image as an anchor, which collapses every generated image into the same object (`SlideSpeak CLAUDE.md` §Moodboard step). Keep aspect ratio, colour temperature and lighting direction constant within a series (`vstorm content-image/SKILL.md` §Consistency Across Assets).

**5.7 Every slide needs a visual element** — image, chart, icon or shape (`anthropics pptx/SKILL.md` §For Each Slide). Text-only slides are forgettable; but "visual element" includes a rule, a number, or a typographic gesture, not only a picture.

### 6. Anti-AI-slop rules

**6.1 The canonical default clusters** (`anthropics frontend-design.md` §Process; reproduced in `huashu content-guidelines.md` §2026 年的 AI 默认外观):

1. cream ground `#F4F1EA` + high-contrast serif + terracotta accent `#D97757`;
2. near-black ground + one acid-green or vermilion accent;
3. broadsheet: hairline rules, zero radius, dense columns;
4. SaaS card kit: identical rounded cards, one radius, one soft shadow `rgba(0,0,0,.1)`, gradient washes;
5. template chrome: tracked all-caps eyebrow above every heading, "A · B · C" mid-dot meta, "WORD — fragment" labels, `#0B0B0B`/`#111` instead of black, monospace micro-labels, "→" appended to links.

**6.2 The typographic tells** — accenting one word in a headline; all caps for labels; labels above content that carry no information (`frontend-design.md` §Process). Huashu adds: numbering `01/02/03` when the content is not a sequence (`content-guidelines.md` §5).

**6.3 The deck-level tells** — accent lines under titles; decorative colour bars / edge stripes / single-side borders; centred body text; 5+ bullets; "Let's dive in"; an agenda slide; "Questions?" as the last slide; a "Thank you" slide; a wall of text; orphan slides (`anthropics pptx/SKILL.md` §Avoid; `vstorm content-presentation/SKILL.md` §Anti-Slop Rules for Slides).

**6.4 The content tells** — a curated string list (openers, fillers, transitions, metaphors, vocabulary, closers) with per-item fixes (`vstorm slop-detector.md` §Categories 1–9), scored −8/−5 critical, −3/−2 warning, −1/−0.5 info, floor 0 (`scoring.md` §Anti-Slop Score). **Em-dash rate >2 per 500 words** is a warning (`slop-detector.md` §Category 7); SlideSpeak bans em dashes in rendered copy outright (`SKILL-FORMAT.md:114`). Fake precision (`73%`, `4.2x`, `$12.4M`, `10,000+`) is banned unless sourced or marked illustrative (`anti-slop-adoption.md` §2).

**6.5 The structural tells** — paragraph-length uniformity (>60% within 15% of the mean), sentence-length monotony (std-dev <4), the three-point pattern (every section has exactly three sub-points), listicle flatness, symmetrical sections (`slop-detector.md` §Category 6). These are detectable mechanically, which is why they matter.

**6.6 The restraint rules** — spend boldness in one place; one detail at 120%, the rest at 80%; remove one accessory (`huashu content-guidelines.md` §正向做什么; `frontend-design.md` §Restraint and self-critique). Every decoration must answer "if I remove this, does the viewer lose information?" (`vstorm design-principles.md` §Data-Ink Ratio; `huashu critique-guide.md` §4).

**6.7 The positive replacement rules** — structure must encode information (outlines, borders, numbering, eyebrows only when they mean something) (`frontend-design.md` §Design principles); at least three drawn graphic constructs per style, and never blobs, squiggles, Memphis confetti, corner swooshes or generic network meshes as filler (`SlideSpeak SKILL-FORMAT.md:116`).

### 7. Render-then-inspect QA loops

**7.1 The trust ladder.** Never trust a thumbnail as a render. On macOS: `qlmanage -t` is unreliable (it passed four real overlap bugs); LibreOffice headless is layout-faithful but may drop CJK fonts wholesale; Keynote→PDF is trustworthy; the target application is final. Always render a known-good control file through the same tool to separate tool defects from product defects (`huashu verification.md` §第 0 条).

**7.2 The three-pass scan** (per page, from the screenshot): (1) border patrol — four corners, four edges, footer band, looking for clipping and elements within <30px of the frame; (2) depth scan — title zone, focus zone, support zone, overlap/stacking, image integrity (`object-fit`), decoration layer order; (3) whole-page impression — the one-second focus test ("close your eyes, open them: is the first thing you see the most important thing?"), the "bare concrete" test ("does this look like a designed deck or a default HTML page?"), style consistency, and difference from the previous page (`sunbigfly page-review-playbook.md` §Part A).

**7.3 Severity and gates.** P0 blocks the page: clipped content, `scale()` hacks, >40% empty canvas, unreadable core text, a missing planned card, severe overlap, pixel clipping from `box-sizing`, broken/distorted images. P1 must be fixed: truncated text, uneven gaps, decoration above text, no focal point, hard-coded colours, data numbers the same size as body, line-height <1.4, and the design-independence failure (three pages sharing one grid). P2 is polish (`§Part B`).

**7.4 Round discipline.** Minimum two rounds; the first round may **never** finalise; archive each round's screenshots; from round two read only the newest image and tick off the previous report item by item; if the same P0/P1 survives two rounds, stop fixing CSS and **roll back to planning**, changing at least one of density/layout/allocation (`§Part E`). "I changed the CSS so it should be fine" is explicitly not evidence (`§闭环承诺`).

**7.5 Mechanical checks that a human eye cannot fake.** Text diff after whitespace normalisation must be identical, and element counts per page must match (`huashu verification.md` §第 0 条). Placeholder grep: `\bx{3,}\b|lorem|ipsum|\bTODO|\[insert|this.*(page|slide).*layout` (`anthropics pptx/SKILL.md` §Content QA). Occupancy measure: flag slides with large empty bands and hollow cells, and fix by re-templating, never by stretching (`SlideSpeak CLAUDE.md`).

**7.6 Visual QA must be done on images, fresh.** "After staring at the generating code you tend to see what you expect rather than what rendered" — inspect every rendered page, and check **text overflow first**, because it is the most common and most visible defect (`anthropics pptx/SKILL.md` §Visual QA).

**7.7 The rubric that closes the loop.** A deck ships at **≥85/100 with no category below 60% of its weight** across narrative, style fit, brand fidelity, hierarchy, readability, data clarity, pacing and delivery readiness (`Phlegonlabs presentation-quality-rubric.md`). Hard fails override the score.

### 8. Rules that are renderer-specific and cannot be executed through Canva's editing ops

| Rule family | Why it is HTML/PPTX-only | What Canva can actually do |
|---|---|---|
| Font family, pairing, fallback chains, `font-synthesis`, `font-size-adjust` | `format_text` has **no font-family** parameter | Choose a `create-design` brief/template whose fonts are right; never restyle family afterwards |
| Letter-spacing / tracking, `text-transform: uppercase`, `text-wrap: balance`, hyphenation, `text-spacing-trim`, `hanging-punctuation`, `vertical-rl` | No such properties exist in any editing op | Line breaks are whatever the box produces; use `replace_text` with explicit short lines where a break matters |
| `clamp()`, `vw/vh`, responsive layout, container queries | Static 1920×1080 canvas | — |
| Background colour, paper texture, grain, fold marks, `background_mode` paper/white | No background-change op; `update_fill` targets existing elements | Choose the page background at generation time; cover unwanted decoration with an inserted opaque fill (which sits *above* existing elements) |
| Adding text boxes, labels, callouts, footnotes, source bars | **No new text box op** | Only `replace_text` within existing boxes; a footnote must already exist in the template |
| Creating shapes, arrows, connectors, charts, diagrams, icons | No shape or chart creation op | Upload a rendered image (`create-upload-url`) or reuse existing shapes via `position_element`/`resize_element` |
| Shadows, gradients, blur, `clip-path`, `mask-image`, blend modes, multi-layer z-depth | Not expressible | Template decides; `insert_fill` is the only layering tool and it lands on top |
| Overflow/occupancy measurement, contrast measurement, DOM assertions, automated lint | No DOM, no computed styles | Per-page thumbnail inside an editing transaction + eyes + checklist |
| `@page`, print CSS, PDF page ranges, `beforeprint` | Canva exports its own PDF | `export-design` with a chosen format |
| Speaker notes authoring | `get-presenter-notes` is read-only | Ship notes as a side artifact keyed to slide numbers |
| localStorage playback position, keyboard navigation, presenter window, step reveals | Canva's own player | Use Canva's presentation mode |
| Per-element `data-*` instrumentation for richness/occupancy gates | No DOM | Convert gates into a visual checklist |

**Rules that survive unchanged** — worth stating explicitly, because they are the majority of what matters: type *sizes* (via `format_text` font_size), weight, italic, alignment, text colour, line-height, list level/marker; all colour-system logic (via `update_fill` and text colour); all composition and density *decisions* (they determine what you ask `create-design` for); all content rules (one idea per page, action titles, banned patterns, slop strings); all imagery rules (generation prompts, upload decisions); and the entire QA *discipline*, expressed as a thumbnail checklist rather than a measurement harness.
