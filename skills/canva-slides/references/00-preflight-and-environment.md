# 00 - Pre-flight: mode, environment, capability gate

Sources merged: official `edit-design` capability matrix, dev-kit "honesty clause", `brand-check` "Can't verify"; TerminalSkills surface decision, capabilities gate and rate limits;
design-director pre-flight; 10x preservation rules; live verification of this mount.

## 1. Pick the mode (one line each, then go to the matching reference)

| User says | Mode | Go to |
|---|---|---|
| "làm slide về X", "make a deck" | **Build** | 01 -> 02 -> 03 -> 04 -> 05 -> 07 |
| "làm lại slide này" + a Canva link | **Rebuild** (new design, original untouched) | read original (`get-design-content`, transaction inspect) -> 01 -> 02 ... |
| "sửa / chỉnh slide N", "font bự hơn" | **Edit** (surgical or declared pass) | 05 (+ 03 for targets) |
| "thêm ví dụ / thêm slide", "đổi thứ tự" | **Structure** | 06 |
| "xem giúp / đánh giá" | **Review only** (never edits) | 04 |
| "dịch / bilingual" | **Translate** | 06 section 6 |
| "xuất PDF / PPTX / notes" | **Deliver** | 07 |
| "áp thương hiệu / template" | **Brand** | 08 |
| comments on the design | **Feedback round** | 07 section 6 |

If the user gives a link: `canva.link/xyz` -> `resolve-shortlink { shortlink_id:"xyz" }`; a full URL `.../design/DAH.../...` -> the id after `/design/`; a raw `D...` id -> use as is. **Never** call `search-designs` for something you already have an id for.

## 2. Environment checks (once per session, 4 calls, show results in one line)

1. `get-logged-in-account-details {}` -> `{id, name, team_id}`. Say whose account it is. If the name is not the user's, warn before creating anything: designs land in that team. (Observed: account "Hui Centralized".)
2. `list-brand-kits {}` and `search-brand-templates { dataset:"any", design_types:["presentation"] }`. An empty `{"items":[]}` is **normal** here (plan or no match), not an error: record "no brand kit / no template" and continue with the written token block (`08-templates-and-brand.md`).
3. Mounted tools: trust the live tool list, not a skill's tool names. In this mount: `create-design`, `merge-designs`, `copy-design`, `resize-design`, `export-design`, `get-export-formats`, `create-upload-url`, `upload-asset-from-url`, `import-design-from-url`, `generate-image`, `get-presenter-notes`, comments tools, folder tools, brand tools, `get-design-dataset`. **Not mounted**: `autofill-design`, `generate-design-structured`, `prepare-design-generation`, any notes-write tool. Community skills name tools that do not exist: `get-design-export-formats` (real: `get-export-formats`), `generate-design-structured` (none), `Canva:`-prefixed names (prefix is cosmetic).
4. Optional: `help { prompt }` for product questions (plan features, editor steps) instead of answering from memory; show its answer as returned.

Endpoint facts: this mount is `https://api.canva.com/connect/v1/mcp` (Developer-Portal app, static OAuth, redirect `127.0.0.1:3333`). The Canva-hosted connector `https://mcp.canva.com/mcp` is a **different** server with dynamic client registration; its skills (official packs, openai/plugins) work on the same tool names. A `Missing scopes` error: ask the user to disconnect and reconnect to mint a new token. A 503 from `start-editing-transaction` is an upstream problem: retry once after 15-30 s; if it persists (it lasted 35+ min on 2026-11-07) use the no-transaction path in `05` s.10.

### Tool health matrix (probe cheaply; record it in the plan folder)

Two independent failure domains were observed on 2026-11-07: the **AI-credit quota** (`create-design`, `generate-image`) and the **editing-transaction service** (`start-editing-transaction`). The rest kept working, so degrade by capability, not all-or-nothing:

| Capability | Needs | If down |
|---|---|---|
| Generate a deck | credits (`create-design`) | no-credit mode: recombine existing decks (`02` s.8) |
| Generate art | credits (`generate-image`) | user art, local diagrams, public images |
| Read text/page count, export, copy, merge, upload | none of the above | normal |
| Edit text/format/media, thumbnails, diagram placement | transaction service | review via PNG export; structure via copy/merge; manual checklist for edits |

Probe order at session start (a few calls, one line of report): `get-logged-in-account-details`; `get-design` on a known deck; `start-editing-transaction` + immediate `cancel`; the first `create-design` response doubles as the credit probe (never spend a generation just to test).

## 3. Capability matrix (state limits BEFORE promising; never invent an operation)

| Want | Possible? | How / alternative |
|---|---|---|
| Generate a deck from an outline | yes | `create-design` (`format` + `outline`) |
| Apply a brand kit / brand template to generation | only legacy `generate-design` (+ `list-brand-kits`) | not with `create-design` |
| Change text, size, weight, colour, alignment, line height, lists, links | yes | `format_text`, `replace_text` |
| Change **font family** | **no** | consistency by scale/weight/colour; font comes from the generator's theme |
| Add a **new text box / shape** | **no** | clone a donor slide; custom image via `insert_fill` |
| Change **background** colour/image | **no** | cover with an opaque `insert_fill` image if essential |
| Add / delete / reorder pages | yes, **not** in transactions | `merge-designs`, `copy-design` |
| Write **presenter notes** | **no** | deliver a notes file; HTML import `[UNVERIFIED]` |
| Read presenter notes | yes | `get-presenter-notes` |
| Write alt text | only when inserting a fill | `insert_fill.alt_text` |
| Delete a design | **no** | tell the user; keep backups tidy by naming |
| Undo after commit | **no** | backup via `copy-design` first |
| Animations, transitions, opacity of existing elements | **no** | manual in editor |
| Video timeline editing | **no** | out of scope |
| Export | yes, credit-free **[V]** | `export-design` (pdf, pptx, png, jpg, gif, mp4, csv); per-page PNG also serves as the review substitute for thumbnails |
| Generate decks and pictures | **quota-limited** | `create-design` and `generate-image` share one AI-credit quota (`quota_exceeded`); no-credit mode in `02` s.8, image ladder in `06` |
| Resize | yes (Pro) | `resize-design`; always re-review |

Honesty clause (Canva dev-kit): when a capability is missing, say so in one line, give the nearest alternative, and **never silently switch** to a different method.

## 4. Inputs to collect (ask ONE question per missing item that would change the deck; infer the rest and state assumptions)

Required: topic and source material (notes, textbook passages, the original deck); audience and setting (course, lecturer, seminar); talk length in minutes; language; deliverable (slides only, or + notes/Q&A). Optional but valuable: required terminology and sources (e.g. "theo Giáo trình Triết học Mác - Lênin"), required slide count, must-have examples, visual references (the user's own images), what the lecturer will grade. When the user already supplied a plan, **respect its sequence and vocabulary** and flag every addition (official `classroom-helper`).

Never ask for what a tool or file already tells you. Never open with a two-part "paste plan or describe topic" question.

## 5. Rate and quota budget

Per user per minute (TerminalSkills): `create-design` 20, `start-editing-transaction` 20, `perform-editing-operations` 50, `commit/cancel` 20, `copy-design` 20, `resize-design` 20, reads (get-design, pages, content, thumbnail, notes, formats, search) 100, `upload-asset-from-url` 30, `export-design` / `import-design-from-url` 20, anything else 300. Exports 75 per 5 min per document, 500 per day. **`create-design` and `generate-image` share an AI-credit quota** that can be 100% used (observed until 2026-12-01 00:00 UTC) and fails synchronously with `quota_exceeded`. A full 16-slide build + review + font pass stays far inside the request limits if you batch: expect ~4 creates/copies, ~6 transactions, ~100 reads.

## 6. Protect the user's original

Default for any "làm lại / redo / improve" request: **build a new design** and hand back the new link; the original stays untouched (nothing on the API deletes it, so the original is also the user's backup). For in-place edits take a `copy-design` backup first when more than ~3 pages change.

## 7. Surfaces: MCP first, CLI only for named gaps

The mounted MCP is the workhorse (generate, read, edit, structure, export). `canva` CLI (`@canva/cli`, Node >= 22; run via `npx -y @canva/cli@latest`) is a Connect REST wrapper with **no element-editing endpoint**; use it only for scripted bulk runs, raw REST endpoints the MCP lacks, or unattended pipelines, and only after the user logs in (`canva login`, browser approval). It needs a separate login that can land on a different account than the MCP. Do not install anything without the user saying so.

## 8. Skill hygiene

When this skill and a community skill disagree, this skill wins for **tool names and limits** (verified live); community skills win only for ideas this skill lacks. Re-verify limits quarterly or when a tool errors unexpectedly (`SOURCES.md` lists provenance and last-verified dates).
