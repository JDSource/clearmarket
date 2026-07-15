/**
 * ClearMarket API — Cloudflare Worker.
 * Serves the enriched prediction-market reference dataset from D1.
 *
 * Endpoints:
 *   GET  /health
 *   GET  /v1/events            list + filter (category, platform, grade, q, limit, offset)
 *   GET  /v1/events/:slug      full event + its markets
 *   GET  /v1/markets/:id       single market
 *   GET  /v1/markets/movers    day-over-day volume movers (volume_spike signal)
 *   POST /v1/keys              { email } -> issues a free API key
 *
 * Auth (Option 3): demo events are public no-auth; everything else needs a
 * free key (Authorization: Bearer <key>, or ?key=). 1,000 calls/day per key.
 */

import { handleMcp } from './mcp';
import { AGENT_CARD, handleA2A } from './a2a';

export interface Env {
  DB: D1Database;
  // Base URL of the published static site that serves the CM Signal feed
  // (/signals.json, /signals/<slug>.json). MCP signal tools fetch from here so
  // wires stay single-sourced as static content (no D1 duplication). Defaults to prod.
  SIGNALS_BASE?: string;
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

// Valid filter values — used to validate + hint on /v1/events, and surfaced in /health for discovery.
const KNOWN_CATEGORIES = ['economics', 'financials', 'crypto', 'companies', 'technology', 'politics', 'geopolitics', 'health', 'climate'];
const KNOWN_PLATFORMS = ['kalshi', 'polymarket'];
const KNOWN_GRADES = ['A', 'B', 'C'];
// D1 caps bound parameters at 100; the per-page markets query binds one per event, so the page
// size ceiling is 100 (a larger limit overflows the IN-clause and 500s).
const MAX_PAGE = 100;

// ---- serving shapes ----------------------------------------------------
export const num = (v: unknown) => (v === null || v === undefined ? null : Number(v));
export const parseJson = (v: unknown, fallback: unknown) => {
  if (v === null || v === undefined) return fallback;
  try { return JSON.parse(v as string); } catch { return fallback; }
};

// ---- call logging ------------------------------------------------------
// One row per data request (REST or MCP): WHAT was queried (endpoint/tool + key arg),
// WHO (api key or ip), and from WHERE (country). Fire-and-forget via waitUntil so it
// never adds latency; wrapped in try/catch so a logging failure can never break a request.
export function logCall(
  env: Env,
  ctx: { waitUntil(p: Promise<any>): void },
  req: Request,
  surface: 'rest' | 'mcp' | 'a2a',
  action: string,
  target?: unknown,
): void {
  try {
    const h = req.headers.get('Authorization');
    const key = h?.startsWith('Bearer ') ? h.slice(7).trim() : null;
    const requester = key ? `key:${key}` : `ip:${req.headers.get('CF-Connecting-IP') ?? 'unknown'}`;
    const country = (req as any).cf?.country ?? null;
    const ua = req.headers.get('User-Agent') ?? null; // crawlers self-identify here (GPTBot, ClaudeBot, …)
    const tgt = target == null ? null : typeof target === 'string' ? target : JSON.stringify(target);
    ctx.waitUntil(
      env.DB.prepare('INSERT INTO call_log (ts, surface, action, target, requester, country, user_agent) VALUES (?,?,?,?,?,?,?)')
        .bind(new Date().toISOString(), surface, action, tgt, requester, country, ua).run(),
    );
  } catch { /* logging must never break a request */ }
}

// ---- provenance / attribution watermark --------------------------------
// Stamped on every event + market in API and MCP responses. Triple duty:
//  (1) attribution notice / licensing terms,
//  (2) scrape watermark — `ref` is a CM id that exists only in ClearMarket's
//      namespace, so if it surfaces downstream it's provable origin,
//  (3) names the canonical id as the citation unit (adopters propagate it).
// Applied at serve time — no dataset rewrite.
export const provenance = (ref: string) => ({
  source: 'clearmarket.fyi',
  ref,
  terms: 'Attribution required. clearmarket.fyi',
});

// ---- free-key conversion notice -----------------------------------------
// One stable object on every REST data response. The `policy` line is a public
// promise: never rename, restructure, or rotate this field — a diff-watching cron
// should see it change exactly once (when it first ships). The offer is insurance,
// not a gate: anonymous access stays; keyed users get emailed (manually, from
// hello@clearmarket.fyi) before schema changes. MCP deliberately excluded — agents
// re-reading the same notice every tool call is context pollution; MCP carries the
// equivalent once in its initialize instructions.
const NOTICE = {
  type: 'free_key_offer',
  message: 'Free and anonymous access is staying. If this endpoint is in your pipeline, a free key adds advance notice before any schema change or deprecation. POST /v1/keys {"email": "you@firm.com"} — nothing else required. Something broken or missing? hello@clearmarket.fyi reaches a human.',
  docs: 'https://clearmarket.fyi/for-data/',
  policy: 'This field is additive and its shape will not change.',
};
// Movers has had one anonymous consumer pulling daily since 2026-06-05 — the
// recognition line is what makes the offer land with whoever reads that cron's log.
const MOVERS_NOTICE = { ...NOTICE, message: 'This endpoint has served a daily pull since 2026-06-05 — thanks for relying on it. ' + NOTICE.message };

export function marketOut(m: any) {
  // source_status is STAMPED at enrichment as a pure function of the LLM commitment judgment
  // (enrich_universe.enrich_event) — the serve layer reads it, never re-derives from raw field
  // presence. The fallback below exists ONLY for pre-refactor rows (seeded before 2026-07-03)
  // and checks commitment BEFORE presence, so a hedge with a non-empty verbatim source field
  // can never read platform_named. Keep in sync with web/src/lib/labels.ts sourceStatusOf().
  const source_status = m.source_status
    ?? (m.source_commitment === 'uncommitted' ? 'no_committed_source'
    : m.source_commitment === 'none' ? 'no_source_stated'
    : m.source_commitment === 'named' ? 'platform_named'
    : (m.resolution_source != null && String(m.resolution_source).trim() !== '') ? 'platform_named'
    : 'unknown');
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
      source_status,   // always present: platform_named | no_committed_source | no_source_stated | unknown
      source_citation: m.source_citation,
      // the FULL source set — every venue-listed source (provenance: platform_api) plus
      // prose-named authorities surfaced by the commitment judgment (clearmarket_editorial).
      // This is what separates "committed authority" from "menu of outlets" — visible, not
      // just baked into the grade. null on pre-refactor rows.
      sources: parseJson(m.resolution_source_list, null),
      source_of_record: m.source_of_record ?? null,   // the committed authority (grade basis)
      source_mechanism: m.source_mechanism ?? null,   // single_authority | precedence | quorum
      source_type: m.resolution_source_type,
      source_quality: m.resolution_source_quality,
      // source COMMITMENT: did the venue commit to a definitive source, or only hedge/placeholder?
      // named = concrete authority committed to; uncommitted = gestured-at but hedged
      // ("for example …") or pure placeholder ("consensus of credible reporting"); none = no source.
      source_commitment: m.source_commitment ?? null,
      source_commitment_subtype: m.source_commitment_subtype ?? null,
      source_hedge_text: m.source_hedge_text ?? null,
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
    question_id: m.question_id ?? null,  // canonical question id: markets sharing it are the same question (across venues + events)
    also_on: parseJson(m.also_on, null),  // the same question priced on other venues [{venue, market_id, price}]; null if unique to this venue
    tags: parseJson(m.tags, []),
    // Jurisdiction-specific distribution rule-set fit (e.g. ciro-26-0076): eligible / review /
    // not_eligible against ONE named rule-set. NOT market quality — quality is rcg.grade.
    eligibility_screens: parseJson(m.eligibility_screens, null),
  };
}

// Concise per-market view: a STRICT SUBSET of marketOut() — identical field names, fewer of them.
// Keeps the high-signal "can I trust this price" fields and drops the heavy prose (rules_raw,
// description) + long-tail metadata. Used by get_event(detail="concise") to keep big multi-market
// events small. Computed off marketOut() so names/shapes can never drift from the full view.
export function marketConcise(m: any) {
  const f: any = marketOut(m);
  return {
    market_id: f.market_id,
    platform: f.platform,
    question: f.question,
    last_price: f.last_price,
    implied_probability: f.implied_probability,
    status: f.status,
    rcg: { grade: f.rcg.grade, score: f.rcg.score },
    resolution: {
      arbitration_model: f.resolution.arbitration_model,
      source: f.resolution.source,
      source_status: f.resolution.source_status,
    },
    question_id: f.question_id,
    also_on: f.also_on,
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
    status: primary?.status ?? null,   // open / resolved — lets an agent filter without a get_event round-trip
    updated_at: e.updated_at,
    _provenance: provenance(e.event_id),
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
  // "live" = has at least one market still open (resolve/close in the future or unknown). Used to
  // subordinate resolved events (active first) and to support ?status filtering. Evaluated against
  // date('now') so it stays accurate continuously, not just at the last reseed.
  const liveExpr = `EXISTS (SELECT 1 FROM markets m WHERE m.event_id = e.event_id AND m.status = 'open' AND (
    (m.resolve_at IS NULL AND m.close_at IS NULL) OR COALESCE(m.resolve_at, m.close_at) >= date('now')))`;
  const status = (p.get('status') || 'all').toLowerCase();
  if (status === 'active') where.push(liveExpr);
  else if (status === 'resolved') where.push(`NOT (${liveExpr})`);
  // category match is CASE-INSENSITIVE (stored values are lowercase); an unrecognized value still
  // queries (returns []) but we hand back the valid set so a caller isn't left guessing on an empty result.
  const notices: Record<string, unknown> = {};
  if (p.get('category')) {
    const c = p.get('category')!.toLowerCase();
    where.push('LOWER(e.category) = ?'); args.push(c);
    if (!KNOWN_CATEGORIES.includes(c)) { notices.category_notice = `Unknown category "${p.get('category')}". Valid: ${KNOWN_CATEGORIES.join(', ')}.`; notices.valid_categories = KNOWN_CATEGORIES; }
  }
  // platform + grade filter IN SQL (was post-pagination, which silently returned [] when the first
  // page happened to be one venue / no A-grades). EXISTS-subquery so it filters the whole universe.
  if (p.get('platform')) {
    const v = p.get('platform')!.toLowerCase();
    // Filter the DIRECT events.venue column, NOT a correlated EXISTS on markets. The EXISTS version
    // 500'd (D1 1101): Polymarket events sort last by updated_at, so the subquery ran against ~800
    // rows before the first match and blew D1's CPU budget. A single-table column compare is cheap.
    where.push('e.venue = ?'); args.push(v);
    if (!KNOWN_PLATFORMS.includes(v)) { notices.platform_notice = `Unknown platform "${p.get('platform')}". Valid: ${KNOWN_PLATFORMS.join(', ')}.`; notices.valid_platforms = KNOWN_PLATFORMS; }
  }
  if (p.get('grade')) {
    const g = p.get('grade')!.toUpperCase();
    where.push('EXISTS (SELECT 1 FROM markets m WHERE m.market_id = e.primary_market_id AND m.resolution_clarity_grade = ?)'); args.push(g);
    if (!KNOWN_GRADES.includes(g)) { notices.grade_notice = `Unknown grade "${p.get('grade')}". Valid: ${KNOWN_GRADES.join(', ')}.`; notices.valid_grades = KNOWN_GRADES; }
  }
  // q = token-AND across question + tags (was a single contiguous-substring LIKE, so natural
  // multi-word queries like "us recession" silently returned nothing). Each whitespace token must appear.
  if (p.get('q')) {
    for (const t of p.get('q')!.trim().split(/\s+/).filter(Boolean).slice(0, 6)) {
      where.push('(e.question LIKE ? OR e.tags LIKE ?)'); args.push(`%${t}%`, `%${t}%`);
    }
  }

  const limit = Math.min(Number(p.get('limit') ?? 50) || 50, MAX_PAGE);
  if (Number(p.get('limit')) > MAX_PAGE) notices.limit_notice = `limit capped at ${MAX_PAGE} (page-size ceiling); use offset to page.`;
  const offset = Math.max(Number(p.get('offset') ?? 0) || 0, 0);
  // total = full count under the active filters (count below is just this page) so an agent knows
  // the real universe size and when to stop paging, instead of mistaking a 100-row page for "100 total".
  const totalRow = await env.DB.prepare(`SELECT COUNT(*) AS n FROM events e WHERE ${where.join(' AND ')}`).bind(...args).first<{ n: number }>();
  const total = totalRow?.n ?? 0;
  // Active events first (is_live DESC), resolved subordinate to the bottom but still returned.
  const sql = `SELECT *, (${liveExpr}) AS is_live FROM events e WHERE ${where.join(' AND ')} ORDER BY is_live DESC, e.updated_at DESC LIMIT ? OFFSET ?`;
  const { results: evs } = await env.DB.prepare(sql).bind(...args, limit, offset).all<any>();

  if (!evs.length) return json({ count: 0, total, limit, offset, keyed: auth.keyed, ...notices, _notice: NOTICE, events: [] });

  // pull markets for this page in one query
  const ids = evs.map((e) => e.event_id);
  const ph = ids.map(() => '?').join(',');
  const { results: mkts } = await env.DB.prepare(
    `SELECT market_id, event_id, platform, last_price, resolution_clarity_grade, rcg_score, status FROM markets WHERE event_id IN (${ph})`
  ).bind(...ids).all<any>();
  const byEvent = new Map<string, any[]>();
  for (const m of mkts) (byEvent.get(m.event_id) ?? byEvent.set(m.event_id, []).get(m.event_id)!).push(m);

  const out = evs.map((e) => ({ ...eventSummary(e, byEvent.get(e.event_id) ?? []), resolved: !e.is_live }));

  return json({
    count: out.length,
    total,
    limit,
    offset,
    keyed: auth.keyed,
    ...notices,
    _notice: NOTICE,
    events: out,
  });
}

async function getEvent(env: Env, slug: string, auth: Auth, detail: string = 'full'): Promise<Response> {
  const concise = detail === 'concise';
  // Accept the CM event_id as well as the slug: every list/wire surface advertises event_id,
  // so a client that follows it must not dead-end (both columns are unique-indexed lookups).
  const e = await env.DB.prepare('SELECT * FROM events WHERE (slug = ? OR event_id = ?) AND published = 1')
    .bind(slug, slug).first<any>();
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

  // Resolved-market history. Defensive: returns [] if the table hasn't been seeded yet, so the
  // Worker can ship ahead of the D1 reseed without 500-ing every event.
  let resolutionLog: any[] = [];
  try {
    const { results } = await env.DB.prepare(
      `SELECT market_id, platform, to_value, occurred_at, final_price, recorded_at, source, source_ref
         FROM resolution_log WHERE event_id = ? ORDER BY occurred_at DESC`
    ).bind(e.event_id).all<any>();
    resolutionLog = results.map((r) => ({
      market_id: r.market_id, platform: r.platform, outcome: r.to_value,
      resolved_at: r.occurred_at, final_price: num(r.final_price), recorded_at: r.recorded_at,
      source: r.source, source_ref: r.source_ref,
    }));
  } catch { resolutionLog = []; }

  return json({
    _notice: NOTICE,
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
    markets: mkts.map(concise ? marketConcise : marketOut),
    resolution_log: resolutionLog,
    _provenance: provenance(e.event_id),
  });
}

// Resolve a market by whatever id the caller has — deterministic + index-friendly:
//   1) ClearMarket id (CM-MKT-… — PK, ALWAYS wins)
//   2) venue-native market id / Kalshi ticker (platform_market_id, indexed)
//   3) best-effort: trailing segments of a URL (resolves Kalshi tickers / any native id that appears
//      in the path; Polymarket slug URLs won't match — pass the Polymarket conditionId instead).
// Two ordered point-lookups (not an OR) so market_id wins and each query uses an index.
export async function findMarketRow(env: Env, raw: string): Promise<any | null> {
  const id = (raw || '').trim();
  if (!id) return null;
  let m = await env.DB.prepare('SELECT * FROM markets WHERE market_id = ? LIMIT 1').bind(id).first<any>();
  if (!m) m = await env.DB.prepare('SELECT * FROM markets WHERE platform_market_id = ? LIMIT 1').bind(id).first<any>();
  if (!m && /[/?#]/.test(id)) {
    for (const seg of id.split(/[/?#]/).filter(Boolean).slice(-2).reverse()) {
      m = await env.DB.prepare('SELECT * FROM markets WHERE platform_market_id = ? LIMIT 1').bind(seg.trim()).first<any>();
      if (m) break;
    }
  }
  return m ?? null;
}

async function getMarket(env: Env, id: string, _auth: Auth): Promise<Response> {
  const m = await findMarketRow(env, id);
  if (!m) return err(404, 'Market not found');
  return json({ ...marketOut(m), _provenance: provenance(m.market_id), _notice: NOTICE });
}

// Volume movers: day-over-day 24h-volume change from the two most recent marks_daily snapshots.
// The deterministic signal behind volume_spike wires. Open; returns [] until >=2 days have accrued.
async function listMovers(env: Env, url: URL): Promise<Response> {
  const minMult = Math.max(Number(url.searchParams.get('min_mult') ?? 2) || 2, 1);
  const limit = Math.min(Math.max(Number(url.searchParams.get('limit') ?? 50) || 50, 1), 200);
  const { results: days } = await env.DB.prepare(
    'SELECT DISTINCT day FROM marks_daily ORDER BY day DESC LIMIT 2'
  ).all<{ day: string }>();
  if (days.length < 2) {
    return json({ metric: 'volume_24h', min_mult: minMult, count: 0, movers: [],
      notice: `Need two daily snapshots to compute a move; have ${days.length}. Series accrues nightly.` });
  }
  const [dayNow, dayPrev] = [days[0].day, days[1].day];
  // Day-over-day only: if the prior snapshot is stale (seed-era rows after a deploy, or a cron
  // outage), a fresh-vs-frozen volume ratio is a mechanical artifact, not a real move — and it would
  // feed a fake "volume spike" straight into published wires. Require near-adjacent snapshots.
  const gapDays = Math.round((Date.parse(dayNow) - Date.parse(dayPrev)) / 86400000);
  if (gapDays > 3) {
    return json({ metric: 'volume_24h', min_mult: minMult, count: 0, movers: [],
      notice: `Prior snapshot is ${gapDays} days old; a day-over-day move needs near-adjacent snapshots. Series re-accrues nightly.` });
  }
  const { results } = await env.DB.prepare(
    `SELECT t.market_id, t.last_price, t.volume_24h_usd AS vol_now, p.volume_24h_usd AS vol_prev,
            m.platform, m.question_raw, m.event_id, e.slug, e.question AS event_question, e.category
       FROM marks_daily t
       JOIN marks_daily p ON p.market_id = t.market_id AND p.day = ?
       JOIN markets m ON m.market_id = t.market_id
       JOIN events e ON e.event_id = m.event_id AND e.published = 1
      WHERE t.day = ? AND p.volume_24h_usd > 0 AND t.volume_24h_usd >= p.volume_24h_usd * ?
      ORDER BY t.volume_24h_usd / p.volume_24h_usd DESC
      LIMIT ?`
  ).bind(dayPrev, dayNow, minMult, limit).all<any>();
  const movers = results.map((r) => ({
    market_id: r.market_id, slug: r.slug, event_question: r.event_question, category: r.category,
    platform: r.platform, question_raw: r.question_raw, last_price: num(r.last_price),
    volume_24h_usd: num(r.vol_now), volume_24h_usd_prev: num(r.vol_prev),
    volume_mult: Math.round((r.vol_now / r.vol_prev) * 100) / 100,
    volume_delta_pct: Math.round(((r.vol_now - r.vol_prev) / r.vol_prev) * 1000) / 10,
  }));
  return json({ metric: 'volume_24h', day: dayNow, prior_day: dayPrev, min_mult: minMult,
    count: movers.length, _notice: MOVERS_NOTICE, movers });
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
  return json({ window_days: days, from: today, to: until, count: items.length, _notice: NOTICE, catalysts: items });
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
// Keeps prices fresh — the credibility floor. Scoped to ALL open markets (~11.5k) so no live
// market goes stale (the old linked+primary scope silently froze ~8.8k open markets). Requires
// Workers Paid for the D1 write budget; an unchanged-price guard keeps writes to actual movers,
// so a typical hour is well under the included allowance. UPDATE current last_price only.
const KALSHI_BASE = 'https://api.elections.kalshi.com/trade-api/v2';
const POLY_GAMMA = 'https://gamma-api.polymarket.com';

// Returns the set of platform_market_ids seen in the live OPEN venue feed this run, so the daily
// reconcileStatus pass can reuse the exact same snapshot (zero extra open-feed subrequests, and no
// drift between "what marks saw" and "what reconcile treats as still-listed").
async function refreshMarks(env: Env): Promise<Set<string>> {
  const { results } = await env.DB.prepare(
    `SELECT market_id, platform_market_id, last_price, volume_24h_usd, volume_total_usd FROM markets
     WHERE platform_market_id IS NOT NULL AND status = 'open'`
  ).all<{ market_id: string; platform_market_id: string; last_price: number | null; volume_24h_usd: number | null; volume_total_usd: number | null }>();
  const want = new Map<string, { mid: string; price: number | null; v24: number | null; vtot: number | null }>();
  for (const r of results) want.set(r.platform_market_id, { mid: r.market_id, price: r.last_price, v24: r.volume_24h_usd, vtot: r.volume_total_usd });
  if (!want.size) return new Set();

  type Mark = { price: number; v24: number; vtot: number };
  const fresh = new Map<string, Mark>();
  // Every tracked market the live OPEN feed returned this run (priced or not). This — NOT fresh —
  // is the "still listed" signal handed to reconcileStatus, so an open-but-untraded market (no price,
  // so absent from `fresh`) is never mistaken for delisted.
  const seenOpen = new Set<string>();

  // Kalshi: paginate open events with nested markets. Caps are a safety backstop; the whole open
  // venue universe must be scanned to cover ~11.5k tracked markets, so log if a cap is hit (tail
  // would silently get no fresh price). Subrequest budget is fine on Workers Paid.
  let cursor: string | undefined;
  let kHitCap = true;
  for (let i = 0; i < 300; i++) {
    const u = new URL(`${KALSHI_BASE}/events`);
    u.searchParams.set('with_nested_markets', 'true');
    u.searchParams.set('status', 'open');
    u.searchParams.set('limit', '200');
    if (cursor) u.searchParams.set('cursor', cursor);
    const d: any = await (await fetch(u.toString(), { headers: { 'User-Agent': 'clearmarket-marks/0.1' } })).json();
    for (const ev of d.events ?? [])
      for (const m of ev.markets ?? [])
        if (want.has(m.ticker)) {
          seenOpen.add(m.ticker);
          if (m.last_price_dollars != null) {
            const px = Number(m.last_price_dollars);
            // Kalshi volume is in contracts; approximate USD via current price (matches the generators' live_refresh).
            fresh.set(m.ticker, { price: px, v24: Number(m.volume_24h_fp ?? 0) * px, vtot: Number(m.volume_fp ?? 0) * px });
          }
        }
    cursor = d.cursor;
    if (!cursor) { kHitCap = false; break; }
  }
  if (kHitCap) console.warn('marks refresh: Kalshi pagination cap hit — tail markets may be unrefreshed; raise cap');

  // Polymarket: paginate open Gamma events
  let offset = 0;
  let pHitCap = true;
  for (let i = 0; i < 300; i++) {
    const u = new URL(`${POLY_GAMMA}/events`);
    u.searchParams.set('closed', 'false');
    u.searchParams.set('limit', '100');
    u.searchParams.set('offset', String(offset));
    const b: any = await (await fetch(u.toString())).json();
    if (!Array.isArray(b)) { pHitCap = false; break; }
    for (const ev of b)
      for (const m of ev.markets ?? [])
        if (want.has(m.conditionId)) {
          seenOpen.add(m.conditionId);
          if (m.lastTradePrice != null)
            // Polymarket volumes are USD-native.
            fresh.set(m.conditionId, { price: Number(m.lastTradePrice), v24: Number(m.volume24hr ?? 0), vtot: Number(m.volume ?? 0) });
        }
    offset += 100;
    if (b.length < 100) { pHitCap = false; break; }
  }
  if (pHitCap) console.warn('marks refresh: Polymarket pagination cap hit — tail markets may be unrefreshed; raise cap');

  // Write movers: skip only when price AND both volume figures are unchanged (the dead tail stays
  // cheap), so active markets get fresh price + volume — the latter feeds marks_daily → the /movers
  // day-over-day signal, which was inert while volume was frozen at the monthly seed value.
  const nowIso = new Date().toISOString();
  const stmts: D1PreparedStatement[] = [];
  for (const [pmid, w] of want) {
    const f = fresh.get(pmid);
    if (f == null) continue;
    if (f.price === w.price && f.v24 === w.v24 && f.vtot === w.vtot) continue;
    stmts.push(env.DB.prepare('UPDATE markets SET last_price = ?, volume_24h_usd = ?, volume_total_usd = ?, last_updated_at = ? WHERE market_id = ?')
      .bind(f.price, f.v24, f.vtot, nowIso, w.mid));
  }
  for (let i = 0; i < stmts.length; i += 100) await env.DB.batch(stmts.slice(i, i + 100));
  console.log(`marks refresh: ${stmts.length} changed / ${want.size} open markets`);
  return seenOpen;
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
// Scoped to all open markets — same set refreshMarks now keeps fresh.
const EOD_UTC_HOUR = 21; // ~5pm EDT / 4pm EST — end of the US day

async function snapshotDaily(env: Env): Promise<void> {
  const day = new Date().toISOString().slice(0, 10);
  const now = new Date().toISOString();
  const res = await env.DB.prepare(
    `INSERT INTO marks_daily (market_id, day, last_price, volume_24h_usd, volume_total_usd, captured_at)
     SELECT market_id, ?, last_price, volume_24h_usd, volume_total_usd, ?
       FROM markets
      WHERE last_price IS NOT NULL AND status = 'open'
     ON CONFLICT(market_id, day) DO UPDATE SET
        last_price = excluded.last_price,
        volume_24h_usd = excluded.volume_24h_usd,
        volume_total_usd = excluded.volume_total_usd,
        captured_at = excluded.captured_at`
  ).bind(day, now).run();
  console.log(`marks_daily snapshot ${day}: ${res.meta?.changes ?? '?'} rows`);
}

// ---- daily status reconciliation (zombie killer) ----------------------
// The hourly cron refreshes PRICE for open markets but never STATUS, and silently skips markets the
// venue stopped returning — so a resolved/delisted market stays status='open' with a frozen price
// (and the API serves it as live). Once a day we reconcile: any open market ABSENT from today's live
// open feed is venue-confirmed against the recently-settled feed and flipped to resolved/closed with
// the true settlement price. Venue-authoritative — never inferred from staleness. A delisted market we
// cannot confirm is left open (only closed if its own close date has already passed). Reuses the open
// set refreshMarks already pulled this run (zero extra open-feed subrequests, same snapshot).
const RECONCILE_UTC_HOUR = 6;   // 06:00 UTC — low-traffic, before the 08:00 cm-signal wire run
const SETTLE_WINDOW_DAYS = 14;  // recently-settled lookback; tolerates a few missed daily runs

type RowLite = { market_id: string; event_id: string; platform: string };
function resLogRow(env: Env, m: RowLite, eventType: string, fromV: string | null, toV: string,
                   finalPrice: number | null, occurredAt: string | null, recordedAt: string): D1PreparedStatement {
  // occurred_at is half the (market_id, occurred_at) PK — never bind NULL (SQLite treats NULLs as
  // distinct, which would let duplicate rows accrue), so fall back to the record time.
  return env.DB.prepare(
    `INSERT INTO resolution_log (market_id, event_id, platform, event_type, occurred_at, recorded_at, from_value, to_value, final_price, source, source_ref, actor)
     VALUES (?,?,?,?,?,?,?,?,?,?,?,?) ON CONFLICT(market_id, occurred_at) DO NOTHING`
  ).bind(m.market_id, m.event_id, m.platform, eventType, occurredAt ?? recordedAt, recordedAt,
         fromV, toV, finalPrice, 'platform_api', null, 'clearmarket-reconcile-cron');
}

async function reconcileStatus(env: Env, seenOpen: Set<string>): Promise<void> {
  const { results } = await env.DB.prepare(
    `SELECT market_id, event_id, platform, platform_market_id, close_at FROM markets
     WHERE platform_market_id IS NOT NULL AND status = 'open'`
  ).all<{ market_id: string; event_id: string; platform: string; platform_market_id: string; close_at: string | null }>();

  const unseen = results.filter((r) => !seenOpen.has(r.platform_market_id));
  if (!unseen.length) { console.log('reconcile: 0 unseen open markets'); return; }

  // recently-settled feeds -> platform_market_id -> { resolved, price (settlement, 0..1), closeTime }
  type Settle = { resolved: boolean; price: number | null; closeTime: string | null };
  const settled = new Map<string, Settle>();
  const cutoffMs = Date.now() - SETTLE_WINDOW_DAYS * 86_400_000;

  // Kalshi settled markets (min_close_ts in unix SECONDS)
  let kCursor: string | undefined;
  let kCap = true;
  for (let i = 0; i < 100; i++) {
    const u = new URL(`${KALSHI_BASE}/markets`);
    u.searchParams.set('status', 'settled');
    u.searchParams.set('min_close_ts', String(Math.floor(cutoffMs / 1000)));
    u.searchParams.set('limit', '1000');
    if (kCursor) u.searchParams.set('cursor', kCursor);
    const d: any = await (await fetch(u.toString(), { headers: { 'User-Agent': 'clearmarket-reconcile/0.1' } })).json();
    for (const m of d.markets ?? []) {
      const result = String(m.result ?? '').toLowerCase();
      const closeTime = m.close_time ?? m.expiration_time ?? null;
      if (result === 'yes' || result === 'no')
        settled.set(m.ticker, { resolved: true, price: result === 'yes' ? 1.0 : 0.0, closeTime });
      else
        settled.set(m.ticker, { resolved: false, price: null, closeTime }); // settled w/o yes/no -> closed
    }
    kCursor = d.cursor;
    if (!kCursor) { kCap = false; break; }
  }
  if (kCap) console.warn('reconcile: Kalshi settled pagination cap hit — raise cap or shorten window');

  // Polymarket closed events, newest-first by EVENT endDate. Record ONLY UMA-resolved markets: a closed
  // event whose UMA outcome isn't final yet may still resolve, so we leave those 'open' to re-check next
  // run rather than terminalize them. Stop at PAGE granularity on the event sort key — a still-recent
  // multi-outcome event can nest an old eliminated sub-market, so a per-market endDate must never halt
  // pagination (that silently truncated the feed ~1800 events short of the genuinely recent settlements).
  let pOffset = 0;
  let pStop = false;
  for (let i = 0; i < 200 && !pStop; i++) {
    const u = new URL(`${POLY_GAMMA}/events`);
    u.searchParams.set('closed', 'true');
    u.searchParams.set('limit', '100');
    u.searchParams.set('offset', String(pOffset));
    u.searchParams.set('order', 'endDate');
    u.searchParams.set('ascending', 'false');
    const b: any = await (await fetch(u.toString())).json();
    if (!Array.isArray(b) || !b.length) break;
    let pageMaxEnd = NaN;
    for (const ev of b) {
      const evEnd = ev.endDate ? Date.parse(ev.endDate) : NaN;
      if (Number.isFinite(evEnd)) pageMaxEnd = Number.isFinite(pageMaxEnd) ? Math.max(pageMaxEnd, evEnd) : evEnd;
      for (const m of ev.markets ?? []) {
        if (!m.conditionId) continue;
        if (String(m.umaResolutionStatus ?? '').toLowerCase() !== 'resolved') continue; // not final -> leave open
        let price: number | null = null;
        if (m.outcomePrices != null) {
          try {
            const p = typeof m.outcomePrices === 'string' ? JSON.parse(m.outcomePrices) : m.outcomePrices;
            if (Array.isArray(p) && p.length) price = Number(p[0]);
          } catch { /* unparseable -> leave null, handled as PENDING below */ }
        }
        settled.set(m.conditionId, { resolved: true, price, closeTime: m.endDate ?? null });
      }
    }
    pOffset += 100;
    if (Number.isFinite(pageMaxEnd) && pageMaxEnd < cutoffMs) pStop = true; // whole page older than the window
  }

  const nowIso = new Date().toISOString();
  const stmts: D1PreparedStatement[] = [];
  const logStmts: D1PreparedStatement[] = [];
  const counts = { resolved: 0, closed: 0, left: 0 };

  for (const m of unseen) {
    const s = settled.get(m.platform_market_id);
    if (s && s.resolved && s.price != null) {
      const outcome = s.price >= 0.5 ? 'YES' : 'NO';
      stmts.push(env.DB.prepare('UPDATE markets SET status=?, last_price=?, resolve_at=COALESCE(?, resolve_at), reconciled_at=? WHERE market_id=?')
        .bind('resolved', s.price, s.closeTime, nowIso, m.market_id));
      logStmts.push(resLogRow(env, m, 'resolved', 'open', outcome, s.price, s.closeTime ?? m.close_at, nowIso));
      counts.resolved++;
    } else if (s && s.resolved) {
      // venue says resolved but no parseable settlement price — flip status, keep price, outcome PENDING (no guess)
      stmts.push(env.DB.prepare('UPDATE markets SET status=?, resolve_at=COALESCE(?, resolve_at), reconciled_at=? WHERE market_id=?')
        .bind('resolved', s.closeTime, nowIso, m.market_id));
      logStmts.push(resLogRow(env, m, 'resolved', 'open', 'PENDING', null, s.closeTime ?? m.close_at, nowIso));
      counts.resolved++;
    } else if (s) {
      // Kalshi affirmatively SETTLED with no determinable yes/no outcome (void/cancelled) -> terminal 'closed'.
      // (Polymarket never lands here: the Poly pull only records UMA-resolved markets above.)
      stmts.push(env.DB.prepare('UPDATE markets SET status=?, reconciled_at=? WHERE market_id=?')
        .bind('closed', nowIso, m.market_id));
      logStmts.push(resLogRow(env, m, 'status_change', 'open', 'closed', null, s.closeTime ?? m.close_at, nowIso));
      counts.closed++;
    } else {
      // Absent from the live open feed AND from the in-window settled/resolved feeds. Could be closed-
      // awaiting-settlement, a true delist, or settled outside the window. NEVER terminalize here — that
      // would drop the eventual YES/NO outcome. Leave it 'open' and just record the check; the monthly
      // settle_status_sweep.py queries each carried market directly (no window) and makes the firm call,
      // and liveExpr's status+date logic already keeps a past-date open market out of the 'active' set.
      stmts.push(env.DB.prepare('UPDATE markets SET reconciled_at=? WHERE market_id=?').bind(nowIso, m.market_id));
      counts.left++;
    }
  }

  for (let i = 0; i < stmts.length; i += 100) await env.DB.batch(stmts.slice(i, i + 100));
  for (let i = 0; i < logStmts.length; i += 100) await env.DB.batch(logStmts.slice(i, i + 100));
  console.log(`reconcile: ${unseen.length} unseen / ${results.length} open -> resolved ${counts.resolved}, closed ${counts.closed}, left-open ${counts.left}`);
}

// ---- agent-economy discovery documents ----------------------------------
// Canonical card path is /.well-known/agent-card.json; the rest are aliases directories
// actually probe (observed 404s: /a2a/agent.json, /agents/.well-known/agent-card, …).
const A2A_CARD_PATHS = new Set([
  '/.well-known/agent-card.json', '/.well-known/agent.json',
  '/a2a/agent.json', '/a2a/agent-card.json', '/a2a/.well-known/agent.json', '/a2a/.well-known/agent-card.json',
  '/agent.json', '/agent-card.json', '/v1/agent.json',
  '/agents/agent.json', '/agents/agent-card.json', '/agents/.well-known/agent-card', '/agents/.well-known/agent-card.json',
]);

const X402_MANIFEST = {
  x402Version: 2,
  pricing: 'free',
  note: 'All ClearMarket endpoints are free (price 0) — this manifest exists for discovery, no payment is required or accepted yet. Attribution required: clearmarket.fyi.',
  resources: [
    { type: 'http', resource: 'https://api.clearmarket.fyi/v1/events', description: 'Graded prediction-market events (Kalshi + Polymarket): Resolution Clarity Grade, committed resolution source + provenance, cross-venue question_id. Filters: category, platform, grade, q.', mimeType: 'application/json', price: '0', accepts: [] },
    { type: 'http', resource: 'https://api.clearmarket.fyi/v1/markets/movers', description: 'Day-over-day volume movers.', mimeType: 'application/json', price: '0', accepts: [] },
    { type: 'http', resource: 'https://api.clearmarket.fyi/v1/signals', description: 'CM Signal wires (cross-venue divergence, benchmark drift, news cycle, volume spikes).', mimeType: 'application/json', price: '0', accepts: [] },
    { type: 'mcp', resource: 'https://api.clearmarket.fyi/mcp', description: 'MCP server: read-only reference tools (events, markets, catalysts, signals).', mimeType: 'application/json', price: '0', accepts: [] },
    { type: 'http', resource: 'https://api.clearmarket.fyi/a2a', description: 'A2A endpoint (JSON-RPC message/send); agent card at /.well-known/agent-card.json.', mimeType: 'application/json', price: '0', accepts: [] },
  ],
};

// RFC 9727 linkset. Link relations per RFC 8631: service-desc = machine-readable
// description, service-doc = human docs, service-meta = metadata about the service.
const API_CATALOG = {
  linkset: [
    {
      anchor: 'https://api.clearmarket.fyi/',
      'service-desc': [
        { href: 'https://clearmarket.fyi/schema.json', type: 'application/json', title: 'ClearMarket 4-table schema (events/markets/marks/resolution_log)' },
      ],
      'service-doc': [
        { href: 'https://clearmarket.fyi/for-data/', type: 'text/html', title: 'ClearMarket for data buyers' },
        { href: 'https://clearmarket.fyi/llms.txt', type: 'text/plain', title: 'LLM-readable index' },
      ],
      'service-meta': [
        { href: 'https://api.clearmarket.fyi/.well-known/agent-card.json', type: 'application/json', title: 'A2A agent card' },
        { href: 'https://api.clearmarket.fyi/.well-known/x402', type: 'application/json', title: 'x402 pricing manifest (free)' },
        { href: 'https://api.clearmarket.fyi/health', type: 'application/json', title: 'Live status + filter vocabulary' },
      ],
    },
  ],
};

// ---- router ------------------------------------------------------------
export default {
  async fetch(req: Request, env: Env, ctx: any): Promise<Response> {
    const url = new URL(req.url);
    const path = url.pathname.replace(/\/+$/, '') || '/';

    if (req.method === 'OPTIONS') return new Response(null, { status: 204, headers: CORS });

    // Attribution beacon. A static page (e.g. /for-data/?partner=tmx) fetches this on load so a
    // named-recipient visit lands in call_log (ts, ip, country, ua) — the HTML layer is otherwise
    // invisible to the Worker. `p` names the recipient; nothing is served back.
    if (path === '/v1/ping') {
      logCall(env, ctx, req, 'rest', 'ping', url.searchParams.get('p') || null);
      return new Response(null, { status: 204, headers: { ...CORS, 'Cache-Control': 'no-store' } });
    }

    if (path === '/' || path === '/health') {
      const ev = await env.DB.prepare('SELECT COUNT(*) AS n FROM events').first<{ n: number }>();
      const mk = await env.DB.prepare('SELECT COUNT(*) AS n FROM markets').first<{ n: number }>();
      return json({
        service: 'clearmarket-api',
        status: 'ok',
        schema: 'v0.2.0',
        events: ev?.n ?? 0,
        markets: mk?.n ?? 0,
        docs: '/v1/events (filters: category, platform, grade, q, limit, offset). q is token-AND across question+tags. Open access; optional free key (POST /v1/keys) for higher limits. MCP at /mcp.',
        // Valid filter values, so an agent discovers them without guessing or a failed call.
        filters: {
          category: KNOWN_CATEGORIES,
          platform: KNOWN_PLATFORMS,
          grade: KNOWN_GRADES,
          max_limit: MAX_PAGE,
          signals_detection_path: ['news_cycle', 'cross_venue_divergence', 'benchmark_drift', 'volume_spike'],
        },
      });
    }

    if (path === '/v1/spot') {
      logCall(env, ctx, req, 'rest', 'spot');
      const { results } = await env.DB.prepare('SELECT coin, price_usd, as_of FROM spot ORDER BY coin').all();
      return json({ source: 'coingecko', vs_currency: 'usd', spot: results });
    }

    if (path === '/v1/catalysts/upcoming') {
      logCall(env, ctx, req, 'rest', 'upcoming_catalysts', { days: url.searchParams.get('days') });
      return upcomingCatalysts(env, url);
    }

    // CM Signal wire is served as static JSON by Pages (it's content, not D1). Proxy it here so the
    // obvious REST path resolves for agents (an external agent hit /v1/signals and got a 404).
    // /v1/signals -> wire index; /v1/signals/:slug -> one bulletin.
    if (path === '/v1/signals' || path.startsWith('/v1/signals/')) {
      const slug = path === '/v1/signals' ? '' : path.slice('/v1/signals/'.length).replace(/\/+$/, '');
      logCall(env, ctx, req, 'rest', 'signals', slug || 'index');
      const target = slug
        ? `https://clearmarket.fyi/signals/${encodeURIComponent(slug)}.json`
        : 'https://clearmarket.fyi/signals.json';
      const upstream = await fetch(target, { cf: { cacheTtl: 300, cacheEverything: true } });
      if (!upstream.ok) return err(upstream.status === 404 ? 404 : 502, upstream.status === 404 ? 'Signal not found' : 'Upstream error', 'Try /v1/signals or /signals.json');
      // The static signals.json takes no query params; apply the MCP list_signals filters here so
      // REST agents can narrow the wire feed (?detection_path=, ?category=, ?venue=, ?event_id=, ?limit=)
      // instead of pulling all 45 and filtering client-side. Single-signal (slug) path is passed through.
      if (!slug) {
        const feed: any = await upstream.json();
        let items: any[] = Array.isArray(feed) ? feed : (feed.signals ?? []);
        const dp = url.searchParams.get('detection_path');
        const cat = url.searchParams.get('category');
        const ven = url.searchParams.get('venue');
        const eid = url.searchParams.get('event_id');
        if (dp) items = items.filter((s) => s.detection_path === dp);
        if (cat) { const c = cat.toUpperCase(); items = items.filter((s) => (s.category_tag ?? '').toUpperCase() === c); }
        if (ven) items = items.filter((s) => (s.venues ?? []).includes(ven));
        if (eid) items = items.filter((s) => s.target_event_id === eid || (s.linked_event_ids ?? []).includes(eid));
        const lim = Math.min(Math.max(Number(url.searchParams.get('limit') ?? 100) || 100, 1), 200);
        return json({ count: items.length, _notice: NOTICE, signals: items.slice(0, lim) }, 200, { 'cache-control': 'public, max-age=300' });
      }
      return new Response(await upstream.text(), {
        status: 200,
        headers: { ...CORS, 'content-type': 'application/json; charset=utf-8', 'cache-control': 'public, max-age=300' },
      });
    }

    // Glama connector-ownership proof (glama.ai/mcp/connectors/fyi.clearmarket/clearmarket):
    // Glama polls this well-known file on the connector's domain and verifies the
    // maintainer email against the claiming Glama account.
    if (path === '/.well-known/glama.json') {
      return json({
        $schema: 'https://glama.ai/mcp/schemas/connector.json',
        maintainers: [{ email: 'jeremyd2255@gmail.com' }],
      }, 200, { 'cache-control': 'public, max-age=3600' });
    }

    if (path === '/mcp') return handleMcp(req, env, ctx);

    // ---- agent-economy discovery surfaces (2026-07-14) -------------------
    // The alias set below is the union of card paths agent directories were observed
    // probing (as 404s) in zone logs the week before this shipped — serve them all.
    if (A2A_CARD_PATHS.has(path)) {
      logCall(env, ctx, req, 'a2a', 'agent_card', path);
      return json(AGENT_CARD, 200, { 'cache-control': 'public, max-age=3600' });
    }
    if (path === '/a2a') {
      // message/send does up to 3 D1 queries and skips authenticate() (like /mcp) — meter it
      // with the same anon per-IP daily cap /v1 uses, under its own namespace so it doesn't
      // double-count REST usage. Card GETs stay unmetered.
      if (req.method === 'POST') {
        // Fail open: the cap is defense-in-depth — a throttle-storage error must not 500 a
        // discovery endpoint that otherwise works.
        let count = 0;
        try { count = await bumpUsage(env, `a2a:${req.headers.get('CF-Connecting-IP') ?? 'unknown'}`, new Date().toISOString().slice(0, 10)); } catch { /* fail open */ }
        if (count > ANON_DAILY_LIMIT) return err(429, `Rate limit exceeded (${ANON_DAILY_LIMIT}/day per IP).`, 'Use the REST API with a free key for higher limits: POST /v1/keys { "email": "you@firm.com" }');
      }
      return handleA2A(req, env, ctx);
    }

    // x402 discovery stub — there is no official well-known format (Bazaar listing is
    // facilitator-based), but x402/agent directories probe this path daily. Everything
    // is free (empty `accepts`, price 0): this exists for discovery, not revenue.
    if (path === '/.well-known/x402') {
      logCall(env, ctx, req, 'rest', 'x402_manifest');
      return json(X402_MANIFEST, 200, { 'cache-control': 'public, max-age=3600' });
    }

    // RFC 9727 API catalog (linkset) — one machine-readable index of every surface.
    if (path === '/.well-known/api-catalog') {
      logCall(env, ctx, req, 'rest', 'api_catalog');
      return new Response(JSON.stringify(API_CATALOG, null, 2), {
        status: 200,
        headers: { 'Content-Type': 'application/linkset+json', 'cache-control': 'public, max-age=3600', ...CORS },
      });
    }

    if (path === '/v1/keys' && req.method === 'POST') return createKey(env, req);

    if (req.method !== 'GET') return err(405, 'Method not allowed');

    const auth = await authenticate(env, req, url);
    if (auth instanceof Response) return auth;

    if (path === '/v1/events') {
      logCall(env, ctx, req, 'rest', 'list_events', {
        q: url.searchParams.get('q'), category: url.searchParams.get('category'),
        platform: url.searchParams.get('platform'), grade: url.searchParams.get('grade'),
      });
      return listEvents(env, url, auth);
    }
    if (path === '/v1/markets/movers') { logCall(env, ctx, req, 'rest', 'list_movers'); return listMovers(env, url); }
    const evMatch = path.match(/^\/v1\/events\/([^/]+)$/);
    if (evMatch) { const slug = decodeURIComponent(evMatch[1]); logCall(env, ctx, req, 'rest', 'get_event', slug); return getEvent(env, slug, auth, url.searchParams.get('detail') ?? 'full'); }
    const mkMatch = path.match(/^\/v1\/markets\/([^/]+)$/);
    if (mkMatch) { const id = decodeURIComponent(mkMatch[1]); logCall(env, ctx, req, 'rest', 'get_market', id); return getMarket(env, id, auth); }

    return err(404, 'Not found', 'Try /health or /v1/events');
  },

  // Hourly cron (0 * * * *) — refresh prices for linked + primary markets + crypto spot.
  // Once a day at EOD_UTC_HOUR, also append the daily history snapshot (after the refresh).
  async scheduled(_event: any, env: Env, ctx: any): Promise<void> {
    const hour = new Date().getUTCHours();
    if (hour === EOD_UTC_HOUR) {
      ctx.waitUntil((async () => {
        await refreshMarks(env);
        await snapshotDaily(env);
        await refreshSpot(env);
      })());
    } else if (hour === RECONCILE_UTC_HOUR) {
      ctx.waitUntil((async () => {
        const seen = await refreshMarks(env);
        await reconcileStatus(env, seen);
        await refreshSpot(env);
      })());
    } else {
      ctx.waitUntil(Promise.all([refreshMarks(env), refreshSpot(env)]));
    }
  },
};
