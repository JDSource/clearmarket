#!/usr/bin/env node
// Build guardrail: assert every event + signal page ships a Dataset JSON-LD block.
// Runs as `postbuild` (after `astro build`), so a regression fails the build BEFORE deploy —
// exactly the gap that shipped silently once (event pages had only the site-wide WebSite block).
// Event indexes use DataCatalog, not Dataset, so we only scan the per-slug detail pages.
import { readFile, readdir } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import { join } from 'node:path';

const DIST = fileURLToPath(new URL('../dist/', import.meta.url));
const NEEDLE = '"@type":"Dataset"';

async function detailPages(base) {
  let entries;
  try { entries = await readdir(base, { withFileTypes: true }); } catch { return []; }
  return entries.filter((e) => e.isDirectory()).map((e) => join(base, e.name, 'index.html'));
}

async function check(label, base) {
  const files = await detailPages(base);
  const missing = [];
  for (const f of files) {
    let html = '';
    try { html = await readFile(f, 'utf8'); } catch { continue; }
    if (!html.includes(NEEDLE)) missing.push(f);
  }
  return { label, total: files.length, missing };
}

let failed = false;
for (const [label, sub] of [['events', 'events'], ['signals', 'signals']]) {
  const { total, missing } = await check(label, join(DIST, sub));
  if (total === 0) {
    console.warn(`! ${label}: no detail pages found under dist/${sub}/ (skipped)`);
    continue;
  }
  if (missing.length) {
    failed = true;
    console.error(`✗ ${label}: ${missing.length}/${total} pages missing Dataset JSON-LD`);
    missing.slice(0, 5).forEach((m) => console.error(`    ${m}`));
    if (missing.length > 5) console.error(`    ...and ${missing.length - 5} more`);
  } else {
    console.log(`✓ ${label}: all ${total} pages carry Dataset JSON-LD`);
  }
}

if (failed) {
  console.error('check-jsonld FAILED — Dataset JSON-LD missing on pages above. Build gated.');
  process.exit(1);
}
console.log('check-jsonld passed');
