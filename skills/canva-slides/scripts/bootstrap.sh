#!/bin/bash
# bootstrap.sh - make this skill runnable on this machine. Idempotent: safe to run every session.
#
# Checks and, when missing, INSTALLS: uv, the Python runtimes used by the scripts (via `uv run --with`,
# cached once here), Node >= 22, the Canva CLI (via npx), git. Then verifies Canva CLI login and reports
# what still needs the human (login, MCP mount, PowerPoint).
#
# Usage: scripts/bootstrap.sh [--yes] [--no-install]
#   --yes         do the installs without asking (default asks once per missing tool)
#   --no-install  / --check   report only; never install anything
# Nothing that is already present is ever reinstalled: present tools print "[ok] ... (already installed, skipped)"
# and the script only checks what it cannot do for the user (Canva CLI login, MCP mount).
#
# Exit: 0 = ready for the MCP workflow; 1 = something still needs a human (login / MCP mount).
set -uo pipefail
YES=0; NOINSTALL=0
for a in "$@"; do case "$a" in --yes|-y) YES=1;; --no-install|--check) NOINSTALL=1;; esac; done

ok=0; warn=0; act=0
say() { printf '%-14s %s\n' "$1" "$2"; }
OK()   { say "[ok]" "$1"; ok=$((ok+1)); }
MISS() { say "[missing]" "$1"; act=$((act+1)); }
NOTE() { say "[note]" "$1"; warn=$((warn+1)); }

ask() {  # ask <question>; returns 0 = proceed
  [ "$NOINSTALL" = 1 ] && return 1
  [ "$YES" = 1 ] && return 0
  [ -t 0 ] || return 1
  printf '%s [Y/n] ' "$1"; read -r r; case "${r:-y}" in [Yy]*) return 0;; *) return 1;; esac
}

have() { command -v "$1" >/dev/null 2>&1; }
brew_install() {  # brew_install <formula>
  if ! have brew; then MISS "Homebrew (needed to install $1 automatically)"; return 1; fi
  if ask "Install $1 with Homebrew?"; then
    say "[install]" "brew install $1 (this can take a minute)"; brew install "$1" && OK "$1" || MISS "$1 (brew failed)"
  else MISS "$1"; return 1; fi
}

echo "== environment =="
uname -s -m
say "shell" "$SHELL"

# --- uv (runs every python script here with --with deps, nothing global) -------------------------
if have uv; then OK "uv $(uv --version 2>/dev/null | awk '{print $2}') (already installed, skipped)"; else
  MISS "uv"
  if ask "Install uv?"; then
    if have brew; then brew install uv && OK "uv"; else
      say "[install]" "curl -LsSf https://astral.sh/uv/install.sh | sh"
      curl -LsSf https://astral.sh/uv/install.sh | sh && OK "uv" || MISS "uv"
    fi
  fi
fi

# --- Python 3 -----------------------------------------------------------------------------------
if have python3; then OK "python3 $(python3 -V 2>&1 | awk '{print $2}')"; else MISS "python3 (install Xcode CLT: xcode-select --install)"; fi

# --- git ----------------------------------------------------------------------------------------
have git && OK "git $(git --version | awk '{print $3}') (already installed, skipped)" || MISS "git"

# --- Node + npx (Canva CLI is run through npx, no global install required) ----------------------
NODE_MAJ=0; have node && NODE_MAJ=$(node -v | sed 's/^v//' | cut -d. -f1)
if have node && [ "$NODE_MAJ" -ge 22 ]; then OK "node $(node -v) (already installed, skipped)"; else
  MISS "node >= 22 (found: $(have node && node -v || echo none))"
  if ask "Install Node with Homebrew?"; then brew install node && have node && OK "node $(node -v)" || MISS "node"; fi
fi
have npx && OK "npx $(npx --version 2>/dev/null) (already installed, skipped)" || MISS "npx (comes with npm/node)"

# --- Canva CLI ----------------------------------------------------------------------------------
if command -v canva >/dev/null 2>&1; then
  OK "Canva CLI $(canva --version 2>/dev/null | tail -1) (global install, already present, skipped)"
elif have npx; then
  CLI_CACHE=$(npm config get cache 2>/dev/null)/_npx
  if ls -d "$CLI_CACHE"/*/node_modules/@canva/cli >/dev/null 2>&1; then
    OK "Canva CLI (npx cache, already present, skipped)"
  else
    VER=$(npx -y @canva/cli@latest --version 2>/dev/null | tail -1)
    [ -n "$VER" ] && OK "Canva CLI $VER (fetched once into npx cache)" || NOTE "Canva CLI could not be fetched (network/proxy?)"
  fi
fi

# --- Python libs used by the scripts (pre-warm the uv cache) ------------------------------------
if have uv; then
  if uv run --quiet --with pillow --with numpy --with scipy --with python-pptx --with lxml --with pymupdf --with pypdf \
       python -c "import PIL, numpy, scipy, pptx, lxml, pymupdf, pypdf" >/dev/null 2>&1; then
    OK "python libs cached (pillow, numpy, scipy, python-pptx, lxml, pymupdf, pypdf) - already present, skipped"
  else
    MISS "python libs"
    if ask "Fetch them now with uv (cached, no global install)?"; then
      uv run --with pillow --with numpy --with scipy --with python-pptx --with lxml --with pymupdf --with pypdf \
        python -c "import PIL, numpy, scipy, pptx, lxml, pymupdf, pypdf" && OK "python libs cached" || MISS "python libs"
    fi
  fi
fi

echo "== Canva access =="
# --- Canva CLI login (needs a human: browser approval) ------------------------------------------
if have npx; then
  OUT=$(npx -y @canva/cli@latest api users me 2>&1)
  if printf '%s' "$OUT" | grep -q '"ok": true'; then
    WHO=$(npx -y @canva/cli@latest api users profile 2>/dev/null | python3 -c 'import sys,json,re;s=sys.stdin.read();m=re.search(r"\{.*\}",s,re.S);print(json.loads(m.group(0))["data"]["profile"]["display_name"] if m else "?")' 2>/dev/null)
    OK "Canva CLI logged in${WHO:+ as $WHO}"
  else
    MISS "Canva CLI login"
    if ask "Run 'canva login' now (you approve in the browser)?"; then
      npx -y @canva/cli@latest login
      npx -y @canva/cli@latest api users me 2>&1 | grep -q '"ok": true' && OK "Canva CLI logged in" || MISS "Canva CLI login"
    else
      NOTE "run: npx -y @canva/cli@latest login   (needed for import/export/in-place updates)"
    fi
  fi
fi

# --- MCP mount (needs Developer-Portal credentials; never overwritten) --------------------------
MCP="${HOME}/.omp/agent/mcp.json"
if [ -f "$MCP" ] && grep -q '"canva"' "$MCP"; then OK "MCP 'canva' configured in $MCP"
else
  MISS "MCP 'canva' entry in $MCP"
  NOTE "add it from templates/mcp-canva.snippet.json, then restart the agent (OAuth app client id/secret required)"
fi

# --- macOS PowerPoint (only for the PPTX fidelity render) --------------------------------------
if [ "$(uname -s)" = "Darwin" ]; then
  [ -d "/Applications/Microsoft PowerPoint.app" ] && OK "Microsoft PowerPoint (PPTX render)" \
    || NOTE "PowerPoint not installed: PPTX render.sh unavailable (import path still works)"
fi

echo
echo "ready: $ok ok, $warn note(s), $act needing attention"
[ "$act" -eq 0 ] && exit 0 || exit 1
