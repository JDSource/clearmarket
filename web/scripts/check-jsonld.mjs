#!/usr/bin/env node
// Build guardrail for Dataset JSON-LD. Two assertions per event + signal page:
//   1. PRESENCE — the page ships at least one top-level Dataset block.
//   2. COMPLETENESS — every Dataset object anywhere in the graph (including nested
//      ones like isBasedOn / itemReviewed / DataCatalog.dataset[]) carries the fields
//      Google Search Console requires: name + description (critical). A bare nested
//      `{@type:Dataset,@id}` is exactly what tripped GSC, so we walk the whole graph.
// Event indexes use DataCatalog, not Dataset, so only per-slug detail pages are scanned.
import { readFile, readdir } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import { join } from 'node:path';

const DIST = fileURLToPath(new URL('../dist/', import.meta.url));
const REQUIRED = ['name', 'description']; // critical GSC fields

function* datasetsIn(node, path = '$') {
  if (Array.isArray(node)) {
    for (let i = 0; i < node.length; i++) yield* datasetsIn(node[i], `${path}[${i}]`);
  } else if (node && typeof node === 'object') {
    if (node['@type'] === 'Dataset') yield { obj: node, path };
    for (const [k, v] of Object.entries(node)) if (k !== '@type') yield* datasetsIn(v, `${path}.${k}`);
  }
}

async function detailPages(base) {
  let entries;
  try { entries = await readdir(base, { withFileTypes: true }); } catch { return []; }
  return entries.filter((e) => e.isDirectory()).map((e) => join(base, e.name, 'index.html'));
}

async function check(label, base) {
  const files = await detailPages(base);
  let scanned = 0;
  const problems = [];
  for (const f of files) {
    let html;
    try { html = await readFile(f, 'utf8'); } catch { continue; }
    scanned++;
    const blocks = [...html.matchAll(/<script type="application\/ld\+json">(.*?)<\/script>/gs)];
    let topDataset = false;
    for (const m of blocks) {
      let obj;
      try { obj = JSON.parse(m[1]); } catch { problems.push(`${f}: unparseable JSON-LD`); continue; }
      if (obj['@type'] === 'Dataset') topDataset = true;
      for (const { obj: ds, path } of datasetsIn(obj)) {
        const missing = REQUIRED.filter((field) => !ds[field]);
        if (missing.length) problems.push(`${f} ${path}: Dataset missing ${missing.join(', ')}`);
      }
    }
    if (!topDataset) problems.push(`${f}: no top-level Dataset block`);
  }
  return { label, scanned, problems };
}

let failed = false;
for (const [label, sub] of [['events', 'events'], ['signals', 'signals']]) {
  const { scanned, problems } = await check(label, join(DIST, sub));
  if (scanned === 0) { console.warn(`! ${label}: no detail pages under dist/${sub}/ (skipped)`); continue; }
  if (problems.length) {
    failed = true;
    console.error(`✗ ${label}: ${problems.length} issue(s) across ${scanned} pages`);
    problems.slice(0, 6).forEach((p) => console.error(`    ${p}`));
    if (problems.length > 6) console.error(`    ...and ${problems.length - 6} more`);
  } else {
    console.log(`✓ ${label}: all ${scanned} pages — every Dataset (incl. nested) has name + description`);
  }
}

if (failed) { console.error('check-jsonld FAILED — Dataset structured data incomplete. Build gated.'); process.exit(1); }
console.log('check-jsonld passed');
