#!/bin/bash
# Push a locally built PPTX into an EXISTING Canva design, keeping the SAME design id and link.
# Default: replace only the pages you list (safe on a shared design). --all replaces every page.
# Usage: update_canva_deck.sh <TARGET_DESIGN_ID> <deck.pptx> "<Title for the temporary import>" [--pages "5,7,12-14"]
#   --pages "5,7,12-14" = DEFAULT: replace ONLY those 1-based pages (the pages you actually changed).
#                         Every other page, and any manual Canva edit on it, is left untouched.
#                         Each replacement is net-zero (insert 1, delete 1), so numbering stays stable.
#   --all               = replace EVERY page. Only for decks nobody else edits (wipes manual edits).
#   No flag            = refuse to run: on a shared design an accidental all-pages replace is unrecoverable.
# Needs: node >= 24, one prior `npx -y @canva/cli@latest login`.
# Docs: POST /v1/merges with type=modify_existing_design (preview), one operation per request by default.
set -euo pipefail
TARGET=${1:?target design id}
PPTX=${2:?pptx path}
TITLE=${3:-Deck import $(date +%Y%m%d-%H%M%S)}
SEL=""
MODE=pages
case "${4:-}" in
  --pages) SEL=${5:?page list like 5,7,12-14} ;;
  --all)   MODE=all ;;
  "")      echo "refusing to run: pass --pages \"1,5,9\" (only the pages you changed) or --all for a solo deck." >&2; exit 2 ;;
  *)       echo "unknown flag ${4}; use --pages \"1,5\" or --all" >&2; exit 2 ;;
esac
CLI="npx -y @canva/cli@latest"
MIME="application/vnd.openxmlformats-officedocument.presentationml.presentation"

clean() { grep -v -i -E "deprecat|trace-dep" || true; }
jget() { python3 -c 'import json,sys;d=json.load(sys.stdin);
k=sys.argv[1].split(".")
for p in k:
    d=d[int(p)] if isinstance(d,list) else d[p]
print(d)' "$1"; }

poll_design_import() {  # $1 job id -> json on stdout
  for _ in $(seq 1 40); do
    out=$($CLI api design-imports get "$1" 2>&1 | clean)
    case "$out" in *'"status": "success"'*|*'"status": "failed"'*) echo "$out"; return;; esac
    sleep 4
  done
  echo "$out"; }

poll_merge() {
  for _ in $(seq 1 40); do
    out=$($CLI api merges get "$1" 2>&1 | clean)
    case "$out" in *'"status": "success"'*|*'"status": "failed"'*) echo "$out"; return;; esac
    sleep 3
  done
  echo "$out"; }

echo "1/4 importing $PPTX ..." >&2
imp=$($CLI api design-imports create --file "$PPTX" --title "$TITLE" --mime-type "$MIME" 2>&1 | clean)
jid=$(echo "$imp" | jget data.job.id)
res=$(poll_design_import "$jid")
echo "$res" | grep -q '"status": "success"' || { echo "IMPORT FAILED: $res" >&2; exit 1; }
NEW=$(echo "$res" | jget data.job.result.designs.0.id)
N=$(echo "$res" | jget data.job.result.designs.0.page_count)
echo "    imported $NEW ($N pages)" >&2

pages_list() {  # "5,7,12-14" -> "5 7 12 13 14"
  python3 -c '
import sys
out=[]
for part in sys.argv[1].split(","):
    part=part.strip()
    if "-" in part:
        a,b=part.split("-"); out+=list(range(int(a),int(b)+1))
    elif part: out.append(int(part))
print(" ".join(str(x) for x in out))' "$1"; }

if [ "$MODE" = pages ]; then
  PICK=$(pages_list "$SEL")
  echo "2/3 replacing ONLY pages: $PICK (all other pages untouched) ..." >&2
  for p in $PICK; do
    if [ "$p" -lt 1 ] || [ "$p" -gt "$N" ]; then echo "page $p out of range 1..$N" >&2; exit 1; fi
    ops=$(python3 -c 'import json,sys;print(json.dumps([{"type":"insert_pages","source":{"type":"design","design_id":sys.argv[2],"page_numbers":[int(sys.argv[3])]},"after_page_number":int(sys.argv[3])-1}]))' x "$NEW" "$p")
    m=$($CLI api merges create --type modify_existing_design --design-id "$TARGET" --operations "$ops" 2>&1 | clean)
    mj=$(echo "$m" | jget data.job.id); mres=$(poll_merge "$mj")
    echo "$mres" | grep -q '"status": "success"' || { echo "INSERT FAILED for page $p: $mres" >&2; exit 1; }
    del=$(python3 -c 'import json,sys;print(json.dumps([{"type":"delete_pages","page_numbers":[int(sys.argv[1])+1]}]))' "$p")
    d=$($CLI api merges create --type modify_existing_design --design-id "$TARGET" --operations "$del" 2>&1 | clean)
    dj=$(echo "$d" | jget data.job.id); dres=$(poll_merge "$dj")
    echo "$dres" | grep -q '"status": "success"' || { echo "DELETE FAILED after inserting page $p: $dres" >&2; exit 1; }
    echo "    page $p replaced" >&2
  done
  echo "3/3 verifying ..." >&2
  final=$($CLI api designs get "$TARGET" 2>&1 | clean)
  FC=$(echo "$final" | jget data.design.page_count)
  [ "$FC" = "$N" ] || { echo "MISMATCH: target has $FC pages, expected $N" >&2; exit 1; }
  echo "{\"target\":\"$TARGET\",\"source\":\"$NEW\",\"replaced\":$(python3 -c 'import json,sys;print(json.dumps([int(x) for x in sys.argv[1].split()]))' "$PICK"),\"pages\":$FC,\"mode\":\"pages\",\"ok\":true}"
  exit 0
fi

echo "2/4 inserting $N pages into $TARGET at the beginning ..." >&2
PAGES=$(python3 -c "import json,sys;print(json.dumps(list(range(1,$N+1))))" "$N")
ops=$(python3 -c 'import json,sys;print(json.dumps([{"type":"insert_pages","source":{"type":"design","design_id":sys.argv[2],"page_numbers":json.loads(sys.argv[3])},"after_page_number":0}]))' x "$NEW" "$PAGES")
m=$($CLI api merges create --type modify_existing_design --design-id "$TARGET" --operations "$ops" 2>&1 | clean)
mj=$(echo "$m" | jget data.job.id)
mres=$(poll_merge "$mj")
echo "$mres" | grep -q '"status": "success"' || { echo "INSERT FAILED: $mres" >&2; exit 1; }
TOTAL=$(echo "$mres" | jget data.job.result.design.page_count)
echo "    now $TOTAL pages" >&2

if [ "$TOTAL" -le "$N" ]; then
  echo "3/4 nothing to delete (design had no old pages)" >&2; else
  echo "3/4 deleting the $((TOTAL-N)) old pages ($((N+1))..$TOTAL) ..." >&2
  del=$(python3 -c 'import json,sys;n,t=int(sys.argv[1]),int(sys.argv[2]);print(json.dumps([{"type":"delete_pages","page_numbers":list(range(n+1,t+1))}]))' "$N" "$TOTAL")
  d=$($CLI api merges create --type modify_existing_design --design-id "$TARGET" --operations "$del" 2>&1 | clean)
  dj=$(echo "$d" | jget data.job.id)
  dres=$(poll_merge "$dj")
  echo "$dres" | grep -q '"status": "success"' || { echo "DELETE FAILED: $dres" >&2; exit 1; }
fi

echo "4/4 verifying ..." >&2
final=$($CLI api designs get "$TARGET" 2>&1 | clean)
FC=$(echo "$final" | jget data.design.page_count)
[ "$FC" = "$N" ] || { echo "MISMATCH: target has $FC pages, expected $N" >&2; exit 1; }
echo "{\"target\":\"$TARGET\",\"source\":\"$NEW\",\"pages\":$N,\"ok\":true}"
