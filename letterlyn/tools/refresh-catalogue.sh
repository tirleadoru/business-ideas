#!/bin/bash
# Rebuild the LetterLyn catalogue page (pages/catalogue.html) from the current catalogue.
# Then publish pages/catalogue.html to its artifact (URL in ../MEMORY.md).
set -e
T="$(cd "$(dirname "$0")" && pwd)"
CONTENT="/Users/dorutirlea/Business Ideas/letterlyn/packages/content"
mkdir -p "$T/build"
cd "$CONTENT"
node scripts/check-catalog.mjs --lang ro --learn ro:en > /dev/null 2>&1 || true
cp catalog/report.json "$T/build/report.ro.json"
node scripts/check-catalog.mjs --lang en > /dev/null 2>&1 || true   # leaves catalog/report.json = English
python3 scripts/wordfill/compile_extras.py > /dev/null
python3 "$T/shelf_metrics_all.py"
python3 "$T/round2q.py" > /dev/null
python3 "$T/round3q.py" > /dev/null
python3 "$T/catalog_page.py"
echo "built: $T/../pages/catalogue.html"
