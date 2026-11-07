#!/usr/bin/env bash
# Upload one local file to Canva using the single-use URL from create-upload-url.
# Usage: post_upload.sh "<uploadUrl>" /path/to/file.png
# Prints the JSON body, e.g. {"mediaId":"MAH..."}. Exit 1 on a non-2xx status.
# The URL is single-use and short-lived: on any failure request a NEW one, never retry this one.
set -euo pipefail
[ $# -eq 2 ] || { echo "usage: $0 <uploadUrl> <file>" >&2; exit 2; }
out=$(mktemp)
code=$(curl -sS -o "$out" -w '%{http_code}' -X POST \
  -H 'Content-Type: application/octet-stream' --data-binary "@$2" "$1")
cat "$out"; echo
rm -f "$out"
case "$code" in 2*) exit 0 ;; *) echo "HTTP $code - request a fresh upload URL" >&2; exit 1 ;; esac
