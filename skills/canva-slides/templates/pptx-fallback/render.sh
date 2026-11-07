#!/bin/bash
# Render deck.pptx through real PowerPoint (macOS) -> build/render.pdf -> build/png/sNN.png -> contact sheet.
# Usage: run INSIDE the deck folder (the one holding deck.pptx):  render.sh [label]
# Why: Canva's importer and PowerPoint both re-layout text; looking at the engine's own render is the only
# trustworthy check before importing. PowerPoint is sandboxed: export to the project folder through a POSIX
# file object, and never read back from ~/Library/Containers/... (EPERM).
set -e
[ -f deck.pptx ] || { echo "run this from the folder that holds deck.pptx" >&2; exit 1; }
LABEL="${1:-sheet}"
HERE="$(cd "$(dirname "$0")" && pwd)"
DECK_DIR="$(pwd)"
mkdir -p build
rm -f build/render.pdf
osascript - "$DECK_DIR" <<'AS'
on run argv
  set d to item 1 of argv
  tell application "Microsoft PowerPoint"
    repeat while (count of presentations) > 0
      close presentation 1 saving no
    end repeat
    open POSIX file (d & "/deck.pptx")
    delay 3
    save presentation 1 in (POSIX file (d & "/build/render.pdf")) as save as PDF
    delay 1
    close presentation 1 saving no
  end tell
end run
AS
rm -rf build/png && mkdir -p build/png
uv run --with pymupdf python - <<'PY' 2>&1 | grep -v -i warn
import pymupdf
d = pymupdf.open('build/render.pdf'); print('pages', len(d))
for i, p in enumerate(d, 1):
    p.get_pixmap(dpi=144).save(f'build/png/s{i:02d}.png')
PY
rm -f build/thumbs.tsv
for f in build/png/s*.png; do n=$(basename "$f" .png | tr -d 's'); printf "%d\t%s\n" "$((10#$n))" "$f" >> build/thumbs.tsv; done
uv run --with pillow python "$HERE/../../scripts/contact_sheet.py" build/thumbs.tsv "build/$LABEL.png" 4 480 | tail -1
