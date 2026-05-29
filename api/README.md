# ClearMarket API

Cloudflare Worker serving the enriched prediction-market reference dataset from D1.

**Live:** https://clearmarket-api.jeremyd2255.workers.dev
**Deployed:** 2026-05-27. Worker `clearmarket-api`, D1 db `clearmarket` (id `03c1760a-9a99-49b1-b388-6f118d7c31fb`).

## Build env (IMPORTANT)
Wrangler needs **Node ≥ 22**; the machine's default `node` is v20. Use the brew keg-only build:

```sh
export PATH="/usr/local/opt/node@22/bin:$PATH"
```

Prepend that to PATH for every `wrangler`/`npx` call below. Cloudflare auth is already done
(`wrangler login`, OAuth creds in `~/Library/Preferences/.wrangler` — no API token in `.env`).

## Endpoints
| Method | Path | Notes |
|---|---|---|
| GET | `/health` | counts + doc string |
| GET | `/v1/events` | filters: `category`, `platform`, `grade`, `q`, `limit`, `offset` |
| GET | `/v1/events/:slug` | full event + its markets |
| GET | `/v1/markets/:id` | single market (`CM-MKT-######`) |
| POST | `/v1/keys` | `{ "email": "..." }` → issues a free key |

**Auth (Option 3):** 3 demo events are public no-auth (`when-will-bitcoin-hit-150k`,
`strait-of-hormuz-traffic-returns-to-normal-by-end-of-may`, `kxlayoffsyinfo-26`). Everything else
needs a free key, sent as `Authorization: Bearer <key>` or `?key=<key>`. Limit 1,000 calls/day/key.

## Data source & refresh
Serving store is **D1** (not R2 — see now.md storage-decision note). Data is a point-in-time load
from the enriched bundle. To refresh after a new enrichment run:

```sh
cd api
node scripts/export-d1.mjs            # regenerates seed/{schema,seed,meta}.sql from web/data/universe-enriched-full.json
export PATH="/usr/local/opt/node@22/bin:$PATH"
npx wrangler d1 execute clearmarket --remote --file=seed/schema.sql   # drops + recreates events/markets, keeps api_keys/usage
npx wrangler d1 execute clearmarket --remote --file=seed/seed.sql     # bulk load (statements byte-bounded < 60KB for D1's 100KB cap)
```

Seed SQL (`seed/*.sql`, ~32MB) is gitignored — regenerable from the bundle.

## Deploy
```sh
cd api && export PATH="/usr/local/opt/node@22/bin:$PATH" && npx wrangler deploy
```

## Not yet built (next sessions)
- Hourly marks-refresh cron (credibility floor per locked decision #16).
- `api.clearmarket.fyi` custom domain (needs clearmarket.fyi on Cloudflare DNS).
- Bulk dataset-export object in R2.
- Catalyst + CM Signal endpoints (separate pipelines).
