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

**If the Worker writes a NEW column, apply its migration BEFORE `wrangler deploy`** — the live tables won't
have the column until then, and the cron's `UPDATE` will throw "no such column" and silently stall. e.g.:
```bash
cd api && wrangler d1 execute clearmarket --remote --file=zombie-cols-migration.sql   # last_updated_at, reconciled_at, from_value (run from api/)
```
Freshness migration (2026-09-17): `cd api && wrangler d1 execute clearmarket --remote --file=freshness-migration.sql` — adds
`markets.last_checked_at`, `marks_daily.price_as_of/carried_forward`, and the `cron_runs` + `feed_meta` tables. The Worker's
daily 15:00 UTC step applies the site-side sweep (`status-sweep-latest.json`) and screen (`eligibility-ciro-26-0076*.json`)
files from R2 into D1, so a reseed is no longer the only path from bundle to API. (15:00 because GitHub schedules on this repo start
~5 hours late: the 06:30 sweep runs ≈12:00Z and the 08:00 screen ≈13:00Z — check `gh run list` before moving it.)
Kalshi prices come from `kalshi-marks.yml` (GitHub runner, hourly) via `kalshi-tracked-latest.json` in R2 because Kalshi 429s
Cloudflare egress; rows are stamped with the snapshot's own time. Operator trigger for any step:
`POST /v1/admin/run?step=sweep_apply|screen_apply|marks|snapshot` with `Authorization: Bearer $ADMIN_TOKEN` (Worker secret).
Feed health: `GET /v1/status`; hourly GitHub check `status-check.yml` fails (and emails) when a core pipeline is stale.

**ALTER-only deploys: do NOT run `npm run seed:remote`.** A reseed drops+recreates `markets` from the bundle,
which clobbers the cron-fresh `last_price`/`volume`/`status` in D1 with the (older) bundle snapshot. For a
Worker-logic + new-column change (like the zombie fix), the steps are just: apply the migration, then
`wrangler deploy`. Reseed only when you have a genuinely newer bundle to ship.

Worker code is defensive where it reads not-yet-seeded tables (e.g. `resolution_log` returns `[]` until the reseed), so the Worker can ship ahead of the reseed without 500-ing.

## Full re-enrichment (monthly) — regenerate the bundle from scratch

After unify/link, run `./reconcile-bundle.sh` (REQUIRED — the step that used to get forgotten): it runs
`settle_status_sweep.py` (re-marks carried markets the venue has settled/delisted) then
`build_resolution_log.py`. Skip it and the bundle re-ships the "zombie" markets (status='open', frozen
price) the union carried verbatim. Kept out of `build-data.sh` because the sweep makes ~thousands of
venue calls (~10 min) — a plain site rebuild shouldn't trigger it.

`build-data.sh` is the canonical chain (runs on a FRESH, reconciled, enriched+linked bundle, NOT a patched one):
`fix_questions → retitle_multidate_events → patch_ladders → patch_sources → merge_canon → export D1 → build site`.
Then upload the rebuilt bundle + `canon-pairs.json` + `resolution-log.json` to R2 (Procedure B upload), reseed D1 (Procedure C), `wrangler deploy`, `pages deploy`. See `now.md` "Monthly re-enrich" for the pull→enrich→unify→link→filter_stale→reconcile-bundle→build_resolution_log front half.

Note: the live data layer also self-heals daily — the Worker's `reconcileStatus` cron (06:00 UTC) flips
zombies to resolved/closed in D1 between re-enrichments. The monthly sweep is the comprehensive/backlog
pass + the only one that reaches the static event pages (which render from the bundle, not D1).

## Verify live

```bash
curl -fsSL https://clearmarket.fyi/events/<slug>/ | grep -oE "<h1[^>]*>[^<]+"   # title/render
curl -fsSL https://clearmarket.fyi/events/<slug>.json | python3 -m json.tool | head   # parallel JSON
curl -fsSL https://api.clearmarket.fyi/health                                   # API up + counts
```
(The IPv6-only apex isn't reachable from some sandboxes; the `clearmarket-1dg.pages.dev` mirror works for audits.)
