# 02 — Community Canva skills: structured extraction

Reader: `CommunityCanva`. Sources read in full under `/tmp/skills-src` (all markdown/JSON; every
`references/`, `assets/`, `scripts/` doc and `samples/` note in the four assigned clusters).
All paths below are relative to `/tmp/skills-src`.

---

## Inventory

| Skill | Repo path | License | What it is (one sentence) | Verdict |
|---|---|---|---|---|
| **canva-design-director** | `mavericraven_canva-design-director/` (SKILL.md, README.md, 17 refs, 5 assets) | MIT — declared in `README.md` §License ("MIT License"); **no LICENSE file in the clone**, no repo metadata | A strict "elite design director" persona that forces a stated plan (grid/type/colour/focal point) before any Canva MCP call, plus an anti-AI-slop rulebook. | **B** — the doctrine and the numeric limits are the most reusable thing in the whole cluster; its tool names are largely stale/nonexistent against our server. |
| **canva** (TerminalSkills) | `TerminalSkills_skills/skills/canva/SKILL.md` + `_scores.json` | Apache-2.0 (`TerminalSkills_skills/README.md` §License; LICENSE absent from the clone) | The only source that documents the *two* Canva automation surfaces (AI Connector MCP vs Connect REST API) with per-tool rate limits, per-endpoint scopes, and the async-job contract. | **A** — the reference for facts, not for design. |
| **use-case: batch-produce-brand-designs-with-canva** | `TerminalSkills_skills/use-cases/batch-produce-brand-designs-with-canva.md` | Apache-2.0 | A 240-variant autofill run told as an ops story, with the throttle maths spelled out. | **A−** — best worked example of "jobs are not results" at scale. |
| Incidental Canva mentions in TerminalSkills | `skills/growth-hacking/SKILL.md:61`, `use-cases/build-ai-content-monetization-pipeline.md:214`, `use-cases/build-design-editor-canvas.md`, `use-cases/pivot-struggling-startup.md:94` | Apache-2.0 | Not Canva skills: one pricing mention, one "Canva watermark" aside, one in-app canvas-engine build, one competitor mention. | **C** — no transferable Canva content; excluded. |
| **canva** (social-media-skills) | `social-media-skills_skills/skills/canva/` (SKILL.md, 4 refs, evals) | MIT (`README.md`:64-65, 320-322; `SKILL.md` has no `license:` field but siblings do) | Canva craft skill built on the SCALE framework: brand-kit-first, de-template past recognition, automate with Bulk Create/Resize, layer AI as editable material, export correctly. | **B+** — strong conceptual layer ("the Canva look"), zero tool-level mapping, hard-wired to a vendor (WoopSocial) we do not have. |
| **design-and-templates** (BRAND) | `social-media-skills_skills/skills/design-and-templates/` | MIT | Builds the brand kit token spec + a small template set (5–7) + legibility rules + production workflow. | **B+** — the token spec and the "don't over-build" rule are directly usable. |
| **brand-profile** | `social-media-skills_skills/skills/brand-profile/` | MIT (`license: MIT` in frontmatter) | The upstream identity artifact: interview → `brand-profile.md` with voice dimensions, lexicon, banned words, guardrails, proof. | **B** — not a design skill, but it is the cheapest way to stop generic output. |
| **carousel-writer** | `social-media-skills_skills/skills/carousel-writer/` | MIT (`license: MIT` in frontmatter) | Slide-by-slide writing craft: cover = hook + promise, one idea per slide, headline + ≤1 line, save-leaning CTA. | **A−** — the closest thing in the cluster to multi-slide deck craft. |
| **quote-cards-and-text-graphics** (QUOTE) | `social-media-skills_skills/skills/quote-cards-and-text-graphics/` | MIT | Text-as-hero craft: quotability, attribution honesty, min ~24pt, thumb-size test. | **B+** — good legibility + attribution ethics, narrow format. |
| **thumbnail-design** (CLICK) | `social-media-skills_skills/skills/thumbnail-design/` | MIT | One-image click craft with hard numerics (0–4 words, 1280×720, legible at ~168×94). | **B+** — best source of *stated* mobile-legibility numbers. |
| **infographic-and-data-viz** (CHART) | `social-media-skills_skills/skills/infographic-and-data-viz/` | MIT | Honest chart design: takeaway titles, zero-baseline bars, data-ink reduction, source + a11y tags. | **A−** — the only source that governs diagram/chart slides seriously. |
| **platform-specs-and-validation** (CHECK) | `social-media-skills_skills/skills/platform-specs-and-validation/` | MIT | Validate-before-publish for a multi-platform fan-out (WoopSocial-specific enums and error codes). | **C+** — the atomic-publish idea transfers; the whole spec does not. |
| **tools/integrations/canva.md** | `social-media-skills_skills/tools/integrations/canva.md` | MIT | Connection-layer guide (MCP → Connect APIs → human) + plan gates + hard lines. | **B** — concise, honest about automation limits. |
| **10x-Canva-Skills** | `OpenAnalystInc_10x-Canva-Skills/.claude/skills/` (18 canva skills, 6 identical DESIGN_REFERENCE files, 3 agents, 1 command) | MIT (`README.md`:219-221, `.claude-plugin/plugin.json`:7) | A script-driven Connect-API toolkit with a "3-mode" PLAN→CLARIFY→IMPLEMENT ceremony and a strong design-preservation guardrail set. | **C+** — every script it references is absent; the guardrails and dimension tables survive. |
| 10x local-* skills | `.claude/skills/local-{pdf,pptx,docx,xlsx}-editor`, `local-file-manager` | MIT | Local Office/PDF file editing with a never-touch-the-original rule. | **out of scope** — not Canva; noted only because they share the plugin. |

Counting note (10x): the repo has **23** skill directories — 18 `canva-*` and 5 `local-*` — but
`.claude-plugin/plugin.json` registers only **16** (11 canva + 5 local). `canva`, `canva-design`,
`canva-creative`, `canva-import`, `canva-resize`, `canva-comments`, `canva-user` exist on disk and
are **unregistered**. `README.md` says "16 specialized skills" and "11 Canva API skills", so the
docs, the manifest, and the tree disagree.

---

## Skill: canva-design-director

**Purpose.** Convert a general-purpose agent into a "senior design director" that plans before it
generates, constrains type and colour to a system, and refuses decoration. Source:
`mavericraven_canva-design-director/SKILL.md` (`## Identity`), `README.md` (`## Core Workflow`).

### Process it prescribes

1. **Audit** — call `list-brand-kits` and `search-brand-templates`; "Understand what already exists
 before creating" (`SKILL.md` `### 1. Audit`). Brand rules, once found, are never overridden.
2. **Plan and state it in chat before touching the canvas** — output the format, grid, type palette,
 colour approach, focal point, visual path, CTA priority (`SKILL.md` `### 2. Plan`;
 `README.md` `## Recommended Agent Behavior` gives the literal template: Format / Grid /
 Typography / Color / Focal point / Visual path / Export).
3. **Generate** — prefer "structured" generation over freeform prompts (`SKILL.md` `### 3. Generate`).
4. **Refine in one editing transaction** — `start-editing-transaction` → `perform-editing-operations`
 (batch every change) → `get-design-thumbnail` to verify → `commit-editing-transaction` or
 `cancel-editing-transaction` (`SKILL.md` `### 4. Refine`; `references/editing-transactions.md`
 says "Do not make 10 separate requests").
5. **Verify** against the delivery checklist.
6. **Export** — PNG for digital/social, PDF for presentations/print; check licensing to avoid
 `license_required` (`references/export-standards.md`).

### Pre-flight (the four gates, verbatim intent) — `SKILL.md` `## Pre-Flight: Before You Touch the Canvas`

1. **Check Brand Context:** call `list-brand-kits`; never override established brand parameters.
2. **Define the Format:** determine the output format (presentation, social post, poster, …).
3. **Establish the Grid:** choose a layout approach *before* placing elements — "never drop elements
 on canvas arbitrarily."
4. **Select Type Palette:** constrain to **max 2 typeface families** from the approved brand kit or
 the defaults **Inter / Helvetica Neue / SF Pro**.

### Anti-slop rules and every numeric limit

Anti-slop manifesto (`references/anti-ai-slop.md`, 4 bullets, plus the longer list in
`README.md` `## Anti-AI-Slop Policy`):

- No generic 3D illustrations unless the brand explicitly asks.
- No "kitchen sink" compositions — "Do not fill space just because it is empty."
- Avoid excessive gradients or drop shadows; flat, clean, intentional.
- Refuse prompts that produce overcrowded/illegible/chaotic layouts; use `comment-on-design` to
 suggest simplification instead of rendering them.
- Rejected categories: random decorative blobs, excessive gradients, generic 3D objects, too many
 typefaces, unclear hierarchy, overcrowded layouts, weak CTAs, poor image masking, low-contrast
 text, centre-aligned everything, elements that do not serve the message.

Numeric limits, all from `SKILL.md` `## Design System` unless noted:

| Rule | Value | Source |
|---|---|---|
| Layout grid | 12-column grid or standard thirds | `SKILL.md` `### Layout`; `references/layout-system.md` |
| Typeface families | **max 2** — "Exceeding this is a violation" | `SKILL.md` `### Typography` |
| Hierarchy levels | **exactly 3** (Title / Subtitle / Body) | `SKILL.md` `### Typography`; delivery checklist |
| Body minimum size | **14 pt** (digital) | `SKILL.md`; `references/typography-system.md` |
| Body leading | **1.4–1.5** | `references/typography-system.md` |
| Title treatment | Heavy/Bold, tight tracking, largest | `references/typography-system.md` |
| Spacing grid | **4 pt / 8 pt** | `SKILL.md` `### 4. Refine`; `README.md` checklist |
| Contrast | **4.5:1** standard text, **3:1** large text (WCAG AA) | `SKILL.md` `### Accessibility`; `references/accessibility-standards.md` |
| Colour system | monochrome (black/white/greys) + **exactly one** accent | `references/color-system.md` |
| Instagram square | 1080 × 1080 | `references/social-media-specs.md`; `README.md` |
| Instagram story/reel | 1080 × 1920 | same |
| X/Twitter post | **1600 × 900** | same |
| LinkedIn banner | **1584 × 396** | same |
| Quote card canvas | 1080 × 1080, **120 px** margins all round | `assets/example-social-layouts.md` |
| Attribution gap | **8 pt** below the quote, small sans, all caps | `assets/example-social-layouts.md` |
| Hero slide | full-bleed image **darkened by 30 %** | `assets/example-slide-structures.md` |
| Metric slide | **one** massive number + **one** line of context, no bullets | `assets/example-slide-structures.md` |
| Example brand system | `#000000 / #FFFFFF / #E5E5EA / #0071E3`, Inter **400/600/700**, **24 px** radius | `assets/example-brand-systems.md` |
| Product announcement bg / CTA | `#F5F5F7` / `#0071E3` | `assets/example-marketing-layouts.md` |

### Unique ideas not found in the other skills

- **Plan-before-paint as a hard gate**, with a fixed six-line plan template the agent must print.
- **"Structured generation" preference** — treat freeform generate as a slop risk and abort to the
 controlled path when output is generic (`SKILL.md` `## Error Recovery` row "Generating freeform
 produces slop").
- **Cancel the transaction when the layout is structurally compromised** rather than patching a bad
 base (`references/canva-mcp-workflows.md`).
- **Explicit refusal posture** — the skill sanctions saying no to a cluttered brief.
- **Data-viz minimalism**: strip grid lines and borders, direct-label data points instead of a
 legend, highlight only the most important series in the accent, keep the rest muted grey
 (`assets/example-information-design.md`).

### Pitfalls it warns about

- `license_required` on export → replace restricted assets (`SKILL.md` `## Error Recovery`).
- Design looks cluttered → delete elements until one focal point remains.
- An editing transaction that "feels chaotic" → cancel, replan, restart.
- Brand kit missing → fall back to Inter/Helvetica + monochrome + one accent.
- Resize breaks the layout → resize first, then run an editing transaction to rebalance.

### Outdated / wrong / impossible against our MCP

- **`generate-design-structured` does not exist** in our server (nor anywhere). Its role is taken by
 `create-design` with `format` + `outline.sections[{title,description,points}]`.
- **`create-design-from-candidate` and `generate-design`** are legacy-only in our toolset; the
 director treats the former as the template path, which is wrong for us (`create-design` is the
 live path; brand templates go through `create-design-from-brand-template`/`autofill-design`).
- **`get-design-export-formats`** — the real name in our server is `get-export-formats`.
- **`get-design-thumbnail` is not a standalone preview.** In our server it requires a live
 `transaction_id`; the director's "verify with `get-design-thumbnail`" step must be re-expressed as
 "inside the open transaction, render page thumbnails".
- **`list-brand-kits` exists but returns nothing on our account** — the audit step will always fall
 through to the fallback system. The skill never says what to do when the audit is empty except
 "fall back", which for our deck means the design system must be *invented and written down* before
 slide 1.
- **Endpoint mismatch**: `README.md` configures `https://mcp.canva.com/mcp` via `mcp-remote`; our
 mount is `https://api.canva.com/connect/v1/mcp` with static OAuth.
- **"Exactly 3 hierarchy levels" and 14 pt body** are wrong for a 1920×1080 lecture deck: 14 pt is
 illegible from the back of a room, and a Vietnamese philosophy deck legitimately needs 4 levels
 (title / section label / body / caption/quote attribution). Treat "exactly 3" as "≤3 *type styles*
 plus one caption style".
- **`resize-design`** is a Pro feature and returns a *new* design; the skill implies it is free.

---

## Skill: canva (TerminalSkills_skills/skills/canva)

**Purpose.** Choose the correct Canva automation surface, then execute one of three flows (MCP
interactive, Connect REST batch, or brand-template fan-out) without mistaking a job for a result.
Source: `TerminalSkills_skills/skills/canva/SKILL.md` (247 lines, `license: Apache-2.0`,
`version: 1.1.0`).

### The surface decision (verbatim structure, `## Overview`)

| AI Connector MCP | Connect REST API |
|---|---|---|
| Endpoint | `https://api.canva.com/connect/v1/mcp` | `https://api.canva.com/rest/v1/` |
| Auth | client-managed OAuth (browser once) | OAuth 2.0 + PKCE you implement |
| Best for | interactive work in a chat/agent session | batch jobs, servers, CI, other people's accounts |
| Editing | yes — editing transactions | no (create / autofill / export only) |

It also names a third, irrelevant server: the Dev MCP at canva.dev "only serves docs for building
Canva apps — it does not touch designs." Note the internal inconsistency: the *use-case* file in the
same repo (`use-cases/batch-produce-brand-designs-with-canva.md`, `## The Solution`) says the MCP
endpoint is `https://mcp.canva.com/mcp`, i.e. a different server. Our mount is the
`api.canva.com/connect/v1/mcp` one.

### Process it prescribes

1. Decide the surface (table above). Do not build an OAuth app for a one-off chat edit; do not try
 to drive a 240-row batch through MCP tool calls with a human in the loop.
2. Authenticate. MCP: `claude mcp add --transport http canva https://api.canva.com/connect/v1/mcp`,
 or `npx -y mcp-remote@latest …`; first call opens a browser; verify with `tools/list`. REST: PKCE.
3. **Check capabilities before a batch** — `GET /v1/users/me/capabilities`, look for `autofill`,
 `brand_template`, `resize`.
4. **Read the dataset, never guess field names** — `GET /v1/brand-templates/{id}/dataset`; "A guessed
 key is silently ignored, producing a design with empty placeholders rather than an error."
5. Do the work; treat every heavy POST as an accepted job.
6. Poll with back-off (1 s → 2 s → 4 s, cap ~5 s) until `success`; on `failed`, read
 `job.error.code`, do not resubmit blindly.
7. Take the download/thumbnail/edit URLs at once; never store signed URLs.

### Exact rate limits it documents (per user, per minute unless stated)

From `SKILL.md` `### Setup A — AI Connector MCP`, the tool table:

| Group | Limit |
|---|---|
| `generate-design`, `create-design-from-candidate`, `copy-design` | **20** |
| `search-designs`, `get-design`, `get-design-pages`, `get-design-content`, `get-presenter-notes`, `get-export-formats`, `get-design-thumbnail` | **100** |
| `start-editing-transaction` | **20** |
| `perform-editing-operations` | **50** |
| `commit-editing-transaction`, `cancel-editing-transaction` | **20** each |
| `export-design`, `import-design-from-url` | **20** |
| `resolve-shortlink` | unlimited |
| `upload-asset-from-url` | **30** |
| `get-assets` | **100** |
| `create-folder` | **20** |
| `list-folder-items`, `search-folders`, `move-item-to-folder` | **100** each |
| `comment-on-design`, `list-comments`, `list-replies` | **100** each |
| `reply-to-comment` | **20** |
| `resize-design`, `create-design-from-brand-template` | **20** each |
| `search-brand-templates`, `list-brand-kits`, `get-brand-template-dataset` | **100** each |
| `autofill-design` | **60** |
| Any tool without its own limit | default cap **300/min/user** |

Additional limits and quotas stated elsewhere in the same file:

- Job polling: **120 req/min** for autofill, export, resize and import jobs; **180 req/min** for
 upload jobs (`### The async job pattern`).
- Exports: **75 per 5 min per user and per document**; **500 per 24 h per user** (`## Endpoint map`).
- `GET /v1/users/me/capabilities`: **10 req/min** (`## Guidelines`).
- `GET /v1/designs`: `limit` 1–100; `continuation` pagination.
- `POST /v1/designs`: side 40–8000 px, **max 25 MP area**, title ≤255 chars.
- Asset upload metadata name: ≤**50 chars** (base64-encoded in `Asset-Upload-Metadata`).
- PKCE verifier: **43–128 chars**; access tokens **4 hours**; refresh token **single-use**.
- Blank API-created designs are **deleted after 7 days**.
- URL lifetime: thumbnails ~**15 min**, export downloads **24 h**, `edit_url`/`view_url` **30 days**.

### Exact scopes it documents

The scope list (`### Scopes — nothing is implied`):
`asset:read`, `asset:write`, `design:meta:read`, `design:content:read`, `design:content:write`,
`brandtemplate:meta:read`, `brandtemplate:content:read`, `brandtemplate:content:write`,
`folder:read`, `folder:write`, `folder:permission:write`, `comment:read`, `comment:write`,
`collaboration:event`, `profile:read`, `openid`, `profile`, `email`.

Key property it states: "`asset:write` does **not** grant `asset:read`, so polling an upload job needs
`asset:read`."

Per-endpoint table (same section):

| Endpoint | Scope |
|---|---|
| `POST /v1/autofills` | `design:content:write` |
| `GET /v1/autofills/{jobId}` | `design:meta:read` |
| `GET /v1/brand-templates`, `/{id}` | `brandtemplate:meta:read` |
| `GET /v1/brand-templates/{id}/dataset` | `brandtemplate:content:read` |
| `POST /v1/asset-uploads`, `/url-asset-uploads` | `asset:write` |
| `GET /v1/asset-uploads/{id}`, `/url-asset-uploads/{id}` | `asset:read` |
| `POST /v1/exports`, `GET /v1/exports/{id}` | `design:content:read` |
| `POST /v1/resizes` + poll | `design:content:read` **+** `design:content:write` |
| `POST /v1/folders`, `/folders/move` | `folder:write` |
| `GET /v1/users/me/capabilities` | `profile:read` |

### Error handling it documents (the most valuable paragraph in the cluster)

- **Jobs are not results.** "A `200` on `POST /v1/exports` means *accepted*." Poll until `success`;
 handle `failed` by reading `job.error.code` rather than re-submitting.
- **429 / rate-limited** → back off; "A 240-row batch is a throttled queue, not a `Promise.all`."
- **403 `permission_denied`** → "wrong plan or exhausted trial", not a malformed request; tell the
 user to upgrade instead of retrying (Free-plan autofill trial).
- **Empty brand-template search** → read it as "plan or no match", never as an error to retry.
- **404 on a valid-looking id** → "usually means it belongs to a different team".
- **Unknown autofill field** → silently skipped; the job succeeds with empty placeholders.
- **Lost refresh rotation** → full PKCE re-consent. Persist the rotated token atomically.
- **Export format constraints**: `pdf`, `png`, `jpg` (`quality` 1–100 required), `gif`, `pptx`, `mp4`
 (`quality` required), `csv`, `html_bundle`, `html_standalone`.

### Unique ideas

- The two-surface decision table (interactive vs unattended) — nobody else draws this line.
- **Capabilities as a pre-flight gate** rather than discovering the tier by failing.
- **Dataset-first** discipline for autofill.
- **URL-expiry table** (15 min / 24 h / 30 days) with a rule: download export bytes immediately, hand
 humans the `edit_url`, never a signed export link.
- **Blank designs vanish in 7 days** — the reason a "stub deck" plan fails silently.

### Pitfalls / staleness

- Tool names in the MCP table (`generate-design`, `create-design-from-candidate`) are the legacy set;
 our server exposes `create-design`.
- "Connect API: editing — no" is stale: a Design Editing API is now GA (the social-media skill says
 so explicitly). Only the MCP path has the `perform-editing-operations` op set we use.
- It never mentions `merge-designs`, `get-design-thumbnail`-inside-a-transaction, or the element-id
 grouping quirks — so its MCP guidance is API-shaped, not canvas-shaped.
- No design guidance at all. It is a transport manual.

---

## Skill: canva (social-media-skills, SCALE)

**Purpose.** Treat Canva as an on-brand *volume* machine and kill the recognisable "Canva look".
Source: `social-media-skills_skills/skills/canva/SKILL.md` (108 dense lines), with
`references/the-scale-framework.md`, `references/workflows-and-templates.md`,
`references/canva-2026-reality.md`, `references/scope-and-connections.md`, `evals/evals.json`.

### Process it prescribes

1. **Read the upstream system first** — `brand-profile` + `design-and-templates` + `voice-builder`.
2. **S — Start from the Brand Kit**: lock colours/fonts/logos/voice *before* generating.
3. **C — Customise past the template**: replace every stock element, change the layout bones, apply
 brand type + colour over defaults, strip template decorations.
4. **A — Automate the repeatable**: Bulk Create (one master + CSV), Magic Resize, Magic Switch,
 MCP/Connect for direct operation.
5. **L — Layer in AI as editable material**: Dream Lab / Canva AI 2.0 for imagery and drafts, Magic
 Write only as a second-pass editor, dedicated generators when pure quality matters,
 AI-disclosure where required.
6. **E — Export right and hand to publish**: correct format/size, legibility floor held, alt text
 drafted, then scheduling/publishing.
7. Weekly loop (`references/workflows-and-templates.md`): Brand Kit locked → adapt ONE master layout
 per format → swap stock → Magic Resize to the platform set → QA at thumb size → export → publish.

### Concrete rules and numbers

| Claim | Value | Source |
|---|---|---|
| On-brand first drafts, Brand-Kit-first vs not | ~**80 %** vs ~**20 %** | `SKILL.md` `## The POV`; `the-scale-framework.md` `## S` |
| Canva's own brand-recognition correlation | up to ~**23 %** | `references/canva-2026-reality.md` `## The two facts` |
| Bulk Create output from one master + CSV | **60 graphics** in one run | `SKILL.md` `## The POV` |
| Pro price | ≈ **$12–15/mo** | `references/canva-2026-reality.md` `## Plans + credits` |
| Teams/Business | ≈ **$10/seat, 3-seat minimum** | same |
| Free tier Brand Kit | **1 kit, 3 colours** | same |
| Magic Switch languages | **150+** | `the-scale-framework.md` `## A` |
| Legibility floor | **≤2 fonts**, WCAG contrast, min readable size at thumb scale, no text over busy imagery without a panel, safe zones, alt text | `workflows-and-templates.md` `## Legibility floor` |
| AI-disclosure regime | EU AI Act; C2PA | `SKILL.md` `## Honest scope` |
| Honest ceiling for tools | ~**70–80 %** on-brand; a human finishes the hero | `design-and-templates/SKILL.md` (same family) |

### Unique ideas

- **The de-templating test**: "If a stranger can name the template, keep going."
 (`the-scale-framework.md` `## C`). This is a falsifiable quality gate for generated decks, and the
 closest thing anyone wrote to "don't ship the design generator's default look".
- **Templates are scaffolding for hierarchy and spacing, not the finished design.**
- **Consistency comes from the system, not from one template family** (`evals.json`,
 `core-escape-the-canva-look`).
- Explicit "agent specs / human approves / tool publishes" separation, with a rule that the agent
 never fabricates "that looks great" — directly applicable to our thumbnail review step.
- Honest-scope wording for capabilities: state what the connector can do only "where connected".

### Pitfalls it warns about

- Skipping the Brand Kit and prompting "in my brand colours" each time.
- Shipping the untouched template.
- Ripping a premium template from a screenshot / stripping watermarks / brand impersonation.
- Trusting a blog's credit numbers over the in-app tracker.
- Letting Magic Write's first draft be the voice.
- Bulk Create overflow: QA for text overflow, widows, line breaks, contrast on **every** variant.

### Outdated / impossible against our MCP

- **Bulk Create and Magic Switch are editor features**, not tools. We have `autofill-design` +
 brand templates (and we have **zero** brand templates), and `resize-design` (Pro) — so "Bulk
 Create" must be re-expressed as copy-design + per-page edit loops, or dropped.
- **No publish layer.** The whole "export → WoopSocial" half of the skill is vendor lock-in and must
 be cut for us; delivery ends at a local file / Canva link.
- **Brand Kit is empty on our account**, so "S — Start from the Brand Kit" degrades to "write the
 token spec yourself and hold it constant" (i.e. borrow the design-and-templates token block).
- `canva-2026-reality.md` is explicitly volatile and partly marketing-sourced ("~9M uses in month
 one", credit counts that "conflict across sources"). Do not import its numbers; import only its
 *policy* (verify in-app, attribute, verify-quarterly).
- It cannot state the operational facts we depend on (no font-family change, no new text boxes, no
 notes write, grouped-child delete no-ops).

---

## Skill: design-and-templates (BRAND)

**Purpose.** Ship a brand kit + a small reusable template set so a non-designer produces consistent
on-brand output fast. Source: `social-media-skills_skills/skills/design-and-templates/SKILL.md` +
4 references.

### Process

1. **B — Build the brand kit**: lock colours (primary/secondary/accent + text), fonts (heading + body
 pairing), logo + clear space, spacing (margins/grid).
2. **R — Reusable templates, a small set**: **~5–7**, mapped to real recurring formats only.
3. **A — Anchor each in hierarchy + legibility**: one focal point, type scale, contrast, safe zones,
 mobile-first.
4. **N — Name and systematise**: a non-designer fills it in minutes by swapping text/image.
5. **D — Deploy at scale**: brief image tools for generated imagery, keep grid consistency, human
 finishes the hero pieces.

### Concrete spec (the most directly reusable artifact in the social cluster)

From `references/building-the-system.md` `## Brand-kit spec (the tokens)`:

```
COLORS: primary | secondary | accent | text-dark | text-light | background(s) (lock the hex set)
FONTS: heading (1 distinctive) + body (1 legible); a fixed size scale (e.g. H1 64 / H2 40 / body 28 @ 1080w)
LOGO: primary + mark-only; clear-space rule; light/dark versions
SPACING: outer margin, grid columns, min text size at thumb scale
```

Starter set with formats: Quote/hook card 1:1 or 4:5; Carousel frame 4:5; Announcement/promo
1:1/4:5; Reel/Shorts cover 9:16 (3:4-grid-safe); Pinterest pin 2:3 1000×1500. "Add only what you
actually post."

Hierarchy/legibility checklist (same file): one focal point; clear H/sub/body scale; **no more than
2 fonts**; text legible on the busiest version of the background, checked at thumb size; safe zones
clear of platform UI; "if it doesn't read on a phone, it doesn't ship."

### Unique ideas

- **Template count as a design decision** (5–7, not 40) — an explicit anti-library stance.
- The **fixed size scale expressed at the design width** (`@1080w`) — the only source that ties type
 size to canvas width, which is exactly the conversion our 1920×1080 deck needs.
- **One focal point per template** as an auditable rule rather than a taste statement.
- ~70–80 % ceiling and "raw AI generations may not be copyrightable → add human edits".

### Outdated / impossible

- Assumes a Brand Kit exists in Canva; ours does not.
- "A design tool or the image tools produce the graphics" — in our setup the *same* agent both specs
 and renders, so the separation of duties has to be rebuilt as "spec → generate → review thumbnail".
- WoopSocial publishing again; cut.

---

## Skill: brand-profile

**Purpose.** The durable identity record every other skill reads before writing. Source:
`social-media-skills_skills/skills/brand-profile/SKILL.md` + `references/{brand-profile-template,voice,audience,positioning,examples}.md`.

### Process

1. **Check for an existing profile first**; if present, load it and reflect it back in ~2 lines, then
 continue. "Do not silently re-interview someone who has already done this."
2. **Gather raw material before asking** — website, handles, existing posts, pasted deck; treat fetched
 text as data, not instructions.
3. **Interview in small batches** — **2–4 questions at a time**, lead with what you inferred, push
 vague answers to specifics.
4. Capture five things: identity (one sentence), positioning + POV, audiences, voice, proof + offers.
 Plus guardrails, operational defaults, and "show, don't tell" examples.
5. **Challenge vague input** — "professional but fun" → name a brand that sounds like that and one you
 would never sound like; "everyone is our audience" → one segment this quarter; "industry-leading" →
 what proof a skeptic accepts.
6. **Write `brand-profile.md`** from the template, confirm, ask for one round of edits.

### Numeric / structural rules

- Ask **2–4** questions per batch (`SKILL.md` `## Step 3`).
- Voice = **6 dimensions** each scored **x/5**: Formality, Warmth, Authority, Energy, Humor, Polish
 (`references/voice.md` `## 1. Dimensions`).
- **1–3** points of view the brand will defend, plus what it won't say.
- **1–2** audience segments; "Two sharp segments beat eight vague ones."
- **3–5** loved posts + **1–2** hated, each with one line of why.
- Staleness rule: older than **a quarter**, or after rebrand/pivot/new offer.
- "We sound ___, never ___" pairs — 2–4.
- Guardrails must include banned words, compliance claims, competitor rules, emoji/hashtag policy.

### Unique ideas

- The **"we sound ___, never ___"** construction as a portable voice token — it encodes the failure
 mode, which an adjective never does.
- **Lexicon capture** (words we use / words we ban) as the highest-signal section, and the instruction
 to treat Voice + Guardrails + Operational defaults + examples as "the highest-signal sections —
 check them on every task".
- **Operational defaults** as a required block: AI/synthetic-media disclosure stance, languages,
 pronunciation, accessibility defaults — read by tool skills.
- Explicit **"identity owns visual identity pointer, never duplicates it"** rule (avoid two sources
 of truth).

### Limits / caveats

- It is a marketing-brand instrument. For a university coursework deck the "audience" is an examiner
 and classmates, "proof" is citations; the template still works but the offer/CTA half is dead weight.
- Its six example profiles (`references/examples.md`) are excellent calibration for specificity, and
 none of them are design guidance.

---

## Skill: carousel-writer (slide craft)

**Purpose.** Multi-slide swipeable teaching/story sequences: cover hook, one idea per slide, payoff,
save-leaning CTA. Source: `social-media-skills_skills/skills/carousel-writer/SKILL.md` +
`references/{slide-craft,architecture,platform-specs}.md`.

### Process

1. Read `brand-profile.md` and `voice.md`; carry guardrails.
2. Lock the **one idea**, the goal, and the platform before writing.
3. Write the **cover**: hook **and** promise, plus a swipe cue.
4. **Outline the spine** before designing: "cover promises 5 hooks → one hook per slide → summary →
 save". If you cannot state the spine in one sentence, the carousel is not ready
 (`references/architecture.md` `## The spine`).
5. Write each slide: short bold headline first, **at most one supporting line**, front-loaded.
6. Land a payoff slide, then a CTA slide with **one** ask (default: save).
7. Specify visuals: layout, hierarchy, palette, type, consistent template; or an image-generation
 prompt pack with the exact slide text.
8. Hand the caption to `caption-writer`, the schedule to `scheduling-and-queue`.

### Concrete rules and numbers

| Rule | Value | Source |
|---|---|---|
| Slide text budget | headline + **≤1** supporting line | `references/slide-craft.md` `## Each body slide` |
| Slide hierarchy order | headline (biggest/boldest) → supporting line → slide number/progress → one accent | `references/slide-craft.md` `## Visual hierarchy` |
| Progress cue | "3/7" style, small, consistent corner | same |
| Instagram carousel | up to **20** slides (raised from 10 in 2024); sweet spot **5–10** | `references/platform-specs.md` |
| Ratio | 1:1 or **4:5** portrait; keep all slides identical ratio | same |
| Caption | up to ~**2,200** chars | same |
| LinkedIn document | PDF upload, square or portrait, "generous" slide count, 10x says up to **300** pages | `platform-specs.md`; `10x …/DESIGN_REFERENCE.md` |
| TikTok photo carousel | **9:16** | `platform-specs.md` |
| Slide-count rule | "A 6-slide carousel that's all signal beats a 10-slide one padded to hit a number" | `references/architecture.md` `## Slide count` |
| Legibility test | glance for **one second** — do you get it? | `slide-craft.md` `## Legibility rules` |

Structures it names: how-to, listicle, story, before→after, myth-bust, framework — pick by idea
(`architecture.md` `## Carousel structures`).

### Unique ideas

- **The spine sentence test** before any design work — the cheapest deck-architecture gate I found.
- **"One idea per slide; if it needs a paragraph, it's two slides."** The constraint is framed as the
 craft, not a limitation.
- **Consistency as the professionalism signal**: same type sizes, margins, palette, slide-number
 position across all slides.
- **Handoff as a text spec**: deliver exact per-slide text, labelled and numbered, so it can be fed to
 a renderer verbatim. This is precisely the artifact an MCP-driven deck workflow needs.
- Pushback patterns worth copying: resisting "make it 10 slides" padding; suggesting a Reel/thread
 instead of a forced carousel; providing a text-only template when no design tool exists.

### Outdated / impossible

- Platform numerics are social-feed, not deck, facts — nothing about 1920×1080, presenter notes, or
 projection legibility.
- "Image-generation prompt pack (Nano Banana / Ideogram)" does not exist in our toolset; our analog is
 `create-upload-url` of a locally drawn diagram, or `generate-image` when quota allows.

---

## Skill: quote-cards-and-text-graphics (QUOTE)

**Purpose.** One line, made outsized and honest. Source:
`social-media-skills_skills/skills/quote-cards-and-text-graphics/SKILL.md`.

Process/framework: **Q** quotable line first (a mundane sentence in a beautiful font is still
mundane); **U** undistorted + attributed (never fabricate or misattribute, never strip context,
consent for words/face, real + sourced stats, no copyrighted lyrics); **O** one idea outsized, key
phrase leads, break lines where meaning holds, never mid-word; **T** type on-brand (two fonts max,
whitespace reads premium); **E** ensure legibility (mobile-first, min ~24 pt, high contrast, safe
margins, not over a busy image, test at thumb size on a real phone).

Numbers: **min ~24 pt**; **two fonts max**; "~80 %+ mobile". Honesty spine: `never fabricate a quote`,
`never attribute an invented line to a real person`, `a misattributed quote card is misinformation
with nice typography`. Unique: the **quotability test** ("not every sentence deserves a card") and the
attribution-as-ethics framing — the only skill in the cluster that treats a text slide as a potential
misinformation vector.

Impossible: no MCP mapping (it is a spec skill); "a design tool renders" — for us the same agent
renders.

---

## Skill: thumbnail-design (CLICK)

**Purpose.** One-image click craft, designed as a unit with the title. Source:
`social-media-skills_skills/skills/thumbnail-design/SKILL.md`.

Framework: **C** clarify the promise (thumbnail *shows*, title *tells*, never repeat); **L** lead with
one focal point, parse in **<1 s**; **I** invoke genuine emotion (face + gaze only if it adds
context); **C** contrast + concise text; **K** keep testing.

Hard numbers: thumbnail drives ~**70–80 %** of click decisions; **0–4** bold sans-serif words with an
outline, never a duplicate of the title; legible at ~**168×94**; **1280×720**, 16:9; 60-30-10 colour;
avoid YouTube red/white; pass the B&W test; **3** meaningfully different concepts, one variable at a
time; **50 MB** cap; faces +20–30 % (attribute).

Unique and transferable: **the show/tell division of labour between image and title** (a slide title
and its visual must not say the same thing), the **B&W test** for contrast, and the
**one-variable A/B** discipline. Also the honesty rule that a native A/B by watch-time punishes
clickbait — a good argument for "the deck must keep the promise of the title slide".

Impossible: YouTube Studio upload and Test & Compare; covers not thumbnails; no MCP.

---

## Skill: infographic-and-data-viz (CHART)

**Purpose.** Honest, scannable charts. Source:
`social-media-skills_skills/skills/infographic-and-data-viz/SKILL.md`.

Framework: **C** choose the chart for the relationship (trend→line, comparison→bar, composition→
stacked/donut sparingly, one or two numbers→big stat/table; default to bar); **H** headline the
takeaway ("Revenue tripled", not "Revenue by Quarter"); **A** anchor to honest scales (**bars start
at zero**, no 3D/area/dual-axis/cherry-pick); **R** reduce to the signal (strip 3D/shadows/
gradients/gridlines, direct-label over a busy legend, one colour + an accent); **T** tag the source +
make it accessible (colour-blind-safe + redundant encoding + WCAG contrast + alt text stating the
takeaway).

Numbers: the insight should land in **~3 seconds**; ~**84 %** of misleading reads come from missing
context (attributed to Utah Viz Design Lab); ~**8 %** of men have colour vision deficiency → never
rely on colour alone.

Unique: **"sometimes the honest answer is 'this isn't a chart'"**; the title-as-takeaway rule; the
refusal to visualise undramatic data as drama. This is the single most useful source for the diagram
and data slides in a coursework deck, and it pairs perfectly with the design-director's data-viz
minimalism (`assets/example-information-design.md`).

Impossible: it assumes a chart tool renders; in our flow we either accept Canva's generated chart
look, upload a pre-built chart image, or lay out a text-and-number "stat slide" with editable text.

---

## Skill: platform-specs-and-validation (CHECK)

**Purpose.** Make a multi-platform post publish-ready before an atomic create. Source:
`social-media-skills_skills/skills/platform-specs-and-validation/SKILL.md` +
`references/validation-reference-and-recipes.md`.

Process: **C**ollect targets (confirm same project) → **H**ydrate per-platform required fields,
resolving account values from `platform-inputs` → **E**nforce media/content rules → **C**onfirm
truthful declarations → **K**nock it through `POST /posts/validate` → create atomically.

Transferable ideas (all of the specifics are WoopSocial-only): **validate-then-create**, **atomic
fan-out** ("if any one fails, nothing is created"), **no update endpoint → delete + recreate**, and
the principle that **compliance flags are declarations, not validation knobs** ("never flip them to
clear an error"). Those map cleanly onto a deck: validate the whole deck (every page's text fits, no
overflow, consistent type) before claiming done, and never silently change a doctrinal term to make a
slide "fit".

Everything else — `ValidationField` codes, `CreatePostErrorCode` enums, `pinterestBoardId`,
`TIKTOK_PRIVACY_LEVEL` — is vendor-specific and should not be imported.

---

## The 10x-Canva-Skills pack

**What it actually is.** A Connect-API CLI toolkit (`scripts/*.py`) wrapped in Claude Code skills, with
a compulsory three-mode ceremony. **Every one of the 61 `scripts/*.py` paths referenced by the skills,
agents and command documents is missing from the repo** — `find scripts -type f` returns only
`README.md`, `API_REFERENCE.md` and `local/README.md`. So every "Available Scripts" block is
aspirational; only the prose rules and reference tables survive. All six
`*/DESIGN_REFERENCE.md` files are byte-identical (same md5), so the "per-skill reference" is one
326-line document copied six times.

The **3-mode workflow** (`canva-manager/SKILL.md` `## 3-Mode Workflow`) is stated as mandatory:
PLAN (analyse request, gather current state, document every action, list risks) → CLARIFY (ask the two
required questions: "Does this plan accurately reflect what you want to do?" and "Are there any items
I should exclude from this operation?", plus context questions and an explicit "yes") → IMPLEMENT
(execute with logging, report exactly what changed). `canva-planner.md`, `canva-analyzer.md` and
`canva-executor.md` split those modes across three agents with a plan file in `output/plans/` and an
execution log in `output/logs/`.

### The best thing in the pack: design preservation

`canva-presentation/SKILL.md` opens with "warn CRITICAL DESIGN PRESERVATION RULES (MANDATORY)" and a
list of ten NEVERs that is the closest published analogue of our real MCP limits:

1. NEVER create new text elements
2. NEVER add new shapes or elements
3. NEVER create blank slides — ALWAYS duplicate an existing slide
4. NEVER change font sizes unless explicitly requested
5. NEVER change font colours unless explicitly requested
6. NEVER change alignments unless explicitly requested
7. NEVER change element positions unless explicitly requested
8. NEVER change backgrounds unless explicitly requested
9. NEVER change the template/theme unless explicitly requested
10. NEVER modify decorative elements (logos, lines, shapes, images that are part of the design)

And the paired positive rules: duplicate existing slides to make new ones; replace text **within**
existing elements only; preserve all formatting when replacing content; analyse slide structure first;
distinguish content from decorative elements before editing; use the existing slide as the template.

The wrong/right snippets are worth keeping as a mental model:

```
WRONG add_slide.py --design "ID" --position 6 --template "blank"
CORRECT duplicate_slide.py --design "ID" --slide 5 --position 6
```

`canva-image-editor/SKILL.md` repeats the same doctrine for static designs with a "replace, don't add"
pair (`replace_image.py --element … --new-image …` vs `add_image.py`).

### Per-skill table (18 rows: keep / adapt / drop)

| # | Skill | Content in one line | Verdict | Why |
|---|---|---|---|---|
| 1 | `canva` (hub) | Routing table from user request → specialised skill; 48-endpoint inventory; plan-gated feature matrix (Resize Pro; Brand templates **Enterprise**) | **adapt** | The routing idea and the plan-gate matrix are useful; the endpoint inventory is stale relative to our tool list, and it registers a plan tier that contradicts TerminalSkills. |
| 2 | `canva-manager` | The mandatory 3-mode ceremony + script catalogue | **adapt** | PLAN/CLARIFY/approval is a sane guardrail for destructive ops; 375 lines of missing-script invocations are dead weight. |
| 3 | `canva-design` | Presets, custom dimensions, list/search/get pages/export-formats; "next steps after creating" | **adapt** | Its own output block shows the truth we rely on: creating a design yields an **empty canvas** + edit URL — creation is not composition. |
| 4 | `canva-design-terminology` | Design vocabulary: hierarchy, balance, contrast, alignment, repetition, proximity, white space; colour theory; typography terms; print vs digital; accessibility; 2024 dimension cards | **adapt** | Useful definitions and the 4.5:1 rule; numbers are 2024-era and duplicated from DESIGN_REFERENCE. |
| 5 | `scripts/API_REFERENCE.md` | Connect endpoint catalogue with Python signatures, format lists, 25 MP resize cap, 50 MB/500 MB uploads, import formats | **adapt** | Good factual cross-check (design side 40–8000 px, resize ≤25 MP, `.ppt` unsupported); everything else is REST-shaped, not MCP-shaped. |
| 6 | `canva-creative` | Research → headline options → design plan → create → export; per-format content templates | **adapt** | The **design-plan document** (platform, dimensions, content, visual direction, element list) is a good artifact; "web search for trends" and script invocation are not. |
| 7 | `canva-presentation` | Slide CRUD + the ten NEVERs + duplicate-instead-of-create + slide table + dimensions table | **keep** | The most directly applicable content in the pack; encodes exactly the "no new text boxes / don't restyle what you weren't asked to" discipline. |
| 8 | `canva-image-editor` | Same doctrine for static designs; replace-image-not-add; analyse structure first | **adapt** | Doubles the doctrine (fine), but its scripts replace images in placeholders — our `update_fill`/`insert_fill` semantics differ. |
| 9 | `canva-video` | Timeline ops: add_clip, add_text, update_timing, set_duration, audio, animation types | **drop** | Our MCP has **no** video timeline operations at all; nothing here is executable and the design advice is generic. |
| 10 | `canva-export` | Format/quality matrix (PDF std/print; PNG size+lossless; JPG quality 1–100), async export, 24 h URLs, batch export | **adapt** | The format/quality matrix and "exports are asynchronous" are correct and match our `export-design` + poll flow. |
| 11 | `canva-import` | Import PPTX/PDF/AI/PSD; `.ppt` not supported; URL import; import vs asset upload | **adapt** | `import-design-from-url` exists in our server; the file-upload half does not (no local-file import tool). |
| 12 | `canva-folder-organizer` | Create/rename/delete folders, move items, special ids `root`/`uploads`, 4 sort orders | **drop** | Pure script wrapper over endpoints our MCP already exposes as `create-folder`/`item-to-folder`; adds nothing. |
| 13 | `canva-asset-manager` | Upload images (50 MB) / videos (500 MB) / audio; URL upload (100 MB); tags; asset vs import | **adapt** | The size/format limits are a useful precondition table; our `create-upload-url` accepts raw bytes with a single-use URL, which the skill never mentions. |
| 14 | `canva-brand-kit` | Brand templates + dataset + autofill workflow, Enterprise gate, `brand-config.json` example | **adapt** | Autofill + dataset-first is right (matches TerminalSkills); the Enterprise-only claim is contested (TerminalSkills says Pro+) and our account has zero templates, so the gate check matters more than the workflow. |
| 15 | `canva-resize` | Resize jobs, 25 MP cap, Pro/403 gate, batch resize one → five formats | **adapt** | Correct constraints (25 MP, Pro-only, creates a copy); "always review the resized design" matches our finding that resize breaks layouts. |
| 16 | `canva-comments` | Comment threads, replies, assignee, element attachment; Preview API; `comment:read/write` scopes | **drop** | Our MCP already has comment tools including resolve; the pack adds only the scope names. |
| 17 | `canva-explorer` | Read-only listing of designs/folders/assets, search, account tree, special folder ids | **drop** | Script wrappers; zero design content. |
| 18 | `canva-user` | `users/me`, profile, capabilities; scope names; "check scope before op" | **drop** (keep the idea) | The **capabilities-before-batch** idea is already better expressed in TerminalSkills; the rest is a wrapper. |
| — | `canva-content-generator` (19th dir, unregistered) | Analyses local `samples/` to learn style; generates headlines/captions/outlines | **drop** | Requires absent scripts and local sample corpora; no slide craft. |
| — | `local-*` (5 skills) | Local PDF/PPTX/DOCX/XLSX editing on copies with a never-touch-original rule | **out of scope** | Adjacent; only the "never modify originals" habit transfers (`scripts/local/README.md`, 5 numbered rules). |

### 10x facts worth carrying

- **Design dimension table** (`…/canva-design/DESIGN_REFERENCE.md`): 37 rows — presentation 1920×1080
 (16:9) and 1024×768 (4:3); Instagram 1080×1080 / 1080×1350 / 1080×566 / 1080×1920 / cover 1080×1440;
 LinkedIn 1200×1200, 1200×628, 720×900, banner 1584×396; X 1200×675, header 1500×500;
 YouTube 1280×720, banner 2560×1440; Pinterest 1000×1500 / 1000×2100; A4 595×842; A3 1191×1684;
 business card 1050×600; ad units 728×90 / 300×250 / 160×600.
- **Typography rules** (same file, `### Typography Rules`): max **2** fonts; headline bold; body clean;
 **minimum size 30 px for social**; dark-on-light or light-on-dark contrast.
- **Composition**: rule of thirds, white space, one focal point, hierarchy, campaign consistency; one
 CTA per design; CTA specific + urgent + contrasting.
- **Export quality**: social standard/web; print high, **300 DPI minimum**; presentations high.
- **Slide-type vocabulary** (`canva-presentation/SKILL.md` `## Slide Types`): Title; Title + Content;
 Two Column; Image + Text; Full Image; Quote; Chart/Graph; Comparison; Timeline; Team; Thank You —
 a good checklist for deck completeness.
- **Font pairing suggestions** (`canva-design-terminology/SKILL.md` tail): Montserrat+Merriweather,
 Playfair Display+Source Sans Pro, Roboto+Lora, Oswald+Open Sans, Raleway+Libre Baskerville.
- **Brand config token file** (`samples/brand-kits/brand-config.json`): full colour/typography/logo/
 voice/design-rules schema; heading sizes 48/36/24/20, body 18/16/14/12, `line_height: 1.5`,
 logo clearance 20 px, corner radius 8 px, "shadow_style": subtle drop shadow; `dont_do` list includes
 "Use more than 2 fonts in a single design" and "Place text on busy backgrounds without overlay".
 Note the internal contradiction: it also defines a **third** family (Playfair Display italic for
 quotes) while banning >2.
- **Samples system**: `samples/{images,presentations,videos}` + `style_notes.txt` per folder; the
 presentation style-notes skeleton asks for slide count preference, animation preference, title/body
 font + **title 48 px / body 24 px** example values, content density, max points per slide (example
 **5**), chart style, and platform-specific notes. Useful as a **brief template**, not as a system.

### 10x pitfalls and staleness

- **All scripts absent** (61/61) → the pack cannot run as written; treat it as documentation of intent.
- `DESIGN_REFERENCE.md` is duplicated six times → no per-type specialisation despite the folder names.
- Manifest/tree/doc mismatch (23 dirs, 16 registered, "16 skills" claimed).
- Unsourced performance claims throughout the reference (faces +38 %, carousel 1.4× reach, video 59 %
 more engagement, "10x more clicks"). Do not import.
- "Carousel: Up to 10 images" is stale (Instagram allows 20 since 2024, per social-media-skills).
- Windows-first invocation (`.venv\Scripts\python.exe`) and a `.env`-token model that assumes a
 hand-managed OAuth token — both irrelevant to an MCP-mount workflow.
- The three-agent split (planner/analyzer/executor) is a workflow idea, but in a single-agent MCP
 session the same safety is achieved with plan-then-transaction, not with three personas.

---

## Merge recommendations

| Idea | Source skill(s) | Keep / adapt / drop | Why | Where it belongs |
|---|---|---|---|---|
| State a six-line design plan (format, grid, type, colour, focal point, visual path) before generating | design-director (`SKILL.md` `### 2. Plan`) | **keep** | Cheapest defence against generic output; forces one focal point per slide | **Plan** |
| Pre-flight gates: brand audit → format → grid → type palette (≤2 families) | design-director (`## Pre-Flight`) | **adapt** (turn "audit brand kit" into "record that the kit is empty and write the deck's token set") | Our account has zero brand kits, so the audit must produce a written system, not a lookup | **Plan** |
| Anti-slop veto list (no 3D, no blobs, no gradients/shadows, no kitchen-sink, no centre-everything) | design-director (`references/anti-ai-slop.md`; `README.md`) | **keep** | Directly targets the known failure mode of generated decks | **Review** |
| Max 2 type families; ≤3 type styles + one caption style | design-director; social `design-and-templates`; 10x `dont_do` | **keep** (relax "exactly 3 levels" to "≤4 including caption") | Three sources agree; the strict form breaks real decks | **Review / Edit** |
| Numeric floor for body type, expressed **at the design width** | social `building-the-system.md` (`H1 64 / H2 40 / body 28 @ 1080w`); 10x (30 px); quote-cards (~24 pt) | **adapt** → define our own scale at 1920 px | Nobody states a projection-legible size for 1920×1080; our field note (≈34–38 px body, ≈52 px title) is the live truth | **Plan / Review** |
| 12-column grid or thirds; everything aligned; 4/8 pt spacing | design-director (`references/layout-system.md`) | **keep** | Makes alignment auditable via `position_element` | **Edit** |
| Monochrome + exactly one accent; CTA highest contrast | design-director (`references/color-system.md`) | **adapt** (monochrome+accent is safe; a Vietnamese academic deck may want a two-tone palette) | One accent prevents rainbow decks; two-tone is acceptable if declared | **Plan / Review** |
| One idea per slide; headline + ≤1 supporting line | carousel-writer (`references/slide-craft.md`) | **adapt** (coursework needs 2–3 short bullets; cap at 3, never a paragraph) | The principle holds; the marketing number does not | **Plan / Structure** |
| The "spine" sentence test before building | carousel-writer (`references/architecture.md`) | **keep** | The single best gate against a 16-slide deck with no argument | **Structure** |
| Duplicate an existing page instead of creating a blank one | 10x `canva-presentation` | **keep** | Matches our reality: no new text boxes, and blank pages inherit nothing | **Structure / Edit** |
| The ten NEVERs (no new elements, no unrequested size/colour/position/background changes) | 10x `canva-presentation`, `canva-image-editor` | **keep**, with an explicit "declared typography pass" exception | Otherwise the agent can never satisfy "font bự hơn" | **Edit** |
| Batch all edits into one transaction; verify thumbnails; cancel if structurally compromised | design-director (`references/editing-transactions.md`, `canva-mcp-workflows.md`) | **keep** | Fewer rate-limit hits, one rollback unit | **Edit** |
| Render-and-look review loop (per-page thumbnail inside the transaction) | design-director (`### 4. Refine`), `### 5. Verify` | **keep** | Only way to catch overflow/clipping after retyping | **Review** |
| Validate the whole deck before declaring done | social `platform-specs-and-validation` (atomic create), design-director delivery checklist | **adapt** | Port the *idea* (whole-artifact validation) as a per-page audit table | **Review / Delivery** |
| De-templating test: "if a stranger can name the template, keep going" | social `canva` (`the-scale-framework.md`) | **keep** | Falsifiable anti-generic gate; applies to generated decks | **Review** |
| Brand kit token block (colours/fonts/logo/spacing + fixed size scale) | social `design-and-templates` (`building-the-system.md`) | **keep** | Turns "consistent fonts" into a written constant the editing pass can enforce | **Plan** |
| Template set limited to ~5–7 real recurring formats | social `design-and-templates` (BRAND) | **adapt** (for a deck: 5–7 **slide archetypes**, not 5–7 templates) | Slide archetypes (title, thesis, three-part, example, diagram, quote, summary) are the deck equivalent | **Structure** |
| "We sound ___, never ___" + banned-word lexicon | social `brand-profile` (`references/voice.md`) | **adapt** (for coursework: a terminology list + banned mistranslations) | Prevents doctrinal drift, which is our known generator failure | **Plan / Review** |
| Data-viz honesty: takeaway title, zero-baseline bars, no 3D/dual-axis, direct labels, source line | social `infographic-and-data-viz` (CHART) + design-director `example-information-design.md` | **keep** | Both diagram slides and any chart in a lecture need this | **Visuals / Review** |
| Thumbnail rules: show vs tell, legible at ~168×94, 0–4 words, B&W test, one variable A/B | social `thumbnail-design` (CLICK) | **adapt** to slide titles/cover | Great test for whether a slide reads at a glance and whether title+visual duplicate each other | **Review** |
| Text-graphic honesty: never fabricate/misattribute; break lines on meaning | social `quote-cards` (QUOTE) | **keep** | Directly relevant to quotation slides in a philosophy deck | **Review** |
| Two-surface model (MCP interactive vs REST batch) + capabilities gate | TerminalSkills `SKILL.md` | **keep** the MCP side and the capabilities check; **drop** the REST build | We are MCP-only; the capabilities check still explains "empty brand kit" | **Plan** |
| "Jobs are not results"; poll with back-off; read `job.error.code` | TerminalSkills `SKILL.md`; the 240-variant use-case | **keep** (adapted to `get-create-design-async-job` and upload/export jobs) | Our create-design is exactly this async contract, with a non-obvious terminal status | **Generate / Delivery** |
| Dataset-before-autofill; unknown keys are silently skipped | TerminalSkills; 10x `canva-brand-kit` | **keep as a rule**, even though we have no templates | If a template ever appears, this is the failure that wastes a day | **Generate** |
| URL-expiry discipline (thumbnails ~15 min, exports 24 h, edit URLs 30 days) | TerminalSkills (`## Guidelines`) | **keep** | Download/act immediately; hand humans edit links | **Delivery** |
| Rate-limit budget: 20 creates, 50 ops, 20 commits, 100 reads, 300 default, 75 exports/5 min, 500/24 h | TerminalSkills tool table + export throttles | **keep** | Paces a 16-slide build and prevents 429 mid-run | **Plan / Edit / Delivery** |
| Scope discipline: request every scope each call needs; `asset:write` ≠ `asset:read` | TerminalSkills (`### Scopes`) | **drop for us** (static OAuth already grants), **keep as diagnosis** for 403s | Explains a class of failures | **Delivery** |
| Export format matrix (PDF std/print; PNG size+lossless; JPG 1–100; PPTX; MP4) | 10x `canva-export`; TerminalSkills `## Endpoint map` | **keep** | Delivery decisions (PDF for the room, PPTX for the lecturer) | **Export** |
| Duplicate-before-edit / work on a copy | 10x (`canva-image-editor`), design-director (`README` cleanup prompt) | **keep** | Protects the user's original deck; `copy-design` is cheap | **Generate** |
| 25 MP resize cap, Pro gate, review-after-resize | 10x `canva-resize`; design-director `references/resizing-guidelines.md` | **keep** | Resize never produces a finished layout | **Export** |
| Three-persona plan/analyze/execute split | 10x agents | **drop** | Overkill in a single agent; plan-then-transaction achieves the same safety | — |
| Bulk Create / Magic Switch / WoopSocial publishing | social `canva` | **drop** | Not available to us (no brand templates, no publisher) | — |
| Two-surface REST OAuth implementation (PKCE, token rotation) | TerminalSkills `### Setup B` | **drop** for the skill; keep one line in a troubleshooting note | We never hand-roll OAuth | — |
| 2024-era social dimension cards and seasonal themes | 10x DESIGN_REFERENCE; 10x terminology | **drop** (keep the presentation/A4 rows only) | Stale and irrelevant to decks | — |
| Script-driven CLI catalogue (`scripts/*.py`) | 10x everything | **drop** | 61/61 scripts absent | — |

---

## Contradictions

1. **How many type families?** design-director: max 2, "exceeding this is a violation". social
 `design-and-templates`: "no more than 2 fonts". 10x `DESIGN_REFERENCE.md`: "Maximum 2 fonts". But
 10x's own `samples/brand-kits/brand-config.json` defines **three** (Montserrat, Open Sans, Playfair
 Display accent) while its `dont_do` bans more than two. → **Recommend ≤2 in practice**; allow a
 third only for a single recurring device (quote italic) and declare it as part of the system.

2. **Hierarchy levels.** design-director: "exactly 3 levels". carousel-writer: headline → supporting
 line → slide number → accent (effectively 4 ranks). → **Recommend "≤3 type styles + 1 caption/
 attribution style"**, because a coursework deck needs a source line and a slide number.

3. **Minimum body size.** design-director: **14 pt**. 10x reference: **30 px** for social.
 quote-cards: **~24 pt**. Our field evidence: ≈**34–38 px** body and ≈**52 px** titles at
 1920×1080 read well in a classroom. → **Recommend a px scale at 1920 width**, and reject pt
 entirely (Canva's `font_size` is px in our transactions). 14 pt is dangerously wrong for projection.

4. **Template-first vs structure-first.** social `canva`: start from the Brand Kit and a master
 template, then customise past it. design-director: plan grid/type/focal point, then generate.
 → **Recommend structure-first for bespoke decks, template-first only for volume runs**; and since
 our account has no templates, structure-first is the only executable path.

5. **Which MCP endpoint?** design-director README: `https://mcp.canva.com/mcp` (DCR, mcp-remote).
 TerminalSkills `SKILL.md`: `https://api.canva.com/connect/v1/mcp`. TerminalSkills *use-case*:
 `https://mcp.canva.com/mcp`. Ours: the `api.canva.com/connect/v1/mcp` mount with static OAuth.
 → **Recommend naming our endpoint and never repeating the other two** except as "different server,
 different auth model".

6. **Does the Connect API edit designs?** TerminalSkills table: "Editing — no (create / autofill /
 export only)". social `canva` + `tools/integrations/canva.md`: Design Editing API is **GA**.
 → **Recommend the social side** (GA editing exists); the TerminalSkills table is stale. It does not
 matter operationally for us because we only use the MCP editing ops.

7. **Brand templates plan gate.** TerminalSkills: "Pro and above". 10x `canva` hub: Resize = Pro,
 **Brand templates/Autofill = Enterprise**; 10x `canva-brand-kit`: Enterprise. → **Recommend
 "availability varies; check `get-logged-in-account-details` / the dataset call and treat an empty
 list as normal"**, which is what our account demonstrates (zero kits, zero templates).

8. **Slide/carousel count.** 10x reference: "Carousel: Up to 10 images". social
 `carousel-writer/references/platform-specs.md`: up to **20** since 2024, sweet spot 5–10.
 → **Recommend 20** (and for decks, let the argument set the count; "a tight 6 beats a padded 10").

9. **Surgical vs creative.** 10x: never change size/colour/position/background unless explicitly
 asked; never add elements. The user's actual ask includes "font bự hơn" and stronger diagrams.
 → **Recommend a named scope**: default = surgical; a *declared* "typography pass" or "diagram swap"
 unlocks those operations, and every such pass ends with a full thumbnail review.

10. **Content density.** design-director ("one idea per slide", Apple-Keynote negative space) vs
 10x style-notes ("maximum points per slide: 5") vs our coursework need (definitions, examples,
 citations). → **Recommend one idea per slide with ≤3 short support lines**, and move citations to
 a caption style; never paste paragraphs.

11. **Who renders.** social skills: "the agent specs, a design tool renders, the human approves".
 design-director/10x: the agent drives the tool end to end. → **Recommend the 10x/director model**
 (we do render) **with the social skills' review posture** (look at every page; the human approves
 delivery).

12. **Export recommendation.** design-director: PNG for social, PDF for presentations/print. 10x adds
 PPTX as the editable handoff. TerminalSkills adds `pptx`, `mp4`, `csv`, `html_*`.
 → **Recommend PDF (room) + PPTX (handoff) + PNG per page (review)**, and state that MP4/GIF are
 out of scope for a deck.

---

## Gaps

What a complete slide workflow needs that **none** of these skills cover:

1. **Academic deck architecture.** Nothing addresses thesis → argument → evidence → objection →
 synthesis, or the difference between a lecture deck (teach sequentially) and a defence deck
 (persuade). carousel-writer's structures are marketing structures.
2. **Citation and source handling on slides.** quote-cards covers attribution ethics; nobody covers
 footnoted sources, "theo C. Mác – Ph. Ăngghen", or a references slide.
3. **Diagram authoring.** No skill explains how to *make* a diagram in a system that cannot add
 shapes: drawing it outside (SVG/PNG at 2×), uploading via `create-upload-url`, and placing it with
 `insert_fill` over an existing region. design-director's data-viz rules assume a chart tool.
4. **Text-fidelity controls for generative create.** Nobody warns that `create-design` paraphrases the
 outline and can substitute doctrinal terms. A extraction step + diff against the source outline is
 needed.
5. **Font-family limits.** No skill knows that `format_text` cannot change the family, so "consistent
 typography" has to be achieved by scale/weight/alignment/colour only. Every "max 2 fonts" rule is
 unenforceable at the API level unless the deck was generated with the right faces.
6. **Presenter notes.** Both reading (`get-presenter-notes`) and the impossibility of writing notes are
 unaddressed; a deck workflow needs a notes artifact outside Canva.
7. **Per-slide overflow detection.** No skill gives a method for "did retyping this break the box?"
 beyond "look at the thumbnail". Nothing about measuring text length against a known box.
8. **Deck-level consistency audit.** No skill defines a cross-slide audit: same title y-position, same
 body column, same accent usage, same page-number spot, across N slides.
9. **Undo/version strategy.** 10x says duplicate first; nobody defines a checkpoint scheme (copy per
 milestone, keep the original untouched, name versions) or what to do when a committed transaction
 made things worse.
10. **Quota and failure budgets for image generation.** `generate-image` can fail with
 `credit_quota_exceeded`; no skill has a fallback ladder (draw locally → upload → reuse an existing
 asset → omit the visual).
11. **Restricted/responsive pages.** Nothing about pages where only a subset of operations is legal.
12. **Grouped-element deletion semantics.** 10x's element ids are script-supplied; nobody documents that
 deleting a grouped child silently no-ops and that the page-group id prefix is required.
13. **Ordering semantics of structural merges.** carousel-writer assumes slides stay in order; nobody
 covers `merge-designs` insert order coming back reversed, or how to verify order after a merge.
14. **Bilingual/multi-script typography.** Vietnamese diacritics change line-height and wrapping; no
 skill mentions script-specific metrics or a mixed-script type pairing.
15. **Time/space budget for a 16-slide build.** TerminalSkills gives rate limits per tool but no
 end-to-end plan (how many transactions, when to commit, how many reviews) — the operational shape
 of a full deck run is missing everywhere.
16. **Truthful-content review for a subject matter.** quote-cards' honesty spine is the only ethical
 gate in the cluster; nothing covers "the generator changed a term and the slide is now wrong",
 which is the highest-severity failure in our actual work.
