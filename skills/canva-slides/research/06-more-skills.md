# 06 — Second sweep: additional skills worth studying

Scope: skills NOT already cloned under `/tmp/skills-src` (that set covered 32 repos: canva-sdks/canva-skills, openai/plugins, TerminalSkills/skills, Gabberflast/academic-pptx-skill, SlideSpeak, marp skills, pitch-deck skills, etc.). All new clones live in `/tmp/skills-src2/<owner>_<repo>/` (markdown/json/txt only). Paths cited below are relative to `/tmp/skills-src2/`.

Target environment reminder used for every "mismatch" judgement: the mounted Canva MCP exposes `create-design`, `get-create-design-async-job`, `start-editing-transaction`, `perform-editing-operations`, `commit-editing-transaction`, `cancel-editing-transaction`, `get-design`, `get-design-content`, `get-design-pages`, `get-design-thumbnail`, `get-presenter-notes` (read-only), `merge-designs`, `copy-design`, `resize-design`, `export-design`, `create-upload-url`, `upload-asset-from-url`, `generate-image`, `list-brand-kits`, `search-brand-templates`, `create-design-from-brand-template`, `autofill-design`, `search-designs`, `create-folder`, `move-item-to-folder`, `comment-on-design`, `get-assets`. Editing ops available: `update_title`, `replace_text`, `find_and_replace_text`, `format_text`, `update_fill`, `insert_fill`, `delete_element`, `position_element`, `resize_element`, `update_autofill_field` — **no `add_text`, no shape insertion, no z-order op, no page create/reorder outside `merge-designs`**.

---

## Search log

All queries run with `gh api search/repositories` (repo search) or `gh api search/code` (code search). "Triaged" = results whose title/description I read; "cloned" = shallow markdown-only clone.

| # | Query | Kind | Raw hits | Triaged | Cloned / kept |
|---|---|---|---|---:|---|
| 1 | `canva mcp skill` (sort=stars) | repo | 21 | 25 | 2 |
| 2 | `canva connector skill in:name,description,readme` | repo | 15 | 15 | 0 |
| 3 | `canva skills agent in:name,description` | repo | 15 | 15 | 1 |
| 4 | `lecture slides skill in:name,description` | repo | 15 | 15 | 1 |
| 5 | `presentation speaker notes skill in:name,description` | repo | 15 | 15 | 4 |
| 6 | `seminar defence slides` | repo | 2 | 2 | 0 |
| 7 | `thesis defence presentation skill` | repo | 0 | – | – |
| 8 | `vietnamese presentation slides` | repo | 6 | 6 | 0 |
| 9 | `accessibility contrast slides skill` | repo | 0 | – | – |
| 10 | `WCAG contrast slide deck skill` | repo | 0 | – | – |
| 11 | `diagram infographic skill agent slides` | repo | 1 | 1 | 0 |
| 12 | `data visualization slide skill` | repo | 10 | 10 | 0 |
| 13 | `chart design skill claude` | repo | 12 | 12 | 1 |
| 14 | `rehearsal timing presentation skill` | repo | 0 | – | – |
| 15 | `presentation skill claude code slides` | repo | 15 | 15 | 1 |
| 16 | `awesome presentation skills agent` | repo | 12 | 12 | 1 |
| 17 | `keynote slide deck skill agent` | repo | 3 | 3 | 0 |
| 18 | `teacher slides canva skill` | repo | 0 | – | – |
| 19 | `infographic SVG diagram skill claude` | repo | 2 | 2 | 1 |
| 20 | `Q&A preparation presentation skill` | repo | 0 | – | – |
| 21 | `public speaking practice skill agent` | repo | 1 | 1 | 1 |
| 22 | `canva mcp` (sort=updated) | repo | 20 | 20 | 0 |
| 23 | `canva api automation` | repo | 20 | 20 | 0 |
| 24 | `canva connect api` | repo | 20 | 20 | 1 |
| 25 | `canva agent skill` | repo | 20 | 20 | 1 |
| 26 | `education lecture deck generation skill` | repo | 0 | – | – |
| 27 | `vietnamese education skill` | repo | 4 | 4 | 0 |
| 28 | `academic presentation skill defense` | repo | 5 | 5 | 2 |
| 29 | `conference poster skill academic` | repo | 5 | 5 | 1 |
| 30 | `chart selection data visualization skill claude` | repo | 0 | – | – |
| 31 | `explainer diagram skill SVG agent` | repo | 7 | 7 | 1 |
| 32 | `slide design system typography scale skill` | repo | 1 | 1 | 0 |
| 33 | `color palette contrast checker skill` | repo | 0 | – | – |
| 34 | `start-editing-transaction canva` | code | 0 | – | – |
| 35 | `perform-editing-operations` | code | 473 | 20 | 0 (all already known) |
| 36 | `merge-designs canva` | code | 0 | – | – |
| 37 | `canva filename:SKILL.md` | code | 174,336 | 30 | 0 |
| 38 | `canva path:.claude/skills` | code | 56,192 | 30 | 0 |
| 39 | `canva path:.agents/skills` | code | 54,976 | 30 | 0 |
| 40 | grep `canva` in `cosen1024/awesome-presentation-skills` | file grep | 7 entries / 1 match | 1 | 0 |

Notes on the search log:

- **Code search is near-useless for Canva MCP**: `start-editing-transaction` and `merge-designs` return 0 hits, and `perform-editing-operations` only surfaces files already in `/tmp/skills-src` plus `CEOGPS/life :: perform-editing-operations.json` (a single JSON dump, no prose, no skill). `canva filename:SKILL.md` matches any skill that merely *mentions* Canva in prose, so the top 30 are almost all unrelated (whiteboard video, ASO screenshots, UI skills).
- **The productive query pattern was repo search on capability words**, not tool names: `academic presentation skill defense`, `presentation speaker notes skill`, `explorer/diagram`, `chart design skill`. Repo-name search finds the skill, code search finds nothing because the Canva tool names live inside the MCP server, not in the skills.
- **Vietnamese**: only 6 hits total for `vietnamese presentation slides`, and all are one-off *decks* (slidefly, slide-morph, su-viet-3d, goldml1, water-rocket, lam-slide), not skills to study. `vietnamese education skill` yields 4 unrelated repos. Conclusion recorded in Gaps: there is no Vietnamese-language deck-authoring skill anywhere on GitHub worth copying; the language handling has to be authored.
- **Accessibility**: 0 hits for any "accessibility/contrast + slides" query. The only real accessibility material found is `kasparnorge/canvas-lms-skills` (WCAG 2.1 AA for Canvas LMS pages) reached from query 25/22 — adjacent product, transferable criteria.
- **Rehearsal / timing / Q&A**: 0 direct hits. Timing and notes knowledge came indirectly from `presentation speaker notes skill` (Nathanielguo) and `public speaking practice skill agent` (talk-like-ted); Q&A came from a Chinese academic skill (`bushiAgoni`) and from `Geongyu`'s QA gates.
- Skipped on principle: leaked/system-prompt repos (`Omnls/system-prompts-and-models-of-ai-tools-chinese` appeared in query 35), Canvas **LMS** MCP servers (a different product — `vishalsachdev/canvas-mcp`, `ynbh/canvasmcp`), infinite-canvas image generators, and Affinity/Photoshop bridges (`aboalrejalai/affinity-mcp`).

---

## Ranked finds (all additional finds, relevance 1–5)

Relevance is to *one detailed Canva-MCP slide skill for a Vietnamese university student defending coursework*. Stars/license/last-push read from the GitHub API on 2026-11-07.

| # | Repo | ★ | License | Last push | Rel. | Why ranked here |
|---|---|---:|---|---|---:|---|
| 1 | `OrrZwebner/academic-poster` | 0 | MIT | 2026-10-12 | **5** | The only skill in the whole sweep with a **Canva-MCP-specific recipe + gotcha table + verification loop**, plus a 5-lens pre-print review. Poster-shaped, but the MCP half is deck-shaped. |
| 2 | `Nathanielguo/presentation-speaker-notes` | 2 | NONE | 2026-07-16 | **5** | Full deterministic timing model (per-slide-type seconds, bounded modifiers, deviation threshold) and a notes standard with three script layers. Nothing else in the sweep is close. |
| 3 | `AI272/speaker` (ppt-speech-writer) | 476 | NONE | 2026-06-23 | **5** | Pause-adjusted speaking rates, banned "this slide shows" openings, grounding contract. Highest-starred genuinely useful find. |
| 4 | `bushiAgoni/academic-slide-minimalist` | 1 | MIT | 2026-06-10 | **5** | 10 required Q&A question types, claim risk levels, figure-readability thresholds, 10-dimension score out of 100. The Q&A half of the workflow lives here. |
| 5 | `Faust-Donf/beamer-academic` | 330 | MIT | 2026-08-17 | **5** | 16 slot-defined academic layouts with hard per-layout text budgets; anti-AI title red flags; rhythm rule. Best *content-shape* library found. |
| 6 | `Geongyu/academic-conference-presentation` | 2 | NONE | 2026-10-24 | **4** | 6 QA gates, honest release statuses, pt-level type scale for 16:9, WCAG contrast targets, and a "no reasoning traces in slide text" wording gate. |
| 7 | `YuliangXiu/lecture-slides` | 12 | NONE | 2026-09-20 | **4** | "Layout Doctrine" distilled from **151 real layout complaints** — media ≥80% height, text column ≤1/3, never crop, kill sparse pages. Directly matches this user's feedback pattern. |
| 8 | `lewislulu/html-ppt-skill` | 9008 | MIT | 2026-09-14 | **4** | Speaker-notes iron rules (150–300 characters, 2–3 min/slide, signal not script) and a presenter-mode spec: current/next/script/timer. |
| 9 | `myunwang/ppt-report-skills` | 78 | MIT | 2026-06-03 | **4** | Chart-selection decision table with golden bans (no pie >5, no 3D, y from 0) and an 8-level type scale with px values. |
| 10 | `bentossell/visualise` | 487 | NONE | 2026-03-12 | **4** | Diagram construction rules with real numbers (60px gaps, 24px padding, 4–5 nodes max) and a chart-type table. |
| 11 | `0frost0/academic-evidence-ppt` | 2 | MIT | 2026-10-14 | **4** | Page-type × "what the audience must understand" × "common failure" table; evidence/provenance discipline for figures. |
| 12 | `kanazawahere/talk-like-ted-skill` | 0 | NONE | 2026-09-03 | **3** | Delivery/rehearsal framework: 18-minute rule, story-before-numbers, 60–90 second answer drills. |
| 13 | `borjaperfra/beatdeck` | 232 | NOASSERTION | 2026-10-01 | **3** | 1920×1080 stage, one click = one beat, content-audit ledger and a genuinely strict verification checklist. |
| 14 | `PHY041/claude-skill-academic-ppt` | 31 | NONE | 2026-03-23 | **3** | Pyramid Principle mapping per deck type, **action titles**, ghost-deck test. |
| 15 | `kasparnorge/canvas-lms-skills` | 0 | CC-BY-SA-4.0 | 2026-11-04 | **3** | The sweep's only real accessibility reference: WCAG 2.1 AA pass/fail table with contrast ratios and a checklist. |
| 16 | `appautomaton/presentation` (consultant) | 66 | NONE | 2026-09-13 | **3** | Answer-first / one-message-per-unit instincts, pp vs %, "so what" test. Content-side only. |
| 17 | `wkl0830-glitch/opencode-skills` | 0 | NONE | 2026-10-24 | **3** | Canva MCP connection matrix (two endpoints, DCR vs client secret) and a free-vs-Pro quota table (20 vs 200 AI generations/month). |
| 18 | `hritikvaidwan007/visual-explainer-diagrams` | 1 | NONE | 2026-09-04 | **3** | Diagram-family routing and a visual quality bar for "presentation-quality" figures. |
| 19 | `YuliangXiu/lecture-slides` → `lecture-deck-pipeline` | 12 | NONE | 2026-09-20 | **2** | Thumbnail-wall review + hash/pixel two-layer acceptance. Scaffolding for a bespoke HTML engine; only the review idea transfers. |
| 20 | `hasnainXdev/canva-mcp-and-linkedin-skills` | 1 | NONE | 2026-06-19 | **2** | One-idea-per-slide / ≤2 fonts / visual-mapping table; no MCP operations, generic. |
| 21 | `interagents-ai/openclaw-skill-canva` | 0 | MIT | 2026-04-12 | **1** | Thin wrapper: "use the MCP, return an edit link". One rule worth keeping. |
| 22 | `CatLollipop/dsh-canva` | 0 | MIT | 2026-10-23 | **1** | Byte-identical copy of `canva-sdks/canva-skills` (verified with `diff -q`); already studied. |
| 23 | `studioizle/canva-skills` | 0 | NONE | 2026-11-04 | **1** | Six Portuguese Canva composition skills built from a video-course evidence catalogue (`references/catalogo.json` holds frame timestamps, not design rules). Process theatre, no MCP calls. |
| 24 | `goutham-11-16/Pluto-Agent-Browser` (`.agents/skills/canva`) | 1 | NOASSERTION | 2026-07-20 | **1** | Browser-automation "recreate this image in Canva" mode; contradicts an MCP-first workflow. |
| 25 | `meghal86/stacksignal` (`.agents/skills/canva`) | 0 | NONE | 2026-05-17 | **1** | Canva **Connect REST** (client id/secret, `api.canva.com/rest/v1`), not MCP; different auth surface. |
| 26 | `cosen1024/awesome-presentation-skills` | 9 | CC0-1.0 | 2026-11-06 | **1** | Only 7 catalogue entries; one Canva-adjacent hit (`lewislulu/html-ppt-skill`). Weak as an index. |

---

## Inventory

| Skill (dir under `/tmp/skills-src2`) | Repo path | License | One sentence | Verdict |
|---|---|---|---|---|
| academic-poster | `OrrZwebner_academic-poster/skills/academic-poster/` | MIT | Paper→print-ready poster with a Canva-MCP build route, fig export, and five-lens pre-print review. | **A** — the only concrete, battle-tested Canva MCP recipe + gotcha table in the sweep. |
| presentation-speaker-notes | `Nathanielguo_speaker-notes/` | NONE | PPTX→timed multi-layer speaker notes with deterministic timing math and whole-deck review. | **A** — timing model is fully specified (ranges, modifiers, formula, threshold). |
| ppt-speech-writer (speaker) | `AI272_speaker/ppt-speech-writer/` | NONE | Grounded slide-by-slide academic notes with pause-adjusted rates and banned openings. | **A** — best speaking-rate calibration and strongest anti-slop opening list. |
| academic-slide-minimalist | `bushiAgoni_academic-slide-minimalist/academic-slide-minimalist/` | MIT | Paper→20+ page academic deck with figure integrity gates, Q&A prep and a 100-point rubric. | **A** — the only file set that prepares *questions*, not just slides. |
| beamer-academic | `Faust-Donf_beamer-academic/` | MIT | Thesis-defence Beamer generator with 16 layout skeletons and hard text budgets. | **A** — layout library with per-slot word counts; anti-AI title checks. |
| academic-conference-presentation | `Geongyu_academic-conference/` | NONE | Evidence-grounded conference deck with six QA gates and honest release statuses. | **A−** — QA gates and pt type scale are the most rigorous found; some gates are PPTX-tooling-specific. |
| lecture-slides | `YuliangXiu_lecture-slides/lecture-slides/` | NONE | HTML lecture-deck design system (magazine style) + Layout Doctrine E1–E11. | **A−** — the doctrine is empirically derived from real complaints; style tokens are HTML-only. |
| lecture-deck-pipeline | `YuliangXiu_lecture-slides/lecture-deck-pipeline/` | NONE | Build/verify/polish ops for the same HTML scaffold (hash + pixel acceptance, thumbnail wall). | **B−** — good review pattern, rest is private scaffolding. |
| html-ppt-skill | `lewislulu_html-ppt-skill/` | MIT | 36 themes / 36 layouts / 27 animations HTML deck studio with presenter mode. | **B+** — notes iron rules + presenter card spec are directly reusable; theme library is CSS. |
| ppt-report-skills | `myunwang_ppt-report-skills/` | MIT | Data-report deck generator (1600×900, one file per slide) with ECharts and a token system. | **A−** — chart-mapping bans and 8-level type scale are the most usable dataviz rules found. |
| visualise | `bentossell_visualise/` | NONE | Inline SVG/HTML diagram and chart renderer with design tokens and layout math. | **B+** — diagram geometry numbers are precise and transferable to slide figures. |
| visual-explainer-diagrams | `hritikvaidwan007_visual-explainer-diagrams/` | NONE | Presentation-quality architecture/process diagrams from prose. | **B** — good routing + quality bar, thinner on numbers. |
| academic-evidence-ppt | `0frost0_academic-evidence-ppt/` | MIT | Editable academic deck from paper with page-type contract and evidence provenance. | **B+** — best "what a page type must make the audience understand" table. |
| claude-skill-academic-ppt | `PHY041_academic-ppt/` | NONE | Defence PPTX from LaTeX/PDF with Pyramid Principle and action titles. | **B** — action-title + ghost-deck test is the keep; toolchain is LaTeX/PPTX. |
| talk-like-ted | `kanazawahere_talk-like-ted/` | NONE | Nine delivery secrets from Gallo's book with rehearsal drills. | **B−** — book summary; useful for delivery/pace, not for slide craft. |
| beatdeck | `borjaperfra_beatdeck/skills/building-a-beatdeck/` | NOASSERTION | Talks as scenes/beats on a fixed 1920×1080 React stage. | **B** — beat model + content-audit ledger + verify checklist; React-only. |
| consultant | `appautomaton_presentation/consultant/` | NONE | MBB-style structuring and deliverable content (no visuals). | **B** — four instincts worth quoting; deliberately hands off visuals. |
| opencode canva-mcp | `wkl0830-glitch_opencode-skills/canva-mcp/` | NONE | Configure Canva MCP (edu accounts), verify entitlements, triage auth errors. | **B−** — short, but the endpoint/quota facts are correct and useful. |
| canvas-html (Canvas LMS) | `kasparnorge_canvas-lms-skills/skills/canvas-html/` | CC-BY-SA-4.0 | What Canvas LMS does to HTML + how to meet WCAG 2.1 AA. | **B−** — different product; WCAG table is the transferable part. |
| canva design-optimization | `hasnainXdev_canva-mcp-linkedin/.agent/skills/design-optimization-skill/` | NONE | Generic "LinkedIn carousel" design principles. | **C** — correct but generic; no MCP operations, no numbers beyond colours. |
| canva (OpenClaw) | `interagents-ai_openclaw-skill-canva/` | MIT | Thin wrapper telling an agent to prefer the Canva MCP over browser automation. | **C** — 68 lines, one rule (always return an edit link). |
| canva (Pluto browser) | `goutham-11-16_Pluto-Agent-Browser/.agents/skills/canva/` | NOASSERTION | Browser-driven "recreate this uploaded design in Canva" mode. | **C** — UI automation, contradicts MCP-first; designer-persona lines only. |
| canva (Connect REST) | `meghal86_stacksignal/.agents/skills/canva/` | NONE | Connect REST client skill (client id/secret, `/rest/v1`). | **C** — different API surface from our MCP. |
| canva skills (pt-BR) | `studioizle_canva-skills/` | NONE | Six composition skills derived from a video course's frame catalogue. | **C** — provenance-heavy, no tool calls, no reusable thresholds. |
| dsh-canva | `CatLollipop_dsh-canva/` | MIT | Copy of `canva-sdks/canva-skills`. | **C** — duplicate, already studied. |
| awesome-presentation-skills | `cosen1024_awesome-presentation-skills/` | CC0-1.0 | Curated catalogue of 7 presentation skills. | **C** — too small to be an index; one useful pointer. |

---

## Skill: academic-poster (OrrZwebner) — the Canva-MCP reference implementation

**Purpose.** Turn a paper into a print-ready poster, or review any existing poster, working *natively in Canva through the MCP* when the connector is present, otherwise as an editable PPTX. Every sentence stays traceable to the paper.

**Process as prescribed** (`OrrZwebner_academic-poster/skills/academic-poster/SKILL.md`, §1–§4):

1. Intake once per chat: detect Canva tools by name; verify with one read-only call; find/create `poster-rules.md`; ask the approval style (ask-once-at-PLAN / live-in-Canva / approve-reject-Markdown); collect planning fields (paper, figures, venue + print size + rules URL, audience, sections, wording mode, minimum text size, branding, QR, build route); pick the mode and say it out loud.
2. Modes: SETUP, PLAN, BUILD (Canva), BUILD (PPTX), TEXT-EDIT, FIGURES, VERIFY/EXPORT, REVIEW. A request spanning modes runs PLAN → approval → FIGURES → BUILD → VERIFY.
3. PLAN measures the real state (read design + PNG export), then writes each change as an exact operation with px geometry, style, wording slot and media key, showing the space-budget arithmetic; forks become OPEN DECISIONS with 2–4 options and a recommendation first.
4. BUILD on a **copy** only: `copy-design` → open transaction → batches of ≤15 operations → verify geometry after each batch → commit under the stored approval style → export into a new dated folder.
5. VERIFY: wording traceability + claims check + PNG crop inspection + print PDF check.
6. REVIEW: five lenses (visitor, preflight, proofread, venue, design) fanned out to subagents, merged, de-duplicated, ranked, delivered as one Markdown file with one crop per finding.

**Concrete rules and numeric thresholds**

| Rule | Value | Source |
|---|---|---|
| Print floor for all text (incl. inside figures) | 24 pt at print size = 32 px on a design at print size | `.../SKILL.md` §3 "Print floor"; `references/layout-and-typography.md:18-30` |
| Image resolution at placed size | ≥150 PPI (venue "ideal" reported separately) | §3; `references/layout-and-typography.md:29` |
| Safe margin | ink ≥10 mm from every edge (≈38 px); ask print shop about 3 mm bleed | `references/layout-and-typography.md:33` |
| Type scale at print size | title 110–120 px, subtitle 64–68, authors 44–52, section head 64–70, sub-head 48–60, body 36–42, captions 34 | `references/layout-and-typography.md:20-30` |
| Word budget | ~300–800 words whole poster | `references/layout-and-typography.md:38` |
| Contrast | ≥4.5:1 normal text, ≥3:1 large (≥18 pt / ≥14 pt bold) | `references/layout-and-typography.md:47-49` |
| Canva ops per call | ≤15, `finalize: "keep_open"` | `references/canva-mcp-recipe.md:15` |
| Font size | integers only; round then re-check the floor | `references/canva-mcp-recipe.md:29` |
| Line height | 1.2–1.3 for body | `references/canva-mcp-recipe.md:29` |
| Aspect check | image `height/width` within 0.1 % of `px_h/px_w` | `references/canva-mcp-recipe.md:73` |
| Merge | **one operation per call** | `references/canva-mcp-gotchas.md:12` |
| Export for viewing | PNG width 1700; crops at full design width; print = PDF pro quality | `references/canva-mcp-recipe.md:89-92` |
| Review merge tolerance | same box ±0.02 and same problem → one finding | `references/pre-print-review.md:58` |

**The gotcha table** (`references/canva-mcp-gotchas.md:7-28`) is the single most valuable artefact in the sweep. Observable symptoms and causes that generalise to slides:

- New text arrives as **16 px black in the heading font**; fonts cannot be set over MCP; `format_text` must follow every text insertion and the author applies fonts by hand with **Copy style**.
- `update_fill`/`crop_media` **zoom the image 1.2–4×**; prefer delete + `insert_fill` (cover-fits).
- `insert_fill` can fail with `media bundle not found`; recover by exporting the element on white and black, difference-matting the alpha, re-uploading.
- **Element IDs differ per copy and per page** and change after copies — always take IDs from the document returned by the latest edit call.
- Headings read as "ntroduction"/"ethodology" because the drop-cap is a separate element; match by geometry + remaining text.
- Thumbnails go stale (`No stored thumbnail`); trust `design_content` or a fresh export.
- `resize-design` was observed to shift blocks ≈+130 px vertically and displace header items → re-place every element at `source × s` and restore minimums.
- `read-design` overflows the tool output on a dense sheet → filter fields/pages, or read the spilled file by character ranges.
- `generate-image` rate-limits at ~10 calls/minute.
- **There is no delete-page operation** — ask the user (see mismatch note below: our server *does* have `delete_pages` on `merge-designs`).
- Free-plan `resize-design` quota errors; export downsamples to ≤800 px at "standard" quality.

**Unique ideas not found elsewhere**

1. **Wording fidelity as a computable property**: each poster fragment must be an *ordered subsequence* of a cited source line ±1 window (`verify_wording.py`), and every number must appear in the paper or be registered with a derivation (`check_claims.py`). This is the only anti-hallucination mechanism in the sweep that is mechanical rather than aspirational.
2. **Approval-style setting stored in a rules file** (ask once at PLAN vs live-in-Canva vs approve/reject Markdown), so the agent stops asking mid-build.
3. **Five-lens review with fractional crop boxes** and a fixed finding JSON schema (`references/pre-print-review.md:66-73`) — makes review output diffable and re-renderable.
4. **Space-budget arithmetic before editing** ("show the arithmetic, check every minimum") rather than "make it fit".
5. **Deviation reporting**: the build report states pass/fail per check plus every deviation, so an unverified item can never read as verified.

**Pitfalls it warns about**

- Two parallel builds of the same target; pick one main design and record it.
- Falling back to "please do these steps by hand" — automate through MCP; involve the user only for decisions, page deletion, font application (and plan upgrades).
- Rebuilding a poster element-by-element to change size loses fonts and media; use resize or copy an already-sized page.
- Planning against a stale "main" design without re-reading live state.
- Truncating research questions, and reusing a data colour for decoration (`references/pre-print-review.md:91-94`).

**What is outdated or impossible against our MCP**

- Whole tool vocabulary differs: it calls `read-design` (with `open_transaction`, `filter.fields`) and `edit-design` (with `operations`, `finalize: keep_open|commit`). Ours is `start-editing-transaction` → `perform-editing-operations` → `commit-editing-transaction`. Behaviour (open → batch → verify → commit) maps 1:1; the call names do not.
- **`insert_shape` does not exist here.** No native rectangles, bands, rules, circles or arrows. Every panel, divider or arrow must be uploaded as PNG/SVG via `create-upload-url` + `insert_fill`, or inherited from the template.
- **`add_text` does not exist here.** No new text boxes at all. Content must go into existing boxes (`replace_text`, `find_and_replace_text`), which makes the "space budget" rule harder: new prose has to *replace* prose, not extend it.
- **`layer_element` (z-order) does not exist.** Z-order is insertion order plus the known "inserted fills sit above existing elements" behaviour, so background panels must be present in the template or be full-slide fills inserted first.
- **`crop_media` and `update_stroke_properties` do not exist.** `update_fill` exists but with the same zoom hazard.
- **`add_page`/`reorder_page` do not exist**, but the skill's "no delete-page, ask the user" is wrong for us: `merge-designs` supports `delete_pages`, `insert_pages`, `move_pages`, `create_new_design`. Page surgery is possible — as one operation per call.
- Its SETUP section says the **Canva Dev MCP (`@canva/cli`) is the wrong server** — correct for us too: we are on the connector endpoint, not the CLI.
- Everything print-specific (PPI, bleed, CMYK, QR decode at 300 dpi, `check_export.py`) is out of scope for a 1920×1080 slide deck; keep only the "check the export, don't trust thumbnails" habit.

---

## Skill: presentation-speaker-notes (Nathanielguo) — timing and notes

**Purpose.** Take an existing PPTX and produce a new, validated deck with timed multi-layer speaker notes, without touching the design.

**Process** (`Nathanielguo_speaker-notes/SKILL.md:10-24`): validate the file → copy to a project dir → inspect + render → build `deck-manifest.json` once → analyse the whole deck (goal, takeaway, arc, chapters, key slides, gaps) → allocate time → resolve style → one Schema-validated brief per slide → generate notes in verbatim/outline/hybrid mode → whole-deck consistency review + independent style review (max one localized style revision) → project only `main_script` into Notes → reopen and verify page count, note count, text and source hash.

**Concrete rules and thresholds**

- **Per-slide-type timing budget** (`references/timing-allocation-rules.md:14-25`): cover 15–30 s; section divider 10–20 s; simple conclusion 30–60 s; ordinary content 45–90 s; chart 60–120 s; process 60–120 s; core solution 90–180 s; case 90–180 s; summary 60–120 s; appendix **0 s by default**.
- **Allocation order** (`:29-40`): zero the hidden/appendix slides → reserve slide overrides → reserve chapter overrides → baseline per type → apply modifiers → normalise to the remaining total → clamp and redistribute → record "infeasible timing" when fixed overrides exceed the total. Slide overrides beat chapter overrides; explicit user seconds beat inferred importance.
- **Bounded modifiers** (`:44-54`): text density 0.85 / 1.0 / 1.15; chart complexity 1.0 / 1.15 / 1.3; key slide 1.2–1.5; interaction adds explicit seconds. "Do not reward visual clutter with unlimited time."
- **Timing math** (`:82-87`): `estimated = spoken_units / wpm * 60 + interaction_seconds`; `deviation = |est − allocated| / max(allocated,1)`; recalibrate when deviation > **0.15**, one targeted rewrite only.
- **Chinese reference rates** (`:89-94`): slow training 180–230 characters/min; professional stable 220–260; natural 250–300.
- **Shorten order** (`:101-106`): repeated setup/conclusion → optional examples and minor detail → redundant transitions → secondary evidence. **Lengthen order** (`:108-113`): explain an already-visible relationship → implication for this audience → allowed analogy/reflection question → clearer bridge. "Never add new data or professional claims to fill time."
- **Notes standard** (`references/speaker-notes-standard.md:12-24`): one defensible core message per slide; natural spoken syntax; do not start with "this slide / we can see / as shown"; do not read every bullet; do not invent names, dates, sources, sample sizes or outcomes; delivery actions live in cues, not prose.
- **Three layers** (`:26-34`): `main_script` (fits the allocation), `optional_expansion` (if time remains), `compressed_fallback` (shortest safe version). No new claim only in an optional layer; no safety/uncertainty boundary removed from the compressed layer.
- **Outline mode shape** (`:42-52`): opening conclusion/question → must-say evidence → interpretation → emphasis/pause cue → transition. "Do not write a hidden verbatim script under bullet formatting."
- **Per-type speaking shape** (`:95-103`): chart = conclusion → decisive trend → qualified interpretation → significance; process = whole path → critical nodes → dependencies → meaning; comparison = criterion → difference → trade-off → implication.
- **Verification** (`:77-92`): required artefacts include `deck-analysis.json`, `slide-briefs.json`, `quality-report.json`, `speaker-script.md`; the delivered Notes body is the exact validated `main_script` with no labels, timing or JSON.

**Unique ideas** — the layer model (main / optional / compressed) for live time adaptation, and the "record an infeasible timing risk" escape valve instead of silently squeezing content.

**Pitfalls** — reading bullets, "this slide" openers, report prose instead of speech, style targets leaking into facts, and claiming "naturalness" from a deterministic (non-model) run.

**Mismatch with our MCP** — everything here assumes PPTX Notes injection (`python-pptx`). Our `get-presenter-notes` is **read-only** and there is no notes-write tool, so the deliverable must be a **sidecar Markdown script keyed by page number**, exported next to the deck. The timing model, layer model and quality gates transfer unchanged; only the injection step does not.

---

## Skill: ppt-speech-writer / speaker (AI272) — pacing and openings

**Purpose.** Read a real `.pptx` (text + OOXML + rendered screenshots + OCR + visual inventory) and write academic speaker notes grounded in what is actually visible, then inject clean notes and produce a rehearsal document.

**Process** (`AI272_speaker/ppt-speech-writer/SKILL.md:10-20`, `LOGIC.md`): structured extraction → render one PNG per slide → visual inventory with OCR restricted to image regions → vision review packet → draft → inject → validate. A slide counts as "read" only after all five evidence passes.

**Concrete rules and thresholds**

- **Planning rates with pauses already absorbed** (`SKILL.md:87-91`): English **110 words/min** (range 100–130; use 100 for dense or non-native delivery); Chinese **165 characters/min** (range 150–180; count characters, not words).
- **Calibration beats defaults** (`:92`): if a 15-minute talk actually took 30, recompute at 1800/30 = 60 effective wpm.
- **Reserve before budgeting words** (`:96-100`): ≈3 s per slide transition, ≈1.5 s per deliberate `[PAUSE]`, and a **10–15 % global buffer**.
- **Banned openings** (`:52-68`): "This slide shows/presents/explains…", "On this slide…", "Here we can see…", "The slide is about…" and the Chinese equivalents. Weak → strong example: "This slide shows the optimization setup" vs "The experiments use a fixed optimization protocol so later comparisons stay controlled."
- **Language lock** (`:22-46`): confirm one output language before writing; never mix sentence grammar; keep canonical technical terms.

**Unique ideas** — the *grounding contract* (you may not describe a chart you could not read; ask instead), and the explicit "don't treat raw word count as speaking time" rule.

**Pitfalls** — inferring output language from chat language; narrating the slide object instead of the claim; inventing axis values or screenshot text.

**Mismatch with our MCP** — PPTX-centric. For Canva we substitute `get-design-content` (text extraction) + `get-design-thumbnail` per page (inside a transaction) for the render pass. There is no notes-injection path, so again: sidecar file. Its OCR/vision stack is heavier than a slide deck needs.

---

## Skill: academic-slide-minimalist (bushiAgoni) — Q&A, figure discipline, scoring

**Purpose.** Build (or critique) Chinese academic literature-report/thesis-defence decks from a paper, with real figures only, a fixed page rhythm, and defensible claims.

**Process** (`bushiAgoni_.../SKILL.md:8-110`): derive paper-specific navigation (never hard-code the six-section bar) → `deck_order_map.md` → separate mainline vs backup → one style contract across batches → real figures only → track generation status → assemble from the approved folder → diagnosis mode before redrawing → score.

**Concrete rules and thresholds**

- **Non-negotiable figure rule** (`SKILL.md:20-49`): only real figures from paper/SI/screenshots; allowed operations are crop, scale, align, mask margins, simple labels, thin boxes/arrows/lines, short callouts. Never regenerate a micrograph, spectrum, mechanism, table or performance chart.
- **Default length** (`:51-61`): **≥20 pages** unless the user asked for fewer; one page per claim; split dense results rather than crowd.
- **Rubric** (`references/final-scoring-rubric.md:5-45`): ten dimensions ×0–10 = 100; bands 90–100 presentation-ready, 80–89 strong with fixes, 70–79 usable draft, <70 do not present. Never score high if scientific visuals are not traceable; penalise overclaiming and unreadable-in-presentation-mode slides.
- **Q&A types** (`references/question-prep.md:11-22`): motivation, novelty, method validity, figure interpretation, controls, mechanism, fair comparison, stability/reproducibility, limitations, transferable insight. Template: `slide / likely question / safe answer / source support / caution`.
- **Claim risk levels** (`references/question-risk-level.md:7-39`): low = directly measured (use "shows/indicates" wording); medium = supported + interpretation (use "supports/consistent with"); high = proposed/mechanistic/conditional (use "suggests/may/the authors argue"). High-risk claims need backup support or an explicit limitation note. Common high-risk claims enumerated: mechanism proven, industry-ready, universally generalisable, single figure identifies an active site, "fair comparison across literature", simulation treated as experiment.
- **Figure readability** (`references/figure-readability-standard.md:13-49`): tables with more than ~8 readable rows go to backup (highlight this work + 2–4 comparison rows); more than **4 equally important panels** → split across slides; keep scale bars; annotations must not cover data; crop/split/enlarge instead of shrinking.
- **Gates** (`references/quality-gates.md:5-57`): intake → close reading → figure integrity → story/page (≥20 pages, one claim per slide) → layout (16:9, one dominant figure, no decorative icons/gradients) → assembly.

**Unique ideas** — the *backup-slide* concept as a first-class artefact for Q&A; the risk-level → verb mapping; and "if the figure is missing, say so rather than fabricate".

**Pitfalls** — copying a sample deck's section names instead of its rhythm; letting an image-generation model redraw scientific content; symmetric page counts over argument correspondence.

**Mismatch with our MCP** — assumes an image-generation pipeline ("image2") and PPTX assembly. In Canva, "one claim per page" translates into *one inherited page per claim*, because we cannot add pages except by `merge-designs(insert_pages)` from another design, and cannot add text boxes. The Q&A and figure-readability rules transfer intact.

---

## Skill: beamer-academic (Faust-Donf) — layout library and content budgets

**Purpose.** Generate thesis-defence / proposal / conference Beamer slides from a thesis, with a template library and an interactive revision loop.

**Process** (`Faust-Donf_beamer-academic/SKILL.md`): locate source (.tex > .docx > .pdf) → check LaTeX → ask about a school template → extract material → outline → user confirms → fill content → compile → revision loop.

**Concrete rules and thresholds** (`references/layouts.md`)

- **16 layouts**, each with typed slots: cover, toc, section-divider, text-only, text-left-image-right, image-left-text-right, formula, table, full-image, conclusion-box, transition, list, thanks, statement, stats, hypothesis. Each slot carries a **word/char budget**:
  - text-only: 2–3 paragraphs of **80–120 characters**, total **≤300**;
  - text-left-image-right: left text **120–180** characters; image column 50 %;
  - image-left-text-right: image **40–62 %** width, text **100–150** characters;
  - formula: intro 50–80 chars, explanation 80–120 chars, **≤2 equations per page**;
  - table: **3–8 rows × 3–6 columns**, highlight the row for this work;
  - list: **3–5 items**, each with a short explanation, not a bare title list;
  - conclusion-box: body 100–150 chars + keybox 50–80 chars.
- **Rhythm rule** (`references/writing-style.md:166-173`): adjacent pages must use different composition patterns — "Bad: P4 paragraph, P5 paragraph, P6 paragraph" vs "Good: P4 paragraph+keybox, P5 text+image, P6 paragraph+formula, P7 paragraph+table+conclusion".
- **Anti-AI title test** (`references/writing-style.md:7-27`): rewrite "深入探讨…/全面分析…/…的重要性/方法论/结果与讨论" into specific, informative titles; rewrite "值得注意的是…/综上所述/不难发现/显而易见"; "read every title and ask: does this read like a student defending, or like AI?"
- **Filler-word ban** and "use the paper's own terminology, no translationese".
- **One-sentence pages** (`statementframe`) for chapter ends, contributions and core judgements.

**Unique ideas** — the slot-budget table (a page type *is* a character budget), and the alternating-rhythm rule, which is the cheapest cure for a deck of identical bullet pages.

**Pitfalls** — PDF figure extraction losing quality; installing TeX mid-task; hard-coding a school template.

**Mismatch with our MCP** — Beamer/LaTeX output is irrelevant, and "13/16 layouts" cannot be applied literally because we cannot create new text boxes or shapes. Keep the *budgets* and the *rhythm rule*; realise layouts by choosing which inherited page to clone and by replacing text inside its existing slots.

---

## Skill: academic-conference-presentation (Geongyu) — QA gates and honest status

**Purpose.** Evidence-grounded academic deck (PPTX) with speaker notes, renders and a QA report; Korean-first but the gate structure is language-agnostic.

**Process** (`Geongyu_academic-conference/SKILL.md` + `references/qa.md`): plan with approval → scientific verification → automated structure check → rendered visual review → notes/delivery check → wording check → release decision.

**Concrete rules and thresholds**

- **Six gates, each PASS/FAIL/NOT_RUN** (`references/qa.md:7-99`). Gate 1 also fixes the planning target: sum estimated seconds for main slides at **≈90 % of the speaking time**, subtract a known Q&A allocation before budgeting, and record the assumption if unknown.
- **Gate 2 scientific verification** (`:23-34`): reopen the exact source version; check percent vs percentage points, absolute vs relative change, rounding, evaluation units, internal vs external testing, source qualifiers. "A mapping to a paper is not enough: the cited page/panel must support the claim." A false value, invented source, misleading crop or causal overstatement is a **blocking FAIL**.
- **Gate 4 rendered review** (`:49-67`): fresh PDF + PNG of every slide (including hidden); inspect crops, title wrapping, in-figure labels at displayed size, glyphs/superscripts/minus signs, contrast, stable series colours, redundant encoding, and "static slide/PDF comprehensibility including animation-dependent content".
- **Gate 6 wording** (`:78-98`), four mandatory checks: concrete not abstract ("significantly improved" banned); **no reasoning traces** ("검토 결과", "가정:", "[메모: …]", "this slide should emphasize"); newcomer-readable not childish; no private words (internal IDs, `Fig3a_crop`, self-coined abbreviations).
- **Release statuses** (`:100-114`): `READY` / `DRAFT — FIXES REQUIRED` / `DRAFT — VERIFICATION INCOMPLETE`; native-venue testing reported separately; "a final status must be set by the reviewing agent, not by the geometry script".
- **Type scale for 13.333×7.5 in (16:9)** (`references/design-system.md:66-79`): cover title **44 pt**; slide title **34 pt** (usually 30–40, avoid three-line headings); body **24 pt** (22–28, move detail to notes); chart labels **20 pt** (18–22 at final displayed size); citation 12 pt (12–14, essential caveats must be larger). Assess figure labels *after* scaling onto the slide, not at the source PDF's nominal size.
- **Contrast** (`:45-51`): ≥4.5:1 for ordinary text and ≥3:1 for necessary graphical marks, "prefer the stronger text target even for slide titles"; redundant encoding so colour is never the only carrier.
- **Layout grammar** (`:96-111`): ~0.55 in exterior margins; aligned title/body starts; reserved footer; use lines, spacing and typography before boxes; no mandatory card dashboard, no stock-photo background, no decorative AI illustration; preserve aspect ratios; contain-fit source panels.
- **Tool limits to state once** (`:116-131`): python-pptx does not measure text layout; a successful export is not an inspection; passing WCAG does not prove projector readability; theme generation is RGB mixing, not perceptual.

**Unique ideas** — the "no reasoning traces / no private words" wording gate (this is exactly the failure mode of agent-written decks), and the explicit **limitations section** that prevents over-claiming verification.

**Pitfalls** — describing geometry success as "no text overflow"; treating a contact sheet as proof of small-label readability; declaring approval that was never observed.

**Mismatch with our MCP** — check scripts (`check_deck.py`, `plan_check.py`) are PPTX-only. The substitutable equivalents: `get-design-content` for text, per-page `get-design-thumbnail` for a full visual pass, `export-design` for the "fresh render". The *gates* must be re-implemented as an agent checklist, not scripts.

---

## Skill: lecture-slides + lecture-deck-pipeline (YuliangXiu) — Layout Doctrine

**Purpose.** A design system for HTML lecture decks (one fixed "magazine" style) plus the ops pipeline that builds, verifies and polishes them; the interesting part is a **layout doctrine induced from 151 solved layout complaints**.

**Process** (`lecture-deck-pipeline/SKILL.md:90-104`): create lecture dir → write content module → build → generate comparison metadata → three acceptance scripts → present → optional deploy mirror. `lecture-slides/SKILL.md:32-34` routes by user sentence to a module (style / presenter / offline / QA / **layout doctrine default**).

**Concrete rules and thresholds** (`lecture-slides/SKILL.md:142-201`, module E "Layout Doctrine")

- **E1 media is the protagonist**: any page with media gives it **≥80 % of the body height** (multi-image 90–100 %, wide hero image 100 %); text retreats to a **1/4–1/3 width column** (flex 0.5–0.8, or fixed ~240 px); media column flex 1.2–1.5. "Even if there is more copy, delete words or add a page — never widen the text column."
- **E2 never crop**: each media card's aspect ratio = the media's own ratio; `object-fit: contain`; never normalise cards to one shape; in a row, equal **height**, natural differing widths.
- **E3 brick/masonry fill**: multi-image pages should tile into a **seamless rectangle with both outer edges aligned**, gaps 12–28 px, rows edge-aligned. If images are missing, add images — do not stretch.
- **E4 mutual alignment**: text card bottom edge aligns with media bottom edge; equal widths within a column; text block total height = media block total height; table fills available width with generous row padding (`td padding ≈ 23px 18px`).
- **E5 fill the space**: any large empty region is the top rejection reason; three fixes — split into small cards revealed progressively, insert relevant media, or enlarge type/leading.
- **E7 avatars** occupy ~80 % of the card, centred.
- **E10 kill sparse pages**: delete or merge thin pages rather than padding them (12 historical deletions).
- **E11 quick table**: text+media flex 0.5–0.8 (≤1/3 width) / media ≥80 % height; brick grid gap 12–28 px; media card `aspect-ratio` = source, contain, never crop; top+bottom double alignment; table `td padding 23px 18px`.
- **Presenter notes auto-size** (`SKILL.md:81`): binary-search the note font size so the block fills **80 %** of the available height, clamped **20–36 px**, line-height 1.6; measure the inner wrapper's `offsetHeight` because `scrollHeight` is clamped.
- **Two-layer acceptance** (`lecture-deck-pipeline/references/acceptance.md:25-42`): hash layer proves the generator did not change; **pixel layer** proves the render did not change — criterion: share of pixels with `max|Δ|>8` is **≤0.1 %**, sampled across four risk classes (formulas, video, multi-image, stepped animation).

**Unique ideas** — the doctrine is stated as *defaults that must be met on the first draft*, not preferences discovered through feedback ("do not make a 'normal layout' first and wait for the user to complain"). For a user who has already complained about small text and misalignment, this is the right posture. Also the thumbnail-wall review (a 76-page contact grid) and the "kill sparse pages" rule.

**Pitfalls** — cropping to make a grid tidy; text column creep; treating "fill the space" and "never crop" as conflicting (priority: keep the full frame, then add media to fill); asserting inline styles instead of rendered geometry.

**Mismatch with our MCP** — HTML/CSS only; tokens and scripts are useless here. But E1–E11 translate to Canva primitives: `resize_element` + `position_element` for the media/text split, `insert_fill` with the **exact aspect ratio** for uncropped media, `delete_element` for sparse pages, and `format_text` for the "enlarge type to fill" fix.

---

## Skill: html-ppt-skill (lewislulu) — notes iron rules and presenter mode

**Purpose.** Author static HTML decks from 36 themes, 36 layouts and 27 animations, with a built-in presenter mode (S key).

**Process** (`SKILL.md` "Before you author anything"): establish content/audience, style/theme, and structure before writing slides; then pick a full-deck template; then per-slide layout and animation.

**Concrete rules and thresholds** (`references/presenter-mode.md:51-80`)

- **Rule 1 — notes are signals, not a script**: bold the core words, put transition sentences in their own paragraph. Wrong: "大家好，欢迎来到今天的分享。今天我将要给大家介绍一下…". Right: short lines with `<strong>` on the numbers and `<em>` on the pivot.
- **Rule 2 — 150–300 characters per slide**, which is a **2–3 minute** rhythm. Under 150 → you run out of prompts mid-slide; over 300 → you cannot scan it in time.
- **Rule 3 — spoken language, not written**: "因此"→"所以", "该方案"→"这个方案".
- Presenter view = four cards: CURRENT preview, NEXT preview, SPEAKER SCRIPT, TIMER (elapsed + slide counter + prev/next/reset); previews are pixel-perfect because they load the real deck with `?preview=N`.
- Route trigger list for when presenter mode is required (mentions of 讲稿/逐字稿/speaker notes/30–45–60 minutes/"afraid of forgetting words").

**Unique ideas** — the 150–300 character band with a stated failure mode at each end; the "preview = the real deck in an iframe" trick; and treating presenter mode as a *routing decision* with explicit triggers.

**Pitfalls** — writing a hidden verbatim script under bullet formatting; giving a 45-minute talk 10 slides with 600-character notes.

**Mismatch with our MCP** — presenter view cannot be built inside Canva; the equivalent deliverable is `get-presenter-notes` (read) plus a **sidecar script file** the student keeps on a phone/tablet. The 150–300 rule maps well onto Vietnamese (150–300 *characters* ≈ 60–120 words).

---

## Skill: ppt-report-skills (myunwang) — chart selection and type hierarchy

**Purpose.** Turn multi-group business data + conclusions into a 16:9 web deck (1600×900 design space), one file per slide, ECharts charts, 5 themes.

**Process** (`SKILL.md` Step 1–2): list each page as `(label, title, subtitle/conclusion, body type)` and confirm before drawing → choose a page template by body type (KPI overview, two-object comparison, three-phase timeline, multi-trend, bars+trend, landscape map, 2×2 matrix, human portrait, value chain) → copy, change copy/data/IDs.

**Concrete rules and thresholds**

- **Chart decision table** (`references/chart-mapping.md:7-21`): multi-object single period → horizontal bars (never multi-column bars); single series over time → line with milestone lines; ≤5 series → multi-line (never stacked area); before/after → paired bars + Δ or a metric-row table; composition ≤5 items → 100 % stacked bar (**pie strongly discouraged**); >5 items with a long tail → horizontal bars Top-N + Other; ranking Top-20 → CSS mini-bars; two different units over time → dual-axis line; single KPI → metric card (no chart); 2-D distribution → heatmap; strategic positioning → **CSS 2×2 matrix, not an ECharts scatter**; funnel → funnel or decreasing bars; status overview → status cards with dots.
- **Golden bans** (`:23-30`): **no pie above 5 items**; **no 3-D charts**; dual axes only when the two units are logically related; **>7 lines must be filterable or cut**; **bar y-axis starts at 0** (except genuinely tiny variation, then say so); **no gradient fills on bars** (they corrupt precision reading).
- **8-level type hierarchy** (`references/design-system.md:5-18`), px in a 1600×900 space: L0 label 13/600 · L1 page title 36/800 · L2 subtitle-or-conclusion 18/500 · L3 section head 18/700 · L4 card title / metric 15/600 · L5 body 13/400-500 · L6 caption 12/400 · L7 mini 11/400-600. "Every text must answer: which level am I?" Do not rescale font sizes separately — the whole page scales.
- **Semantic colour contract** (`:39-54`): green = positive/complete, red = negative/risk, orange = attention, blue = brand/key number; `<strong>` only for the key number.
- **Spacing scale of 4** (`:56-68`): 4 / 8 / 12 / 16 / 20–24 / 32–40 / 48–64; slide padding 48 64.

**Unique ideas** — the 2×2 matrix as a CSS layout rather than a chart (avoids label collisions), and "one page = one label + one title + one conclusion sentence + one body type" as a pre-flight contract.

**Pitfalls** — choosing charts "by mood"; pie charts for 6 categories; stock chart-library styling that fights the deck palette; two different palettes across pages.

**Mismatch with our MCP** — the whole rendering stack is web/ECharts, so charts must become **PNG/SVG uploads** (`create-upload-url` → `insert_fill`) because we cannot draw charts natively. That makes the "one chart per figure, exported at slide resolution" workflow mandatory, and it makes the chart-selection discipline *more* important, not less.

---

## Skill: visualise (bentossell) — diagram geometry

**Purpose.** Render inline SVG/HTML diagrams, charts and interactive explainers with a token-based design system.

**Process** (`SKILL.md`): read the design system once → choose mode (SVG for static diagrams, HTML for interactive) → read the module (diagrams / components / charts) → generate → check stream constraints.

**Concrete rules and thresholds** (`references/diagrams.md:30-75`, `:99-107`)

- **Diagram families** (`:5-19`): flowchart (sequence, decisions), structural (containment), illustrative (draw the mechanism). Default to illustrative for "how does X work" — do not retreat to a flowchart.
- **Flowchart sizing** (`:32-36`): at 14 px, one character ≈ **8 px** wide; a 13-character label needs a rect **≥140 px**; **60 px between boxes**, **24 px internal padding**, **10 px arrowhead gap**, two-line boxes **≥56 px** tall; **max 4–5 nodes**; 6+ components → overview + sub-flows; single-direction flows only.
- **Structural rules** (`:64-75`): outer container radius 20–24 with the lightest fill; inner regions 8–12; **≥20 px padding** inside every container; **max 2–3 nesting levels**; nested regions need distinct ramps or the hierarchy flattens.
- **Common failures** (`:99-107`): arrow through a box; text overflow; viewBox too small; floating labels (every text belongs to a box, a legend, or a leader line); connector without `fill="none"`; missing `dominant-baseline="central"`; missing arrow marker.
- **Chart types** (`references/charts.md:69-75`): categories+values → bar (horizontal if labels long); time series → line; parts of whole → doughnut with 60 % cutout, not pie; two variables → scatter with trend line if correlation is the point.

**Unique ideas** — the character-width arithmetic ("a 13-char label needs ≥140 px") which lets you pre-size boxes instead of discovering overflow; and the failure list as a literal pre-render checklist.

**Pitfalls** — drawing cycles as rings; letting a legend float; over-nesting.

**Mismatch with our MCP** — we cannot emit SVG into the design; the numbers still matter because they define the **minimum legible size of an uploaded diagram**: at 1920 px slide width, a 140 px box at SVG-source scale becomes ~7 % of the slide width, which is about the smallest container that survives projection.

---

## Skill: visual-explainer-diagrams (hritikvaidwan) — diagram routing and quality bar

**Purpose.** Presentation-quality architecture, process and concept diagrams from prose.

**Process** (`SKILL.md:14-30`): understand the story (actors, layers, stages, decisions, dependencies, direction) → choose the family (flowchart, layered architecture, sequence, pipeline, dependency map, annotated concept map, multi-panel infographic) → design the information hierarchy (primary path heaviest, secondary quieter, labelled containers) → sketch geometry with reserved space for titles/labels/legend → render vector-first (SVG > HTML/CSS > Mermaid) → inspect and iterate → deliver editable source + raster.

**Rules** — the quality bar (`:32-45`) is a checklist: generous whitespace; strong title hierarchy; consistent node sizes and radii; restrained palette with a few semantic accents; one visual language per element class; readable at normal zoom ("never shrink text merely to fit more content"); single-meaning arrows; aligned columns; concise labels with explanations moved to callouts; subtle borders instead of heavy shadows.

**Unique idea** — "Mermaid only when its automatic layout is sufficient; do not accept a weak Mermaid result because it is quick" — i.e. the diagram's *layout* is a design artefact, not an output of the tool.

**Mismatch with our MCP** — output is SVG/HTML; here it must become an uploaded image. The "inspect the rendered artifact" step is still mandatory, via `insert_fill` + `get-design-thumbnail`.

---

## Skill: academic-evidence-ppt (0frost0) — page contracts

**Purpose.** Editable academic deck (proposal defence, thesis defence, research report) with evidence provenance, per-page speaker notes and acceptance.

**Process** (`SKILL.md` §完整工作流, 9 steps): parse material and versions (build a keep/replace/add/delete list) → design the whole argument (need → evidence → gap → goal → method → evaluation → contribution → next) → allocate chapters/pages/time by logical difficulty → build a coverage map (every source topic has a page; every claim has evidence) → fix the visual system on representative pages first → design pages by *information relation* (time → timeline, contrast → table, mechanism → diagram, evidence → real figure) → build editable output → check the whole deck and rehearse the rhythm → deliver.

**Concrete rules** — the page-type contract table (`references/page-types.md:3-24`) pairs each page type with "what the audience must understand" and "the usual failure". Examples: *current state* → "readable paper panels, comparison, or thematic grouping", failure = "listing authors by year, shrinking the original figure to a stamp"; *gap* → "difference map and specific limitation", failure = "comparing performance across different tasks directly"; *results* → "editable chart with error/interval and sample info", failure = "fake data, truncated axis, only the best run"; *limitations* → "where it fails, whether it generalises", failure = "only strengths, or unfounded generalisation"; *summary* → "what should be remembered", failure = "new method or a conclusion that never appeared".
- **Argument-coverage principles** (`SKILL.md` "不可丢失的原则"): never fabricate results, samples, performance, citations or novelty; distinguish completed / planned / illustrative / pending; do not replace a real diagram with a text box; tables that communicate clearly need no chart; enlarge the key panel and keep axes/labels — **first trim or restructure content, then shrink type**; "a programmatic check is not a visual or academic pass; if you did not render it, you cannot claim you reviewed it".

**Unique idea** — "page type is a contract with the audience": naming what the audience must *understand* (not what the slide contains) immediately exposes slides that are only containers.

**Mismatch with our MCP** — PPTX tooling again; the contract table is pure prose and transfers directly.

---

## Skill: claude-skill-academic-ppt (PHY041) — action titles

**Purpose.** Defence deck (.pptx) from LaTeX/PDF with a narrative framework.

**Concrete rules** (`content_guidelines.md:10-40`)

- **Pyramid Principle mapping**: Situation → Complication → Resolution, with slide counts per venue — defence: background 1–3, motivation 1, method+results 5–10; conference: problem 1, approach+results 4–6; seminar: context 3–5, motivation 2, method+results 10–15.
- **Action titles are "the single most important rule"**: every title is a complete sentence stating the takeaway. Good: "Pre-computed UI transition graphs reduce agent task completion time by 50 %". Bad: "Experimental Results", "Related Work", "System Architecture", "Conclusion".
- **Ghost-deck test**: read all titles in sequence with no slide content; they must tell the whole story.

**Unique idea** — action titles + ghost deck: the cheapest structural QA that exists, and it works on a deck you cannot re-layout (exactly our Canva situation, since `update_title` is available).

**Mismatch with our MCP** — LaTeX/PPTX pipeline; the rule is tool-agnostic and maps onto `update_title`.

---

## Skill: talk-like-ted (kanazawahere) — delivery and rehearsal

**Purpose.** Nine public-speaking principles from Gallo's book, with case studies and self-check drills.

**Rules** (`SKILL.md:12-27`, `cheatsheet.md:3-23`): find the real personal connection first; story before numbers (Bryan Stevenson 65 % story / 25 % data); rehearse to conversational; teach something new; at least one jaw-dropping moment (<5 % of runtime carries most of the memory); humour from observation, never scripted jokes; **the 18-minute rule** (time limits force selection and reduce the audience's "cognitive backlog"); paint mental pictures with concrete numbers instead of vague adjectives; stay in your own lane.

**Drills** (`SKILL.md` "Luyện phản xạ"): interviewer asks unpredictable questions with no advance list; self-imposed **60–90 s** per answer; after each answer score: did you open with a concrete detail or with theory, did you stay in time, did it sound memorised, is there at least one detail/number that survives 10 minutes, can you compress it to one sentence + three points.

**Unique idea** — the 60–90 second answer timer for Q&A rehearsal, which pairs naturally with a "likely questions" list on backup pages.

**Mismatch** — no tooling at all; it is a coaching framework. Use it only for the delivery/notes voice and the Q&A drill.

---

## Skill: beatdeck (borjaperfra) — beats and the content-audit ledger

**Purpose.** Author a talk as a fixed **1920×1080** stage of scenes and beats (one click = one beat), with presenter view and offline build.

**Rules** (`references/beat-model.md:23-30`, `references/checklist.md:5-42`)

- **Scene** = a stage world with its own layout; **beat** = one thing landing (a statement appears, a word is struck, a diagram gains a node, a number counts up, an image replaces another). "A scene with 12 beats probably hides two scenes." Name beats after what happens, not "beat 3".
- **Content audit**: every source slide is accounted for in `docs/CONTENT-AUDIT.md` as kept / restored / cut **with a reason**. No invented quotes, numbers, logos or URLs.
- **Verification**: every beat reached forward, backward and by direct URL renders the same frame (pixel diff ≤0.1 %); no console error; QR decodes; **no visible text outside the stage or overlapping other text**; each beat shows one idea; standby is calm and the first click starts.
- **Reduced motion** keeps the story and the hard cuts, only removes ambient/violent motion.

**Unique ideas** — the kept/restored/cut ledger (so deletion is a decision, not an accident), and "one click = one idea" as the unit of rehearsal.

**Mismatch with our MCP** — React engine; but the 1920×1080 fixed-stage assumption matches Canva presentations exactly, and every checklist item is checkable by eye on a thumbnail.

---

## Skill: consultant (appautomaton) — content instincts

**Purpose.** Produce MBB-grade *content*: structuring, frameworks, executive summaries, deck outlines. Explicitly hands off visuals.

**Rules** (`consultant/SKILL.md` §2 "Behavioral Instincts")

- **Hypothesis first**: "if you can't state what you're testing, you're browsing".
- **Answer first**: state the recommendation before the evidence; the decision-maker reads slide 3, not slide 30; conclusion → supporting arguments → data.
- **So what?**: "Revenue grew 8 %" is data; "…2 percentage points above the industry rate, confirming pricing power" is insight. Facts without implications are noise. Also defines **pp vs %**: 10 % → 8 % is a 2 pp drop, not 2 %.
- **One message per unit**: each slide/section/paragraph has one message; test = can you say it in one sentence; if not, split.

**Unique idea** — the pp/% distinction is a real exam-question trap in a philosophy/economics defence, and "answer first" is the fix for the common student pattern of building up to the conclusion.

**Mismatch** — no tooling; purely content discipline.

---

## Skill: opencode canva-mcp (wkl0830) — connection and entitlements

**Purpose.** Connect an agent to Canva (including Canva for Education) and verify that Pro/EDU entitlements are actually active.

**Rules** (`canva-mcp/SKILL.md`)

- **Two endpoints, different behaviour** (`:10-21`): `https://mcp.canva.com/mcp` = Canva's own AI Connector, DCR/CIMD, **no client secret**, any account incl. education; `https://api.canva.com/connect/v1/mcp` = self-built developer app, needs `client_id`/`client_secret`, and an unpublished app can only be authorised by its owner (others get "invalid client ID").
- **Entitlement probe** (`:68-75`): call `list-brand-kits`; IDs returned ⇒ Pro/EDU active; `{items: []}` ⇒ possibly just no kit yet, **not** a failure. Also probe `search-brand-templates`, `resize-design`, `autofill-design` (Pro-only).
- **Quota table** (`:103-111`): free = design generate/edit/search/export/comments/upload, **20 advanced-AI uses/month**; EDU/Pro = brand kits, brand templates, autofill, resize, **200 advanced-AI uses/month**; reset on the 1st at 00:00 UTC. Standard text AI is metered against the shared pool on free, uncounted on Pro.
- **Auth hygiene** (`:88-93`): OAuth credentials live on the machine, not in the config file; never put a `client_secret` in the public-endpoint config; rotate a leaked app.
- **Troubleshooting rows** (`:79-86`): invalid client ID → wrong endpoint; wrong account → log out first; education account refused → admin disabled third-party integrations; port in use → restart the service; config change ignored → restart.

**Unique idea** — the entitlement probe as a *first action*, which prevents the classic "I tried resize/brand templates and it errored, so the MCP is broken" misdiagnosis. Our account has zero brand kits and templates, so `{items: []}` is the expected answer here, and `resize-design`/`autofill-design` availability depends on the plan.

**Mismatch** — OpenCode-specific commands (`opencode mcp add`, `/mcps`). The endpoint matrix, probe, and quota numbers are server-side facts and apply unchanged.

---

## Skill: canvas-html (kasparnorge) — accessibility thresholds

**Purpose.** Explain what Canvas LMS does to HTML and how to meet **WCAG 2.1 AA** inside that sanitizer's limits.

**Rules** (`skills/canvas-html/SKILL.md:422-479`)

- **1.4.3 Contrast**: text **4.5:1**; large text (**24 px**, or about **18.7 px bold**) **3:1**. Check every fixed colour on its own panel.
- **1.4.11 Non-text contrast**: anything you must see to use or understand needs **3:1** — button outlines, rings that carry order, **chart lines**; purely decorative lines need nothing.
- **1.4.1 Use of colour**: meaning never comes from colour alone.
- **1.1.1 Non-text content**: informative images need an `alt` that says what the picture *shows*; decorative images `alt=""`; icons are decorative and the adjacent text carries the meaning.
- **2.5.8 (WCAG 2.2) target size**: targets ≥**24×24 px** or that much spacing.
- **1.4.3/1.4.4/1.4.10**: works at **200 % text** and reflows at **320 px** with no sideways scroll — the practical form of "no fixed heights / no clipping on text".
- **Sanitizer lesson** (`:16-33`): `font-weight`, `text-transform`, `letter-spacing`, `opacity`, `box-shadow`, `transform`, `text-overflow`, CSS counters, `transition` and `tabindex` are silently stripped; the workaround is a different element, not a different property.

**Unique idea** — "the renderer silently drops things; design within the allowlist instead of fighting it" is exactly the right mental model for Canva's `format_text` (no font family), `add_text` absence and z-order behaviour.

**Mismatch with our MCP** — different product; but the *contrast thresholds*, *redundant encoding*, *alt-text* and *target size* numbers are the only accessibility numbers in the sweep and are directly applicable to slide colours and to `insert_fill` alt text.

---

## Merge recommendations

| Idea | Source | Keep / adapt / drop | Why | Where it belongs |
|---|---|---|---|---|
| Copy-first; never edit the original design | academic-poster §3 "Copy first" | **keep** | Canva commits are not undoable through MCP; `copy-design` is cheap | plan |
| Open transaction → ≤15 ops → verify geometry → commit | academic-poster `canva-mcp-recipe.md:9-20` | **keep** (rename calls) | Matches our `start-editing-transaction` / `perform-editing-operations` / `commit-editing-transaction` exactly | edit |
| Verify `top + height ≤ container bottom` after every batch | `canva-mcp-recipe.md:67-78` | **keep** | Auto-height text is the #1 overflow cause; wrapping changes after every text edit | review |
| Image `height/width` within 0.1 % of source ratio | `canva-mcp-recipe.md:73` | **keep** | Prevents squashed figures after `insert_fill`/`resize_element` | visuals |
| Integer font sizes; re-check the floor after rounding | `canva-mcp-recipe.md:29` | **keep** | `format_text` rejects/rounds; a rounded-down floor breaks the readability rule | edit |
| Typography floor for classroom projection | measured for this user 34–38 px body / ~52 px titles; academic-poster 32 px floor (24 pt); Geongyu 24 pt body | **adapt** | All three cluster at ~32 px at 1920×1080; keep the user's measured 34–38 px body and 52 px titles as the default and treat 32 px as the hard floor | plan |
| 4.5:1 text / 3:1 marks | Geongyu `design-system.md:45-51`, kasparnorge 1.4.3/1.4.11 | **keep** | Projectors wash out low-contrast greys; the two sources agree | visuals |
| One text role per box | `canva-mcp-recipe.md:56-66` | **keep** | `format_text` formats a whole box; mixed roles force compromise sizes | edit |
| Per-slide timing table + bounded modifiers + 0.15 deviation | Nathanielguo `timing-allocation-rules.md:14-54,82-99` | **keep** | Gives a defensible minute budget for a 10–15 min coursework talk | plan |
| Three script layers (main / optional / compressed) | `speaker-notes-standard.md:26-34` | **keep** | Recovers gracefully when a presentation runs short or long | delivery |
| Speaking rate 110 wpm EN / 165 chars·min⁻¹ ZH, pause-adjusted; 3 s/slide + 1.5 s/pause + 10–15 % buffer | AI272 `SKILL.md:87-100` | **adapt** to Vietnamese | Vietnamese is syllable-timed and space-delimited; use ~130–150 wpm as the planning rate and calibrate from one measured rehearsal | delivery |
| Banned openers ("this slide shows…") | AI272 `:52-68` | **keep** | The single most common agent-written-notes tell | delivery |
| Notes = 150–300 characters, 2–3 min per slide | lewislulu `presenter-mode.md:73-78` | **adapt** | Good band; for Vietnamese count characters and target 250–450 (syllables) | delivery |
| "No reasoning traces / no private words" in visible text | Geongyu `qa.md:78-98` | **keep** | Catches "[NEEDS SOURCE]", "Figure 3a_crop", agent self-commentary leaking onto slides | review |
| Six QA gates with PASS/FAIL/NOT_RUN + three release statuses | Geongyu `qa.md:7-114` | **keep** | Honest verification; prevents "looks done" claims | review |
| Five review lenses with crops and a finding schema | academic-poster `pre-print-review.md:66-139` | **adapt** to slides | Visitor / preflight / proofread / venue / design → for a class deck: outsider / projector / wording / rubric / design | review |
| Action titles + ghost-deck test | PHY041 `content_guidelines.md:10-40` | **keep** | `update_title` exists, so titles are the cheapest high-impact edit | structure |
| Pyramid Situation → Complication → Resolution | PHY041; consultant "answer first" | **keep** | The canonical defence narrative and a good antidote to "background, background, results" | structure |
| 16 layout types with per-slot character budgets | beamer `layouts.md` | **adapt** | Can't create layouts; use budgets to decide *which inherited page* to clone and how much text fits | structure |
| Adjacent pages must differ in composition | beamer `writing-style.md:166-173` | **keep** | Kills the wall of identical bullet pages | structure |
| One claim per page; ≥20 pages for a paper talk | bushiAgoni `SKILL.md:51-61`, `quality-gates.md:39-47` | **adapt** | 20+ is right for a literature report; for a 10-minute coursework talk use 12–16 and let backup pages hold detail | structure |
| Backup slides for likely questions | bushiAgoni `mainline-backup-boundary.md`, `question-prep.md` | **keep** | `merge-designs` can append pages at the end; appendices are free time-wise | structure |
| 10 question types + risk-level → verb mapping | bushiAgoni `question-prep.md:11-22`, `question-risk-level.md` | **keep** | Directly reusable for a defence; the verb ladder is subtle enough to be worth copying | delivery |
| Figure readability limits (≤8 table rows, ≤4 panels) | bushiAgoni `figure-readability-standard.md` | **keep** | Concrete split rules for dense evidence | visuals |
| Real figures only; deterministic edits (crop/scale/label) | bushiAgoni `SKILL.md:20-49`; 0frost0 "principles" | **keep** | Blocks generated fake diagrams, which is the fastest way to lose marks | visuals |
| Never crop media; aspect-locked cards | lecture-slides E2 | **keep** | Distorted charts/micrographs read as errors | visuals |
| Media ≥80 % of body height, text column ≤1/3 | lecture-slides E1/E11 | **keep** | Exactly this user's "make the picture bigger, the text narrower" feedback pattern | visuals |
| Fill the space; kill sparse pages | lecture-slides E5/E10 | **keep** | "Too empty" was the top complaint in that corpus and matches the user's aesthetic | visuals |
| Chart-selection table + golden bans | myunwang `chart-mapping.md:7-30`; visualise `charts.md:69-75` | **keep** | No pie >5, no 3-D, y from 0, ≤7 lines — all checkable at a glance | visuals |
| Diagram geometry numbers (60 px gaps, 24 px padding, 4–5 nodes) | visualise `diagrams.md:30-45` | **keep** | Prevents the "spaghetti arrow" diagram; scales to slide px | visuals |
| Uploaded SVG/PNG as the only diagram path | derived (no `insert_shape`/`add_text`) | **keep** | The only way to get real diagrams into the design | visuals |
| Canva gotcha table (16 px default text, image zoom on swap, stale thumbnails, IDs change, merge one-op) | academic-poster `canva-mcp-gotchas.md` | **keep** | Every row is a real time sink; several match already-learned facts | edit |
| Entitlement probe before promising resize/brand templates | wkl0830 `canva-mcp/SKILL.md:68-75` | **keep** | Prevents misdiagnosing a plan limitation as a broken server | plan |
| Speaker notes auto-size to 80 % of the pane, 20–36 px | lecture-slides `SKILL.md:81` | **adapt** | Only relevant if notes live in a sidecar viewer; keep the "fill but don't overflow" principle | delivery |
| 60–90 s answer drills | talk-like-ted | **keep** | Realistic Q&A rehearsal unit | delivery |
| Kept/restored/cut content ledger | beatdeck `checklist.md:30-34` | **keep** | Makes cutting a decision with a reason | plan |
| Presenter card layout (current/next/script/timer) | lewislulu | **adapt** | Impossible in Canva; becomes the layout of the exported sidecar script | delivery |
| 36 themes / 36 layouts / 27 animations | lewislulu | **drop** | No theme or font control in our MCP; tempting but unusable | – |
| Image-generation pipeline, LaTeX/Beamer, python-pptx, React/HTML renderers | several | **drop** | Wrong toolchain; only their content rules were kept | – |
| Browser automation of canva.com | goutham, interagents | **drop** | MCP-first; browser only for OAuth | – |

---

## Contradictions

| Topic | Side A | Side B | Recommendation |
|---|---|---|---|
| **When to crop media** | lecture-slides E2 / academic-poster: never distort, keep aspect, contain-fit | bushiAgoni figure standard: crop the panel that supports the claim and cite the full figure ID | **Both, in order**: keep whole figures uncropped; if a panel is unreadable at slide size, crop *that panel* deliberately and label it "Fig. X (panel B)". Never crop to make a grid tidy. |
| **Body text floor** | Geongyu 24 pt (≈32 px at 1920×1080); academic-poster 32 px floor | our measured practice for this user: 34–38 px body, ~52 px titles | **Follow the user's measured preference (34–38 px body, 52 px title), never below 32 px.** The 24 pt figure is a print/paper-poster floor; classroom projection at the back of a room needs more. |
| **Deck length** | bushiAgoni: ≥20 pages default, no upper limit (literature report) | beamer/PHY041 venue tables: defence 7–13 content slides; talk-like-ted 18-minute rule | **Scale to the slot**: 10-minute coursework ≈ 12–16 main pages + 4–8 backup; 20+ only for a full paper report. Page count is a function of time, not of paper length. |
| **Speaker notes: verbatim or outline** | AI272 and Nathanielguo verbatim mode (complete readable script) | lewislulu "not a script, a signal"; Nathanielguo outline mode | **Hybrid**: a signal-style main script (bolded key words, transitions on their own line) plus a compressed fallback. Full verbatim only for a non-native speaker who explicitly wants it. |
| **Timing rate** | AI272: 110 wpm EN / 165 chars·min⁻¹ ZH, pauses absorbed | Nathanielguo: 180–260 characters·min⁻¹ for Chinese professional delivery | Different measurement units (spoken characters *including* pauses vs planning budget already discounted). **Use one rate consistently and calibrate from a real rehearsal**; for Vietnamese start at ~140 words/min and adjust. |
| **Who may delete pages** | academic-poster: "no delete-page operation; ask the user to delete by hand" | our MCP: `merge-designs` supports `delete_pages` | **Our server wins**: page deletion is possible, one operation per call, and needs explicit approval because it is destructive. |
| **Adding text** | beamer/ppt-report skills: add a text box and format it | academic-poster: `add_text` then `format_text`; fonts applied by hand | **Neither is available**: our MCP has no `add_text`. Text must replace existing text (`replace_text`) or be baked into an uploaded image. This is the single biggest constraint on the whole workflow. |
| **Chart vs table** | myunwang: "no chart for status overviews; metric cards instead" | 0frost0: "when a table communicates the comparison clearly, keep the table" | Agree in substance: choose the cheapest honest encoding; both ban decorative charts. **Keep both rules.** |
| **Accessibility scope** | kasparnorge: WCAG AA is a requirement, 4.5:1 | Geongyu: passing WCAG does not guarantee projector readability | **Both**: treat 4.5:1/3:1 as the floor and add an explicit "read the thumbnail at 25 % zoom" check for projection. |

---

## Gaps

What a complete Canva-MCP slide workflow needs that **none** of these skills covers:

1. **A notes/handout path that survives Canva's read-only presenter notes.** Every notes skill in the sweep injects into PPTX. `get-presenter-notes` reads but cannot write, so the skill must define a sidecar artefact (per-page Markdown, or a printable cue sheet) and say where it lives. Nothing in the sweep has this.
2. **Content replacement without `add_text`.** No source addresses "the outline needs more words than the template's boxes hold". Needed: a page-budget rule (characters per inherited slot), a clone-a-page strategy via `merge-designs(insert_pages)`, and an upload-a-rendered-text-image fallback for the few pages that must carry more.
3. **Page inventory and page choosing.** We have `get-design-pages` and `merge-designs` but cannot create arbitrary layouts. Nothing in the sweep says how to *audit a deck's available page archetypes* and map a storyboard onto them. This is the central planning problem for Canva-native work and it is unaddressed everywhere.
4. **A Vietnamese typographic and rhetorical guide.** Zero skills: tone (academic Vietnamese vs conversational), how to set diacritics at 52 px without clipping, whether to keep Marxist-Leninist terminology in Russian/French transliteration, addressing the panel ("kính thưa hội đồng"), and standard rubric phrasing. All must be authored.
5. **A marking-rubric-driven checklist.** The academic skills encode *venue* rules and *paper* fidelity, never a university grading rubric (content accuracy / structure / visuals / delivery / Q&A). The review machinery exists (five lenses, six gates) but the criteria are missing.
6. **Cost/quota-aware planning.** Only wkl0830 mentions quotas, and only in the abstract (20 vs 200 AI uses). Nothing tells an agent when to prefer template reuse over `create-design`, or how `generate-image` credit exhaustion should change the plan (it has already happened once).
7. **`autofill-design` and brand-template workflows.** Every Canva skill predates or ignores `autofill-design` + `get-brand-template-dataset` + `create-design-from-brand-template`, which is the only *structured* way to push a dataset into a designed layout. On an account with zero brand templates it is moot, but a complete skill should state the branch.
8. **Transactional failure recovery for a long edit session.** The gotchas cover individual errors; nothing covers "the transaction died mid-way — how do you tell what committed", beyond academic-poster's "commit only under the approval style".
9. **Collaboration/comment loop.** `comment-on-design`, `list-comments`, `list-replies`, `reply-to-comment` exist and no skill uses them; a student revising with a supervisor would benefit from a comment-driven revision loop.
10. **Accessibility beyond colour.** The sweep gives contrast, redundant encoding, alt text and target size — no guidance on text-over-image legibility (scrims/opaque panels), motion/animation limits, or reading order in a slide context.
11. **Export and delivery for the actual classroom.** `export-design` PDF vs PNG, `get-export-formats`, and the difference between "open in Canva with presenter view" and "hand in a PDF to the lecturer" is never discussed; the poster skill only covers print.
12. **A measured-feedback loop.** lecture-slides derived its doctrine from 151 real complaints; nothing tells an agent to *record* the user's corrections (font too small, too empty, misaligned) into a durable rules file that future runs read first. That mechanism is the highest-leverage missing piece for this user.
