# ClearMarket — Deploy Runbook

Practical procedures for shipping changes live. Read this before any deploy from a fresh terminal.

## Architecture (what serves what)

| Surface | Hosting | How it deploys |
|---|---|---|
| **Site** `clearmarket.fyi` | Cloudflare **Pages** project `clearmarket` | **Direct-upload — NOT git-connected.** `wrangler pages deploy web/dist`. A git push does **not** update it. |
| **API** `api.clearmarket.fyi/v1/*` + **MCP** `/mcp` | Cloudflare **Worker** `clearmarket-api` | `cd api && npx wrangler deploy` |
| **DB** | Cloudflare **D1** | reseed via `cd api && npm run seed:remote` (drops+recreates events/markets/resolution_log from the bundle; api_keys/usage/call_log/marks_daily persist) |
| **Data bundle** | Cloudflare **R2** bucket `cm-data` | `wrangler r2 object put cm-data/<file> --file web/data/<file> --remote`. Public base: `https://pub-44522f32bfd047a386a961f5a624fd6f.r2.dev` |

**Prereqs:** Node 22 — `export PATH="/usr/local/opt/node@22/bin:$PATH"` (default node is 20; wrangler needs 22). Cloudflare creds live in repo `.env` (`CLOUDFLARE_API_TOKEN`, `CLOUDFLARE_ACCOUNT_ID`, `ANTHROPIC_API_KEY`, …): `set -a; . ./.env; set +a`.

## The two revert-traps (READ THIS)

The daily cron `cm-signal-daily.yml` (08:00 UTC) **rebuilds the entire static site** from (a) the **committed source** on `main` and (b) the **R2 data bundle**, then redeploys Pages. So:

1. **Commit + push any source change** (`.astro`/`.ts`/`.css`/generators) **or the next cron reverts it.**
2. **Any data fix must land in the R2 bundle** (`cm-data/universe-enriched-linked.json`) **or the next cron reverts it** — editing only the local bundle and deploying is not enough.

`web/data/*.json` is **gitignored** (the 42MB bundle, resolution-log.json, canon-pairs.json). The live data source of truth is **R2**, not git, not your local disk.

## Procedure A — ship a STATIC change (template/CSS/page) without shipping local WIP data

Your local `web/data/` bundle is usually Jeremy's in-progress re-enrichment (a *different*, newer dataset than what's live). To deploy a code change against **live** data:

```bash
cd ~/Git/clearmarket
export PATH="/usr/local/opt/node@22/bin:$PATH"
set -a; . ./.env; set +a
BASE="https://pub-44522f32bfd047a386a961f5a624fd6f.r2.dev"

# 1. back up local WIP data (gitignored, but don't lose it)
for f in universe-enriched-linked resolution-log canon-pairs; do
  cp web/data/$f.json web/data/$f.LOCAL-WIP.bak.json 2>/dev/null || true; done

# 2. fetch the LIVE bundle from R2 so the build uses live data
curl -fsSL "$BASE/universe-enriched-linked.json" -o web/data/universe-enriched-linked.json
curl -fsSL "$BASE/canon-pairs.json"             -o web/data/canon-pairs.json
curl -fsSL "$BASE/resolution-log.json"          -o web/data/resolution-log.json

# 3. build + deploy
( cd web && npm run build )
npx wrangler pages deploy web/dist --project-name=clearmarket --branch=main --commit-dirty=true

# 4. restore local WIP
for f in universe-enriched-linked resolution-log canon-pairs; do
  mv -f web/data/$f.LOCAL-WIP.bak.json web/data/$f.json 2>/dev/null || true; done

# 5. commit + push the source change (so the cron doesn't revert it)
git add <changed source files>; git commit; git push origin main
```

## Procedure B — ship a DATA fix (must update R2, or the cron reverts it)

Patch the bundle, validate, re-upload to R2, then redeploy the static site (Procedure A from step 3, using the patched bundle). Keep a backup of the R2 original for rollback.

```bash
# fetch live R2 bundle + keep a rollback copy
curl -fsSL "$BASE/universe-enriched-linked.json" -o web/data/universe-enriched-linked.json
cp web/data/universe-enriched-linked.json web/data/universe-enriched-linked.R2-ORIG.bak.json
# ...run your patch script (e.g. python3 retitle_multidate_events.py)...
# validate counts + JSON before upload (events/markets unchanged, ids in order), then:
npx wrangler r2 object put cm-data/universe-enriched-linked.json \
  --file=web/data/universe-enriched-linked.json --remote
# then build + pages deploy (Procedure A steps 3+), and reseed D1 if the API must match (Procedure C)
```

Rollback: re-`put` the `.R2-ORIG.bak.json` copy.

## Procedure C — ship an API / Worker change

```bash
cd ~/Git/clearmarket/api
export PATH="/usr/local/opt/node@22/bin:$PATH"; set -a; . ../.env; set +a
npm run export            # regenerate seed.sql/schema.sql from web/data bundle (use the LIVE bundle)
npm run seed:remote       # reseed D1 (drops+recreates events/markets/resolution_log; ops tables persist)
npx wrangler deploy       # deploy the Worker
```

Worker code is defensive where it reads not-yet-seeded tables (e.g. `resolution_log` returns `[]` until the reseed), so the Worker can ship ahead of the reseed without 500-ing.

## Full re-enrichment (monthly) — regenerate the bundle from scratch

`build-data.sh` is the canonical chain (runs on a FRESH enriched+linked bundle, NOT a patched one):
`fix_questions → retitle_multidate_events → patch_ladders → patch_sources → merge_canon → export D1 → build site`.
Then upload the rebuilt bundle + `canon-pairs.json` + `resolution-log.json` to R2 (Procedure B upload), reseed D1 (Procedure C), `wrangler deploy`, `pages deploy`. See `now.md` "Monthly re-enrich" for the pull→enrich→unify→link→filter_stale→build_resolution_log front half.

## Verify live

```bash
curl -fsSL https://clearmarket.fyi/events/<slug>/ | grep -oE "<h1[^>]*>[^<]+"   # title/render
curl -fsSL https://clearmarket.fyi/events/<slug>.json | python3 -m json.tool | head   # parallel JSON
curl -fsSL https://api.clearmarket.fyi/health                                   # API up + counts
```
(The IPv6-only apex isn't reachable from some sandboxes; the `clearmarket-1dg.pages.dev` mirror works for audits.)
