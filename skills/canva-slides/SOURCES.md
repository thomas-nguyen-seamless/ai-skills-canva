# SOURCES - provenance, decision log, verification log

Built 2026-11-07 from a two-sweep study of GitHub skills (about 60 read, 26 additional found in the second sweep) plus live verification against the mounted Canva MCP.
Licenses are recorded as facts only (the user confirmed non-commercial personal use and asked to ignore license limits). Full extraction notes, with file/line citations for every claim, are kept in
`research/` (01-official-canva, 02-community-canva, 03-canva-field-notes, 04-slidecraft-academic, 05-slidecraft-tools, 06-more-skills, 00-live-mcp-contracts) so any rule here can be re-checked.

## 1. Sources by role

| Group | Repos (license as found) | Taken from them |
|---|---|---|
| **Official Canva** | `canva-sdks/canva-skills` (Apache-2.0): edit-design, implement-feedback, get-design-feedback, brand-check, bulk-create, resize-for-social-media, cli, + inactive branded-presentation, generate-deck, classroom-helper, design-translation, presentation-time-fitting. `canva-sdks/canva-developer-agent-kit` (none). `openai/plugins` canva (none; mirrors) | transaction protocol, CAN/CANNOT matrix, responsive-page op set, commit gate, one-approval rule, evidence rule (colours/fonts not in payload), 3-way triage, manual-changes checklist, five-rule resize ladder + near-duplicate rule, bulk loop discipline, brief/slide-plan schema, visual-integrity rules, 150 wpm arithmetic, honesty clause |
| **Community Canva** | `mavericraven/canva-design-director` (MIT), `TerminalSkills/skills` canva (Apache-2.0), `social-media-skills/skills` canva/design-and-templates/carousel-writer/CHART/QUOTE/CLICK (MIT), `OpenAnalystInc/10x-Canva-Skills` (declared MIT; all 61 referenced scripts absent) | plan-before-paint, anti-slop veto list, rate-limit table, scopes, "jobs are not results", spine-sentence test, de-templating test, token block, data-viz honesty, ten NEVERs (duplicate slides, never blank), export matrix |
| **Canva field notes** | `rifaterdemsahin/canva-mcp` (none), `nguyenduysphk.../canva-ppt-lesson-designer` (none), `first-fluke/oh-my-agent` oma-slide, `rbld56/pitchdeck-pro`, `anthropics/knowledge-work-plugins` canva-creator, `charlesdove977/carousel-builder` (MIT), `m-binimran/design-pack`, `xpert-ai`, `GPire`, `LeoYeAI` canva-2 | 61-entry quirks catalogue, Vietnamese lesson system (challenge-before-acting, 8-field contract, lesson map, 6 layouts, 1-6-6), find_and_replace_text vs replace_text, screen candidate text, thumbnail expiry |
| **Canva MCP reference** | `OrrZwebner/academic-poster` (MIT), `wkl0830-glitch/opencode-skills` canva-mcp | copy-first, <= 15 ops per batch, verify top+height, aspect within 0.1%, gotcha table, entitlement probe, endpoint matrix |
| **Academic / story / pitch** | `Gabberflast/academic-pptx-skill`, `ItsssssJack/power-design` (20 rules), `yushengchen519-cmd/medical-ppt-designer-skill`, `Stevekaplanai/pitch-deck-mastery-skill`, `josezuma/yc-pitch-deck-max` (thin), `Esther2524/beautiful-hackathon-slides`, `minorun365/minorun-marp-skill` (Apache-2.0), `robonuggets/marp-slides`, `PHY041/claude-skill-academic-ppt`, `Faust-Donf/beamer-academic`, `bushiAgoni/academic-slide-minimalist`, `Geongyu/academic-conference-presentation`, `0frost0/academic-evidence-ppt` | action titles, ghost-deck, SCR, defence playbook, Q&A types and risk verbs, 20 numeric rules, density tiers, content integrity, crossheads, concept 3-piece set, hooks, timing units, luminance method, figure rules, QA gates/statuses |
| **Design craft** | `alchaincyf/huashu-design` (MIT), `SlideSpeak/slide-design-skill` (MIT), `sunbigfly/ppt-agent-skills`, `vstorm-co/content-skills` (MIT), `Phlegonlabs/Powerpoint-fancy-design`, `Taimoorkhan1122/present-now` (MIT), `anthropics/skills` (pptx, canvas-design, frontend-design, theme-factory, brand-guidelines, doc-coauthoring), `YuliangXiu/lecture-slides`, `lewislulu/html-ppt-skill` (MIT), `myunwang/ppt-report-skills` (MIT), `bentossell/visualise`, `hritikvaidwan007/visual-explainer-diagrams`, `borjaperfra/beatdeck`, `appautomaton/presentation` | colour derivation, bounded content island, density register, geometry preservation, chart relation table, slop lists, three-direction gate, P0/P1/P2 review, reader test, Layout Doctrine, notes iron rules |
| **Delivery** | `Nathanielguo/presentation-speaker-notes`, `AI272/speaker`, `kanazawahere/talk-like-ted-skill` | per-type timing budget, 3 script layers, banned openers, pause-adjusted rates, drills |
| **Accessibility** | `kasparnorge/canvas-lms-skills` (CC-BY-SA-4.0) | WCAG thresholds |

## 2. Decision log (where sources disagreed, and what this skill does)

| # | Conflict | Decision | Why |
|---|---|---|---|
| 1 | pt vs px (20 pt vs 24 px vs 26 pt body) | **px on 1920x1080** only; 1 pt = 2 px footnote | Canva's ops take px; the user's own measured need |
| 2 | Body floor 14 pt / 24 px / 28-30 px | **body 34-38, floor 32; support floor 28; tag floor 24** | classroom back-row; observed feedback "font bự hơn" |
| 3 | Density: 25 / 40 / 75 words | **mode token** presenter / talk (default) / document | each source is right for its register |
| 4 | Answer first vs "do not reveal the answer" | **audience-conditional**: answer-first for panels/execs; progressive disclosure for teaching/defence | declare per deck, enforce deck-wide |
| 5 | Agenda forbidden (minorun) vs expected | **short agenda for graded coursework**; none in fast talks | graders expect orientation |
| 6 | Summary slide required vs forbidden | **takeaway slide that stays up during Q&A** | academic Q&A anchor; never end on bare "Thank you" |
| 7 | Action titles vs label headings | **claims for argument decks; labels for step/instructional slides**; one convention per deck | detect mode, then hold it |
| 8 | Slide count: 1/min vs 16 s/slide | **by deck type** (academic <= 1/min; lecture 1.5-2 min; defence 2-3 min; fast demo 16-30 s) | do not mix models |
| 9 | Fonts: 1 vs 2 vs 3 families | **<= 2; one ideal; family is the generator's, verify** | `format_text` has no family op |
| 10 | Accent rule under titles: sunbigfly prescribes, anthropics/lesson-designer/huashu/SlideSpeak ban | **ban** (delete the SHAPE if the theme adds it) | 4:1 vote, carries no information |
| 11 | Logo on every slide vs only bookends | **bookends**; interior only if the institution requires | power-design contradicts itself |
| 12 | Decorative imagery: banned (academic) vs encouraged (hackathon) | **audience-conditional**; never mixed in one deck | institutional vs consumer |
| 13 | Template-first vs structure-first | **structure-first** (no templates here); template-first when a real template exists; never mix in one deck | generated + duplicated pages never match |
| 14 | Approval: gate every commit vs one up-front approval | **default ask once; a request that names the whole job is the approval; always ask for deletions/irreversible ops** | resolves edit-design vs implement-feedback |
| 15 | Parallel vs sequential fan-out | **resize in parallel (independent designs); per-row fills sequential** | stated reason each |
| 16 | Brand kit: auto-use one kit vs always ask | **ask once; if none, say so and proceed** | never silently pick a style authority |
| 17 | Uppercase micro-labels | **ban** (Canva cannot track; shouts) | 3:1 vote |
| 18 | Whitespace >= 40% vs <= 25% unused | **empty space is a margin, not a hole**; hero/cover >= 60%, content 25-40% | they measure different things |
| 19 | Who may delete pages (poster skill says no op) | **`merge-designs delete_pages` exists here; one op per call, explicit approval** | this server's contract |
| 20 | Notes verbatim vs outline | **signals plus three layers (main / if-time / fallback)** | live time adaptation |
| 21 | Speaking rates (110 wpm EN; 165-300 zh chars/min) | **calibrate from one timed rehearsal; Vietnamese starting guess ~140 wpm `[INFERENCE]`** | no Vietnamese baseline in any source |
| 22 | Preview: in-transaction thumbnails vs exported PNG | **both**: thumbnails for review, exports for anything durable | expiry |
| 23 | Accessibility: WCAG 4.5 vs projector washout | **4.5/3 as floor, design for 7:1, 25-50% zoom check** | both true |
| 24 | Style menus (theme-factory, Phlegonlabs) vs derivation | **derive** (anchor -> stance); menus only as internal vocabulary | menus cause sameness |

## 3. Not adopted (and why)

HTML/CSS/Marp/Beamer/python-pptx/pptxgenjs code, 36-theme libraries, presenter windows, animation systems, video timelines, REST OAuth implementations, multi-agent harness protocols, social-publishing integrations (WoopSocial, HubSpot), print-poster specifics (PPI, bleed, CMYK): wrong medium for the Canva MCP. 10x-Canva-Skills scripts: absent. `generate-design-structured`, `prepare-design-generation`, `create-design-from-candidate` workflows: not on this server.

## 4. Verification log (this mount, `https://api.canva.com/connect/v1/mcp`, account "Hui Centralized")

| Date | Verified |
|---|---|
| 2026-11-06 | `create-design` outline -> exact slide count; job statuses; `start-editing-transaction` payload; thumbnails per page; `replace_text`, `format_text`, `position_element`, `insert_fill`, `delete_element` (group-id rule); `create-upload-url` -> `mediaId`; `merge-designs` insert/move (insert order reversed); `copy-design`; `generate-image` quota failure; zero brand kits/templates |
| 2026-11-07 | live tool schemas re-read (`research/00-live-mcp-contracts.md`); `autofill-design` confirmed not mounted; **`create-design` now fails with synchronous `quota_exceeded` (same AI-credit quota as `generate-image`; reset 2026-12-01 00:00 UTC)**; **`start-editing-transaction` 503 persisted 35+ min across two designs and ~8 attempts**; credit-free and transaction-free tools verified: `copy-design` (3 pages), `merge-designs move_pages`, `get-design-content`, `get-export-formats`, `export-design` PDF (3 pages, downloaded, `pypdf` count 3) and per-page PNG (960x540), `create-upload-url` + `post_upload.sh` (first POST `{"mediaId"}`, second POST 403); scripts tested: `diagrams.py` 8 kinds, `fit_check.py` (5 observed wraps), `plan_check.py` (sample 16-slide plan 0 errors), `text_diff.py` (real generated text 0 missing), `deck_audit.py` (synthetic defects: title drift, safe zone, bottom overflow, overlap, accent rules), `contrast.py`, `contact_sheet.py` |
| 2026-11-07 (later) | `create-design` with a real 20-section outline: synchronous `quota_exceeded` again; `start-editing-transaction` still 503 hours later; `generate-image` (Canva) still `credit_quota_exceeded`; omp `generate_image` (google-antigravity/gemini-3-pro-image) works; `create-upload-url` rejects PPTX (`Unsupported file format PPTX`); `import-design-from-url` forbids generated/local files; native PPTX build + PowerPoint render + rendered-PDF text verification worked (`references/11`) |
| 2026-11-07 (docs + CLI) | canva.dev REST `design-imports` lists `.pptx`; Canva CLI 2.17 `api design-imports create --file` (login needed; scope `design:content:write`); Canva Help: PowerPoint import <= 300 slides / 1,400 elements, charts/SmartArt/3D/WordArt ignored, beta; Help: AI allowance covers "Generate a design with Canva AI" in connected assistants (Premium AI tool), Free plan ~20 uses/month, resets 00:00 UTC on the 1st; live: 20-slide PPTX imported to a design in 1 poll, page_count 20, Canva PDF export text layer contained all planned strings (0 missing) |
| 2026-11-07 (import verified end to end) | PPTX import via CLI -> design `DAHaPZNNOhs` (20 pages); Canva PDF export text layer contained every planned string (0 missing); MCP `get-design`/`get-design-content` read the same design, so CLI and MCP are the same account (CLI `team_user` ids are a different namespace); v1 import (`DAHaPYHlshI`) proved the importer drops shape insets and paragraph spacing and flattens freeform strokes |
| 2026-11-07 (sharing) | no share/publish endpoint in Connect API or MCP; UI flow set to "Anyone with the link" + "Can view" produced `https://canva.link/l9vabfoz2xymxne`; that link and `/design/<id>/<token>/view` load signed-out (guest, 20 pages), while bare `/view`/`/edit` redirect to login |
| 2026-11-07 (native check) | Canva PPTX round-trip of `DAHaPZNNOhs`: 20 slides, 199 TEXT_BOX, 99 GROUP, 7 FREEFORM, 0 pictures; fonts Arial/Arial Bold, sizes preserved (52 px -> 39 pt on a 1440x810 pt canvas). MCP `start-editing-transaction` still returned 503 for both this design and `DAHaJknakxI`, so agent-side edits remain blocked while the UI is editable |
| 2026-11-07 (in-place update) | docs: `/v1/merges` preview, `modify_existing_design` + `design_id`, one operation per request by default; live test on throwaway `DAHaQreBJVw`: insert -> page_count 4 same id, delete 2-4 -> page_count 1 same id. sharing preservation VERIFIED same day: public `canva.link` + Can view survived a full 40->20 page replacement (same id, guest access, 20 pages), and the script `scripts/update_canva_deck.sh` ran both replacements |
| 2026-11-07 (per-page replace) | `--pages 5` on a 20-page design: only page 5 changed (1,266 px), other 19 pages pixel-identical, marker text only on page 5; page count unchanged, same design id |
| **Not re-verified on 2026-11-07 (blocked by the two outages)** | full dry-run of `create-design` -> transaction edits -> diagram `insert_fill` -> commit with the skill's templates; these paths were verified end-to-end on 2026-11-06 with the same tools |
| **Unverified** `[U]` | HTML import `data-speaker-notes`; `replace_text` flattening mixed-style text; exact `perform-editing-operations` per-call ceiling (75 ops worked); Vietnamese speaking pace; PNG export of a very long deck; `resize-design` / `import-design-from-url` under exhausted quota |

## 5. Maintenance

Re-verify quarterly or on any unexpected tool error: tool list (`00`), limits (`05`, `10`), export options (`07`), quota behaviour. When a conflict appears between this skill and a community skill, this skill wins on **tool names and limits**; community skills win only on ideas absent here. Update `templates/deck-rules.md` per user, not this file.
