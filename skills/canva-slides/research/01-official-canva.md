# Official Canva skills — extraction for a unified slide-making skill

Cluster: the three first-party Canva sources cloned under `/tmp/skills-src`.

| Repo | Clone path | License (fact) |
|---|---|---|
| `canva-sdks/canva-skills` | `canva-sdks_canva-skills/` | Apache-2.0 (`LICENSE` present in git tree `HEAD`, confirmed via `git show HEAD:LICENSE`; the file is not checked out because sparse-checkout only fetches `*.md,*.json,*.txt,*.yml,*.yaml`) |
| `canva-sdks/canva-developer-agent-kit` | `canva-sdks_canva-developer-agent-kit/` | NO-LICENSE — `git show HEAD:LICENSE` → *fatal: path 'LICENSE' does not exist in 'HEAD'*; repo root contains only `README.md examples recipes skills templates` |
| `openai/plugins` (canva plugin only) | `openai_plugins/plugins/canva/` | NO-LICENSE at repo root; only `plugins/figma/LICENSE.txt` exists in the tree |

All three target the **Canva MCP server at `https://mcp.canva.com/mcp`** (`canva-sdks_canva-skills/plugins/canva/.mcp.json`, `openai_plugins/plugins/canva/.mcp.json`), i.e. the DCR-capable AI Connector. Our mount is the Developer-Portal Connect endpoint `https://api.canva.com/connect/v1/mcp` — same tool surface family, different host and auth. This matters for a handful of calls noted per skill.

Path convention: the Inventory below gives every full path. In the per-skill sections, a leading `.../` expands to `canva-sdks_canva-skills/plugins/canva/` (so `.../skills/edit-design/SKILL.md` = `canva-sdks_canva-skills/plugins/canva/skills/edit-design/SKILL.md`), and `.../inactive-skills/` likewise. All paths are relative to `/tmp/skills-src`.

## Inventory

| Source | Repo path | License | What it is (one sentence) | Verdict |
|---|---|---|---|---|
| `edit-design` | `canva-sdks_canva-skills/plugins/canva/skills/edit-design/SKILL.md` | Apache-2.0 | The canonical transaction-based edit engine: start → perform → commit, with an explicit CAN/CANNOT capability matrix and a commit approval gate. | **A** — the most reusable document in the cluster; its capability matrix is the ground truth every other skill defers to. |
| `implement-feedback` | `.../skills/implement-feedback/SKILL.md` | Apache-2.0 | Converts comment threads into a triaged change plan, applies API-possible fixes after exactly one approval, and emits a manual-change checklist. | **A−** — excellent triage stance and the "one approval, never ask again" rule; step numbering skips Step 6. |
| `get-design-feedback` | `.../skills/get-design-feedback/SKILL.md` | Apache-2.0 | Read-only design critique across seven lenses, prioritised by severity with page-located fixes. | **A** — best epistemic discipline in the cluster (never assert hex/font the API didn't return). |
| `brand-check` | `.../skills/brand-check/SKILL.md` | Apache-2.0 | Brand-kit conformance review producing On brand / Off brand / Can't verify verdicts. | **B+** — honest about the brand-kit data gap, but the rubric is a thin variant of design-feedback and needs a brand kit we don't have. |
| `bulk-create` | `.../skills/bulk-create/SKILL.md` | Apache-2.0 | One design per tabular row via `autofill-design` against a brand template, with column→field mapping and per-row status. | **B+** — the most complete edge-case handling in the cluster; blocked in our account (Enterprise + zero templates). |
| `resize-for-social-media` | `.../skills/resize-for-social-media/SKILL.md` + `references/channel-formats.md` | Apache-2.0 | Creates channel variants of one design at exact canvases, resolving targets through a five-rule ladder and a dated dimension table. | **A−** — the rule ladder and the "few pixels apart" de-dup rule are directly portable; default set omits 1:1. |
| `cli` | `.../skills/cli/SKILL.md` | Apache-2.0 | Drives the `canva api` CLI for REST workflows, with job polling and result-interpretation rules. | **B** — correct but off-path for MCP slide work; registered in `plugin.json` yet missing from the Claude manifest and the README skill list. |
| `branded-presentation` (inactive) | `.../inactive-skills/branded-presentation/SKILL.md` | Apache-2.0 | Outline → on-brand deck through `generate-design` + `create-design-from-candidate`, with a five-section query template. | **B** — the query template is the best-structured deck brief here; the candidate flow it ends on is legacy in our mount. |
| `generate-deck` (inactive) | `.../inactive-skills/generate-deck/SKILL.md` | Apache-2.0 | Sales/marketing deck generation that forces `generate-design` to stay deck-shaped and forbids the prepare-generation step. | **C** — frontmatter is misnamed `canva-branded-presentation` (collides with the other inactive skill), and its central argument targets a tool that does not exist in our MCP. |
| `classroom-helper` (inactive) | `.../inactive-skills/classroom-helper/SKILL.md` | Apache-2.0 | Lesson plan → teaching deck, pedagogy-first, with a long section on why generated visuals misrepresent facts. | **A−** — its visual-integrity rules are the single most transferable content here for our Vietnamese coursework deck. |
| `design-translation` (inactive) | `.../inactive-skills/design-translation/SKILL.md` | Apache-2.0 | Clones a design by resizing to identical dimensions, replaces every text run with a translation, commits. | **B** — the clone-by-resize trick was clever before `copy-design` existed; no reflow handling for length change. |
| `presentation-time-fitting` (inactive) | `.../inactive-skills/presentation-time-fitting/SKILL.md` | Apache-2.0 | Time-boxes an existing deck by writing presenter notes only, at ~150 wpm, never touching slide text. | **C** — good arithmetic, but it depends on a notes-write operation our MCP does not expose; unusable as written. |
| `canva-design-infrastructure` | `canva-sdks_canva-developer-agent-kit/skills/canva-design-infrastructure/SKILL.md` | NO-LICENSE | Chooses between MCP / REST SDK / Apps / CLI for a build, and argues for Canva as default design layer. | **B** — useful as a routing table, contains no slide craft. |
| Agent templates | `canva-sdks_canva-developer-agent-kit/templates/{AGENTS.md,CLAUDE.md,README.md}` | NO-LICENSE | Starter instruction files for coding agents, with word budgets and a definition-of-done rubric. | **B** — the length budgets and DoD list transfer to writing a good SKILL.md. |
| `canva-social-campaign` recipe | `canva-sdks_canva-developer-agent-kit/recipes/canva-social-campaign/{README.md,AGENTS.md,CLAUDE.md}` | NO-LICENSE | Website → campaign kit pipeline; Canva generation is stubbed. | **C** — the pipeline shape (analyze → brief → asset specs → payload) is sound, the Canva half is not implemented. |
| `canva-product-imagery` recipe | `canva-sdks_canva-developer-agent-kit/recipes/canva-product-imagery/{README.md,AGENTS.md}` | NO-LICENSE | Shot list → one generated image per row, with real image-generation job semantics. | **C** — the only place in the cluster that documents image-generation payloads and polling, so worth reading for facts. |
| `campaign-image-studio-starter` example | `canva-sdks_canva-developer-agent-kit/examples/campaign-image-studio-starter/{README.md,AGENTS.md,SANITIZATION.md}` | NO-LICENSE | Runnable OAuth+PKCE app that generates images and imports them into designs. | **C** — OAuth/scopes facts only; no slide workflow. |
| `canva-brand-check` (openai) | `openai_plugins/plugins/canva/skills/canva-brand-check/SKILL.md` | NO-LICENSE | Mirror of `brand-check`. | **B+** — byte-identical to the canva-sdks file. |
| `canva-bulk-create` (openai) | `.../skills/canva-bulk-create/SKILL.md` | NO-LICENSE | Mirror of `bulk-create`. | **B+** — byte-identical. |
| `canva-edit-design` (openai) | `.../skills/canva-edit-design/SKILL.md` | NO-LICENSE | Mirror of `edit-design`. | **A** — byte-identical. |
| `canva-design-feedback` (openai) | `.../skills/canva-design-feedback/SKILL.md` | NO-LICENSE | Mirror of `get-design-feedback`. | **A** — byte-identical. |
| `canva-implement-feedback` (openai) | `.../skills/canva-implement-feedback/SKILL.md` | NO-LICENSE | Mirror of `implement-feedback`. | **A−** — byte-identical. |
| `canva-resize-for-social-media` (openai) | `.../skills/canva-resize-for-social-media/SKILL.md` | NO-LICENSE | Older, self-contained resize variant: five hardcoded formats, asks the user which to make. | **C** — a regression against the canva-sdks version; wrong IG feed size, no de-dup, no reference table. |
| `canva-branded-presentation` (openai) | `.../skills/canva-branded-presentation/SKILL.md` | NO-LICENSE | Byte-identical to the **inactive** `branded-presentation`, promoted to active. | **B** — same content as above; fixes the naming collision by living in a folder that matches its frontmatter. |
| `canva-translate-design` (openai) | `.../skills/canva-translate-design/SKILL.md` | NO-LICENSE | Byte-identical to the **inactive** `design-translation`, promoted to active. | **B** — same content. |

**Host entrypoints (all read; none contains slide guidance).** `canva-sdks_canva-skills/README.md` is the only one with real content: the architecture rule "marketplace/catalog → plugin → skills", the install commands per host, and two lists that disagree with the filesystem — "Active Plugin Skills" documents six and omits `cli`, "Inactive Skills" documents four and omits `generate-deck`. `.agents/plugins/README.md`, `.claude-plugin/README.md`, `.cursor-plugin/README.md`, `.cursor/README.md` and `plugins/canva/.cursor/README.md` are install-only (marketplace add, `codex mcp login canva`, Cursor Settings → MCP Tools → Connect). Manifests: `plugins/canva/plugin.json` lists **seven** skills including `./skills/cli`; `plugins/canva/.claude-plugin/plugin.json` lists **six** (no `cli`, because "Claude requires an explicit list" per the README contributing note); `.cursor-plugin/plugin.json` and `.codex-plugin/plugin.json` auto-discover `./skills/`. MCP registration is `https://mcp.canva.com/mcp` in `.mcp.json` and `mcp_config.json`, while the repo-level `.cursor/mcp.json` wraps the same URL in `npx -y mcp-remote@latest`. Practical consequence: `cli` is visible to Codex/Cursor-style hosts and invisible to Claude, which is why it appears in neither README list.

---

## Skill: edit-design (the edit engine)

**Purpose.** Apply changes to an existing design without losing the user's work, and state honestly what the API cannot do.

**Prescribed process** (`.../skills/edit-design/SKILL.md`, "The Transaction Protocol" and "Workflow"):

1. `start-editing-transaction` with `design_id`. Keep the returned `transaction_id` **and** the `pages` array — later calls need both. Show the returned thumbnail(s).
2. `perform-editing-operations` with `transaction_id`, the `pages` array, `page_index` of the first changed page, and an `operations` array. Batch.
3. `commit-editing-transaction` only after explicit approval. After commit the `transaction_id` is invalid; a new edit needs a new transaction.
4. `cancel-editing-transaction` to discard a draft — including when the transaction was opened only to look.
5. Resolve the design first: `canva.link/...` → `resolve-shortlink`; full URL → take the segment after `/design/`; raw `D...` id → use directly and **do not** call `search-designs`.
6. Confirm scope before a `find_and_replace_text` whose target string could match in several places.
7. Show the resulting thumbnail + plain-language change list, then commit and hand back the edit link.

**Rules and thresholds.**

- Capability matrix ("Capabilities — what the API CAN and CANNOT do"): CAN — `replace_text`, `find_and_replace_text`, `format_text` (size, weight, style, color, alignment, line height, underline, strikethrough, links, list level/marker), `update_fill`, `insert_fill`, `delete_element`, `position_element`, `resize_element`, `update_title`, `update_autofill_field` (fixed-page designs only). CANNOT (lines 28–34) — "Change font **family/typeface** (only size, weight, style)", "Add **new text elements**", "Change background colors or gradients", "Add, remove, or reorder pages/slides", animations/transitions/opacity (except on newly inserted fills), group/ungroup, shape restyling.
- Responsive pages (lines 39–42): when a page returns `is_responsive: true`, "ONLY these operations are allowed: `update_title`, `replace_text`, `update_fill`, `delete_element`, `find_and_replace_text`". The skill tells you to *refuse the call* rather than attempt `format_text` / `position_element` / `resize_element` / `insert_fill` there. This is the only skill in the cluster that checks `is_responsive` before operating.
- Commit gate (lines 44–52): must show what changed + the preview and get a clear yes; must not claim saved before the commit succeeds; "If a commit fails, all changes are lost — start a new transaction to retry."
- Composition escape hatch: a caller skill that already collected one up-front batch approval may treat that as covering the commit and must not re-ask.

**Unique ideas.** (a) The transaction as a *read* facility — open, inspect element ids, cancel. (b) The explicit instruction that other skills build on this one, with an override rule for the approval gate. (c) Naming the exact failure semantics of a failed commit rather than hand-waving.

**Pitfalls it warns about.** Reusing an id after commit; leaving a transaction dangling without telling the user the draft was discarded; unbatched calls; substring replacement hitting multiple contexts.

**Against our MCP.** Everything named exists under the same kebab-case names (`start-editing-transaction`, `perform-editing-operations`, `commit-editing-transaction`, `cancel-editing-transaction`); the `Canva:` prefix is cosmetic. The `pages`-array requirement matches our known contract and is the single most important porting detail. `update_autofill_field` is only usable on fixed-page (non-responsive) designs. Nothing here is stale except the missing awareness of `copy-design` and `merge-designs`, which give safer structural change than anything in this skill's CAN list.

---

## Skill: implement-feedback

**Purpose.** Turn scattered reviewer comments into applied changes, and be honest about the residue.

**Prescribed process** (`.../skills/implement-feedback/SKILL.md`):

1. Resolve the design (shortlink → `resolve-shortlink`; URL → extract id; raw `D...` → use directly, never `search-designs`).
2. Read all feedback: `list-comments`; for each thread with replies `list-replies`; `get-design-content` for current text on every page.
3. Triage every thread into **Actionable** / **Requires manual action** / **Resolved** (positive acknowledgements like "LGTM").
4. Present the plan by category, get approval **once**.
5. `start-editing-transaction` → `perform-editing-operations` (batched) → `commit-editing-transaction`, with no second confirmation.
6. Present the manual-change checklist (step numbering jumps from 5 to 7 in the source — an editorial defect, not a missing instruction).
7. `reply-to-comment` on each thread to close the loop; for manual-only threads, say what was done as the nearest alternative and what remains.

**Rules and thresholds.**

- "**Be helpful, not cautious** — interpret feedback generously"; escalate only when intent is genuinely undeterminable (two reviewers contradict, or a comment references something absent from the design).
- Explicitly banned phrasings: "NEVER ask 'shall I commit?', 'ready to save?', or any variation".
- Manual changes are normal: "don't over-explain or apologise for API limitations".
- Batch into one `perform-editing-operations` call.
- Manual-checklist item shape: slide number, what to change, `Reviewer: @name`, `Why:` the API limit, then a `→` step-by-step editor instruction.

**Unique ideas.** The **manual-changes checklist as a deliverable** — it converts API impossibility into user work with provenance (who asked, why it can't be automated). Also the one-approval contract, which is the correct UX for batch edits and directly conflicts with edit-design's per-commit gate unless you adopt the override clause.

**Pitfalls.** Asking twice (kills throughput); treating "make the title punchier" as ambiguous instead of just rewriting; over-apologising; not mapping comments to specific pages before editing.

**Against our MCP.** `list-comments`, `list-replies`, `reply-to-comment`, `get-design-content` all exist. Two gaps: the skill never anchors a comment to a `page_id`, so with a 16-slide deck the agent must infer which page a thread belongs to; and it never snapshots before batch edits, so a mis-scoped `find_and_replace_text` across 16 slides is unrecoverable (`copy-design` exists in our mount and should be used as a pre-flight backup).

---

## Skill: get-design-feedback

**Purpose.** Produce prioritised, located design critique without changing anything.

**Prescribed process** (`.../skills/get-design-feedback/SKILL.md`):

1. Resolve the design.
2. Read it: `get-design` for title and page count; `get-design-thumbnail` and/or `get-design-pages` to see pages; `get-design-content` for text; optionally a **read-only transaction** (start → inspect `richtexts`/`fills` → `cancel`) for positions and sizes.
3. Evaluate across seven lenses: visual hierarchy, layout & spacing, copy & messaging, consistency, readability & contrast, accessibility, fit for purpose — skipping any lens that doesn't apply to the design type.
4. Return findings organised by page, each with a **High / Med / Low** severity and a concrete fix, preceded by a "Top priorities" shortlist and followed by "What's working".
5. Offer to implement the API-fixable items by handing off to edit-design, naming what needs manual work.

**Rules and thresholds.**

- The epistemic core (section "What you can actually read (and the gap to know about)"): `get-design-content` returns "text (`richtexts`) only — … it does NOT include colors, fonts, sizes, or element positions"; a transaction "reliably" gives text, positions and sizes; "**Colors and fonts are NOT reliably exposed.** Tested: the transaction payload often returns only text + position + dimension per element". Therefore "treat the **thumbnail as the primary source**" and "Never report a specific hex/font as fact unless the payload actually contained it."
- Report shape: `## Feedback — "<title>" (N pages)`, then `### Top priorities`, `### Page-by-page`, `### What's working`.
- Example fix quantifies a ratio: "bump the title to ~1.5× and bold it so it reads first" — the only typographic scale number in the entire cluster.
- Ban on generic advice ("make it pop"); every point must be grounded in something observed.
- "A ranked shortlist beats an exhaustive list".

**Unique ideas.** Separating *what the API returns* from *what you may assert*; using a cancelled transaction purely to inspect; the severity ladder; the "what's working" section, which stops the critique reading as an attack.

**Pitfalls.** Reporting colours from the thumbnail as if measured; rating every issue High; reviewing page 1 only.

**Against our MCP.** Step 2 calls `get-design-thumbnail` directly, but our tool is documented as needing an editing-transaction id ("Get the thumbnail for a particular page of the design in the specified editing transaction"). So the read path must be re-ordered: `get-design-pages` for the page list, and either its thumbnails (field-reported: real only for page 1) or one transaction that fetches each page thumbnail then cancels. Otherwise the skill ports cleanly. It also never mentions `get-assets` or `export-design`, which are alternate ways to see a page.

---

## Skill: brand-check

**Purpose.** Compare a design to a brand kit on five dimensions and mark each finding as verifiable or not.

**Prescribed process** (`.../skills/brand-check/SKILL.md`):

1. Resolve the design.
2. `list-brand-kits`; if several, ask which (or infer from team context); capture name, thumbnail, and colours/fonts **if present**.
3. Read the design: `get-design-thumbnail` for logo/tone; read-only transaction for colours/fonts.
4. Compare on colour, typography, logo, tone & copy, consistency — each marked **On brand / Off brand / Can't verify**.
5. Report in the shape `## Brand check — "<design>" vs "<kit>"` with `### Off brand`, `### Can't verify (need input)`, `### On brand`, and an "Overall:" line with an issue count.
6. Offer fixes via edit-design, restating that text colour and size/weight/style are editable but font family and background are not.

**Rules and thresholds.**

- The data gap: `list-brand-kits` "may NOT return the machine-readable palette (hex values) and font families"; if it only returns a thumbnail, fall back to visual comparison and **ask the user to paste hex codes and font names**.
- "Never invent brand colors or fonts."
- Scope failure handling: `Missing scopes: [brandkit:read]` → tell the user to disconnect and reconnect the connector to refresh the token.
- Distinguish "hard violations (wrong logo, off-palette color) from soft ones (slightly inconsistent spacing)".

**Unique ideas.** **"Can't verify" as a first-class verdict** — the only skill in the cluster that treats ignorance as a reportable result rather than a failure. The reconnect-to-refresh-scopes instruction is also unique.

**Pitfalls.** Fabricating a palette; asserting "off brand" from a compressed thumbnail; ignoring the logo-stretch/recolour check that only a visual pass can catch.

**Against our MCP.** Blocked in this account: `list-brand-kits` and `search-brand-templates` both return `{"items":[]}` here, so there is nothing to check against and the skill degrades to "compare against values the user pastes". `brandkit:read` scope errors are plausible on the Connect endpoint. Keep the *method* (five dimensions + three verdicts), drop the dependency on a kit existing.

---

## Skill: bulk-create

**Purpose.** One design per data row using a brand template's autofill fields.

**Prescribed process** (`.../skills/bulk-create/SKILL.md`):

1. Get the data from an uploaded file, a pasted table, JSON, or a URL; show headers, row count, and a preview of the first rows.
2. `search-brand-templates dataset=non_empty`; let the user pick (or search with their named template).
3. `get-brand-template-dataset template_id=...` for field names and types (text, image, chart).
4. Build a mapping table (template field | type | matched column | notes) with case-insensitive fuzzy matching; confirm before proceeding, especially for unmapped or ambiguous fields.
5. Loop **sequentially** — "Call them **sequentially**, not all at once — the API may have rate limits" — calling `autofill-design` per row with a `data` payload of `{"<field>": {"type": "text", "text": ...}}` and image fields as `{"type": "image", "asset_id": ...}`, plus a descriptive title.
6. Track per-row status inline (`Row 3 / 50: Failed — <error>`), then summarise totals and offer a CSV with columns `row, status, design_url, error`.

**Rules and thresholds.**

- Three image-field patterns: **A** asset-id column used directly; **B** URL column → `upload-asset-from-url` first, "Do the upload immediately before creating that row's design so failures stay localised"; **C** no image column → ask whether to skip (omit the key) or abort.
- "Autofill requires a Canva Enterprise plan."
- "For large CSVs (50+ rows), warn the user … Offer to do a test run on the first 3 rows."
- "Template field names are case-sensitive in the API."
- "There is no 'undo bulk create' — warn the user before starting large runs."
- Continue past failures; skip all-empty rows and warn.

**Unique ideas.** The three image patterns; the just-in-time upload ordering; the test-run-the-first-3 heuristic; the results CSV schema.

**Pitfalls.** Parallel fan-out hitting rate limits; passing URLs straight into `autofill-design` (they are rejected); case-mismatched field keys silently dropping content; half-finished batches with no rollback.

**Against our MCP.** Tools exist (`search-brand-templates`, `get-brand-template-dataset`, `autofill-design`, `upload-asset-from-url`), but this account has **zero brand templates** and is not Enterprise, so the whole skill is dead here. The *loop discipline* (sequential, per-item status, test-first-3, no-undo warning) is portable to any repeated create operation, including repeated `create-design` calls.

---

## Skill: resize-for-social-media (+ channel-formats reference)

**Purpose.** One source design → several exact canvases, with links back, leaving the source untouched.

**Prescribed process** (`.../skills/resize-for-social-media/SKILL.md`):

1. Identify the design by id, URL, name (`search-designs`, present options if several), or conversation context.
2. `get-design` to confirm existence and type.
3. Resolve targets through the five-rule ladder (below); state the planned variants.
4. One `resize-design` per unique canvas with `design_type: {type: "custom", width, height}` and a concise `user_intent`; keep `job.result.design.id`, `.thumbnail.url`, `.urls.edit_url`, `.urls.view_url`.
5. Present a table of requested placement(s) | canvas | status | thumbnail | edit link, plus a count line ("Created 2 of 3 requested canvas variants").

**Rules and thresholds** (`.../references/channel-formats.md`).

Resolution ladder (SKILL.md "Step 3"), verbatim ordering:

1. exact pixel dimensions → use only those;
2. platform + placement → look up in the placement table;
3. aspect ratio only → resolve via the aspect-ratio set;
4. "each channel / all channels / every platform / platform-ready variants" with no dimensions → default channel set, "Do not ask which placement to use";
5. "social versions / common formats / all formats" → aspect-ratio set.

Plus: one platform with no placement → ask which placement (rule 4 is not that question); de-duplicate identical width×height pairs "while retaining every requested platform label".

Default channel set (4 canvases, `channel-formats.md` lines 10–18):

| Covers | Canvas |
|---|---:|
| Instagram Feed portrait, Facebook Feed portrait | 1080 × 1350 |
| TikTok vertical, Instagram Story / Reel, Facebook Story / Reel, YouTube Short | 1080 × 1920 |
| LinkedIn single-image landscape, X image landscape, Facebook link image | 1200 × 627 |
| YouTube standard video | 1920 × 1080 |

The near-duplicate rule (line 11, verbatim): LinkedIn 1200×627, X 1200×628 and Facebook link 1200×630 "are a few pixels apart. On this generic request, create 1200 × 627 once and label it for all three. Create 1200 × 628 or 1200 × 630 only when the user names that placement."

Aspect-ratio set: 9:16 → 1080×1920; 4:5 → 1080×1350; 1:1 → 1080×1080; 16:9 → 1920×1080.

Placement lookup (12 rows): Instagram Feed portrait 1080×1350; Instagram Story/Reel 1080×1920; TikTok vertical 1080×1920; LinkedIn single-image landscape 1200×627; LinkedIn single-image square 1200×1200; X image landscape 1200×628; Pinterest standard Pin 1000×1500; YouTube Short 1080×1920; YouTube standard 1920×1080; Facebook Feed portrait 1080×1350; Facebook Story/Reel 1080×1920; Facebook Feed/link landscape 1200×630.

Currency discipline: "**Last verified:** 2026-11-02" and "**Review cadence:** Every 90 days, or when a platform changes its creative specifications."

**Unique ideas.** The near-duplicate cluster rule is genuinely rare and prevents four near-identical exports. The rule ladder that decides *when not to ask* is the best interaction-design pattern in the cluster. The 90-day review cadence is the only maintenance contract present.

**Pitfalls.** Fanning out duplicate canvases; assuming a placement when only a platform was named; treating resize as a redesign (the skill draws the boundary explicitly: use edit-design "when the user asks to recompose, adjust crop or safe areas, change copy, or use generative fill").

**Against our MCP.** `resize-design` exists and returns the documented `job.result.design.*` shape. Caveats: the default set has no 1:1 square, so an "all channels" request silently skips the most common feed format for some platforms; the skill says "Resize operations should be performed in parallel" while bulk-create says the opposite for its loop — for resize, parallelism is fine (independent new designs), but it contradicts the general "sequential is safer" instinct and should be stated with its reason. Resized copies reflow layout, which is exactly what a 16-slide deck cannot survive un-reviewed.

---

## Skill: cli

**Purpose.** Use the `canva api` CLI when a task needs local files, scripting, or REST resources the MCP doesn't expose.

**Prescribed process** (`.../skills/cli/SKILL.md`):

1. Check `canva --version`; if missing, install with `npm install -g @canva/cli@latest` **only when the user approved it**.
2. `canva login` (browser flow; `--mode manual` when headless); never request, print, inspect or copy the stored token; use `--profile <name>` for one-offs.
3. Discover operations rather than guessing: `canva api --help` → `canva api <group> <command> --help` → `canva api describe <group> <command>`.
4. Before a write, run with `--dry-run` when available.
5. Interpret one JSON object from stdout: check `ok`; on success read `data`; on failure report `error.code`, `error.message`, `meta.status`; treat `next` as a suggestion to verify, not a command to run.
6. Async jobs: save the job id, poll the "Get job" command with exponential backoff, never concurrent or tight-loop polls, stop immediately on `success`/`failed`.
7. Report action, target, result, ids/URLs — no credentials.

**Rules and thresholds.** Requires "Node.js v24 and npm v11"; `MISSING_SCOPE` → log in again before retrying; a usage error means consult `--help`, not retry with guessed flags; if a job outlives the task, report the job id and latest status.

**Unique ideas.** The discover-help-describe ladder; `--dry-run` as a validation step; the rule that a *suggested* next command must be verified before running.

**Against our MCP.** Off-path: the CLI needs a global install, Node v24 (a version claim worth verifying against the published package, which field notes put at engines node=22), and its own OAuth, while the MCP is already mounted. Nothing in this skill is needed for slide work. Keep only the async-polling contract, which is the same discipline `get-create-design-async-job` needs.

---

## Skill: branded-presentation (inactive)

**Purpose.** Outline or brief → on-brand deck via the legacy generator.

**Prescribed process** (`.../inactive-skills/branded-presentation/SKILL.md`):

1. Get the content source: pasted text, a raw `D...` id (`start-editing-transaction` to read it), a design link, or a doc found with `search-designs`.
2. `list-brand-kits`; if exactly one exists, use it automatically; if several, present and ask.
3. `generate-design` with `design_type: "presentation"`, `brand_kit_id`, and a structured `query`.
4. Show the candidates; ask which one; `create-design-from-candidate`; return the link.

**Rules and thresholds.** The query template (section "Presentation Query Format") has five parts: **Presentation Brief** (Title, Topic/Scope 1–2 lines, Key Messages **3-5**, Style Guide), **Narrative Arc** (one paragraph, e.g. Hook → Problem → Solution → Proof → CTA), **Slide Plan** (per slide: `Slide N — "Exact Title"`, Goal one sentence, Bullets **3-6** short parallel phrases, Visuals an explicit recommendation, Speaker Notes **2-4** sentences), then expansion rules: sparse outline → expand into a full plan; briefs → extract and structure; titles action-oriented.

**Unique ideas.** The per-slide record (title / goal / bullets / visual / notes) is the cleanest deck-outline schema in the cluster and maps one-to-one onto `create-design`'s `outline.sections[{title, description, points}]`.

**Pitfalls.** Auto-selecting a kit; leaving a sparse outline sparse; returning candidates without a chosen design.

**Against our MCP.** `generate-design` and `create-design-from-candidate` are legacy-only here ("DO NOT CALL WHEN create-design IS AVAILABLE"), and `brand_kit_id` is unusable with zero kits. `list-brand-kits` returns empty, so step 2 must become "state that no kits exist and continue, or ask the user for colours/fonts". The *schema* survives; the *mechanism* does not.

---

## Skill: generate-deck (inactive)

**Purpose.** Force the broad generator to produce deck-shaped output for sales/marketing.

**Prescribed process** (`.../inactive-skills/generate-deck/SKILL.md`):

1. Call `generate-design` **directly** with `design_type: "presentation"` — never `prepare-design-generation` / `_prepare_design_generation`.
2. Infer missing parameters (audience, length, tone, objective) rather than blocking; ask only when the choice would materially change the deck.
3. `list_brand_kits`; always ask the user to choose; never auto-select "even if only one kit is available".
4. Pass `brand_kit_id`; if none exist, say so and ask whether to continue without one.
5. Write the prompt as a deck brief (11 components, below).
6. Present candidates; `create-from-candidate`; return the link.

**Rules and thresholds.** "for a normal first draft, aim for **8-12 slides**". Three narrative arcs: Problem → insight → solution → value → proof → next step; Market shift → customer need → product story → differentiation → results → CTA; Audience pain → desired outcome → offer → capabilities → credibility → buying path. Eleven required prompt components: working title; audience and objective; slide count/range; narrative arc; brand/product/offer/category/positioning; customer pain points and desired outcomes; value props/differentiators/proof; slide-by-slide outline with titles; bullets per slide; visual direction per slide (chart, timeline, comparison table, product screenshot, diagram, image subject); speaker-note guidance; plus any supplied constraints. Bans template tools explicitly (`search-brand-templates`, `get-brand-template-dataset`, `autofill-design`, `create-design-from-brand-template`) and bans doc/proposal/report/infographic/poster/social design types.

**Unique ideas.** "Always give `generate-design` enough deck-specific context in its `query` so it does not produce a document-like or single-page result" — i.e. the generator's failure mode is *becoming a document*, and the fix is explicit per-slide visual direction. Also the instruction to *stop and tell the user* rather than take a forbidden intermediate step.

**Pitfalls.** Letting the generator choose structure; a document-shaped prompt; auto-selecting a brand kit; mixing template workflows into direct generation.

**Against our MCP.** Its entire central argument is moot: our mount has no `prepare-design-generation` tool at all, and `generate-design` is legacy. Worse, the file's frontmatter is `name: canva-branded-presentation`, colliding with the other inactive skill — two skills claim one identity, both are unregistered, and the root README doesn't even list `generate-deck` among the inactive set (`canva-sdks_canva-skills/README.md`, "Inactive Skills", lists four of the five that exist). Treat this file as dead weight except for the 11-component brief checklist and the "decks degrade into documents" insight.

---

## Skill: classroom-helper (inactive)

**Purpose.** Lesson plan → teachable deck, with pedagogy first and a long, unusually honest section on generated imagery.

**Prescribed process** (`.../inactive-skills/classroom-helper/SKILL.md`):

1. Get the lesson plan first — text, `D...` id, link, or doc-by-name via `search-designs`; if absent, ask **one** question matching that step only, and explicitly **do not** open with a two-part "paste the plan / describe the topic" prompt.
2. `list-brand-kits`; one → use it; several → ask (school/district brand if relevant).
3. `generate-design` with `design_type: "presentation"`, `brand_kit_id`, and a pedagogy-first query.
4. Show candidates, ask which, `create-design-from-candidate`, return the link plus a one-line reminder of slide order vs lesson phases.
5. Query should open with **one line** stating total slide count and that the output must be a standard multi-slide deck, "never a poster, flyer, or single-page layout".

**Rules and thresholds.**

- Query sections: **Lesson brief** (subject/unit/grade, title + duration, learning objectives "verbatim from the plan when provided", standards only if supplied); **Classroom arc** (one paragraph — Engage → Explore → Explain → Elaborate → Evaluate, or I Do / We Do / You Do); **Slide plan** (Slide N exact title; teaching goal one sentence; on-slide content **3–6** bullets, "avoid walls of text"; visuals; speaker notes **2–5** sentences with misconceptions, checks for understanding, timing hints); optional **Materials & logistics**; optional **Differentiation/extensions**.
- Pedagogy rules: "Respect the lesson plan" (sequence, vocabulary, activities); "One main idea per slide"; age-appropriate; sparse plan → standard structure **and flag the assumptions**.
- Visual-integrity rules (lines 81–84, the most valuable passage in the cluster), verbatim: prefer "simple photos, textures, icons, or abstract backgrounds; avoid asking the generator for dense infographics, labeled illustrations, or 'posters with lots of text' in the image itself"; "**Do not rely on text baked into images** — state that key terms, definitions, questions, numbers, and all curriculum-critical wording belong in on-slide text"; for accuracy-critical slides ask for "minimal or decorative imagery" and put the content in bullets; optionally request an "image-light or clean-template feel so educators can swap in vetted Elements, uploads, or screenshots".
- Hand-off honesty (line 90): "auto-generated lesson visuals are **drafts** … treat images and on-slide facts as **unverified** until reviewed."
- Lists what automated visuals reliably get wrong: readable text inside images, exact facts (dates, names, quotes, vocabulary), precise maps/timelines/charts, depictions of specific people/places/events, and any slide where wording matters for assessment.

**Unique ideas.** Naming the *classes of content that generative imagery corrupts*, rather than a generic "check the images". The instruction to deliberately design an image-light deck so a human can drop in vetted assets afterwards. The "one question, matching this step only" anti-pattern note — a rare example of a skill criticising prior skill design.

**Pitfalls.** Asking for topic + plan twice; walls of text per slide; letting the generator render terminology inside pictures; presenting the deck as final.

**Against our MCP.** Same generator problem as branded-presentation (`generate-design` legacy, `create-design-from-candidate` legacy, zero brand kits). Everything from "Lesson brief" through the visual rules is mechanism-independent and should be lifted wholesale into the planning prompt for `create-design`, which accepts `outline.sections[{title, description, points}]` and paraphrases — so the no-text-in-images rule must be enforced *after* generation, not relied on in the brief.

---

## Skill: design-translation (inactive)

**Purpose.** Produce a translated copy of a design without touching the original.

**Prescribed process** (`.../inactive-skills/design-translation/SKILL.md`):

1. Locate the design (id / URL / name — never pass an id to `search-designs`).
2. Clone with `resize-design` at **the same dimensions** — "This preserves the original design untouched."
3. `start-editing-transaction` on the copy to get `transaction_id` plus every text element's `element_id` and current text.
4. Translate each element; preserve line breaks and emphasis patterns; keep proper nouns, brand names and technical terms as appropriate.
5. Apply all translations as `replace_text` operations batched in a **single** call; append the language to the design title.
6. Show the preview thumbnail, get explicit approval, `commit-editing-transaction`, hand back the link.

**Rules and thresholds.** Always copy, never edit the original; batch all replacements; "If translation significantly changes text length, warn user that layout adjustments may be needed"; translate all pages inside the same transaction.

**Unique ideas.** Clone-by-resize-as-same-dimensions as a poor-man's duplicate; the language suffix in the title; the length-change warning.

**Pitfalls.** Editing the original; per-element calls; silent overflow after expansion (it warns but does not check); translating names that shouldn't be translated.

**Against our MCP.** The clone step is obsolete: `copy-design` exists and duplicates without reflow, which is strictly safer than `resize-design` at identical dimensions. `replace_text` per element works, but the skill never checks whether a translation overflowed its text box — with `format_text` unable to change font family and no auto-fit operation, expansion must be handled by authoring shorter Vietnamese/English text up front. Also note `replace_text` on a grouped child id is a known no-op in this environment; the skill has no element-scope warning.

---

## Skill: presentation-time-fitting (inactive)

**Purpose.** Fit a deck to a speaking duration using presenter notes only.

**Prescribed process** (`.../inactive-skills/presentation-time-fitting/SKILL.md`):

1. Collect design **and** total speaking duration before any other Canva call; parse to seconds; ask and wait if either is missing.
2. Resolve the design (shortlink / URL / id / name).
3. Clone with `resize-design` at the same dimensions.
4. `get-design-content` on the copy; slide count = number of content-bearing pages.
5. Equal split per slide; derive a word budget.
6. Compose notes per slide in-session from that slide's text plus its budget; stay faithful to the visible message; for visual-heavy slides, describe what to say about the visual.
7. `get-design-pages` for page ids; open the transaction **early** (before composing) to avoid timeouts; `perform-editing-operations` with **only** the notes operation, batched; commit.
8. Hand off the copy link plus a one-line recap of total time and per-slide allocation.

**Rules and thresholds.** `target speaking time per slide = total_duration ÷ number_of_slides`; `target_words ≈ target_minutes_per_slide × 150` — "~**150 words/minute** as a guide … treat as guidance, not a hard cap". Scope fence: notes only; never `replace_text`/`find_and_replace_text`/formatting/media/layout/title. If the target is impossible for the slide count, say so — "The API cannot add or remove pages." Timeout protocol: retry once after 15–30 s; open the transaction earlier in the flow; test on a smaller copy; final fallback is to paste the notes into chat grouped by slide so the user can enter them manually. Acknowledge the squeeze in the notes ("prioritise X, skim Y") rather than cutting slide text.

**Unique ideas.** The 150 wpm → word-budget arithmetic is the only quantitative speaking-pace model in the cluster. The transaction-early ordering to survive long generation gaps is an operational insight that applies to *every* long edit session. The degradation ladder (retry → reorder → smaller copy → manual paste) is the best failure-handling pattern here.

**Pitfalls.** Cloning before confirming duration; deferring `start-editing-transaction` until after a long composition; treating notes as licence to edit slides.

**Against our MCP.** **Unusable as written.** Step 7 says to use "only the operation type the Canva MCP exposes for presenter/speaker notes (name may vary by connector)" — our mount exposes `get-presenter-notes` (read-only) and `perform-editing-operations` has no notes operation at all. So the entire deliverable must be redirected to chat or to a sidecar document. The rest (duration math, per-slide budgets, the timeout ladder) is reusable; the write path is not. Flag it explicitly rather than let the agent call a non-existent op.

---

## Skill: canva-design-infrastructure (dev kit)

**Purpose.** Decide *whether* and *how* to use Canva when building something, not how to make a slide.

**Prescribed process** (`canva-sdks_canva-developer-agent-kit/skills/canva-design-infrastructure/SKILL.md`):

1. Ask whether the output must become a designed asset (editable, branded, resized, exported, approved, published, reused).
2. If yes, pick the simplest path: Canva MCP (open-ended agent creation/editing from a prompt, brief, image); Developers SDK REST (structured data, templates/autofill/exports/folders/resize, backend generation); Apps (runs inside Canva); CLI/docs (building the integration).
3. Explain the choice in one sentence.
4. When a capability is missing: "Do not silently switch to another provider"; state what Canva can do today; use a mock or future-API note; prefer honest buildability.

**Rules and thresholds.** "If the output needs to become a designed asset, start with Canva." Use standalone image generation "only when the user needs an isolated image, concept visual, or background". Anti-pattern list: do not position Canva as an image model; do not default to OpenAI image gen, Flux, Ideogram, Gamma, or custom HTML when the task is designed assets; "Do not claim a Canva REST generation API exists unless it is available in the current docs."

**Unique ideas.** The MCP-vs-REST-vs-Apps-vs-CLI decision matrix (mirrored in `templates/AGENTS.md` and `templates/CLAUDE.md`). The "never silently downgrade to another provider" rule.

**Against our MCP.** Nothing to port mechanically; the one transferable rule for a skill file is the honesty clause — do not invent a tool or operation, state the gap. That clause is exactly what a slide skill needs around notes, font family, background, and page count.

## Agent templates (dev kit)

`templates/README.md` gives concrete budgets: `AGENTS.md` "stays around **300–600 words**, with a hard cap around **900 words**"; `CLAUDE.md` "roughly **50 lines** or a few thousand tokens, and ideally readable in under a minute"; "The file should help an agent make good decisions quickly, not act as a second README." `templates/AGENTS.md` ends with a six-item **Definition of Done for Visual Assets**: integration path selected; brand/format requirements met; auth and failure states handled; result editable/exportable/usable; limitations documented; tests or mock flows pass. Useful as the acceptance list for a generated deck (swap items to: deck opens, text unclipped, every slide readable at projection size, links resolve, no placeholder content, review pass done).

## Recipes and example (dev kit)

- `recipes/canva-product-imagery/README.md` is the only place in the cluster documenting image generation mechanics: POST with `prompt`, `aspect_ratio`, `count`, `model`, `idempotency_key`; poll while `job.status` is `in_progress`; read `job.result.image.url`; and the important detail that "`aspect_ratio` is a name, not a pixel ratio: `1:1` maps to `square`, taller frames to `portrait`, wider frames to `landscape`" while "the exact ratio stays in the prompt as `framed 4:5`". Directly relevant to `generate-image` prompting and to the `credit_quota_exceeded` failure we hit.
- `recipes/canva-social-campaign/README.md` describes the analyse → brand summary (metadata, colours, logo candidates) → campaign brief → asset specs → generation payload pipeline; Canva generation is stubbed (`src/lib/canva/generate-design.ts`), so it is a shape, not an implementation.
- `examples/campaign-image-studio-starter/README.md` contributes OAuth facts: Authorization Code with **PKCE**, server-side tokens, HTTPS callback required, scopes `asset:write, asset:read, design:content:write, design:content:read, design:meta:read`, and the warning that "OAuth access alone does not guarantee access to these endpoints". `SANITIZATION.md` is a model of stating export scope; not relevant to slide craft.
- The remaining dev-kit files add nothing to slide craft and are listed for completeness: `recipes/canva-product-imagery/CLAUDE.md` is a one-line include (`@AGENTS.md`) — a neat de-duplication pattern for a skill package that must support several host filenames; `examples/.../CLAUDE.md` is a condensed mirror of its `AGENTS.md` with a concrete command list (`pnpm install --frozen-lockfile`, `pnpm --filter @workspace/db push`, two `PORT=`-prefixed dev commands, `test`, `typecheck`); `examples/.../scripts/` holds only `package.json` + `tsconfig.json` for a `tsx` typecheck helper; `recipes/*/package.json` and `tsconfig.json` are Next.js scaffolding (Next 16.3.4, React 19.2.8). There are **no** skill scripts, generators, or reference assets anywhere in this cluster — every skill is prose plus, in one case, a markdown table.

---

## openai/plugins — every variant and every difference

The OpenAI package is a **repackaging of the canva-skills set**, not an independent implementation. Eight skills, `./skills` auto-discovery, no `references/` directory anywhere, no `inactive-skills/`, no CLI skill.

Manifest facts: `openai_plugins/plugins/canva/.codex-plugin/plugin.json` is `version: 14.0.0` (canva-skills is `1.0.0`), points at `./skills`, adds `apps: ./.app.json` (connector id `connector_68df33b1a2d081918778431a9cfca8ba`), and its marketing description lists only **six** skills — `canva-branded-presentation` and `canva-translate-design` are shipped but never advertised. `.mcp.json` is identical to canva-skills (`https://mcp.canva.com/mcp`). Marketplace entry (`openai_plugins/.agents/plugins/marketplace.json`) is `installation: AVAILABLE`, `authentication: ON_INSTALL`, `category: Creativity`.

| openai skill | canva-sdks counterpart | Difference |
|---|---|---|
| `canva-edit-design` | `edit-design` | **Byte-identical** (5769 bytes). No change. |
| `canva-implement-feedback` | `implement-feedback` | **Byte-identical** (7170). No change. |
| `canva-design-feedback` | `get-design-feedback` | **Byte-identical** (4735); only the folder is renamed to match the frontmatter `name: canva-design-feedback`. |
| `canva-brand-check` | `brand-check` | **Byte-identical** (5147). |
| `canva-bulk-create` | `bulk-create` | **Byte-identical** (5309). |
| `canva-resize-for-social-media` | `resize-for-social-media` | **Differs** (5887 vs 6646) — detailed below. This is an *older* revision, not an improvement. |
| `canva-branded-presentation` | inactive `branded-presentation` | **Byte-identical** (3090) to the inactive file, promoted to active. Because the folder name now matches the frontmatter, OpenAI's copy does not have canva-skills' naming collision. |
| `canva-translate-design` | inactive `design-translation` | **Byte-identical** (2846), promoted to active, folder renamed to the frontmatter name. |

Skills present in canva-skills but **absent** from openai/plugins: `cli`, `generate-deck`, `classroom-helper`, `presentation-time-fitting`, and `references/channel-formats.md`. So the OpenAI set is: six active mirrors + two promoted-inactive skills, minus the CLI, minus the two deck-craft skills, minus the dimension reference.

### Skill: openai `canva-resize-for-social-media` (the one substantive fork)

**Purpose.** Same goal, weaker execution: resize into five named formats.

**Process.** Identify the design (id / URL — and here it tells you to extract the id — / name / context); `get-design` (also to get the title for naming outputs); **ask the user which platforms and formats**; run `resize-design` once per selected format, in parallel; report links grouped by platform, plus a note that Facebook Story and Instagram Story are the same size.

**Differences from the canva-sdks version, explicitly:**

1. **No reference file.** `references/channel-formats.md` is absent; the five dimensions are inlined as literals. There is no review cadence and no "last verified" date.
2. **Five formats only**: Facebook post 1200×630, Facebook story 1080×1920, Instagram post **1080×1080**, Instagram story 1080×1920, LinkedIn post 1200×627. No TikTok, X, YouTube, Pinterest, no 4:5 portrait, no video canvas.
3. **Interactivity inverted**: it always asks "Which platforms and formats would you like to resize for?" whereas canva-sdks deliberately *does not ask* for an all-channels request (rule 4) and asks only for a named platform without a placement.
4. **No de-duplication.** It says "Create both versions but inform the user they're the same size" — the exact opposite of canva-sdks' de-dup-with-multiple-labels rule.
5. **Instagram feed size is 1:1 (1080×1080)**, while canva-sdks defaults feed to 4:5 (1080×1350) and reserves 1:1 for the aspect-ratio set. For a phone-first audience the 4:5 default occupies materially more screen.
6. **Presentation**: an emoji checklist ("✅ Successfully resized…") and per-platform bullet blocks instead of a status table; it adds "Consistent naming: use the source design title with platform suffix", which canva-sdks lacks.
7. **URL handling**: it explicitly says to extract the id from the URL and pass the id; canva-sdks permits passing the share URL straight to `get-design`.

**Verdict.** Port nothing from this variant except the naming convention (title + platform suffix). Its 1:1 feed default, missing de-dup, and always-ask interaction are all regressions.

---

## Merge recommendations

| Idea | Source skill(s) | Keep / adapt / drop | Why | Where it belongs |
|---|---|---|---|---|
| Transaction protocol: start → perform(batched) → commit/cancel, with `transaction_id` + `pages` reused | edit-design | **Keep verbatim** | The only correct way to mutate a design; `pages` reuse is mandatory in our mount | edit |
| Explicit CAN / CANNOT capability matrix | edit-design, implement-feedback (duplicated) | **Keep, one copy only** | Prevents hallucinated edits; dedupe to avoid drift between two lists | edit (referenced from every other phase) |
| Responsive-page restricted op set (`update_title`, `replace_text`, `update_fill`, `delete_element`, `find_and_replace_text`) | edit-design | **Keep** | Silent failures otherwise; no other skill checks `is_responsive` | edit |
| Commit approval gate + the "caller already approved" override | edit-design, implement-feedback | **Keep both, and state the precedence rule** | Resolves a real contradiction between the two files in one sentence | edit |
| "One approval, then never ask 'shall I commit'" | implement-feedback | **Keep** | Correct UX for a 16-slide batch; prevents confirmation fatigue | edit / review |
| "Be helpful, not cautious" triage; escalate only on contradiction or unlocatable reference | implement-feedback | **Keep** | Converts vague review comments into work instead of questions | review |
| 3-way triage: Actionable / Requires manual action / Resolved | implement-feedback | **Keep** | Clean output contract for review rounds | review |
| Manual-changes checklist with slide no., what, who, why, and a → step | implement-feedback | **Keep verbatim shape** | Turns API impossibility into a usable worklist | delivery |
| Reply-to-comment to close each thread | implement-feedback | **Keep** | Closes the loop; tool exists (`reply-to-comment`) | review |
| "Colors and fonts are NOT reliably exposed — never assert a hex/font unless the payload contained it" | get-design-feedback, brand-check | **Keep, promote to a global evidence rule** | The single biggest anti-hallucination guard; applies to every claim about a slide | review |
| Read-only transaction (start → inspect → cancel) for layout/spacing data | get-design-feedback, brand-check | **Keep** | Only way to get element geometry; also the safest inspection mode | review / edit |
| Seven review lenses + High/Med/Low + "what's working" | get-design-feedback | **Keep** | Produces a critique a student can act on; the positive section keeps it usable | review |
| "~1.5× body" title ratio | get-design-feedback | **Keep as a starting scale, then extend** | Only number in the cluster; insufficient alone for 1920×1080 classroom viewing | review / structure |
| On brand / Off brand / **Can't verify** | brand-check | **Keep the verdict system, drop the brand-kit dependency** | "Can't verify" is the right answer when we have no kit; the check itself is unusable here | review |
| Five-rule target-resolution ladder; "do not ask" on all-channels; ask only for platform-without-placement | resize-for-social-media | **Keep verbatim** | Best interaction design in the cluster; removes pointless questions | export |
| Near-duplicate canvas cluster (627/628/630) → create once, label thrice | resize-for-social-media + channel-formats.md:11 | **Keep verbatim** | Prevents four near-identical exports and the review burden that follows | export |
| Dated dimension tables with 90-day review cadence | channel-formats.md:3-5 | **Adapt** | Keep the cadence and `Last verified` header; add 1:1 to the default set for our use | export |
| Sequential bulk loop, per-item status line, test-first-3 for 50+ items, "no undo" warning | bulk-create | **Keep as a general batch contract** | Applies to any repeated create/edit; the autofill-specific parts die here | generate / edit |
| Just-in-time upload ordering (upload asset immediately before the row that needs it) | bulk-create | **Keep** | Localises failures; same logic applies to inserting diagrams one page at a time | visuals |
| Clone by `resize-design` at identical dimensions | design-translation, presentation-time-fitting | **Drop** | `copy-design` exists in our mount and clones without reflow | edit / structure |
| Translation workflow: batch `replace_text`, keep proper nouns, append language to title | design-translation | **Adapt** | Good for bilingual decks; must add an overflow pass and element-scope warning | edit |
| 150 wpm → per-slide word budget; equal split; state the assumption | presentation-time-fitting:39-40 | **Keep the arithmetic, drop the write path** | Notes cannot be written through our MCP; budgets still drive slide density | plan / delivery |
| Open the transaction early so long composition doesn't sit between "ready" and "started" | presentation-time-fitting:52-57 | **Keep** | Directly addresses the transaction-timeout failures we have seen | edit |
| Timeout ladder: retry once after 15–30 s → reorder → smaller copy → paste notes in chat | presentation-time-fitting, "When start-editing-transaction fails" | **Keep** | Concrete, ordered, and honest about whose fault it isn't | edit |
| Per-slide record: exact title / goal / 3–6 bullets / visual / 2–5 note sentences | branded-presentation, classroom-helper | **Keep, merge into one schema** | Maps cleanly onto `create-design` `outline.sections` | plan / generate |
| "Open the query with one line: total slide count + standard multi-slide deck, never a poster/flyer" | classroom-helper:39 | **Keep** | Cheapest known guard against single-page output | generate |
| "One main idea per slide"; respect the source's sequence and vocabulary; flag expansions | classroom-helper | **Keep** | Protects doctrinal accuracy — our specific failure mode | plan / structure |
| Visual-integrity rules: no text baked into images, no dense infographics/labeled illustrations, put curriculum-critical wording in on-slide text, request image-light layouts for later human swap-in | classroom-helper:81-84 | **Keep verbatim — highest-value passage in the cluster** | Directly explains why generated diagrams arrive garbled and mislabeled | visuals |
| "Warn that generated visuals are drafts / unverified" | classroom-helper:90 | **Keep** | Sets expectations before the user presents | delivery |
| 8–12 slide first-draft range; three narrative arcs; 11-component deck brief | generate-deck | **Keep the numbers and the arcs, drop the anti-`prepare-generation` polemic** | The tool it argues about doesn't exist here | plan / generate |
| "The generator's failure mode is becoming a document" → always give per-slide visual direction | generate-deck:14 | **Keep** | Explains a symptom we have seen in generated decks | generate |
| Brand-kit selection rule | branded-presentation:20 vs generate-deck:49 | **Adapt: ask once; if zero kits, say so and proceed** | Our account has zero kits, so both variants collapse to the same behaviour | plan |
| Dev-kit honesty clause: don't invent a capability, document the gap, never silently downgrade | canva-design-infrastructure | **Keep as a hard rule** | The skill must state that notes/font-family/background/page-count are impossible | global |
| AGENTS/CLAUDE word budgets (300–600, cap ~900; ~50 lines) and six-item DoD | templates/README.md, templates/AGENTS.md | **Adapt** | Good discipline for the skill file itself; rewrite the DoD for deck output | meta |
| Image-generation facts: `aspect_ratio` is a name (`square`/`portrait`/`landscape`), exact ratio stays in the prompt, poll `job.status` until not `in_progress`, read `job.result.image.url` | canva-product-imagery/README.md | **Keep** | Needed to prompt and poll `generate-image` correctly, and to fail gracefully on quota errors | visuals |
| CLI discovery ladder, `--dry-run`, one-JSON-object result contract | cli | **Drop** | Off-path for MCP work; requires a separate install and login | — |
| Candidate flow (`get-design-candidates` → `create-design-from-candidate`) | branded-presentation, generate-deck, classroom-helper | **Drop** | Legacy-only in our mount | — |
| Always-ask-which-platforms interaction | openai `canva-resize-for-social-media` | **Drop** | Canva-sdks' rule 4 is strictly better | — |
| "Create both story variants since they're the same size" | openai `canva-resize-for-social-media` | **Drop** | Contradicts de-dup; doubles review work | — |
| Naming convention: source title + platform/section suffix | openai `canva-resize-for-social-media` | **Keep** | Cheap, and makes a folder of variants navigable | export / delivery |

---

## Contradictions

1. **Brand-kit selection.** `branded-presentation:20` — "If only one brand kit exists, use it automatically without asking." `generate-deck:49` — "Do not auto-select a brand kit, even if only one kit is available." *Recommend:* generate-deck's rule, softened for the degenerate case: ask when a kit exists, and if none exist say so in one line and proceed. In this account `list-brand-kits` returns empty, so the branch never triggers; but the *principle* (never silently pick a style authority) is the right one, and a student's deck has no kit at all.

2. **Approval granularity.** `edit-design` requires an approval before every commit; `implement-feedback` requires exactly one approval and forbids any later "shall I commit?". *Recommend:* adopt edit-design's gate as the default and implement-feedback's override explicitly — one up-front approval may cover a batch commit, provided the skill says so in advance and shows a preview afterwards. Without the override, a 16-slide feedback round becomes 16 confirmations.

3. **Parallel vs sequential fan-out.** `resize-for-social-media` — "Resize operations should be performed in parallel for efficiency." `bulk-create:81` — "Call them **sequentially**, not all at once — the API may have rate limits." *Recommend:* both, with the reason stated: resize creates independent designs and parallelises cleanly; bulk autofill writes into one template lineage and benefits from sequential calls plus per-item status. Do not generalise either rule.

4. **Feed creative size.** openai `canva-resize-for-social-media` uses Instagram post 1080×1080; canva-sdks defaults feed to 1080×1350 (4:5) and lists 1:1 only in the aspect-ratio set. *Recommend:* 4:5 as the default for feed, 1:1 on request — more vertical screen use on phones.

5. **De-duplication.** canva-sdks: "De-duplicate identical width × height pairs while retaining every requested platform label" (SKILL.md Step 3) and the 627/628/630 rule (channel-formats.md:11). openai: "Create both versions but inform the user they're the same size." *Recommend:* canva-sdks. Two identical canvases are two things to review and two links to lose track of.

6. **Generator entry point.** Every deck skill routes through legacy `generate-design` (+ `brand_kit_id`, + candidates). Our mount's primary path is `create-design(brief, format, outline.sections, user_intent)` with an async job, and `generate-design` is marked legacy-only. *Recommend:* create-design for structure. Use `generate-design` only if a brand kit ever exists, and never cite `prepare-design-generation` (absent here).

7. **`generate-deck` vs `branded-presentation` identity.** Both inactive files declare `name: canva-branded-presentation` (`generate-deck/SKILL.md:2`, `branded-presentation/SKILL.md:2`). *Recommend:* ignore `generate-deck` as a skill; harvest only its brief checklist and the document-degradation insight.

8. **Thumbnail access.** `get-design-feedback` Step 2 and `brand-check` Step 3 call `get-design-thumbnail` without a transaction; our tool requires an editing-transaction id. *Recommend:* our skill must specify the access order (`get-design-pages` → thumbnails, or open one transaction, fetch per page, cancel). This is an environment correction, not a disagreement between sources.

9. **Resize as clone.** `design-translation:22` and `presentation-time-fitting:29` both clone via `resize-design` at identical dimensions. `copy-design` exists in our mount. *Recommend:* `copy-design`; resize-at-same-size risks a reflow pass for no benefit.

10. **What "all channels" means.** canva-sdks rule 4 creates four canvases (no 1:1); openai creates five (no 4:5 portrait video, no 16:9). *Recommend:* publish one explicit default set for our use — 1080×1350 feed, 1080×1920 vertical, 1920×1080 presentation/video, 1200×627 link — and name what was skipped, so "all" is never ambiguous.

---

## Gaps

A complete slide workflow still needs all of the following; **no official skill covers them**.

1. **A create-then-verify loop.** Every deck skill generates and hands back candidates; none re-reads the output. Since `create-design` paraphrases the outline and can substitute doctrinal terms (the exact failure we hit with "phát triển" replacing a required property), the mandatory step "generate → `get-design-content` on every page → diff against the approved outline → repair" exists nowhere. This is the single largest gap.
2. **A numeric typographic scale for 1920×1080.** The cluster offers one ratio ("~1.5× body"). There is no title/body/caption ladder, no minimum body size for projection, no line-length or line-height target, and no rule for Vietnamese diacritics at distance.
3. **Layout system.** No margins, grid, safe area, alignment axis, or "max N bullets / max M words per bullet" budget tied to slide count. `classroom-helper` gives 3–6 bullets and `branded-presentation` 3–6, but nothing about text volume per slide or where the content block sits.
4. **Slide architecture.** No title slide, agenda, section divider, comparison, timeline, quote, or closing/CTA page patterns; no rule for how many consecutive text-only slides are acceptable.
5. **Diagrams and custom visuals.** Nothing on producing a diagram outside Canva (render PNG → `create-upload-url` → `insert_fill`), nothing on when a diagram beats text, nothing on labeling diagrams in-language, and nothing on the known trap that labels baked into a PNG are not editable. `generate-image` prompting is covered only by dev-kit recipes (aspect-ratio names, polling), never by a slide skill.
6. **Inserting/moving/reordering pages.** `resize-design` is the only structural tool any skill mentions. `merge-designs` (insert_pages / move_pages / delete_pages / create_new_design), `copy-design` with page ranges, and the reversed-insert-order bug are entirely absent.
7. **Export and delivery.** No skill calls `export-design` or `get-export-formats`; there is no PPTX-vs-PDF guidance, no print/handout advice, no filename convention, no "verify the exported file before you present" step. A deck skill that ends at a Canva link is not finished for a classroom.
8. **Presenter notes mechanics.** One skill wants to write notes; our MCP cannot. A real skill must say up front that notes are read-only here and offer a concrete substitute (chat block, sidecar file, or notes on a duplicated deck for manual paste).
9. **Backup/rollback discipline.** `bulk-create` warns "no undo"; `implement-feedback` commits without a snapshot. Nothing says "duplicate before a risky batch". With no `delete-design` tool, an accidental commit is permanent, so a pre-flight `copy-design` should be mandatory before multi-slide edits.
10. **Comment-to-page anchoring.** `implement-feedback` never resolves a thread to a `page_id`, and `list-comments` gives no slide index. A 16-slide deck needs that mapping before edits can be scoped.
11. **Accessibility actions.** `get-design-feedback` lists alt text as a lens but no operation writes alt text; contrast is judged by eye from a thumbnail. No guidance on what to do about it.
12. **Quota and cost failure.** Nothing on `credit_quota_exceeded` from `generate-image` (resets, fallbacks like diagram-by-PNG or vector shapes), and nothing on rate limits for large decks.
13. **Responsive-page strategy for decks.** edit-design states the restricted op set but not what to do when a whole deck is responsive: whether to rebuild as fixed-page, which pages can still take `format_text` for a font-size pass, or how to plan edits that survive.
14. **Language and text expansion.** One sentence ("warn user that layout adjustments may be needed") covers translation overflow. There is no rule for authoring longer Vietnamese strings up front, no per-locale length multiplier, and no reflow check after `replace_text`.
15. **Multi-round review state.** `implement-feedback` handles one pass. Nothing tracks which findings were fixed across rounds, or how to re-verify only what changed.
16. **Deck-length to time mapping.** Time-fitting assumes a finished deck. Nothing connects "10-minute talk → N slides → words per slide" at the planning stage, which is when the decision is cheap.
