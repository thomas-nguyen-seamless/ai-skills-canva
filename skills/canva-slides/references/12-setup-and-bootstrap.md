# 12 - Setup and bootstrap (install whatever is missing)

Run this **before** phase 0 on a new machine, and any time a script fails with "command not found" or a
missing module. `scripts/bootstrap.sh` is idempotent and prints a readiness table.

```sh
scripts/bootstrap.sh            # asks once per missing tool
scripts/bootstrap.sh --yes      # install unattended (CI, throwaway container)
scripts/bootstrap.sh --no-install   # report only
```

Exit `0` = ready for the MCP workflow; `1` = something still needs a human (see the `[missing]` lines).

## What it checks and how it fixes it

| Item | Why the skill needs it | Auto-fix |
|---|---|---|
| `uv` | every script runs as `uv run --with …,` so nothing is installed globally | `brew install uv`, else the official `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| `python3` | all checkers/converters | `xcode-select --install` (macOS); ask the user, never guess a distro |
| `git` | cloning the skill, versioning deck folders | `brew install git` |
| `node` >= 22, `npx` | `npx -y @canva/cli@latest` — the CLI is run from npx, **no global install** | `brew install node` |
| Canva CLI | local-file import, export, in-place page updates (`canva api …`) | fetched by npx; version printed |
| Python libs | `pillow` (art/diagrams/QA), `numpy`+`scipy` (ink extraction), `python-pptx`+`lxml` (PPTX build), `pymupdf`+`pypdf` (PDF render/text) | pre-warmed into the uv cache with one `uv run --with …` call |
| Canva CLI login | token for `canva api` | `npx -y @canva/cli@latest login` — **human approves in the browser** |
| MCP `canva` | the primary tool surface | never overwritten; prints the snippet to add |
| PowerPoint (macOS only) | `templates/pptx-fallback/render.sh` fidelity render | manual install; the import path still works without it |

## Mounting the Canva MCP (one time, needs Developer-Portal credentials)

The hosted connector (`https://mcp.canva.com/mcp`) supports dynamic client registration and is a different
service; this skill targets the **Developer MCP** mount used in testing:

1. Canva Developer Portal -> create an integration -> add the scopes the MCP asks for -> add the redirect URL
   `http://127.0.0.1:3333/callback`.
2. Copy `clientId` / `clientSecret` into `templates/mcp-canva.snippet.json` and merge that object into your
   client's MCP config (`~/.omp/agent/mcp.json` for omp, under `mcpServers`).
3. Restart the agent; the tool surface should list `create-design`, `get-design`, `export-design`,
   `start-editing-transaction`, `merge-designs`, …
4. If a tool answers `Missing scopes`, disconnect and reconnect the integration (new token), do not edit scopes
   in the token by hand.

## Account and identity facts worth knowing

- `canva api users me` returns `team_user.user_id` / `team_id`, which are a **different id namespace** from the
  ids MCP tools report for the same design. The design still shows up in both — do not treat a mismatch as a
  wrong account. Confirm with a read: `canva api designs get <id>` and MCP `get-design <id>`.
- The AI allowance is per account, not per machine: a Free account gets roughly 20 AI uses a month, resetting
  at 00:00 UTC on the 1st. `create-design` and `generate-image` spend it (`quota_exceeded`, synchronous).
- `canva login` stores the token locally; `canva logout` removes it. Multiple logins are supported with
  `--profile <name>` (e.g. a personal and a work account).

## Offline / locked-down machines

- `npx` needs the registry once; run `npx -y @canva/cli@latest --version` while online, then it is cached.
- Without `uv`, install with `pip3 install --user pillow numpy scipy python-pptx lxml pymupdf pypdf` and run the
  scripts with plain `python3` instead of `uv run --with …` (the scripts import only those packages).
- Without Homebrew: install Node from nodejs.org (>= 22) or use `nvm`; install uv from its installer script.
- No PowerPoint and no LibreOffice? Then `render.sh` cannot produce a fidelity render; either install one or
  accept that the only visual proof comes from Canva's own export (`canva api exports create --format png`).

## Fonts

`templates/pptx-fallback/build_deck.py` measures text with **Arial** (macOS:
`/System/Library/Fonts/Supplemental/Arial*.ttf`). On Linux install `fonts-liberation` and point the font path
at `LiberationSans-Regular.ttf` (metric-compatible with Arial); it maps to the same Canva font family. Keep one
family per deck — the measurement is what guarantees the text fits.
