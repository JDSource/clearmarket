/**
 * ClearMarket API — Cloudflare Worker.
 * Serves the enriched prediction-market reference dataset from D1.
 *
 * Endpoints:
 *   GET  /health
 *   GET  /v1/events            list + filter (category, platform, grade, q, limit, offset)
 *   GET  /v1/events/:slug      full event + its markets
 *   GET  /v1/markets/:id       single market
 *   POST /v1/keys              { email } -> issues a free API key
 *
 * Auth (Option 3): demo events are public no-auth; everything else needs a
 * free key (Authorization: Bearer <key>, or ?key=). 1,000 calls/day per key.
 */

import { handleMcp } from './mcp';

export interface Env {
  DB: D1Database;
}

const CORS = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
  'Access-Control-Allow-Headers': 'Authorization, Content-Type',
};

const json = (data: unknown, status = 200, extra: Record<string, string> = {}) =>
  new Response(JSON.stringify(data, null, 2), {
    status,
    headers: { 'Content-Type': 'application/json; charset=utf-8', ...CORS, ...extra },
  });

const err = (status: number, message: string, hint?: string) =>
  json({ error: message, ...(hint ? { hint } : {}) }, status);

// ---- serving shapes ----------------------------------------------------
export const num = (v: unknown) => (v === null || v === undefined ? null : Number(v));
export const parseJson = (v: unknown, fallback: unknown) => {
  if (v === null || v === undefined) return fallback;
  try { return JSON.parse(v as string); } catch { return fallback; }
};

export function marketOut(m: any) {
  return {
    market_id: m.market_id,
    event_id: m.event_id,
    platform: m.platform,
    platform_market_id: m.platform_market_id,
    question: m.question_raw,
    description: m.description_raw,
    contract_type: m.contract_type,
    settlement_currency: m.settlement_currency,
    underlying_reference: m.underlying_reference,
    close_at: m.close_at,
    resolve_at: m.resolve_at,
    status: m.status,
    resolution: {
      rules_raw: m.resolution_rules_raw,
      arbitration_model: m.arbitration_model,
      proposer: m.resolution_proposer,
      source: m.resolution_source,
      source_citation: m.source_citation,
      source_type: m.resolution_source_type,
      source_quality: m.resolution_source_quality,
    },
    rcg: {
      grade: m.resolution_clarity_grade,
      score: num(m.rcg_score),
      caps: parseJson(m.rcg_caps, []),
      applied_factors: num(m.rcg_applied_factors),
    },
    last_price: num(m.last_price),
    implied_probability: num(m.last_price),
    volume_24h_usd: num(m.volume_24h_usd),
    volume_total_usd: num(m.volume_total_usd),
    settlement_style: m.settlement_style ?? null,
    direction: m.direction ?? null,
    threshold: num(m.threshold),
    claim_sig: m.claim_sig ?? null,    // cross-venue link: markets sharing claim_sig are the same claim
    tags: parseJson(m.tags, []),
  };
}

export function eventSummary(e: any, mkts: any[]) {
  const venues = [...new Set(mkts.map((m) => m.platform))].sort();
  const primary = mkts.find((m) => m.market_id === e.primary_market_id) ?? null;
  return {
    event_id: e.event_id,
    slug: e.slug,
    question: e.question,
    category: e.category,
    event_type: e.event_type ?? 'BINARY',
    tags: parseJson(e.tags, []),
    venues_covered: venues,
    market_count: mkts.length,
    primary_market_id: e.primary_market_id,
    grade: primary?.resolution_clarity_grade ?? null,
    rcg_score: num(primary?.rcg_score),
    last_price: num(primary?.last_price),
    updated_at: e.updated_at,
  };
}

// ---- catalysts: read-time join -----------------------------------------
// Catalysts are NOT stored denormalized per event. Each event carries catalyst_types
// (pointers like "cpi","fomc","earnings:NVDA"); the shared catalyst_calendar holds the
// dates per type. We join + window (strictly before the event's resolution) at read-time,
// so the set is always fresh as the calendar rolls forward. Bespoke per-event catalysts
// (Exa/FDA) live in events.catalyst_dates and are merged in.
export type CalEntry = { label: string; source_url: string; dates: string[] };

export async function loadCalendar(env: Env): Promise<Map<string, CalEntry>> {
  const { results } = await env.DB.prepare(
    'SELECT type, label, source_url, dates FROM catalyst_calendar'
  ).all<{ type: string; label: string; source_url: string; dates: string }>();
  const m = new Map<string, CalEntry>();
  for (const r of results) m.set(r.type, { label: r.label, source_url: r.source_url, dates: parseJson(r.dates, []) as string[] });
  return m;
}

// Expand types -> dated catalysts before `cutoff`, merge bespoke, dedupe by (date,type), soonest 5.
export function windowCatalysts(types: string[], cal: Map<string, CalEntry>, cutoff: string | null, bespoke: any[]): any[] {
  const out: any[] = [];
  if (cutoff) {
    for (const t of types) {
      const c = cal.get(t);
      if (!c) continue;
      for (const d of c.dates) {
        if (d < cutoff) out.push({ date: d, type: t, label: c.label, source_url: c.source_url });
      }
    }
  }
  for (const b of bespoke) out.push(b); // bespoke entries already dated; not cutoff-filtered (Exa stores in-window)
  const seen = new Set<string>();
  const deduped = out.filter((c) => {
    const k = `${c.date}|${c.type}`;
    return seen.has(k) ? false : (seen.add(k), true);
  });
  deduped.sort((a, b) => (a.date < b.date ? -1 : a.date > b.date ? 1 : 0));
  return deduped.slice(0, 5);
}

// ---- auth --------------------------------------------------------------
type Auth = { keyed: boolean; key?: string };

function readKey(req: Request, url: URL): string | null {
  const h = req.headers.get('Authorization');
  if (h?.startsWith('Bearer ')) return h.slice(7).trim();
  return url.searchParams.get('key');
}

// Open by default: the full universe is served with NO key (agent-first adoption). A key is an
// OPTIONAL upgrade for higher limits (+ it tells us who's interested). Limits are app-level throttles,
// not provisioned resources; the real ceiling is Cloudflare's free tier (~100k Worker req/day total).
const ANON_DAILY_LIMIT = 1000;   // per IP, no key
const KEY_DAILY_LIMIT = 10000;   // per free key

async function bumpUsage(env: Env, id: string, day: string): Promise<number> {
  const used = await env.DB.prepare(
    'INSERT INTO usage (key, day, count) VALUES (?, ?, 1) ON CONFLICT(key, day) DO UPDATE SET count = count + 1 RETURNING count'
  ).bind(id, day).first<{ count: number }>();
  return used?.count ?? 0;
}

async function authenticate(env: Env, req: Request, url: URL): Promise<Auth | Response> {
  const day = new Date().toISOString().slice(0, 10);
  const key = readKey(req, url);

  if (!key) {
    // anonymous: full access, throttled per IP so one actor can't drain the global budget
    const ip = req.headers.get('CF-Connecting-IP') ?? 'unknown';
    const count = await bumpUsage(env, `ip:${ip}`, day);
    if (count > ANON_DAILY_LIMIT) {
      return err(429, `Anonymous rate limit exceeded (${ANON_DAILY_LIMIT}/day).`,
        `Grab a free key for ${KEY_DAILY_LIMIT}/day: POST /v1/keys { "email": "you@firm.com" }`);
    }
    return { keyed: false };
  }

  const row = await env.DB.prepare(
    'SELECT key, daily_limit FROM api_keys WHERE key = ? AND revoked = 0'
  ).bind(key).first<{ key: string; daily_limit: number }>();
  if (!row) return err(401, 'Invalid API key', 'Omit the key for anonymous access, or request one: POST /v1/keys { "email": "you@firm.com" }');
  const count = await bumpUsage(env, key, day);
  if (count > row.daily_limit) {
    return err(429, 'Daily rate limit exceeded', `Limit is ${row.daily_limit} calls/day. Resets 00:00 UTC.`);
  }
  return { keyed: true, key };
}

// ---- handlers ----------------------------------------------------------
async function listEvents(env: Env, url: URL, auth: Auth): Promise<Response> {
  const p = url.searchParams;
  const where: string[] = ['e.published = 1'];
  const args: unknown[] = [];
  if (p.get('category')) { where.push('e.category = ?'); args.push(p.get('category')); }
  if (p.get('q')) { where.push('e.question LIKE ?'); args.push(`%${p.get('q')}%`); }

  const limit = Math.min(Number(p.get('limit') ?? 50) || 50, 200);
  const offset = Math.max(Number(p.get('offset') ?? 0) || 0, 0);
  const sql = `SELECT * FROM events e WHERE ${where.join(' AND ')} ORDER BY e.updated_at DESC LIMIT ? OFFSET ?`;
  const { results: evs } = await env.DB.prepare(sql).bind(...args, limit, offset).all<any>();

  if (!evs.length) return json({ count: 0, limit, offset, keyed: auth.keyed, events: [] });

  // pull markets for this page in one query
  const ids = evs.map((e) => e.event_id);
  const ph = ids.map(() => '?').join(',');
  const { results: mkts } = await env.DB.prepare(
    `SELECT market_id, event_id, platform, last_price, resolution_clarity_grade, rcg_score FROM markets WHERE event_id IN (${ph})`
  ).bind(...ids).all<any>();
  const byEvent = new Map<string, any[]>();
  for (const m of mkts) (byEvent.get(m.event_id) ?? byEvent.set(m.event_id, []).get(m.event_id)!).push(m);

  // optional platform/grade filters applied post-rollup
  let out = evs.map((e) => eventSummary(e, byEvent.get(e.event_id) ?? []));
  if (p.get('platform')) out = out.filter((e) => e.venues_covered.includes(p.get('platform')!));
  if (p.get('grade')) out = out.filter((e) => e.grade === p.get('grade'));

  return json({
    count: out.length,
    limit,
    offset,
    keyed: auth.keyed,
    ...(auth.keyed ? {} : { notice: `Anonymous access (full universe, ${ANON_DAILY_LIMIT}/day per IP). Free key for ${KEY_DAILY_LIMIT}/day: POST /v1/keys.` }),
    events: out,
  });
}

async function getEvent(env: Env, slug: string, auth: Auth): Promise<Response> {
  const e = await env.DB.prepare('SELECT * FROM events WHERE slug = ? AND published = 1').bind(slug).first<any>();
  if (!e) return err(404, 'Event not found');
  const { results: mkts } = await env.DB.prepare('SELECT * FROM markets WHERE event_id = ?').bind(e.event_id).all<any>();
  const venues = [...new Set(mkts.map((m) => m.platform))].sort();
  const primary = mkts.find((m) => m.market_id === e.primary_market_id) ?? null;

  // catalysts: join catalyst_types against the shared calendar + merge bespoke, windowed by resolution
  const cutoff = mkts.reduce<string | null>((max, m) => {
    const d = (m.close_at ?? '').slice(0, 10);
    return d && (!max || d > max) ? d : max;
  }, null);
  const cal = await loadCalendar(env);
  const catalysts = windowCatalysts(
    parseJson(e.catalyst_types, []) as string[],
    cal,
    cutoff,
    parseJson(e.catalyst_dates, []) as any[],
  );

  return json({
    event_id: e.event_id,
    slug: e.slug,
    question: e.question,
    category: e.category,
    event_type: e.event_type ?? 'BINARY',
    ladder_distribution: parseJson(e.ladder_distribution, null),
    tags: parseJson(e.tags, []),
    catalyst_types: parseJson(e.catalyst_types, []),
    catalyst_dates: catalysts,
    editorial_notes: e.editorial_notes,
    venues_covered: venues,
    primary_market_id: e.primary_market_id,
    current_primary_mark: primary ? { last_price: num(primary.last_price), implied_probability: num(primary.last_price) } : null,
    created_at: e.created_at,
    updated_at: e.updated_at,
    markets: mkts.map(marketOut),
  });
}

async function getMarket(env: Env, id: string, _auth: Auth): Promise<Response> {
  const m = await env.DB.prepare('SELECT * FROM markets WHERE market_id = ?').bind(id).first<any>();
  if (!m) return err(404, 'Market not found');
  return json(marketOut(m));
}

// Cross-event view: every scheduled catalyst in the next N days, across the whole calendar.
// Public (shared reference data, no per-event linkage). The query the old per-event arrays couldn't answer.
async function upcomingCatalysts(env: Env, url: URL): Promise<Response> {
  const days = Math.min(Math.max(Number(url.searchParams.get('days') ?? 30) || 30, 1), 365);
  const today = new Date().toISOString().slice(0, 10);
  const until = new Date(Date.now() + days * 864e5).toISOString().slice(0, 10);
  const cal = await loadCalendar(env);
  const items: any[] = [];
  for (const [type, c] of cal) {
    for (const d of c.dates) {
      if (d >= today && d <= until) items.push({ date: d, type, label: c.label, source_url: c.source_url });
    }
  }
  items.sort((a, b) => (a.date < b.date ? -1 : a.date > b.date ? 1 : 0));
  return json({ window_days: days, from: today, to: until, count: items.length, catalysts: items });
}

async function createKey(env: Env, req: Request): Promise<Response> {
  let body: any;
  try { body = await req.json(); } catch { return err(400, 'Body must be JSON: { "email": "you@firm.com" }'); }
  const email = (body?.email ?? '').toString().trim();
  if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) return err(400, 'A valid email is required');
  const key = 'cm_' + crypto.randomUUID().replace(/-/g, '');
  await env.DB.prepare('INSERT INTO api_keys (key, email, created_at, daily_limit) VALUES (?, ?, ?, ?)')
    .bind(key, email, new Date().toISOString(), KEY_DAILY_LIMIT).run();
  return json({ key, email, daily_limit: KEY_DAILY_LIMIT, usage: 'Optional — anonymous access works too. Send as `Authorization: Bearer <key>` or ?key=<key> for the higher limit.' }, 201);
}

// ---- marks cron (hourly) -----------------------------------------------
// Keeps prices fresh — the credibility floor. Scoped to cross-venue-linked + each event's
// primary market (~2.7k rows) to stay inside D1 free-tier writes. No marks-history table:
// its only consumer was divergence, which is parked. UPDATE current last_price only.
const KALSHI_BASE = 'https://api.elections.kalshi.com/trade-api/v2';
const POLY_GAMMA = 'https://gamma-api.polymarket.com';

async function refreshMarks(env: Env): Promise<void> {
  const { results } = await env.DB.prepare(
    `SELECT market_id, platform_market_id FROM markets
     WHERE platform_market_id IS NOT NULL
       AND (claim_sig IS NOT NULL
            OR market_id IN (SELECT primary_market_id FROM events WHERE primary_market_id IS NOT NULL))`
  ).all<{ market_id: string; platform_market_id: string }>();
  const want = new Map<string, string>();
  for (const r of results) want.set(r.platform_market_id, r.market_id);
  if (!want.size) return;

  const fresh = new Map<string, number>();

  // Kalshi: paginate open events with nested markets
  let cursor: string | undefined;
  for (let i = 0; i < 40; i++) {
    const u = new URL(`${KALSHI_BASE}/events`);
    u.searchParams.set('with_nested_markets', 'true');
    u.searchParams.set('status', 'open');
    u.searchParams.set('limit', '200');
    if (cursor) u.searchParams.set('cursor', cursor);
    const d: any = await (await fetch(u.toString(), { headers: { 'User-Agent': 'clearmarket-marks/0.1' } })).json();
    for (const ev of d.events ?? [])
      for (const m of ev.markets ?? [])
        if (want.has(m.ticker) && m.last_price_dollars != null) fresh.set(m.ticker, Number(m.last_price_dollars));
    cursor = d.cursor;
    if (!cursor) break;
  }

  // Polymarket: paginate open Gamma events
  let offset = 0;
  for (let i = 0; i < 80; i++) {
    const u = new URL(`${POLY_GAMMA}/events`);
    u.searchParams.set('closed', 'false');
    u.searchParams.set('limit', '100');
    u.searchParams.set('offset', String(offset));
    const b: any = await (await fetch(u.toString())).json();
    if (!Array.isArray(b)) break;
    for (const ev of b)
      for (const m of ev.markets ?? [])
        if (want.has(m.conditionId) && m.lastTradePrice != null) fresh.set(m.conditionId, Number(m.lastTradePrice));
    offset += 100;
    if (b.length < 100) break;
  }

  const stmts: D1PreparedStatement[] = [];
  for (const [pmid, mid] of want) {
    const p = fresh.get(pmid);
    if (p == null) continue;
    stmts.push(env.DB.prepare('UPDATE markets SET last_price = ? WHERE market_id = ?').bind(p, mid));
  }
  for (let i = 0; i < stmts.length; i += 100) await env.DB.batch(stmts.slice(i, i + 100));
  console.log(`marks refresh: ${stmts.length}/${want.size} linked+primary markets updated`);
}

// ---- crypto spot (free, keyless CoinGecko — underlying context for crypto price markets) ----
const COINGECKO = 'https://api.coingecko.com/api/v3/simple/price';
const SPOT_COINS = 'bitcoin,ethereum,solana,ripple,dogecoin,cardano';

async function refreshSpot(env: Env): Promise<void> {
  const r = await fetch(`${COINGECKO}?ids=${SPOT_COINS}&vs_currencies=usd`, { headers: { 'User-Agent': 'clearmarket/0.1' } });
  if (!r.ok) return;
  const d: any = await r.json();
  const now = new Date().toISOString();
  const stmts: D1PreparedStatement[] = [];
  for (const [coin, obj] of Object.entries(d)) {
    const p = (obj as any)?.usd;
    if (p == null) continue;
    stmts.push(env.DB.prepare(
      'INSERT INTO spot (coin, price_usd, as_of) VALUES (?,?,?) ON CONFLICT(coin) DO UPDATE SET price_usd=?, as_of=?'
    ).bind(coin, p, now, p, now));
  }
  if (stmts.length) await env.DB.batch(stmts);
}

// ---- end-of-day history snapshot --------------------------------------
// Appends one row per refreshed market to marks_daily (the daily time-series). Runs once a
// day at the EOD cron hour, AFTER refreshMarks, so it captures the day's freshest prices.
// Scoped to the same linked+primary set the marks cron refreshes (others have stale last_price).
const EOD_UTC_HOUR = 21; // ~5pm EDT / 4pm EST — end of the US day

async function snapshotDaily(env: Env): Promise<void> {
  const day = new Date().toISOString().slice(0, 10);
  const now = new Date().toISOString();
  const res = await env.DB.prepare(
    `INSERT INTO marks_daily (market_id, day, last_price, volume_24h_usd, volume_total_usd, captured_at)
     SELECT market_id, ?, last_price, volume_24h_usd, volume_total_usd, ?
       FROM markets
      WHERE last_price IS NOT NULL
        AND (claim_sig IS NOT NULL
             OR market_id IN (SELECT primary_market_id FROM events WHERE primary_market_id IS NOT NULL))
     ON CONFLICT(market_id, day) DO UPDATE SET
        last_price = excluded.last_price,
        volume_24h_usd = excluded.volume_24h_usd,
        volume_total_usd = excluded.volume_total_usd,
        captured_at = excluded.captured_at`
  ).bind(day, now).run();
  console.log(`marks_daily snapshot ${day}: ${res.meta?.changes ?? '?'} rows`);
}

// ---- router ------------------------------------------------------------
export default {
  async fetch(req: Request, env: Env): Promise<Response> {
    const url = new URL(req.url);
    const path = url.pathname.replace(/\/+$/, '') || '/';

    if (req.method === 'OPTIONS') return new Response(null, { status: 204, headers: CORS });

    if (path === '/' || path === '/health') {
      const ev = await env.DB.prepare('SELECT COUNT(*) AS n FROM events').first<{ n: number }>();
      const mk = await env.DB.prepare('SELECT COUNT(*) AS n FROM markets').first<{ n: number }>();
      return json({
        service: 'clearmarket-api',
        status: 'ok',
        schema: 'v0.2.0',
        events: ev?.n ?? 0,
        markets: mk?.n ?? 0,
        docs: '/v1/events (filters: category, platform, grade, q, limit, offset). Open access; optional free key (POST /v1/keys) for higher limits. MCP at /mcp.',
      });
    }

    if (path === '/v1/spot') {
      const { results } = await env.DB.prepare('SELECT coin, price_usd, as_of FROM spot ORDER BY coin').all();
      return json({ source: 'coingecko', vs_currency: 'usd', spot: results });
    }

    if (path === '/v1/catalysts/upcoming') return upcomingCatalysts(env, url);

    if (path === '/mcp') return handleMcp(req, env);

    if (path === '/v1/keys' && req.method === 'POST') return createKey(env, req);

    if (req.method !== 'GET') return err(405, 'Method not allowed');

    const auth = await authenticate(env, req, url);
    if (auth instanceof Response) return auth;

    if (path === '/v1/events') return listEvents(env, url, auth);
    const evMatch = path.match(/^\/v1\/events\/([^/]+)$/);
    if (evMatch) return getEvent(env, decodeURIComponent(evMatch[1]), auth);
    const mkMatch = path.match(/^\/v1\/markets\/([^/]+)$/);
    if (mkMatch) return getMarket(env, decodeURIComponent(mkMatch[1]), auth);

    return err(404, 'Not found', 'Try /health or /v1/events');
  },

  // Hourly cron (0 * * * *) — refresh prices for linked + primary markets + crypto spot.
  // Once a day at EOD_UTC_HOUR, also append the daily history snapshot (after the refresh).
  async scheduled(_event: any, env: Env, ctx: any): Promise<void> {
    if (new Date().getUTCHours() === EOD_UTC_HOUR) {
      ctx.waitUntil((async () => {
        await refreshMarks(env);
        await snapshotDaily(env);
        await refreshSpot(env);
      })());
    } else {
      ctx.waitUntil(Promise.all([refreshMarks(env), refreshSpot(env)]));
    }
  },
};
