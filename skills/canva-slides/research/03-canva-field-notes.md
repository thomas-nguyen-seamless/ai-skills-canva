# 03 — Canva Field Notes, Practitioner Skills & Verified Quirks

Reader: `CanvaFieldNotes`. Scope: ten repos under `/tmp/skills-src`, with emphasis on
(a) real-world Canva-MCP testing notes (`rifaterdemsahin_canva-mcp`, 105 md files read),
(b) the Vietnamese lesson-designer skill (`canva-ppt-lesson-designer`),
(c) mid-size Canva/design skills, and (d) a dedicated catalogue of every concrete
MCP quirk, limit, error and workaround these sources evidence.

Citation convention: every path is relative to `/tmp/skills-src`. Line numbers are given
where a claim is line-precise. "Our verified list" refers to the facts the author already
confirmed live (V1–V17, defined in the quirks catalogue preamble).

---

## Inventory

| Skill / package | Repo path | License (plain fact) | What it is, in one sentence | Verdict |
|---|---|---|---|---|
| `rifaterdemsahin_canva-mcp` (field notes) | `rifaterdemsahin_canva-mcp/` | MIT (declared in `README.md` "## License → MIT"; no LICENSE file at root; `rifaterdemsahin_canva-mcp/5_Symbols/lower-third-text/LICENSE.md` is Canva's own proprietary Apps-SDK licence) | A 7-stage "delivery pilot" repo whose 105 markdown files are a running lab notebook of building Canva decks through the claude.ai Canva MCP, including capability scans, end-to-end flow docs and retrospectives. | **A** — the single richest source of verified MCP behaviour and failure modes; noisy scaffolding around it, but every Canva claim is dated and evidenced with a design ID. |
| `canva-ppt-lesson-designer` | `nguyenduysphk3407051993_OPENCLAW_SKILL/canva-ppt-lesson-designer/` | NO-LICENSE (repo has no LICENSE file) | A Vietnamese KHTN lesson-deck designer that is explicitly Canva-first: brand kit → outline → generate → refine via editing transaction → export, with a per-slide 8-field output contract, a lesson map per grade, and an anti-pattern catalogue. | **A** — the best match to our user's actual context (Vietnamese classroom, projection legibility, doctrinal correctness); its Canva workflow section is the most accurate MCP procedure in the whole cluster. |
| `canva-prompt-creator` | `nguyenduysphk3407051993_OPENCLAW_SKILL/canva-prompt-creator/` | NO-LICENSE | Companion advisor that turns a lesson topic into Canva search keywords, Magic Media prompts, font/colour/layout advice — no MCP calls at all. | **B** — no tooling, but the "1-6-6" density rule, Vietnamese-safe font list and per-subject palettes are directly reusable in a planning phase. |
| `canva-workspace` (Xpert AI Canva plugin) | `xpert-ai_xpert-plugins/agent-plugins/canva/` | AGPL-3.0 (`package.json` `"license": "AGPL-3.0"`) | A packaging exercise that binds the official remote server `https://mcp.canva.com/mcp` to a workspace-level shared connector, plus a very short skill. | **C** — the skill is three paragraphs; the value is the OAuth/scope reconnaissance in `README.md`, which is the most precise auth description in the cluster. |
| `canva-master` | `GPire_claude-skills-swarm/canva-master/SKILL.md` | MIT claimed (`README.md` badge "MIT license"; **no LICENSE file in repo**) | An Italian "Canva Master Agent — Livello Fable 5" mega-prompt: platform dimension table, visual-hierarchy golden rules, brand-kit structure, YouTube-thumbnail formula, export settings. | **C** — a prompt persona, not a procedure: it never touches MCP schemas, lists no failure modes, and its workflow is the legacy `search-designs → generate-design` path. |
| `canva-2` | `LeoYeAI_agent-master-skills/skills/canva-2/` | NO-LICENSE (skill `_meta.json` points at `openclaw/skills`; no license declared) | An auto-generated reference card for 22 Canva MCP tools, each with parameter tables and the tool's own prompt text. | **C** (thin wrapper — one line: it is a tool-schema dump with zero judgment) but **keep**: it is the only source that records `user_intent` being effectively mandatory and quotes the tools' own guardrail text. |
| `pitchdeck-pro` | `rbld56_pitchdeck-pro/` | MIT (declared in `README.md`) | An HTML-first pitch-deck generator (fixed 1920×1080) with 15 style presets, 16 slide archetypes, a browser-only deck reviewer, and an optional Canva/AI-graphics path. | **A−** for deck craft: hard numeric typography and density rules, a scoring rubric, and the 2026 anti-AI-slop catalogue; the Canva part is a thin export/graphics channel. |
| `canva-creator` (+ `brand-style`) | `anthropics_knowledge-work-plugins/small-business/skills/canva-creator/`, `.../brand-style/` | NO-LICENSE at repo root (no LICENSE file anywhere at root; individual `bio-research/skills/*/LICENSE.txt` exist for other skills only) | A campaign executor: brief → calendar → slot-level asset inventory → Canva designs → copy → HubSpot staging, with the best failure-mode documentation ("gotchas") in the cluster. | **A** for the gotchas file; the workflow itself is social-post shaped, not deck shaped. |
| `carousel-builder` | `charlesdove977_carousel-builder/` | MIT (`plugin.json` `"license": "MIT"`) | Template-duplication pipeline: generate images elsewhere, then `copy-design` a fixed 8-page Canva template and swap text spans and image fills in place. | **A** for edit mechanics — it documents run-level formatting preservation and frame-effect preservation better than anything else here. |
| `design-pack` | `m-binimran_design-pack/` | MIT claimed (`README.md` "MIT - see LICENSE"; **no LICENSE file present**) | A connector-first design ops pack: rules (design quality, brand consistency, accessibility, truth-telling, licensing), hooks, review agents, and a compact `canva-design` skill. | **B** — mostly generic craft rules, but the truth-telling rule, the WCAG numbers and the design-critic report format transfer directly. |
| `oma-slide` | `first-fluke_oh-my-agent/skills/oma-slide/` | MIT (`plugin.json`, `.claude-plugin/plugin.json`) | An HTML-deck skill with a deterministic CLI: 1920×1080 fixed stage, anti-AI-slop doctrine, density modes, a geometry validator, and an *optional* Canva import/export channel. | **B+** — the Canva channel is deliberately minimal and honest; the typography/atmosphere doctrine and the "incomplete transfer is a failure" rule are worth taking. |
| Adjacent, non-slide (checked, not Canva) | `nguyenduysphk3407051993_OPENCLAW_SKILL/stem-lesson-creator/`, `.../ke-hoach-day-hoc/` | NO-LICENSE | Word (.docx) lesson-plan generators for Vietnamese STEM/KHBD paperwork. | **D** for our purpose — no slides, no Canva; only their shared "challenge-before-acting" interaction contract is transferable (see merge table). |

---

## Skill: rifaterdemsahin_canva-mcp (real-world MCP field notebook)

### Purpose
Not a skill but a lab notebook: 105 markdown files organised as a 7-stage delivery
framework, documenting eight concrete attempts to produce Canva decks from an agent
session — lower-third text, a 5-slide architecture deck, a glossary grid page, a
voiceover-to-deck API, a 100-badge grid, and a comic-panel narrative deck. Its value is
that every claim is bound to a design ID, a job ID, an element coordinate or an
`updated_at` timestamp.

### Prescribed process (as executed)
1. **Capability scan before planning.** Re-pull the live tool schemas instead of trusting
 the previous session's matrix (`rifaterdemsahin_canva-mcp/4_Formula/llm_thinking_log.md`, 2026-07-12 SPEC-016 entry:
 "Re-pulled the live tool schemas … rather than trusting the SPEC-015 matrix from memory").
2. **Write the spec and surface the gap to the user with 2–3 options** before any write call
 (`rifaterdemsahin_canva-mcp/4_Formula/architecture_course_mcp_spec.md`, "Resolution — Chosen Approach").
3. **Outline → generate → screen candidates.** `request-outline-review` (user approves in a
 widget) → `generate-design-structured` (4 candidates) → `create-design-from-candidate`.
4. **Select the candidate by page count**, not by vibe: "candidate 1 was selected as it
 matched the 5-slide spec exactly (other candidates had 6 thumbnails, implying an extra
 AI-inserted slide)" (`rifaterdemsahin_canva-mcp/4_Formula/architecture_course_mcp_spec.md`, Delivery Notes).
5. **Open a transaction, locate elements by text content, batch the formatting ops, commit.**
6. **Verify persistence with `updated_at` > `created_at`** and render every page thumbnail to
 the user (`rifaterdemsahin_canva-mcp/7_Testing_Known/architecture_course_shape_deck_flow.md`, Step 7).
7. **Screen candidate *content*, not thumbnails**, before showing options — call
 `get-design-content` on each converted candidate and look for duplicates, garbling and
 wrong templates (`rifaterdemsahin_canva-mcp/7_Testing_Known/glossary_grid_flow.md`, Attempt 3 screening table).
8. **Fix one bad label in place** rather than regenerating: `start-editing-transaction` →
 `replace_text` on the specific `element_id` from `richtexts` → show draft link → user
 approves → `commit-editing-transaction` (`rifaterdemsahin_canva-mcp/7_Testing_Known/glossary_grid_flow.md`, "Fix").
9. **Match canvas before merging:** `resize-design {type: custom, width: 1920, height: 1080}`
 then `merge-designs {type: modify_existing_design, operations: [{type: insert_pages,
 after_page_number: N}]}` (`rifaterdemsahin_canva-mcp/4_Formula/specs.md` SPEC-019 Key Behaviors).
10. **Record the run** (prompt, tool chain, coordinates, verdict) in `prompts.md`,
 `llm_thinking_log.md`, `logic.md`, and a flow doc under `rifaterdemsahin_canva-mcp/7_Testing_Known/`.

### Concrete rules and thresholds (with sources)
- **Lower-third formula on a 1920×1080 page:** `width = pageWidth × 0.6` → **1152**;
 `left = (pageWidth − width)/2` → **384**; `top = pageHeight − 150` → **930**
 (`rifaterdemsahin_canva-mcp/4_Formula/lower_third_mcp_spec.md`, "Lower-third formula (1920×1080 page)").
- **Header size used in a real 1920×1080 deck:** 28 px bold, per-slide accent hex
 (`rifaterdemsahin_canva-mcp/4_Formula/architecture_course_mcp_spec.md`, Target Slide Map). *Note: this is the one
 number in the cluster that conflicts with our classroom-legibility finding — see
 Contradictions #3.*
- **Generation latency grows with slide count:** the 8-slide "balanced" generation timed
 out on the first call and succeeded on retry; the tool itself warns that extra slides add
 latency (`rifaterdemsahin_canva-mcp/7_Testing_Known/coordinator_subagents_comic_flow.md`, tool chain).
- **Batch, then verify counts:** one `perform-editing-operations` call carrying 4–5 ops
 returned `status: success` for all of them; results are in `edit_operation_results`
 (`rifaterdemsahin_canva-mcp/4_Formula/lower_third_mcp_spec.md`, test table).
- **Apps-SDK shape limits** (the only true native-shape path, not used by the deck itself):
 1–30 paths per shape, combined path data ≤ 2 KB, ≤ 6 unique fill colours, every path must
 begin with a single `M`, `Q` commands not allowed
 (`rifaterdemsahin_canva-mcp/2_Environment/canva_capability_research.md`, section 2).
- **One raster per object when you need things to move together:** PPTX `p:grpSp` groups are
 flattened on import, so the retry baked circle+numeral into one PNG per badge and imported
 100 pictures (`rifaterdemsahin_canva-mcp/6_Semblance/workarounds.md` #1; `rifaterdemsahin_canva-mcp/7_Testing_Known/numbers_1_100_grouped_flow.md`).

### Unique ideas not found elsewhere
- **Capability boundaries are per-surface *and* per-session** — the same task that failed on
 the REST API + Apps SDK succeeded later on the MCP connector, so re-derive the matrix rather
 than declaring impossibility (`rifaterdemsahin_canva-mcp/6_Semblance/lessons_learned.md`, lower-third retrospective).
- **Don't fight the generated grid.** "AI-generated layouts commit to their own
 left-text/right-graphic grid; fighting that grid with `position_element` … risks overlapping
 the artwork … Text alignment is the safer lever" (`rifaterdemsahin_canva-mcp/6_Semblance/lessons_learned.md`).
- **Page names do not exist.** "Canva pages have no MCP-settable 'name'/'label' field — only
 index + thumbnail", so slide names live in project docs
 (`rifaterdemsahin_canva-mcp/6_Semblance/lessons_learned.md`; `rifaterdemsahin_canva-mcp/4_Formula/canva_pages_table_recipe.md` Step 4).
- **A candidate URL opened in a browser materialises as a real design** in the account
 (`rifaterdemsahin_canva-mcp/7_Testing_Known/canva_design_DAHPLiS4suo_steps.md`, Step 5) — useful to know, and a trap
 if you open candidates casually.
- **AI artwork provenance is testable:** compare `created_at` against the generation window,
 opaque batch filenames, `smart_tags`, and asset owner via `get-assets`
 (`rifaterdemsahin_canva-mcp/7_Testing_Known/coordinator_subagents_comic_flow.md`, evidence table).

### Pitfalls and failure modes it warns about
- `design_generation_error` when the prompt is over-constrained with negative constraints
 (`rifaterdemsahin_canva-mcp/7_Testing_Known/glossary_grid_flow.md`, Attempt 2).
- `infographic` as a design type has a "strong template prior toward narrative/stats layouts"
 and will invent fake statistics rather than render your literal list (same file, Attempt 1).
- `poster` works for literal grids but is "ambiguous with event-poster templates" — one of four
 candidates came back as a registration poster (same file, Attempt 3).
- Opening candidates casually creates designs you didn't intend to keep
 (`rifaterdemsahin_canva-mcp/7_Testing_Known/canva_design_DAHPLiS4suo_steps.md`).
- A write-only token makes success look like failure: creation returns 200 while listing
 returns 403 `missing_scope` (`rifaterdemsahin_canva-mcp/6_Semblance/canva_document_visibility.md`, root causes 1–3).
- API-created designs do not appear in the Canva home "Recents" rail; they live under Projects
 (same file, cause #1).

### Outdated / wrong / impossible against our MCP
- Tool names throughout are the **older connector generation**:
 `request-outline-review`, `generate-design-structured`, `create-design-from-candidate`,
 `create-design-from-brand-template`. Our server exposes `create-design` +
 `get-create-design-async-job` instead; `request-outline-review` **does not exist**, so the
 outline-approval widget must be replaced by an in-chat confirmation gate.
- `upload-asset-from-url` / `insert_fill` are used as image plumbing; our account can still do
 this, but note their own finding that `insert_fill` accepts media only, never shapes
 (`rifaterdemsahin_canva-mcp/4_Formula/architecture_course_mcp_spec.md`, Capability Scan).
- The whole Apps-SDK/Developer-Portal branch (`rifaterdemsahin_canva-mcp/5_Symbols/lower-third-text/`,
 `rifaterdemsahin_canva-mcp/4_Formula/architecture_components_app_spec.md`) is out of scope for a pure-MCP skill: it
 requires a human to run a dev server and click buttons inside the editor.
- `create_design` via `POST /rest/v1/designs` creates a blank design only — it has no
 outline/AI content (`rifaterdemsahin_canva-mcp/4_Formula/voiceover_presentation_api_spec.md`, Capability Scan).

---

## Skill: canva-ppt-lesson-designer (deep analysis — Vietnamese education)

### Purpose
Produce a complete Vietnamese classroom deck (KHTN / Vật lý / Hoá / Sinh, GDPT 2018) as a
planning document first and a Canva design second, with fixed brand colours, fixed font
roles, a 6-layout system, per-slide image/icon/shape keyword sets, and an export step.
Everything is authored in Vietnamese; English is reserved for search keywords.

### Prescribed process
1. **Challenge vague requests before acting** (`SKILL.md`, "Khi yêu cầu chưa đủ cụ thể"):
 mandatory criteria are *môn · lớp · bài/chủ đề · số slide · thời lượng tiết · phong cách*;
 missing **2 or more** → must push back with a pre-filled sample prompt; missing **exactly 1**
 → pick a sensible default, continue, and state it.
2. **Choose a design system** from eight (Editorial Minimalist … EduTechND Earth Dark);
 default to Academic Editorial (university/THPT) or EduTechND Earth (THCS KHTN).
3. **Derive slide count from class time** (`SKILL.md:105-107`): 20–30 min → 6–8 slides;
 35–45 min → 8–12; 60 min+ → 12–18.
4. **Fix the pedagogical spine** (`SKILL.md`, step 3): opener → learning objectives → prior
 knowledge → content group → example/practice → summary → closing/assignment.
5. **Write each slide through an 8-field contract** (`SKILL.md`, step 4 and
 `references/slide-output-contract.md` PART B): slide purpose · main content · proposed
 layout · image keywords · video suggestion · colour & font · interaction · teacher notes.
6. **Resolve content against a lesson map, not from the model's memory**
 (`references/maps/README.md`): find Chương → Bài in `MAP_<MÔN><LỚP>.md`, take `Đơn vị KT`
 as the content outline, `Trọng tâm` for emphasis, `Liên hệ` for the opener, `Visual` for
 keywords, `Accent` for the subject colour.
7. **Build in Canva in this order** (`references/canva-workflow.md` §1–6):
 `list-brand-kits` → `search-brand-templates` / `create-design-from-brand-template`
 **or** `request-outline-review` → `generate-design-structured` (with `brand_kit_id`,
 `asset_ids`) → `upload-asset-from-url` for user images →
 `start-editing-transaction` → `perform-editing-operations` → `commit-editing-transaction`
 → `get-export-formats` → `export-design` (pptx/pdf) → hand the download URL to the user.
8. **QA against the checklist before delivery** (`references/slide-design-framework.md` §7):
 background hex, cream text, correct font set, accent < 10 %, one knowledge unit per slide,
 no overflow, one icon per slide, Vietnamese diacritics rendered, file produced only by
 `export-design`.
9. **Export, never synthesise.** "TUYỆT ĐỐI KHÔNG dựng .pptx bằng python-pptx hay bất kỳ code
 nào" — the .pptx is only ever a Canva export (`references/canva-workflow.md` §0, §7).

### Concrete rules and thresholds
| Rule | Value | Source |
|---|---|---|
| Default canvas | 16:9 `13.333" × 7.5"`; EduTechND Earth uses `20" × 11.25"` | `SKILL.md`, "Slide canvas" |
| Margin | ≥ 0.5" per side (EduTechND ≥ 0.8", gap 0.5") | `SKILL.md`; `references/styles/edutechnd-earth-dark.md` "Do" |
| Typography hierarchy (default) | Title 36–54 pt bold · Section 22–28 pt bold · Body 14–18 pt regular · Caption 10–12 pt | `SKILL.md`, "Phan cap typography" |
| Typography hierarchy (EduTechND, 20" canvas) | Section 63–95 pt · Title 44–72 pt · Sub-heading 40–46 pt · Body 36 pt · Caption 24–28 pt · Footnote 18 pt | `references/styles/edutechnd-earth-dark.md`, "Font sizes" |
| Size ratio between tiers | **≥ 1.3×** | `SKILL.md`; style file "Quy tắc vàng" |
| Minimum projection size | **24 pt** (hard rule) | `SKILL.md:159`; `references/slide-design-framework.md:22` |
| Max tiers of type per slide | 4 | style file, "Phân cấp chính — phụ" |
| Content per slide | one main idea; **≤ 6–7 lines**; each idea **≤ ~14 words** | `SKILL.md` "Quy tac noi dung"; `references/slide-output-contract.md` PART B |
| Colour roles | dominant 60–70 % · supporting 1–2 tones · accent 1 colour **< 10 % of area**, one accent point per slide | `SKILL.md`; `references/slide-design-framework.md` §1 |
| EduTechND palette | bg `#4B2E2B`, panel `#8C5A3C`, ink `#FFF8F0`; accents Vật lý `#D98E48`, Hoá `#6FA89C`, Sinh `#8FAE5D`, chung `#C08552` | `assets/brand-standard.json`; `references/slide-design-framework.md` §1 |
| Second EduTechND palette set (ANKENE reference) | `#3F2313`, `#D7A550`, `#D28119`, `#FCFBF9`, `#F2F3EC`, `#75502C`, `#6A4115` | `references/styles/edutechnd-earth-dark.md`, "Palette" |
| Font selection by string length | titles: ≤25 → `#9Slide01 Tieu de ngan`, ≤45 → `#9Slide02 Tieu de dai`, >45 → `#9Slide02 Tieu de rat dai 01`; body: ≤40 / ≤90 / >90 chars | `assets/brand-standard.json` → `font_rules` |
| Layout templates | 6 (Cover, Single Concept, Process, Comparison, Big Number, Quote) — a 6–14-slide deck should use 5–6 of them | `references/slide-design-framework.md` §3 |
| Keywords | ≥ 5 English keyword clusters per slide, 2–6 words each; never "beautiful image"/"nice video" | `SKILL.md` "Quy tac tu khoa"; `references/keyword-expansion-framework.md` §4 |
| Per-slide keyword groups | image **+** icon **+** shape — all three mandatory | `references/slide-output-contract.md` PART B |
| Vietnamese specifics | headings never in English; diacritics must render; body left-aligned only (centre only for title/big number/conclusion) | `SKILL.md` top matter; `references/anti-patterns.md` "Canh giua doan van" |

### Unique ideas not found elsewhere
- **Brand kit as the only font-delivery mechanism.** Because MCP cannot set a font family, the
 skill makes the 9Slide font set a *precondition inside the Brand Kit / Brand Template*
 (`references/canva-workflow.md:14`, `:78`). This is the correct architectural answer for a
 font-family-less API, and no other source states it as a hard rule.
- **A local lesson map with a stable schema** (`references/lesson-map-format.md`): per-Bài
 blocks of `Đơn vị KT / Trọng tâm / Liên hệ / Visual / Accent / Slide gợi ý`, plus a rule that
 the map is a living document the agent extends when it finds a missing unit (§5). This is the
 cheapest hallucination control I saw in the whole cluster for school content.
- **A machine-readable per-slide contract** with fixed Vietnamese labels so output can be
 parsed and re-checked (`references/slide-output-contract.md`), plus a PART C acceptance
 checklist including "each slide's main content must be traceable to a `Đơn vị KT`".
- **Anti-pattern catalogue written for a specific design system**, including the honest
 admission that an accent rule line under every title is "the single most recognisable sign
 of an AI slide" (`references/anti-patterns.md`, Category 1).
- **Component-level typography doctrine**: "sans cứng → serif trang nghiêm → sans mềm → sans
 nhẹ" as a four-tier personality ladder, with the rule that bolding all body text means
 nothing is emphasised (style file §2–§3).

### Pitfalls it warns about
- Reporting "done" before `commit-editing-transaction`: "Chưa commit là CHƯA lưu — không báo
 'đã xong' trước khi commit thành công" (`references/canva-workflow.md` §4).
- Promising a font change via API (`§7`).
- Building .pptx with code (§7).
- Calling generation before outline approval (§7).
- Light background when the system demands dark; replacing 9Slide with Calibri/Cambria/Arial;
 accent flooding > 10 % (`references/anti-patterns.md`, "LOI 1–5b").
- Text overflow: fix by −2 pt, splitting the slide, or widening the box — "never publish with
 overflow" (`references/anti-patterns.md`, Category 5).

### Outdated / impossible against our MCP
- `request-outline-review`, `generate-design-structured` and `create-design-from-candidate` do
 not exist on our server (same substitution as above); the equivalent is `create-design` with
 `outline.sections[]` + polling.
- The skill assumes a **brand kit already exists** (`brand_kit_id_hint: kAHLq3RErqs` in
 `assets/brand-standard.json`) and a Canva **Pro** plan for custom fonts. Our account has zero
 brand kits and zero brand templates, so the whole "brand kit delivers the font" mechanism is
 unavailable until a kit is created — the skill has no fallback for that case (see Gaps).
- `assets/palettes.json` still contains python-pptx `RGBColor` instructions and per-system
 `title_size_pt`/`body_size_pt` fields — leftovers of the removed python-pptx generator.
- `references/styles/edutechnd-earth-dark.md` is full of `python-pptx` snippets
 (`Inches`, `MSO_SHAPE`, `add_shape`) that contradict the skill's own "no code" rule; treat
 them as geometry/colour reference only.

---

## Skill: canva-prompt-creator (Vietnamese keyword & design advisor)

### Purpose
Give Vietnamese teachers the vocabulary and design judgement to search Canva and write Magic
Media prompts — no MCP calls, no file output beyond an answer shaped by a fixed template.

### Process
1. Classify the request: `template` / `element` / `magic-media` / `design-advice` / `all`.
2. Identify subject (Physics/Chemistry/Biology/KHTN), grade band (6–12) and slide purpose
 (lecture, revision, experiment, assessment, observed/open lesson).
3. Recommend one of 4 font combos, one of 6 layout patterns, and a subject palette.
4. Produce keywords in three tiers (general → styled → specific) for templates, and by asset
 type (illustrations, diagrams, icons, backgrounds, frames, stickers, charts) for elements.
5. Produce 3–4 Magic Media prompt variants using
 `[style], [subject doing action], [environment], [lighting], [colour scheme], [mood], [composition]`.
6. Output in a fixed Vietnamese guide format with sizes, palette, fonts, layouts, keywords,
 prompts and tips.

### Concrete rules and thresholds
- **"Quy tắc 1-6-6":** 1 main idea per slide, **max 6 lines**, **max 6 words per line**.
- Font sizes: heading 36–44 pt bold; subheading 24–28 pt semibold; body 18–22 pt regular —
 "KHÔNG nhỏ hơn 18pt trên slide"; caption 12–14 pt; **max 2 font families per slide**.
- Vietnamese-safe font families: Montserrat, Open Sans, Roboto, Nunito, Inter.
- Margins 10–15 % per side; element gap ≥ 20 px; 3–4 colours maximum.
- Sizes table: lecture slide 1920×1080 (16:9); legacy projector 1024×768; A4 worksheet;
 infographic 800×2000; A2 poster; Google Classroom banner 1000×250.
- Magic Media prompt: 15–40 English words, no negations, add `isolated on white background` or
 `seamless pattern` when needed.
- Subject palettes are fully enumerated (e.g. Physics `#1E40AF / #06B6D4 / #F59E0B / #64748B`).

### Unique / pitfalls
- The **challenge-before-acting** contract is shared across this author's whole skill family
 (also `stem-lesson-creator/SKILL.md`, `ke-hoach-day-hoc/SKILL.md`): missing ≥ 2 mandatory
 criteria ⇒ push back with a filled-in template; missing exactly 1 ⇒ choose and state. This is
 the cleanest anti-guessing interaction pattern in the cluster and is directly reusable.
- Warns that a "beautiful slide" request must be converted into subject/lesson/grade/purpose
 before doing anything.
- No pitfalls about MCP at all — it never touches the API.

### Outdated / wrong / impossible
- It advises Magic Media/Magic Resize/Magic Animate as if they were agent-callable; they are
 editor-only. Also assumes Canva Pro features.
- Font advice is unusable through MCP (no font-family operation), so it must be reframed as
 "choose once in the template/brand kit, then never change via API".

---

## Skill: canva-workspace (Xpert AI connector packaging)

### Purpose
Bind the official remote Canva server into a workspace shared connector and give the agent a
minimal operating contract. Three paragraphs of skill; the reconnaissance is in the README.

### Process
1. Verify the endpoint is `https://mcp.canva.com/mcp` (streamable HTTP, OAuth 2.0).
2. Read tools only when the live schema lists them — "Call a tool only when the live schema
 lists it" (`skills/canva-workspace/SKILL.md`).
3. Treat every write (`generate-design`, `create-design`, … `export-design`) as requiring an
 explicit user request plus host approval; "Search or read before proposing a change."
4. Include the design link whenever a tool returns one.
5. Report provider errors honestly; never claim a write succeeded without a successful result.

### Verified auth facts (the real value)
- Unauthenticated `initialize` → **401**, and `WWW-Authenticate` names protected-resource
 metadata `https://mcp.canva.com/.well-known/oauth-protected-resource/mcp`
 (`README.md`, "Connector setup", checked 2026-10-10).
- `/.well-known/oauth-authorization-server/mcp` returns **404**; use the issuer document
 `https://mcp.canva.com/.well-known/oauth-authorization-server`.
- PKCE **S256** advertised; token-endpoint auth methods `none`, `client_secret_basic`,
 `client_secret_post`; registration endpoint `https://mcp.canva.com/register`.
- `scopes_supported` list (no smaller required subset is published): `profile:read`,
 `design:meta:read`, `design:content:write`, `design:content:read`, `folder:read`,
 `folder:write`, `brandtemplate:content:read`, `brandtemplate:meta:read`,
 `brandtemplate:content:write`, `comment:write`, `comment:read`, `asset:read`, `asset:write`,
 `brandkit:read`, `help:answers:read`, `help:answers:write`.
- "Do not add scopes outside that list"; "The redirect URI must be the … callback. This package
 does not invent that URI."

### Pitfalls / impossible
- The package explicitly cannot verify anything live without a completed OAuth grant, and it
 refuses to write a client id/secret/token into the repo or chat — the right posture for a
 skill that ships in a repo.
- Not useful beyond auth: it lists a legacy tool-name set (`generate-design`,
 `create-design-from-candidate`) and has no workflow.

---

## Skill: canva-master (Italian mega-prompt)

Thin value: a persona. It prescribes a **design hierarchy doctrine** and a **dimension table**,
and a 6-step MCP workflow.

### Rules worth taking
- Contrast: "titolo 3-4x più grande del body"; accent colour for the key element only; bold for
 titles, regular for body.
- Alignment: 12-column grid, margins ≥ 5 % of the edge, Gestalt proximity.
- Repetition and proximity, and "spazio bianco: respiro = lusso — più spazio = più premium".
- Brand kit structure: **max 5–6 colours** (primary, secondary, accent, light, dark, white) and
 **2–3 fonts** (heading, body, optional accent), with 5 logo variants.
- Carousel architecture: slide 1 hook → one point per slide → summary → CTA, with an edge arrow
 pushing the swipe.
- Export matrix: web PNG/JPG/WebP under 500 KB (< 200 KB social); print PDF 300 DPI CMYK with
 3 mm bleed; video MP4 / GIF < 5 s.
- Workflow (legacy): `search-designs` → `get-design-content` → `start-editing-transaction` →
 `perform-editing-operations` → `commit-editing-transaction` → `export-design`.

### Why it is C-grade
Zero tool schemas, zero failure modes, no note that font-family/background/new-text are
impossible, and it recommends `generate-design` (legacy on our server, and on this account
cannot apply a brand kit because none exists). Its dimension table is still handy as a
quick reference for social sizes.

---

## Skill: canva-2 (generated tool reference)

One line: **thin wrapper** — an auto-generated parameter dump of 22 Canva MCP tools.

### What it uniquely records
- `user_intent` appears on every tool as "Mandatory description … This should always be
 provided by LLM clients … 255 characters or less recommended" (`SKILL.md`, any tool section).
- `upload-asset-from-url`'s own instruction: if the API returns `Missing scopes: [asset:write]`,
 "ask the user to disconnect and reconnect their connector. This will generate a new access
 token with the required scope."
- `search-designs` carries a strongly worded guardrail that any template intent must go to
 `search-brand-templates` instead, and that `search-designs` "ONLY searches existing designs …
 DOES NOT find templates and MUST NOT be used as a fallback".
- Continuation-token rule stated three times: only send a token that came back in a previous
 response; "NEVER EVER fabricate a token"; omit rather than send null/empty.
- `import-design-from-url` refuses local paths and explains the pattern check
 (`/`, `C:\`, `file://`, "Downloads/Documents/Desktop"); requires a public HTTPS URL.
- `merge-designs` requires explicit confirmation for every call, and for `delete_pages` the
 user must type **"I approve the deletion"**; "Operations are applied sequentially. Page
 numbers are 1-based and evaluated at the time each operation runs."
- `get-design-content` supports only `content_types: ["richtexts"]` and says to use
 `start-editing-transaction` when editing is the goal.
- `export-design` guidance: call `get-export-formats` first and always show the download URL.
- `create-folder` / `move-item-to-folder` accept the literal `'root'` as the parent id.

### Limits
No process, no judgment, no thresholds; tool names already drift from our server (it lists
`generate-design` and `create-design-from-candidate`, not `create-design`).

---

## Skill: pitchdeck-pro (deck craft + optional Canva graphics)

### Purpose
Generate a PDF-ready single-file HTML deck (or an interactive HTML deck) with hard numeric
rules, then optionally route "graphic" slides through Canva (`generate-design` →
`export-design` PNG) and embed the PNG.

### Process
1. Phase 0 — detect mode: new deck / PPT conversion / enhancement.
2. Phase 1 — one bundled question set: audience, industry, structure (YC / Sequoia / a16z /
 custom), content readiness, output mode, generation path, graphics source.
3. Phase 2 — style discovery: mood multi-select, then generate **three single-slide HTML
 previews** (safe preset + bold + wildcard) and let the user pick.
4. Phase 3 — generate: read slide archetypes, VC structure, CSS base, data-viz, audience guide,
 MCP graphics guide; then the 5-check generation gate.
5. Phase 4 — PPTX conversion via `scripts/extract-pptx.py`, then re-style.
6. Phase 5 — delivery: open in browser, export PDF via print (`@page landscape, margin 0`),
 run the pre-send checklist.

### Concrete rules and thresholds
| Rule | Value | Source |
|---|---|---|
| Canvas | exactly 1920×1080, `overflow: hidden` | `skills/pitchdeck/references/SLIDE_TYPES.md:6-8` |
| Padding | 80 px all sides → usable 1760×920 | `SLIDE_TYPES.md:8` |
| Type scale | hero/metric **96–120 px**; titles **56–72 px**; body/table **32 px**; labels **24 px**; **nothing below 20 px, ever** | `skills/pitchdeck/SKILL.md`, "NON-NEGOTIABLE RULES → Font Sizes" |
| Density | ≤ **30 words** body (presenter) / **75 words** (async-PDF); ≤ **6 bullets**; overflow ⇒ split the slide | `SKILL.md`, "Content Density" |
| Breathing room | a quote / single-stat / divider slide **every 3–4 content slides** | `SKILL.md`, "Visual Quality" |
| Colour hygiene | never `#FFFFFF` background, never `#000000` text; 2 font families; ≥1 atmospheric element per deck | `SKILL.md`, "Visual Quality" |
| Time budget | investors spend **≤ 150 seconds**; every slide must pass the "Icon-and-Number" test | `SKILL.md`, "Core Principles" |
| Slide-count by structure | YC 10–12 (10 core) · Sequoia 15–20 (13 core) · a16z 12–15 | `skills/pitchdeck/references/VC_STRUCTURES.md` |
| Banned display fonts | Inter, Roboto, Arial, system, Calibri (as display) | `skills/pitchdeck/references/ANTI_PATTERNS.md`, "Fonts: DO NOT USE as Display" |
| Dated patterns to avoid | gradient blobs, pure white bg, pure black text, Montserrat/Poppins headlines, bullet-heavy slides, TAM/SAM/SOM concentric circles, pie charts, 3-D charts, stock team photos, "Questions?" final slide, slide numbers, drop shadows everywhere, dual-axis charts | `ANTI_PATTERNS.md`, table |
| Image guardrails | never photorealistic team photos; never generic stock; prefer abstract/geometric/atmospheric; always ask permission; match preset palette | `skills/pitchdeck/references/MCP_GRAPHICS_GUIDE.md`, "AI Image Guardrails" |

### The Canva part (what actually matters to us)
- `MCP_GRAPHICS_GUIDE.md` "Canva MCP Integration" describes the two deployment shapes:
 1. **Graphics-only pipeline** — `generate-design(infographic|poster|report)` → present
 candidates → `create-design-from-candidate` → `export-design {type: png, width: 1920}` →
 download → embed as `<img>`.
 2. **Canva-native deck** — outline from `VC_STRUCTURES.md` → `request-outline-review` (user
 approves in the widget) → `generate-design-structured` → user edits in Canva →
 `export-design {type: pdf}`.
- Prompting tips that transfer to `create-design` briefs: put brand hexes in the query, state
 the data literally ("TAM $50B, SAM $8B, SOM $1.2B as concentric circles"), and demand style
 ("Modern, minimal infographic style, no clip art").
- Tool-selection table: Canva for infographics/charts, CSS/SVG for diagrams (no external
 dependency), FLUX/Nano-Banana for photographic hero art.

### Pitfalls it documents
- AI image generators produce "AI-slop" stock imagery; the guardrails forbid photorealistic team
 photos outright (instant credibility loss with investors).
- The deck reviewer's **first automatic check** is a font-size scan: any `font-size` below 20 px
 is an automatic Critical issue, with `-2.0` per critical, `-1.0` per warning, `-0.25` per
 suggestion, scored from 10.0 (`agents/deck-reviewer.md`, "FIRST CHECK" and "Scoring Rubric").
- Narrative-arc checks: strongest metric early enough to hook; final slide must be a CTA, never
 "Thank You"/"Questions?".

### Outdated / impossible against our MCP
`generate-design`, `generate-design-structured`, `request-outline-review`,
`create-design-from-candidate` are all legacy/absent here. `mcp__claude_ai_Canva__*` namespacing
in its front-matter is client-specific. Its HTML-first architecture is orthogonal to a
Canva-native deliverable, so only the *rules* transfer, not the pipeline.

---

## Skill: canva-creator (Anthropic small-business) + brand-style

### Purpose
Execute an approved content brief into a finished multi-channel campaign: posting calendar →
slot-level asset inventory → Canva designs with candidate review → captions/emails →
HubSpot staging. `brand-style` is its companion for capturing and applying brand look and
output preference.

### Process (five approval-gated stages)
1. **Pre-flight** — confirm brief, Canva tier (Pro/Teams manual template selection vs Enterprise
 autofill), HubSpot tier, brand assets (read product list from the connected storefront,
 read-only), and a **generation budget** shown to the owner.
2. **Stage 1 — posting calendar** with a `Path` column routing every row to `Canva (social)` or
 `Text-only`; cap 30 days; **Checkpoint 1** = explicit calendar approval before any API call.
3. **Stage 2 — asset inventory, slot by slot** (Enterprise: `dataset[].label` from the brand
 template; Pro/Teams: count every distinct image rectangle), then a **gap table** with one row
 per slot, resolve mismatches with the owner, upload missing photos, and capture a **verified
 `asset.id`**.
4. **Stage 3 — generation, one calendar row at a time**, N candidates per row fired in parallel,
 verify job status, export to a **permanent PNG**, **visually verify each export**, retry only
 the failed candidate, present the row, then **pause 30 s**.
5. **Stage 4 — copy** per channel with length caps (IG ≤ 2,200 chars; FB ≤ 500 recommended;
 X ≤ 280; email subject ≤ 50, preheader ≤ 90, body 100–250 words, one CTA).
6. **Stage 5 — HubSpot staging** with `status: SCHEDULED` (never `PUBLISHED`), confirm the
 queue, surface email copy inline.

### Concrete rules and thresholds
| Rule | Value | Source |
|---|---|---|
| Canva API rate limit | **100 requests/minute per token** | `reference/canva-api.md`, "Rate limits" |
| Cost per design | **~5 API calls** (1 autofill + 1 export + ~3 polls) | same |
| Polling cadence | every **3–5 s**; faster "burns quota without speeding up completion" | same |
| Safe pacing | 3 candidates × 1 row at a time × 30 s gap ≈ **12 designs/minute**, ~half the ceiling | same |
| Overflow rule | projected designs > **30** ⇒ recommend single-candidate mode up front | `SKILL.md`, Pre-flight |
| Retry rule | first `RATE_LIMIT_EXCEEDED` → wait 60 s, retry that one candidate once; **second hit or any quota/daily-cap error → stop and ask** | `SKILL.md`, Stage 3 step 3 |
| Default candidates | 3 per Canva-bound row, locked for the session | `SKILL.md`, Pre-flight |
| Tier matrix | brand templates read + autofill + brand-kit asset upload = **Enterprise only**; user asset upload = Pro/Teams+ | `reference/canva-api.md`, "Tier requirements" |
| Asset upload limits | max **100 MB**; `image/jpeg`, `image/png`, `image/webp` | same, "Asset upload" |

### The gotchas file (best failure documentation in the cluster)
Each is written as ✗ Bad / ✓ Good, and each maps to something an agent will actually do:
1. Generating *any* Canva design for an email row → placeholder graphics; email is text-only.
2. Generating without a budget plan → hitting quota mid-campaign with no recovery path.
3. Skipping the calendar checkpoint → most expensive wasted work.
4. Template has more image slots than the brief has photos → unfilled slots silently render
 Canva's default landscape.
5. Trusting `status: success` without exporting and looking → a success job can still contain
 placeholder or wrong assets.
6. One design in a batch fails → presenting a partial batch destroys trust in the good ones.
7. Generating without confirming every autofill field has a value.
8. **Passing invalid values to image autofill fields** — empty string, file path, URL or a stale
 `asset.id` does not error; it silently renders the default placeholder.
9. **Embedding `design.canva.ai` thumbnail URLs** — short-lived authenticated CDN URLs that
 expire within minutes.
10. Listing designs one-by-one instead of one grouped batch (carousel rendering).
11. Generating sequentially instead of parallel within a batch.
12. Auto-selecting a brand template for Pro/Teams users.
13. Caption voice drift across a long calendar.
14. Staging posts with `scheduledAt` in the past.

### Unique ideas
- **Slot-by-slot inventory with a gap table** before any generation — the only source that
 treats "template has 3 image slots, brief has 1 photo" as a first-class decision.
- **Visual verification of the exported PNG is mandatory** because job success ≠ correct render.
- **Two delivery URLs, only one of which is safe**: `design.canva.ai` (expires) vs
 `export-download.canva.com` (permanent).
- `brand-style`'s capture contract: never ask for hex codes or uploads — take a website link or
 a plain-words description, translate it yourself, **preview on real components**, then save
 with approval; and "Do not restyle old deliverables."

> Sibling note: `small-business/skills/social-content-engine/reference/canva-api.md` is
> byte-identical to the `canva-creator` one (verified with `diff`, no output), so the
> rate-limit / tier / error table above is the library-wide Canva reference; that skill's
> `reference/gotchas.md` adds only calendar-continuity and caption-voice traps, no new MCP facts.

### Outdated / impossible against our MCP
- Built on the **Connect REST API** (`POST /v1/autofills`, `POST /v1/exports`,
 `POST /v1/asset-uploads`) with MCP only as an aside; our toolset is MCP-only. The MCP
 equivalents it maps are `export-design`, `get-design-thumbnail`, `get-design`,
 `upload-asset-from-url` (`reference/canva-api.md`, "Canva MCP equivalents").
- Its autofill/brand-template stage is Enterprise-gated — on our account (0 brand templates) this
 whole branch is dead, and the `Pro/Teams` fallback ("create a blank design, then describe the
 edits the user makes by hand") is exactly the manual work a skill should avoid.
- HubSpot staging is out of scope for us.

---

## Skill: carousel-builder (template duplication + span-preserving edits)

### Purpose
Assemble an 8-page Instagram carousel by duplicating a fixed Canva template and swapping text
spans and image fills inside existing elements, with character budgets enforced *before* image
generation, and a caption step at the end.

### Process
1. Load the framework: read all 8 reference PNGs so the layout, two-tone headline, highlight
 colour, glow frame and CAPS-word body are internalised.
2. Interview: topic → 4–6 pillars (each one job), CTA keyword + deliverable, pillar count.
3. Generate **3–4 cover options** in one parallel batch; user picks one; that pick becomes the
 **theme anchor** (`media_id` held for all later generations).
4. Draft the markdown with **live character counts** per line and get explicit approval
 (no image credits spent before this gate).
5. Generate all pillar images in one batch, each passing the cover as a reference image with the
 instruction to match palette/lighting/style and change only the subject.
6. **Assemble:** `copy-design` (with `page_numbers` to trim a pillar) → `start-editing-transaction`
 → `replace_text` for whole-element copy, `find_and_replace_text` span-by-span for headlines
 that must keep one coloured word → `upload-asset-from-url` → `update_fill` on existing image
 elements → preview → approval → `commit-editing-transaction`.
7. Capture `edit_url` / `view_url` via `get-design`; write a link file.
8. Write the caption with a fixed shape (CTA first line, 5 hashtags, ≤ 500 chars, no em dashes).

### Concrete rules and thresholds (measured from the live template)
- Pillar headline: **45–58 characters** total, exactly **one** highlighted span (renders in the
 accent colour).
- Pillar body: **65–80 characters**, ending in **one ALL-CAPS word**.
- Cover headline: **≤ ~22 characters**; cover subtext 3–4 short italic lines.
- Reason given: "The Canva text boxes are sized for these lengths. Go over and the text reflows,
 the slide no longer matches the deck, and the carousel breaks visual unity."
- Caption hard caps: exactly **5 hashtags**, **≤ 500 characters total**, no em dashes, no
 markdown, body ≤ 80 words, CTA on line 1.

### Unique ideas — the best edit mechanics in the cluster
- **`find_and_replace_text` preserves per-run formatting; `replace_text` flattens it.**
 "`format_text` colors an ENTIRE element, so you cannot recolor a single word; whole-element
 `replace_text` would flatten the existing orange run" (`commands/carousel.md:131`). This is the
 practical answer to our V16 (text stored as multiple regions/runs): edit *inside* the runs.
- **`update_fill` swaps the asset inside the existing element and therefore preserves frame
 effects** (glow/shadow); "Do NOT delete + re-insert the image (that loses the glow)"
 (`commands/carousel.md:136`). The complementary hazard to our V3 (inserted fills sit above):
 prefer `update_fill` over delete+insert+insert_fill whenever a styled frame exists.
- **`copy-design` with `page_numbers` to fit a different pillar count**, plus the honest note
 that duplicating a page *inside* a transaction may be unsupported, in which case degrade and
 say so (`commands/carousel.md`, Step 5.1).
- **Character budgets derived from the template, not chosen by taste** — a transferable
 discipline for our deck: measure the existing text boxes, then write to size.
- **Drafts are permanently lost if not committed** — the approval gate is not politeness, it is
 the only recovery point (`commands/carousel.md:138`; `README.md:160`).
- Responsive pages accept only `update_title, replace_text, update_fill, delete_element,
 find_and_replace_text` — an independent confirmation of our V10.

### Pitfalls it warns about
- Over-budget text reflows and breaks deck unity.
- Baking text into generated images (text belongs on a Canva overlay).
- Generating pillar images without the cover reference (theme drift).
- Baking glow into the prompt instead of preserving the frame effect.
- Skipping the copy-approval gate (wastes image credits).
- Editing the static closer slide; stripping the template's swipe arrows.
- Silently falling back to another image generator when the image MCP is missing.

### Outdated / impossible against our MCP
- Depends on a second MCP (Higgsfield) for images; our only generation tool is
 `generate-image` (which is credit-limited) plus `upload-asset-from-url` for user assets.
- No page-duplication operation exists, as it admits.
- Placeholder template id must be substituted before anything runs.

---

## Skill: design-pack (design ops rules + compact canva skill)

### Purpose
A rules-and-agents pack that forces connector-first behaviour, brand consistency, accessibility,
asset hygiene, licensing and truth-telling around design work.

### Process (`loops/design-it.md`)
brief → direction (named style) → produce via the right connector → critique (design-critic +
brand-compliance-reviewer) → accessibility check → export (asset-export) → hand off with
`[verify]` items.

### Rules worth keeping
- **Truth-telling** (`rules/truth-telling.md`): "Never claim a visual exists if it wasn't
 generated/exported… No invented asset URLs, file paths, dimensions, or token values… mark it
 `[verify]`… A mockup description is not a delivered asset; a spec is not an export."
- **Design quality / anti-template** (`rules/design-quality.md`): pick a named direction; avoid
 "clean minimal" as a non-decision and avoid auto-defaulting to dark; "type is 90% of most
 graphic design"; iterate on generations, don't ship the first raw output; "would this look
 believable in a real brand's portfolio?"
- **Accessibility** (`rules/accessibility.md`): WCAG AA 4.5:1 normal / 3:1 large-bold ≥ 24 px;
 don't rely on colour alone; alt text for meaningful imagery; respect `prefers-reduced-motion`.
- **Asset hygiene**: kebab-case names, right format per job, sRGB vs CMYK, don't commit binaries.
- **Licensing** (`rules/licensing-attribution.md`): record source + licence per asset; fonts have
 licences; disclose AI where required; keep an asset manifest.
- **Critic output format** (`agents/design-critic.md`): findings grouped **Must-fix /
 Should-fix / Polish**, each with element + concrete fix, verdict **SHIP / REVISE**; "You can't
 see pixels you weren't given — say what needs a real visual check."

### Why it is B-grade
`skills/canva-design/SKILL.md` is five steps with no schemas and no failure modes; the value is
the surrounding rule files, which are the cleanest statement of *reporting honesty* in the
cluster (and directly counter our author's biggest risk: claiming a deck is done when the commit
did not land).

---

## Skill: oma-slide (HTML deck, Canva as optional channel)

### Purpose
Author a distinctive HTML deck at a fixed 1920×1080 stage, validate it deterministically, then
optionally import from / export to Canva.

### Process (Canva-relevant subset)
1. Probe Canva availability with `search-designs` **before** any Canva operation; on auth failure
 explain OAuth and keep the local deck.
2. **Import from Canva:** resolve design id → `get-design` → inspect `get-export-formats` →
 `export-design` (PPTX) → download → import locally.
3. **Export to Canva:** produce local PPTX → if `import-design-from-url` exists, use an
 *authorised reachable URL*; if only local files exist, "deliver the PPTX for manual Canva
 import… Do not publish the file or enable public sharing merely to satisfy the remote tool's
 URL requirement."
4. Report the Canva design URL only after the **complete** deck imported: "A missing or failed
 page makes the transfer incomplete; report it rather than silently skipping slides."

### Concrete rules and numbers
- Stage exactly **1920×1080**; safe margins **80 px** left/right, **60 px** top/bottom;
 **8 px grid**; z-index layers 0/10/100/200.
- Body **28–36 px** doctrine floor, headings **64–120 px**; the validator hard-fails only below
 **18 px** — "18–27 px passes the gate but is reserved for captions/labels".
- Density modes: `sparse` (headline 64–120 px, body 0–3 lines at 32–48 px, no bullets, visuals
 ≥ 40 % of canvas, 1 slide per 1–2 min) vs `dense` (headline 48–72 px, body 28–36 px, max 8
 lines, ≤ 6 bullets of ≤ 20 words).
- WCAG AA: 4.5:1 normal (< 24 px), 3:1 large (≥ 24 px).
- Slide-count guidance table by purpose and density (pitch 5 min: 6–10 sparse / 8–14 dense;
 conference 30 min: 20–35 sparse / 30–50 dense).
- Forbidden display typefaces: Inter, Roboto, Arial/Helvetica unmodified, Open Sans, Lato — fine
 as body/fallback, not as display.

### Unique ideas
- **"Incomplete transfer is a failure"** — the strongest statement in the cluster about partial
 merges/imports.
- **Explicitly refuses to invent tools**: "Do not invent a presentation-creation call that maps
 an asset-ID array to pages, or pass a local filepath to a URL-upload tool."
- **PPTX from HTML is raster-backed** ("each slide is a PNG, so importing it does not make text
 editable") — matches rifater's finding from the other direction.
- The atmospheric-intention / "committed aesthetic" framing (palette with named roles, one
 accent, typographic commitment) is the best-written version of anti-AI-slop in the cluster.

### Outdated / impossible
- Its Canva channel is intentionally bare; no `create-design`, no transactions, no thumbnails.
- Auto-provisioning writes MCP config files — not our job inside a skill.

---

## Verified quirks catalogue

Legend for **Match**: `YES` = our live finding is corroborated by this source; `PARTIAL` =
related but not identical; `NEW` = not on our list, adds capability knowledge; `NO` = not
mentioned. Our verified list: **V1** `create-design` paraphrases outline text · **V2**
`delete_element` on a grouped child id no-ops · **V3** inserted fills sit above existing
elements · **V4** `merge-designs` insert order can come back reversed · **V5** no font-family ·
**V6** no background change · **V7** no new text boxes · **V8** presenter notes read-only ·
**V9** no delete-design · **V10** responsive pages accept a restricted op set · **V11** slides
1920×1080 · **V12** body < ~30 px too small for a classroom · **V13** 0 brand kits / 0 brand
templates · **V14** `generate-image` `credit_quota_exceeded` · **V15** `create-design` async job
contract · **V16** text stored as multiple runs, naive joining invents typos · **V17**
`get-design-pages` returns a real thumbnail only for page 1.

### A. Generation / composition
| # | Quirk, limit or error | Evidence | Match | Handling |
|---|---|---|---|---|
| Q1 | Generated candidates routinely drop, duplicate or garble requested labels; AI substitutes its own template | `rifaterdemsahin_canva-mcp/7_Testing_Known/glossary_grid_flow.md` (Attempt 1 and screening table) | **YES (V1)** | Screen every candidate with `get-design-content` before showing options; fix single bad labels with `replace_text` |
| Q2 | `infographic` design type has a template prior toward stats/quote narrative and will fabricate statistics rather than render a literal list | same file, "Attempt 1" lesson | NEW | Avoid for literal lists; prefer `poster`-like or a deck outline with explicit numbering |
| Q3 | Over-constraining a generation prompt with negative constraints can fail the whole job: `status: "failed"`, `error.code: "design_generation_error"` | same file, "Attempt 2" | NEW | Prefer one switch of design type over repeated negative constraints |
| Q4 | A generation returns **4 candidates**; the practical selector is page count vs the approved outline | `rifaterdemsahin_canva-mcp/4_Formula/architecture_course_mcp_spec.md` (Delivery Notes); `rifaterdemsahin_canva-mcp/7_Testing_Known/coordinator_subagents_comic_flow.md` ("page counts: 9, 4, 10, 9") | NEW | Choose closest page count, favouring the direction that preserves named structure |
| Q5 | Longer decks take materially longer and can time out on the first call; an identical retry then succeeds | `rifaterdemsahin_canva-mcp/7_Testing_Known/coordinator_subagents_comic_flow.md` | PARTIAL (V15) | Treat timeout as retryable; don't tighten the brief |
| Q6 | Canva's own AI image generation runs inside deck generation when the outline describes artwork that isn't in the stock library; supporting graphics come from Elements | `rifaterdemsahin_canva-mcp/7_Testing_Known/coordinator_subagents_comic_flow.md`, provenance table using `get-assets` | NEW | Ask for scene/illustration descriptions in `create-design` sections instead of spending image credits |
| Q7 | Opening a candidate's preview URL in a browser **materialises it as a real design** in the account | `rifaterdemsahin_canva-mcp/7_Testing_Known/canva_design_DAHPLiS4suo_steps.md`, Step 5 | NEW | Only open the candidate you intend to keep, or expect orphan designs |
| Q8 | Autofill / brand-template usage is **Enterprise-gated** across API and MCP (`autofill-design`, `create-design-from-brand-template`, `list-brand-kits`, `publish-brand-template`) | `rifaterdemsahin_canva-mcp/2_Environment/canva_capability_research.md` §3; `anthropics…/canva-creator/reference/canva-api.md` tier table | **YES (V13)** | Treat brand templates as unavailable unless a kit/template demonstrably exists |
| Q9 | No tool inserts a **native shape, icon, line or connector**; `insert_fill` accepts pre-uploaded image/video only | `rifaterdemsahin_canva-mcp/2_Environment/canva_capability_research.md` §1, §4; `rifaterdemsahin_canva-mcp/4_Formula/architecture_course_mcp_spec.md` Capability Scan; `rifaterdemsahin_canva-mcp/7_Testing_Known/architecture_course_shape_deck_flow.md` | PARTIAL (V7) | Build diagrams as uploaded PNG/SVG assets, or accept AI-interpreted shapes, or draw them by hand |
| Q10 | True native shapes exist only through the Apps SDK `addElementAtPoint({type:"shape", paths, viewBox})`: 1–30 paths, ≤ 2 KB path data, ≤ 6 unique fills, one leading `M` per path, no `Q` | `rifaterdemsahin_canva-mcp/2_Environment/canva_capability_research.md` §2 | NEW | Not available via MCP; keep as a documented manual escape hatch |
| Q11 | Animations cannot be applied programmatically on any surface; confirmed via Canva's own Help tool ("editor-only") | `rifaterdemsahin_canva-mcp/7_Testing_Known/canva_lower_third_flow.md`, "Animation boundary re-confirmed (official)"; `rifaterdemsahin_canva-mcp/4_Formula/lower_third_mcp_spec.md`, manual step | NEW | Do not promise animation; hand over editor steps (Animate → Fade → On enter) |

### B. Editing transaction semantics
| # | Quirk | Evidence | Match | Handling |
|---|---|---|---|---|
| Q12 | **No operation inserts a new standalone text element**; the working pattern is to put the text in the generation brief and then reposition/reformat it | `rifaterdemsahin_canva-mcp/4_Formula/lower_third_mcp_spec.md` "Key design decision"; `rifaterdemsahin_canva-mcp/2_Environment/canva_connection.md` capability matrix | **YES (V7)** | Plan every string you will ever need into `create-design` sections |
| Q13 | `format_text` applies to the **entire element** — you cannot recolour a single word | `charlesdove977_carousel-builder/commands/carousel.md:131` | **YES (V5, V16)** | Use `find_and_replace_text` span-by-span to preserve an existing coloured run |
| Q14 | `find_and_replace_text` preserves per-run formatting, `replace_text` flattens the element to one style | same line | NEW (complements V16) | Default to `find_and_replace_text` on any headline with mixed styling |
| Q15 | `update_fill` swaps the asset inside an existing element and preserves frame effects (glow/shadow); delete+re-insert loses them | `carousel.md:133-137` | PARTIAL (V3) | Prefer `update_fill` over delete/`insert_fill` whenever a styled frame exists; expect inserted fills to sit on top |
| Q16 | Operations are draft-only until `commit-editing-transaction`; **uncommitted drafts are permanently lost** | `carousel.md:138`; `charlesdove977_carousel-builder/README.md:160`; `…/canva-ppt-lesson-designer/references/canva-workflow.md` §4 | NEW | Never report success pre-commit; preview → explicit approval → commit |
| Q17 | `position_element` / `resize_element` are valid only on **fixed (non-responsive)** pages; presentations qualify | `rifaterdemsahin_canva-mcp/4_Formula/specs.md:197`; `rifaterdemsahin_canva-mcp/2_Environment/canva_connection.md` ("fixed pages only") | **YES (V10)** | Check `is_responsive` per page before planning geometry |
| Q18 | On `is_responsive` pages the allowed op set is exactly `update_title, replace_text, update_fill, delete_element, find_and_replace_text` | `…/canva-ppt-lesson-designer/references/canva-workflow.md:56`; `carousel.md:128` | **YES (V10)** | Two independent sources agree; treat as closed |
| Q19 | Batch many ops in one `perform-editing-operations` call; results come back per-op in `edit_operation_results` with `status: success` | `rifaterdemsahin_canva-mcp/4_Formula/lower_third_mcp_spec.md` (5/5), `rifaterdemsahin_canva-mcp/7_Testing_Known/architecture_course_shape_deck_flow.md` (4/4) | NEW | Verify the result count, not just the call's success |
| Q20 | Element discovery is by reading the transaction's `richtexts[]` / `fills[]` and matching text content or coordinates; `element_id`s exist only inside a transaction | `rifaterdemsahin_canva-mcp/7_Testing_Known/glossary_grid_flow.md` (matched duplicate label at `top: 1123.93, left: 531.645` to an `element_id`) | NEW | Resolve ids per transaction; never cache them across transactions |
| Q21 | `format_text` exposes size/weight/style/colour/align/line-height/list — **no font family, no background** | `rifaterdemsahin_canva-mcp/2_Environment/canva_connection.md` matrix; `…/canva-ppt-lesson-designer/references/canva-workflow.md:14` | **YES (V5, V6)** | Fix type at the brand-kit/template level; treat the deck's font as immutable |
| Q22 | Generated layouts commit to their own grid; forcing a header into "the right column" with `position_element` overlaps artwork and orphans the header from its body | `rifaterdemsahin_canva-mcp/6_Semblance/lessons_learned.md` | NEW | Use `text_align` (start/center/end) instead of frame relocation |
| Q23 | Editing a poster-shaped design at a different canvas than the target requires `resize-design {type: custom, width, height}` before merging | `rifaterdemsahin_canva-mcp/4_Formula/specs.md` SPEC-019; `rifaterdemsahin_canva-mcp/7_Testing_Known/glossary_grid_flow.md` | PARTIAL (V4) | Always resize to 1920×1080 before `merge-designs` |
| Q24 | Responsive/fixed-page detection and page metadata come back in the transaction's `pages[]` (page_id, page_number, dimension, is_responsive, is_editable) | `rifaterdemsahin_canva-mcp/2_Environment/canva_connection.md` §"start-editing-transaction returns …"; `carousel.md:128` | PARTIAL (V10) | Use `pages[]` for structure; use per-page `get-design-thumbnail` for visuals |

### C. Structure, pages and merge
| # | Quirk | Evidence | Match | Handling |
|---|---|---|---|---|
| Q25 | Pages have **no settable name/label**; only index + thumbnail | `rifaterdemsahin_canva-mcp/6_Semblance/lessons_learned.md`; `rifaterdemsahin_canva-mcp/4_Formula/canva_pages_table_recipe.md` Step 4 ("Canva REST API does not support page renaming") | NEW | Keep slide names in project notes; map name → page number externally |
| Q26 | `merge-designs` is the only page-level structural tool (insert/move/delete/create-new) and must not be used for content edits | `LeoYeAI_agent-master-skills/skills/canva-2/SKILL.md`, `### merge-designs` | PARTIAL (V4) | Use for structure only; content via transactions |
| Q27 | `merge-designs` requires explicit confirmation on **every** call; `delete_pages` requires the literal phrase "I approve the deletion", and the tool text warns "CANNOT BE UNDONE" | same section | NEW | Implement a confirmation gate; echo exactly what will change |
| Q28 | `merge-designs` operations are **sequential and 1-based, evaluated at the time each operation runs** — so a delete shifts later page numbers | same section | **YES-adjacent (V4)** | Compute page numbers against the running state, or issue one operation per call |
| Q29 | No page-duplication operation inside a transaction; template-driven skills admit they must degrade to fewer pages | `carousel.md`, Step 5.1 | NEW | Design around a fixed page count, or copy designs and merge |
| Q30 | `copy-design` takes `page_numbers` to select a subset of pages from the source | `carousel.md`, Step 5.1 | NEW | Use it to fit a template to an arbitrary slide count |
| Q31 | `import-design-from-url` refuses local paths (`/`, `C:\`, `file://`, "Downloads/Documents/Desktop") and requires public HTTPS | `canva-2/SKILL.md`, `### import-design-from-url` | NEW | Never promise local-file import; require a reachable URL or manual import |
| Q32 | `upload-asset-from-url` needs a publicly reachable HTTPS URL and uploads **one** asset per call | `canva-2`, `### upload-asset-from-url`; `anthropics…/canva-creator/reference/canva-api.md` MCP equivalents table | NEW | Budget one call per image; host assets somewhere public |
| Q33 | `export-design` should be preceded by `get-export-formats`, and the returned download URL must be shown to the user | `canva-2`, `### export-design` / `### get-export-formats`; `…/canva-ppt-lesson-designer/references/canva-workflow.md` §5 | NEW | Always surface the URL; it is the deliverable |

### D. Previews, URLs and verification
| # | Quirk | Evidence | Match | Handling |
|---|---|---|---|---|
| Q34 | `design.canva.ai` thumbnails from async responses are short-lived authenticated CDN URLs; embedding them yields broken images within minutes | `anthropics…/canva-creator/reference/gotchas.md` ("Embedding Canva CDN thumbnail URLs"); `reference/canva-api.md`, "Export" | PARTIAL (V17) | Re-export to PNG for anything durable; use in-transaction thumbnails for review only |
| Q35 | API `edit_url` / `view_url` are expiring JWT links (`canva.com/api/design/…`); the permanent form is `canva.com/design/<ID>/…` | `rifaterdemsahin_canva-mcp/6_Semblance/canva_document_visibility.md`, resolution table | NEW | Capture and store the permanent URL right after creation |
| Q36 | Designs created via API do not appear in Canva home "Recents"; they are under **Projects** | `rifaterdemsahin_canva-mcp/6_Semblance/canva_document_visibility.md`, cause #1 | NEW | Tell the user where to look; search by title instead |
| Q37 | `updated_at` bumping past `created_at` is the cheap proof a commit landed | `rifaterdemsahin_canva-mcp/4_Formula/lower_third_mcp_spec.md`; `rifaterdemsahin_canva-mcp/7_Testing_Known/architecture_course_shape_deck_flow.md` | NEW | Make it a mandatory check before saying "done" |
| Q38 | Job success does not mean correct render: a success job can contain placeholder graphics if a field/asset was empty, stale or wrong-typed | `anthropics…/canva-creator/reference/gotchas.md` (three separate gotchas) | NEW | Export and look at the pixels; verify per slide |
| Q39 | Placeholder landscape with clouds/hills is Canva's tell for an unfilled image slot | `gotchas.md` ("Template has more image slots…") | NEW | Add it to the visual QA list, alongside gray rectangles and lorem-ipsum |
| Q40 | A partial batch (one broken item) destroys trust in the good items; regenerate only the failed item | `gotchas.md` ("One design in a batch fails to render") | NEW | Per-item retry, never whole-batch regeneration |

### E. Permissions, auth, scopes
| # | Quirk | Evidence | Match | Handling |
|---|---|---|---|---|
| Q41 | "Access Restricted by Team Admin" on the consent screen is a **Canva Team** permission, fixed at `canva.com/settings/apps-and-integrations`, not an integration bug | `rifaterdemsahin_canva-mcp/2_Environment/canva_connection.md`, "Team admin restriction" | NEW | Recognise it; it needs the team admin, not retries |
| Q42 | Missing scope surfaces as HTTP **403 `missing_scope`**; `design:meta:read` is needed to list designs, `profile:read` for `/users/me`, `design:content:read` for pages | `rifaterdemsahin_canva-mcp/6_Semblance/canva_document_visibility.md` cause #3; `rifaterdemsahin_canva-mcp/4_Formula/canva_pages_table_recipe.md` Step 2 | NEW | Re-consent with the wider scope; a write-only token makes success look like failure |
| Q43 | `Missing scopes: [asset:write]` → disconnect and reconnect the connector to get a new token with the scope | `canva-2/SKILL.md`, `### upload-asset-from-url` | NEW | Document the remedy; do not retry blindly |
| Q44 | Unauthenticated `initialize` returns **401** with `WWW-Authenticate` pointing at protected-resource metadata; `/.well-known/oauth-authorization-server/mcp` is **404** (use the issuer document) | `xpert-ai_xpert-plugins/agent-plugins/canva/README.md`, "Connector setup" | NEW | Use the issuer metadata for discovery; don't hand-roll the well-known path |
| Q45 | Published `scopes_supported` list and token-endpoint methods (`none`, `client_secret_basic`, `client_secret_post`), PKCE S256 | same file | NEW | Request only from that list |
| Q46 | `user_intent` is effectively mandatory on every tool call (≤ 255 chars recommended) | `LeoYeAI_agent-master-skills/skills/canva-2/SKILL.md` (every tool section) | NEW | Always pass a one-line intent; it is also useful telemetry |

### F. Rate limits, quota and cost
| # | Quirk | Evidence | Match | Handling |
|---|---|---|---|---|
| Q47 | **100 requests/minute per token**; ~5 API calls per design; poll every 3–5 s; safe pacing ≈ 12 designs/min | `anthropics…/canva-creator/reference/canva-api.md`, "Rate limits & generation budgeting" | PARTIAL (V14: our quota was credits, not requests) | Budget generations before starting; never poll tightly; never parallelise rows |
| Q48 | `RATE_LIMIT_EXCEEDED` retry policy: first hit → wait 60 s, retry once; second hit or any quota/daily-cap error → **stop and ask**, never loop | same file + `gotchas.md` | NEW | Bake in a hard stop with a progress report |
| Q49 | Generation cost estimate: `total_designs = rows × candidates`, `total_api_calls ≈ designs × 5`, `time ≈ designs / 12` minutes | `reference/canva-api.md` | NEW | Surface the estimate before generating a multi-slide deck |
| Q50 | Long generations can time out once and succeed on identical retry | `rifaterdemsahin_canva-mcp/7_Testing_Known/coordinator_subagents_comic_flow.md` | PARTIAL (V15) | Retry once before changing anything |

### G. Text runs, character budgets and typography
| # | Quirk | Evidence | Match | Handling |
|---|---|---|---|---|
| Q51 | Text is stored as multiple regions/runs; a headline can mix a coloured span with plain spans | `carousel.md:131` (formatting-preserving span edits); `canva-2` `get-design-content` ("content_types: richtexts") | **YES (V16)** | Read raw runs; never join naively; edit spans individually |
| Q52 | Text boxes are sized for specific character counts; over-length copy reflows and breaks the layout, so budgets must be enforced at draft time | `carousel.md`, "Character budgets (measured from the live template — HARD caps)" | NEW | Measure the template's box, then write to size |
| Q53 | No font-family operation ⇒ the font must already be inside the brand kit / template | `…/canva-ppt-lesson-designer/references/canva-workflow.md:14, :78` | **YES (V5)** | State this as a limit in the skill; never promise a font change |

### H. Import / export and format
| # | Quirk | Evidence | Match | Handling |
|---|---|---|---|---|
| Q54 | PPTX `p:grpSp` groups are flattened on import — selection separates the parts | `rifaterdemsahin_canva-mcp/6_Semblance/workarounds.md` #1; `rifaterdemsahin_canva-mcp/4_Formula/numbers_1_100_grouped_spec.md` | NEW | Bake composite objects into a single PNG per object |
| Q55 | PPTX exported from HTML (or generated as raster) contains one image per slide — **no editable text** | `first-fluke_oh-my-agent/skills/oma-slide/resources/canva-integration.md`, "PPTX output is raster-backed" | PARTIAL (V5) | Only promise editability where Canva text elements actually exist |
| Q56 | An incomplete import/merge (missing or failed page) is a failure, not a partial success | `oma-slide/resources/canva-integration.md`, Error Handling | PARTIAL (V4) | Verify page count after any structural operation |
| Q57 | Import always creates a **new** design; it never patches an existing one | `rifaterdemsahin_canva-mcp/7_Testing_Known/numbers_1_100_grouped_flow.md`, "Re-run the same app" | NEW | Expect duplicate designs on re-run; name them |

### I. Search, naming and tool-selection traps
| # | Quirk | Evidence | Match | Handling |
|---|---|---|---|---|
| Q58 | `search-designs` never finds templates; template intent must go to `search-brand-templates` | `canva-2/SKILL.md`, `### search-designs` (its own emphatic guardrail) | NEW | Route by intent, not by keyword |
| Q59 | Continuation tokens must be echoed exactly and never fabricated or set to null/empty | `canva-2`, continuation parameter on three tools | NEW | Omit the field when no token was returned |
| Q60 | Tools may be normalised/renamed by the client; always resolve the callable tool list before invoking | `oma-slide/resources/canva-integration.md` ("Client wrappers may normalize their names; resolve the callable tools") | PARTIAL (V1) | Read live schemas at session start; never hardcode a name you have not seen |
| Q61 | Canva pages "have no MCP-settable name" also means **slide ordering must be verified**, not assumed, after structural ops | `rifaterdemsahin_canva-mcp/6_Semblance/lessons_learned.md` + `oma-slide` incomplete-transfer rule | **YES (V4)** | Assert page count and inspect thumbnails after `merge-designs` |

---

## Merge recommendations

| Idea | Source skill(s) | Verdict | Why | Where it belongs |
|---|---|---|---|---|
| "Put every string you might need into the generation brief, then reposition/reformat" | rifater (`lower_third_mcp_spec.md`), lesson-designer | **keep** | Only defence against the missing insert-text op | plan → generate |
| Screen each candidate's **text**, not its thumbnail, before offering it | rifater (`glossary_grid_flow.md`), canva-creator | **keep** | Candidates reliably drop/duplicate/garbled labels | generate → review |
| Pick the candidate whose **page count** matches the approved outline | rifater (`architecture_course_mcp_spec.md`, comic flow) | **keep** | Cheapest structural fidelity check available | generate |
| `find_and_replace_text` for mixed-style headlines; `replace_text` only for single-style elements | carousel-builder (`carousel.md:131`) | **keep** | Preserves accent spans; matches our V16 | edit |
| `update_fill` instead of delete+re-insert when a frame has effects | carousel-builder (`carousel.md:136`) | **keep** | Preserves glow/shadow; complements V3 | edit |
| Draft → preview → explicit approval → commit; never say done pre-commit | carousel-builder, canva-creator, rifater | **keep** | Uncommitted drafts vanish permanently | edit → delivery |
| Per-page thumbnails inside one transaction for whole-deck review | rifater, carousel-builder, lesson-designer | **keep** | The only way to see every slide without N transactions | review |
| Verify `updated_at > created_at` before claiming success | rifater | **keep** | Cheap, decisive persistence proof | review/delivery |
| Export a permanent PNG for anything shown to the user | canva-creator (`gotchas.md`) | **keep** | CDN thumbnails expire; JWT edit URLs expire | review → delivery |
| Slot-by-slot asset gap table before generation | canva-creator (`SKILL.md` Stage 2) | **adapt** | Deck version: one row per image/text slot of the outline, not per template field | plan → generate |
| Rate-limit budget + hard stop on second quota error | canva-creator (`canva-api.md`) | **adapt** | Numbers are for autofill/export, but the discipline (5 calls/design, 3–5 s poll, stop-and-ask) transfers | plan → generate |
| Character budgets measured from the template's text boxes | carousel-builder | **adapt** | Our decks are generated, not templated — but after generation the boxes are real, so measure then rewrite | edit |
| 8-field per-slide content contract with fixed labels | lesson-designer (`slide-output-contract.md`) | **keep** | Makes deck plans machine-checkable and forces visuals/interaction/notes per slide | plan |
| Lesson-map lookup before writing content | lesson-designer (`references/maps/`) | **keep** (adapted) | The strongest anti-hallucination device for factual decks; generalise to a course/syllabus map file | plan |
| 6-layout system, one knowledge unit per slide, default 5–6 of 6 layouts per deck | lesson-designer (`slide-design-framework.md`) | **keep** | Directly serves "aligned, consistent, not repetitive" | plan → design |
| Accent < 10 % of area, one accent point per slide, dominant 60–70 % | lesson-designer; canva-master; oma-slide | **keep** | Three independent sources converge; measurable QA criterion | design → review |
| Type-tier ratio ≥ 1.3×; bold headings, regular body, bold only the emphasis span | lesson-designer (style file §1–§3) | **keep** | Directly fixes the "every slide looks the same" failure | design → review |
| Vietnamese-safe font/family list and diacritics QA line | canva-prompt-creator; lesson-designer | **keep** (adapt to "choose the template font that has full Vietnamese coverage") | Diacritics break silently | design → review |
| Challenge-before-acting: missing ≥2 criteria ⇒ push back with a filled template; missing 1 ⇒ default and say so | lesson-designer; canva-prompt-creator; stem-lesson-creator; ke-hoach-day-hoc | **keep** | Cheapest quality lever for vague student requests | plan (intake) |
| Anti-AI-slop catalogue: no rule line under every title, no full-width bars, no Office-2007 bevels, no centred body, no cream-by-default, no rainbow palettes | lesson-designer `anti-patterns.md`; pitchdeck `ANTI_PATTERNS.md`; oma-slide `design-doctrine.md` | **keep** (merged into one list) | Overlapping lists; merging yields one strong checklist | review |
| Truth-telling rule: never claim a visual exists unless a tool returned it; mark unknowns `[verify]` | design-pack (`rules/truth-telling.md`) | **keep** | The exact failure mode of an agent driving an async API | delivery |
| "Incomplete transfer is a failure" (missing page ⇒ say so) | oma-slide | **keep** | Prevents silently shipping a short deck | structure/delivery |
| Don't invent tool calls: no asset-array→pages call, no local path to a URL tool | oma-slide | **keep** | Directly prevents fabricated pipelines | plan → generate |
| Confirmation gate for structural ops; literal approval phrase for deletes | canva-2 (`merge-designs`) | **keep** | Irreversible operations | structure |
| 1920×1080 fixed-stage numbers (80 px margins, 8 px grid, z-layers) | oma-slide; pitchdeck; rifater | **keep** numbers, **drop** HTML/CSS mechanics | Canva has no z-index control; only margins and alignment transfer | design |
| Type/density numbers: titles 56–72 px, body 32 px, nothing < 20 px, ≤ 30 words presenter / 75 async, ≤ 6 bullets | pitchdeck-pro | **keep** and raise body to ≥ 32 px for classrooms | Best calibrated to projection and to our V12 | design → review |
| Deck reviewer scoring rubric (from 10.0; −2/−1/−0.25) + font-size scan as the first automatic check | pitchdeck-pro (`agents/deck-reviewer.md`) | **keep** | Gives the review phase a verdict instead of vibes | review |
| Design-critic output format: Must-fix / Should-fix / Polish + SHIP/REVISE | design-pack (`agents/design-critic.md`) | **keep** | Same shape as the rubric; merge the two into one reviewer | review |
| Slide-count by duration (6–8 / 8–12 / 12–18) | lesson-designer | **keep** | Student presentations are time-boxed | plan |
| Brand kit as the font-delivery mechanism | lesson-designer | **adapt** | Correct, but we have 0 kits — needs a "no kit" branch | plan → generate |
| Template-first workflow (duplicate a template, then edit) | carousel-builder, design-pack | **drop for now, keep as a branch** | We have no templates; when the user creates one, this becomes the best path | structure |
| Autofill / brand-template automation | canva-creator, rifater | **drop** | Enterprise-gated; our account has none | generate |
| HubSpot / campaign / caption pipelines | canva-creator, carousel-builder | **drop** | Out of scope for a coursework deck | delivery |
| HTML deck generation and PDF print pipeline | oma-slide, pitchdeck-pro | **drop** | We are Canva-native | generate/delivery |
| Second image MCP (Higgsfield / FLUX / Nano Banana) | carousel-builder, pitchdeck-pro | **drop** | Our only image paths are `generate-image` (credit-limited) and `upload-asset-from-url` | visuals |
| python-pptx geometry snippets inside a Canva skill | lesson-designer style file | **drop** the code, **keep** the hex/geometry table | The skill contradicts itself; only the measurements are usable | design |
| `generate-design` / `request-outline-review` / `create-design-from-candidate` workflows | rifater, pitchdeck, lesson-designer, canva-2 | **drop** | Legacy tool names; replace with `create-design` + `get-create-design-async-job` | generate |
| Platform dimension table (social sizes) | canva-master, canva-prompt-creator | **adapt** | Only the 1920×1080 and 4:3 presentation rows matter here | plan |

---

## Contradictions

1. **Canvas size.** oma-slide fixes the stage at 1920×1080 px
 (`resources/fixed-stage.md` §1); pitchdeck-pro the same (`SLIDE_TYPES.md:6`); rifater's real
 pages measured 1920×1080. The lesson-designer sets a default of `13.333" × 7.5"` and an
 EduTechND variant of `20" × 11.25"` (`SKILL.md`, "Slide canvas").
 **Recommendation:** treat 1920×1080 px as the single truth for Canva presentations (it is also
 our V11). The inch values are the same 16:9 ratio at a different authoring scale; when reading
 the lesson-designer's pt numbers, convert rather than copy.

2. **Font sizes across sources are not comparable without the canvas.** pitchdeck-pro says body
 32 px and "nothing below 20 px" on a 1920×1080 canvas; oma-slide says body 28–36 px with a
 validator floor of 18 px; the lesson-designer says body 36 pt on a 20-inch canvas but 14–18 pt
 on a 13.3-inch one; `assets/brand-standard.json` says `body: 17` and `caption: 11`.
 **Recommendation:** never carry a number between sources without its canvas. For our deck:
 title ≈ 52–60 px, section ≈ 40 px, body ≥ 32 px, caption ≥ 24 px — and treat our own
 classroom finding (V12: under ~30 px reads badly from the back) as the tie-breaker, which
 makes pitchdeck's numbers the closest fit and the lesson-designer's `body: 17` unusable.

3. **`body: 17` inside the lesson-designer.** `assets/brand-standard.json` `sizes_pt` (title 36,
 section 24, body 17, caption 11) directly contradicts the same skill's own style file
 (title 44–72, body 36, caption 24–28) and its hard rule "minimum 24 pt when projected"
 (`SKILL.md:159`). **Recommendation:** the `sizes_pt` block is a stale artefact of the removed
 python-pptx generator; discard it, keep the style-file scale.

4. **Two EduTechND palettes.** `references/slide-design-framework.md` and
 `assets/brand-standard.json` use `#4B2E2B / #8C5A3C / #FFF8F0` + subject accents;
 `references/styles/edutechnd-earth-dark.md` uses `#3F2313 / #D7A550 / #D28119 / #FCFBF9`.
 **Recommendation:** pick one. The `brand-standard.json` set is the one the workflow and the
 output contract both reference, and it carries the subject-accent map; the ANKENE set looks
 like an earlier screenshot-derived palette. Use the former and note the latter as legacy.

5. **Generation strategy: brief-to-design vs template duplication.** rifater/pitchdeck/
 lesson-designer generate from an outline; carousel-builder/design-pack duplicate a template.
 **Recommendation:** template-first when a usable template exists (deterministic layout, real
 character budgets, formatting you can preserve); otherwise `create-design`. Never mix within
 one deck — a generated page next to a duplicated page never matches.

6. **How to preview work.** canva-creator forbids embedding `design.canva.ai` URLs and mandates
 exporting a PNG; rifater and the lesson-designer use `get-design-pages` /
 `get-design-thumbnail` inside a transaction. **Recommendation:** both, for different jobs —
 in-transaction per-page thumbnails for fast iteration and whole-deck review (cheap, current),
 and an exported PNG for anything the user keeps, embeds or compares later (permanent).

7. **Whether to "fix in place" or "regenerate".** rifater's cheap-fix rule (replace one bad
 label) vs canva-creator's per-candidate regeneration rule when the *asset* is wrong.
 **Recommendation:** text defects → fix in place with `find_and_replace_text`; image/asset
 defects → regenerate that one candidate (an `update_fill` with a wrong asset cannot be
 "edited" into the right one).

8. **Slide-count guidance.** lesson-designer: 6–8 slides for 20–30 min. oma-slide: one slide per
 1–2 minutes of talk time (i.e. 15–30 slides for 30 min, sparse). pitchdeck: 10–12 for a full
 investor pitch. **Recommendation:** for a university coursework presentation with a strict
 time limit, use the lesson-designer's density (a slide is a teaching unit, not a beat) but cap
 at ~1.5 min per slide; a 15-minute talk lands at 10–12 slides.

9. **Animation.** canva-master and canva-prompt-creator imply the agent can add animation
 (Magic Animate); rifater verified via Canva's Help tool that animation is editor-only.
 **Recommendation:** rifater wins — it is the only one with official confirmation. Never list
 animation as a deliverable; hand over the editor steps.

---

## Gaps

What a complete, Canva-native slide workflow needs that none of these ten sources covers:

1. **The `create-design` + async-job contract.** Every source uses the legacy
 `request-outline-review` → `generate-design-structured` → `create-design-from-candidate`
 chain. Our server's actual contract (`create-design` with `outline.sections[]` returning
 `job_id` + `continuation_token` + `wait_seconds`, and `get-create-design-async-job` whose
 terminal status is `completed`) is documented nowhere in this cluster. The skill must carry
 the real contract, including that the token is reused un-rotated and that status strings are
 not `success`.
2. **A substitute for the outline-approval widget.** Four sources make "user approves the outline
 in the widget" a hard gate; we have no widget. A prompt-level approval gate with an explicit
 "confirm these N sections before I spend a generation" statement is needed, plus a rule for
 what happens when the user edits the outline.
3. **Diagram construction with no shape primitives.** Sources either punt to the Apps SDK
 (unavailable), to manual line-drawing, or to raster icons. Nobody documents a repeatable
 in-MCP diagram recipe (draw PNG/!SVG locally → `create-upload-url` → `upload-asset-from-url`
 → `insert_fill` at computed coordinates → verify). That is the single biggest visual gap for
 a philosophy/coursework deck.
4. **A "no brand kit, no template" branch.** The lesson-designer assumes a kit exists; the
 carousel-builder assumes a template exists. Neither says what to do on an account with zero of
 each (our V13) — i.e. how to enforce a palette and a type system when the only levers are
 hex values inside the generation brief and the restricted `format_text` op set.
5. **Presenter notes.** Nothing in the cluster writes them, and rifater/canva-2 only read them.
 For a coursework presentation the speaker notes are half the deliverable; the skill needs an
 explicit "notes live outside Canva" plan (a sidecar file keyed by page number) and should say
 so up front rather than at delivery.
6. **Whole-deck typography normalisation.** All sources either set type at generation time or
 format element by element. Nobody documents a repeatable pass that walks every text element on
 every page in one transaction and applies a size/weight/alignment ladder — which is exactly
 what "consistent fonts" means when you cannot choose a font family (V5).
7. **Post-commit rollback.** Every source says "commit or lose the draft", none addresses the
 inverse: a bad commit. With no version history and no delete-design (V9), the only recovery is
 `copy-design` before editing, or re-generation. A skill should make a safety copy explicit for
 risky edit passes.
8. **Vietnamese typography in practice.** The lesson-designer names its own 9Slide fonts and Noto
 families that must be uploaded; canva-prompt-creator names Google families. Neither tells you
 which *template-available* families actually render Vietnamese diacritics correctly at display
 sizes in Canva, nor how to QA diacritic clipping on a thumbnail.
9. **Cost/quota budgeting for `create-design`.** canva-creator's budget model is for autofill and
 export calls. Nothing tells you how many `create-design` generations a deck of N slides should
 cost, or how to degrade when `generate-image` returns `credit_quota_exceeded` (V14) — the
 documented fallback of "generate an icon image and `insert_fill` it" is unavailable when image
 generation itself is out of credits.
10. **Accessibility inside Canva.** design-pack and oma-slide give WCAG ratios for CSS; none
 addresses alt text or reading order in a Canva design, and no MCP tool in our set exposes
 alt text. The skill should state the limit rather than imply compliance.
11. **A verification checklist that reads the committed design back.** Only rifater screens content
 (`get-design-content`), and only for candidates. Nobody documents a final pass that reads every
 page's text, compares it against the approved outline, checks page count, checks diacritics,
 and only then exports.
12. **Text-box measurement.** carousel-builder's character budgets came from a hand-measured
 template. For a generated deck nobody explains how to measure the actual box width a run of
 text occupies (the transaction gives `top/left/width/height`, so it is possible) in order to
 predict reflow before committing a longer string.
