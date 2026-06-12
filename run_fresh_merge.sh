#!/usr/bin/env bash
# One-shot fresh-data flip (local). Stops on any error. Backups baked in.
# Stages this session's fresh 1,998-event enriched bundle through the merge +
# patch + build chain so the local site serves the fresh deterministic-ID universe.
set -euo pipefail
cd "$HOME/Git/clearmarket"

STAMP="pre-fresh-2026-06-03"
FRESH_FULL="$HOME/jeremy-os/outputs/clearmarket/samples-universe/universe-enriched-full.json"

echo "[0/6] backups"
cp web/data/universe-enriched-linked.json "web/data/universe-enriched-linked.${STAMP}-bak.json"
cp web/data/universe-enriched-full.json   "web/data/universe-enriched-full.${STAMP}-bak.json"
[ -f canon-registry.json ] && cp canon-registry.json "canon-registry.${STAMP}-bak.json" || true

echo "[1/6] stage fresh -full bundle"
test -s "$FRESH_FULL"
cp "$FRESH_FULL" web/data/universe-enriched-full.json
python3 -c "import json;d=json.load(open('web/data/universe-enriched-full.json'));print('   staged events:',len(d['events']),'markets:',len(d['markets']))"

echo "[2/6] merge_linked_into_bundle"
python3 merge_linked_into_bundle.py

echo "[3/6] canon_extract slice (LLM re-extract; IDs changed)"
python3 canon_extract.py slice

echo "[4/6] build-data.sh (fix_questions / patch_ladders / patch_sources / merge_canon / export / build)"
./build-data.sh

echo "[5/6] verify built bundle"
python3 -c "import json;d=json.load(open('web/data/universe-enriched-linked.json'));print('   final events:',len(d['events']),'markets:',len(d['markets']))"

echo "[6/6] DONE — restart dev server next"
