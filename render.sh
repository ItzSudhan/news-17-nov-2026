#!/bin/sh
# Render layout/index.html to entry.png (1024x1024) with headless Chrome.
# If the PNG is over 1 MiB, re-encode it as a high-quality JPEG (file name stays entry.png).
set -e
cd "$(dirname "$0")"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
OUT="$PWD/entry.png"
"$CHROME" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=1 \
  --window-size=1024,1024 --screenshot="$OUT" "file://$PWD/layout/index.html" >/dev/null 2>&1
SIZE=$(stat -f%z "$OUT")
if [ "$SIZE" -gt 1048576 ]; then
  sips -s format jpeg -s formatOptions 92 "$OUT" --out "$OUT.jpg" >/dev/null
  mv "$OUT.jpg" "$OUT"
fi
sips -g pixelWidth -g pixelHeight -g format "$OUT" | tail -3
stat -f "%z bytes" "$OUT"
