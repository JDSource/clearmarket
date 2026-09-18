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

import { handleMcp, TOOLS, SERVER_INFO, PROTOCOL_VERSION } from './mcp';
import { AGENT_CARD, handleA2A } from './a2a';
import { OPENAPI_SPEC, AGENTS_MANIFEST, CONTRACT_VERSION } from './openapi';

// agents.json probe variants observed as 404s in call_log (AgenstryBot walks all of these daily).
const AGENTS_JSON_PATHS = new Set([
  '/agents.json', '/.well-known/agents.json',
  '/agent-directory.json', '/.well-known/agent-directory.json',
]);

export interface Env {
  DB: D1Database;
  // Base URL of the published static site that serves the CM Signal feed
  // (/signals.json, /signals/<slug>.json). MCP signal tools fetch from here so
  // wires stay single-sourced as static content (no D1 duplication). Defaults to prod.
  SIGNALS_BASE?: string;
  // Public R2 base that serves the bundle + the daily sweep/screen files the Worker applies to D1.
  DATA_BASE?: string;
  // Secret. When set, POST /v1/admin/run?step=… (Bearer) triggers a pipeline step on demand.
  ADMIN_TOKEN?: string;
  // Secret. Fine-grained GitHub PAT (repo JDSource/clearmarket, Actions: read+write) used to dispatch workflows on time.
  GH_DISPATCH_TOKEN?: string;
}

const CORS = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
  'Access-Control-Allow-Headers': 'Authorization, Content-Type',
  'Access-Control-Expose-Headers': 'X-CM-Schema-Version, X-Request-Id',
};

// Response-contract version. Additive field changes bump the patch digit; renames/removals bump minor
// and are announced to keyed users first. Emitted as a header on every JSON response so a consumer can
// detect a contract change programmatically.
const SCHEMA_VERSION = `v${CONTRACT_VERSION}`;

const json = (data: unknown, status = 200, extra: Record<string, string> = {}) =>
  new Response(JSON.stringify(data, null, 2), {
    status,
    headers: { 'Content-Type': 'application/json; charset=utf-8', 'X-CM-Schema-Version': SCHEMA_VERSION, ...CORS, ...extra },
  });

// ISO-8601 UTC timestamp h hours ago — the ONLY timestamp format the Worker writes or compares
// (toISOString: 24 chars, 'T', millis, 'Z'). Never mix with SQLite datetime('now') strings.
const isoAgo = (hours: number) => new Date(Date.now() - hours * 3600e3).toISOString();

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
  surface: 'rest' | 'mcp' | 'a2a' | 'miss',
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

// Vulnerability-scanner and boilerplate-crawler paths excluded from the miss
// log: exploit probes (.php/.env/wp-*/…), dotfiles other than .well-known,
// and standard crawler fetches (robots/favicon/sitemap) that mean nothing.
const SCANNER_NOISE =
  /\.(php\d?|aspx?|jsp|env|git|sql|bak|cgi|ini)\b|wp-|wordpress|phpmyadmin|cgi-bin|\/\.(?!well-known)|^\/(favicon\.ico|robots\.txt|sitemap[^/]*)$/i;

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
export const NOTICE = {
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
    // price recency ≠ record recency: last_updated_at is stamped by the hourly marks cron,
    // while the event-level updated_at reflects the enrichment vintage.
    price_as_of: m.last_updated_at ?? null,
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
    // Two clocks. price_as_of (above) = last time the price CHANGED. last_checked_at = last time the
    // hourly cron saw this market in a venue's live feed and confirmed the price, changed or not.
    // NULL = not seen in any live feed since the last reload: filter these out of "live" displays.
    last_checked_at: m.last_checked_at ?? null,
    // Last time status was verified against the venue (daily reconcile / sweep).
    reconciled_at: m.reconciled_at ?? null,
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
    price_as_of: f.price_as_of,
    status: f.status,
    rcg: { grade: f.rcg.grade, score: f.rcg.score },
    resolution: {
      arbitration_model: f.resolution.arbitration_model,
      source: f.resolution.source,
      source_status: f.resolution.source_status,
    },
    question_id: f.question_id,
    also_on: f.also_on,
    last_checked_at: f.last_checked_at,
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
    price_as_of: primary?.last_updated_at ?? null,
    last_checked_at: primary?.last_checked_at ?? null,
    status: primary?.status ?? null,   // open / resolved — lets an agent filter without a get_event round-trip
    updated_at: e.updated_at,   // enrichment vintage, NOT price recency (that's price_as_of)
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

  const limit = Math.min(Math.max(Number(p.get('limit') ?? 50) || 50, 1), MAX_PAGE);
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
    `SELECT market_id, event_id, platform, last_price, last_updated_at, last_checked_at, resolution_clarity_grade, rcg_score, status FROM markets WHERE event_id IN (${ph})`
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
      `SELECT market_id, platform, event_type, to_value, occurred_at, occurred_basis, final_price, recorded_at, source, source_ref
         FROM resolution_log WHERE event_id = ? ORDER BY occurred_at DESC`
    ).bind(e.event_id).all<any>();
    // A deadline is not a settlement: deadline-basis timestamps (venue exposes no settlement
    // time, e.g. delisted-before-settlement) go out as deadline_at, never as resolved_at.
    resolutionLog = results.map((r) => ({
      market_id: r.market_id, platform: r.platform, event_type: r.event_type, outcome: r.to_value,
      resolved_at: r.occurred_basis === 'deadline' ? null : r.occurred_at,
      deadline_at: r.occurred_basis === 'deadline' ? r.occurred_at : null,
      occurred_basis: r.occurred_basis ?? null,
      final_price: num(r.final_price), recorded_at: r.recorded_at,
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
    current_primary_mark: primary ? { last_price: num(primary.last_price), implied_probability: num(primary.last_price), as_of: primary.last_updated_at ?? null } : null,
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
const KALSHI_SNAPSHOT_MAX_AGE_MIN = 180;  // kalshi-marks.yml is hourly but GitHub schedules lag 20-80 min here; rows are stamped with the snapshot's own time, so the clock stays honest
const POLY_GAMMA = 'https://gamma-api.polymarket.com';

// ---- run ledger + feed metadata -----------------------------------------
// Every cron step writes one cron_runs row (run_id = the UTC hour it ran in). This is how a stalled
// step leaves a trace instead of a console.log nobody reads, and what /v1/status reports under runs[].
async function recordRun(env: Env, runId: string, step: string, venue: string, startedAt: string,
                         fetched: number | null, changed: number | null, error: string | null): Promise<void> {
  try {
    await env.DB.prepare(
      `INSERT INTO cron_runs (run_id, step, venue, started_at, finished_at, fetched, changed, error)
       VALUES (?,?,?,?,?,?,?,?)
       ON CONFLICT(run_id, step, venue) DO UPDATE SET finished_at=excluded.finished_at, fetched=excluded.fetched,
         changed=excluded.changed, error=excluded.error`
    ).bind(runId, step, venue, startedAt, new Date().toISOString(), fetched, changed, error).run();
  } catch (e) { console.error('cron_runs write failed', e); }
}
async function setMeta(env: Env, key: string, value: string | null): Promise<void> {
  try {
    await env.DB.prepare(
      `INSERT INTO feed_meta (key, value, updated_at) VALUES (?,?,?)
       ON CONFLICT(key) DO UPDATE SET value=excluded.value, updated_at=excluded.updated_at`
    ).bind(key, value, new Date().toISOString()).run();
  } catch (e) { console.error('feed_meta write failed', e); }
}
const errStr = (e: unknown) => String((e as any)?.message ?? e).slice(0, 500);
// Retries 429 and 5xx with backoff (venues rate-limit a full 300-page scan now and then); other 4xx throw.
async function fetchJson(url: string, ua?: string, tries = 4): Promise<any> {
  let last: Response | null = null;
  for (let attempt = 0; attempt < tries; attempt++) {
    if (attempt) {
      const ra = Number(last?.headers.get('Retry-After') ?? 0);
      await new Promise((res) => setTimeout(res, ra > 0 ? Math.min(ra, 20) * 1000 : 2000 * 2 ** (attempt - 1)));   // 2s, 4s, 8s
    }
    const r = await fetch(url, ua ? { headers: { 'User-Agent': ua } } : undefined);
    if (r.ok) return r.json();
    last = r;
    if (r.status !== 429 && r.status < 500) break;
  }
  throw new Error(`HTTP ${last?.status} from ${new URL(url).host}`);
}

// Returns the set of platform_market_ids seen in the live OPEN venue feed this run (so the daily
// reconcileStatus pass reuses the exact same snapshot) plus a per-venue ok flag: a venue whose fetch
// FAILED must not be treated as "returned nothing" downstream (that would read as every market delisted).
// Every market seen in a live feed gets last_checked_at stamped, changed or not — the second clock.
type VenueOk = { kalshi: boolean; polymarket: boolean };
async function refreshMarks(env: Env, runId: string): Promise<{ seenOpen: Set<string>; venueOk: VenueOk }> {
  const startedAt = new Date().toISOString();
  const { results } = await env.DB.prepare(
    `SELECT market_id, platform, platform_market_id, last_price, volume_24h_usd, volume_total_usd FROM markets
     WHERE platform_market_id IS NOT NULL AND status = 'open'`
  ).all<{ market_id: string; platform: string; platform_market_id: string; last_price: number | null; volume_24h_usd: number | null; volume_total_usd: number | null }>();
  type Want = { mid: string; platform: string; price: number | null; v24: number | null; vtot: number | null };
  const want = new Map<string, Want>();
  for (const r of results) want.set(r.platform_market_id, { mid: r.market_id, platform: r.platform, price: r.last_price, v24: r.volume_24h_usd, vtot: r.volume_total_usd });
  const venueOk: VenueOk = { kalshi: true, polymarket: true };
  // When Kalshi comes from the R2 snapshot, its rows are stamped with the snapshot's observation time, not ours.
  let kalshiStamp: string | null = null;
  const venueErr: Record<string, string | null> = { kalshi: null, polymarket: null };
  if (!want.size) return { seenOpen: new Set(), venueOk };

  type Mark = { price: number; v24: number; vtot: number };
  const fresh = new Map<string, Mark>();
  // Every tracked market the live OPEN feed returned this run (priced or not). This — NOT fresh —
  // is the "still listed" signal: an open-but-untraded market (no price) is never mistaken for delisted.
  const seenOpen = new Set<string>();

  // Kalshi. Kalshi rate-limits Cloudflare Workers' shared egress IPs at the FIRST request (HTTP 429), so
  // the direct scan only ever got through sporadically (the old code read the 429 body as an empty page and
  // stopped early, silently). Primary source is therefore the hourly snapshot the GitHub job
  // kalshi-marks.yml publishes to R2 (tracked tickers only, venue field names, with status). The direct
  // paged scan is the fallback when the snapshot is missing or older than KALSHI_SNAPSHOT_MAX_AGE_MIN.
  try {
    let usedSnapshot = false;
    try {
      // eslint-disable-next-line no-var
      const snap: any = await fetchJson(`${env.DATA_BASE ?? DATA_BASE_DEFAULT}/kalshi-tracked-latest.json?t=${Date.now()}`, undefined, 2);
      const age = (Date.now() - Date.parse(snap?.generated_at ?? '')) / 60e3;
      if (!Array.isArray(snap?.markets)) throw new Error('snapshot has no markets[]');
      if (!(age <= KALSHI_SNAPSHOT_MAX_AGE_MIN)) throw new Error(`snapshot too old (${Math.round(age)} min)`);
      for (const m of snap.markets)
        if (want.has(m.t) && (m.s === 'active' || m.s === 'open')) {
          seenOpen.add(m.t);
          if (m.p != null) {
            const px = Number(m.p);
            fresh.set(m.t, { price: px, v24: Number(m.v24 ?? 0) * px, vtot: Number(m.v ?? 0) * px });
          }
        }
      usedSnapshot = true;
      kalshiStamp = new Date(Date.parse(snap.generated_at)).toISOString();
      console.log(`marks refresh: kalshi via snapshot ${snap.generated_at} (${Math.round(age)} min old, ${snap.returned}/${snap.tracked} returned)`);
    } catch (e) {
      console.warn('marks refresh: kalshi snapshot unavailable, falling back to direct scan:', errStr(e));
    }
    if (!usedSnapshot) {
      let cursor: string | undefined;
      let hitCap = true;
      for (let i = 0; i < 400; i++) {
        const u = new URL(`${KALSHI_BASE}/markets`);
        u.searchParams.set('status', 'open');
        u.searchParams.set('limit', '1000');
        if (cursor) u.searchParams.set('cursor', cursor);
        const d: any = await fetchJson(u.toString(), 'clearmarket-marks/0.1');
        if (!Array.isArray(d?.markets)) throw new Error('unexpected body: no markets[] (venue schema change?)');
        for (const m of d.markets)
          if (want.has(m.ticker)) {
            seenOpen.add(m.ticker);
            if (m.last_price_dollars != null) {
              const px = Number(m.last_price_dollars);
              // Kalshi volume is in contracts; approximate USD via current price (matches the generators' live_refresh).
              fresh.set(m.ticker, { price: px, v24: Number(m.volume_24h_fp ?? 0) * px, vtot: Number(m.volume_fp ?? 0) * px });
            }
          }
        cursor = d.cursor;
        if (!cursor || d.markets.length === 0) { hitCap = false; break; }
        await new Promise((res) => setTimeout(res, 250));
      }
      if (hitCap) venueErr.kalshi = 'pagination cap hit — tail markets unrefreshed; raise cap';
    }
  } catch (e) { venueOk.kalshi = false; venueErr.kalshi = errStr(e); console.error('marks refresh: kalshi failed:', venueErr.kalshi); }

  // Polymarket: paginate open Gamma events. A non-array FIRST page is a failure; a non-array later page is end-of-list.
  try {
    let offset = 0;
    let hitCap = true;
    for (let i = 0; i < 300; i++) {
      const u = new URL(`${POLY_GAMMA}/events`);
      u.searchParams.set('closed', 'false');
      u.searchParams.set('limit', '100');
      u.searchParams.set('offset', String(offset));
      let b: any;
      try { b = await fetchJson(u.toString()); }
      catch (e) {
        // Gamma returns 422 when offset passes its ceiling: that is the end of the list, not an outage.
        if (offset > 0 && /HTTP 422/.test(errStr(e))) { hitCap = false; break; }
        throw e;
      }
      if (!Array.isArray(b)) { if (offset === 0) throw new Error('unexpected body: not an array (venue schema change?)'); hitCap = false; break; }
      for (const ev of b)
        for (const m of ev.markets ?? [])
          if (want.has(m.conditionId)) {
            seenOpen.add(m.conditionId);
            if (m.lastTradePrice != null)
              // Polymarket volumes are USD-native.
              fresh.set(m.conditionId, { price: Number(m.lastTradePrice), v24: Number(m.volume24hr ?? 0), vtot: Number(m.volume ?? 0) });
          }
      offset += 100;
      if (b.length < 100) { hitCap = false; break; }
    }
    if (hitCap) venueErr.polymarket = 'pagination cap hit — tail markets unrefreshed; raise cap';
  } catch (e) { venueOk.polymarket = false; venueErr.polymarket = errStr(e); console.error('marks refresh: polymarket failed:', venueErr.polymarket); }

  // Writes. Movers: price+volume+both clocks. Seen-but-unchanged: last_checked_at only (batched IN lists).
  const nowIso = new Date().toISOString();
  const stmts: D1PreparedStatement[] = [];
  const checkedOnly = new Map<string, string[]>();   // stamp -> market_ids (Kalshi-via-snapshot rows carry the snapshot time)
  const seenBy: Record<string, number> = { kalshi: 0, polymarket: 0 };
  const changedBy: Record<string, number> = { kalshi: 0, polymarket: 0 };
  for (const [pmid, w] of want) {
    if (!seenOpen.has(pmid)) continue;
    seenBy[w.platform] = (seenBy[w.platform] ?? 0) + 1;
    const ts = w.platform === 'kalshi' && kalshiStamp ? kalshiStamp : nowIso;
    const f = fresh.get(pmid);
    if (f && !(f.price === w.price && f.v24 === w.v24 && f.vtot === w.vtot)) {
      changedBy[w.platform] = (changedBy[w.platform] ?? 0) + 1;
      // row_changed_at = OUR write time (the since= key). last_updated_at/last_checked_at = observation time, only
      // ever moved forward; an observation older than the last price write is ignored (a late snapshot must not
      // roll a newer direct-scan price backwards).
      stmts.push(env.DB.prepare(`UPDATE markets SET last_price = ?, volume_24h_usd = ?, volume_total_usd = ?,
          last_updated_at = ?, last_checked_at = MAX(COALESCE(last_checked_at,''), ?), row_changed_at = ?
        WHERE market_id = ? AND (last_updated_at IS NULL OR last_updated_at <= ?)`)
        .bind(f.price, f.v24, f.vtot, ts, ts, nowIso, w.mid, ts));
    } else {
      (checkedOnly.get(ts) ?? checkedOnly.set(ts, []).get(ts)!).push(w.mid);
    }
  }
  const changed = stmts.length;
  for (const [ts, list] of checkedOnly)
    for (let i = 0; i < list.length; i += 90) {
      const ids = list.slice(i, i + 90);
      stmts.push(env.DB.prepare(`UPDATE markets SET last_checked_at = MAX(COALESCE(last_checked_at,''), ?) WHERE market_id IN (${ids.map(() => '?').join(',')})`).bind(ts, ...ids));
    }
  for (let i = 0; i < stmts.length; i += 100) await env.DB.batch(stmts.slice(i, i + 100));
  console.log(`marks refresh: ${changed} changed / ${seenOpen.size} seen / ${want.size} open markets (kalshi ${venueOk.kalshi ? 'ok' : 'FAILED'}, polymarket ${venueOk.polymarket ? 'ok' : 'FAILED'})`);
  await recordRun(env, runId, 'marks', 'kalshi', startedAt, seenBy.kalshi, changedBy.kalshi, venueErr.kalshi);
  await recordRun(env, runId, 'marks', 'polymarket', startedAt, seenBy.polymarket, changedBy.polymarket, venueErr.polymarket);
  return { seenOpen, venueOk };
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

async function snapshotDaily(env: Env, runId: string): Promise<void> {
  const startedAt = new Date().toISOString();
  const day = startedAt.slice(0, 10);
  // price_as_of = when the stored price last CHANGED. carried_forward = 1 when the market was not seen
  // in any live venue feed in the last 24h, i.e. the row repeats an old value rather than an observation.
  // Rows before 2026-09-17 have NULL in both: that history cannot be corrected retroactively.
  const checkedCutoff = isoAgo(24);
  const res = await env.DB.prepare(
    `INSERT INTO marks_daily (market_id, day, last_price, volume_24h_usd, volume_total_usd, captured_at, price_as_of, carried_forward)
     SELECT market_id, ?, last_price, volume_24h_usd, volume_total_usd, ?, last_updated_at,
            CASE WHEN last_checked_at IS NOT NULL AND last_checked_at >= ? THEN 0 ELSE 1 END
       FROM markets
      WHERE last_price IS NOT NULL AND status = 'open'
     ON CONFLICT(market_id, day) DO UPDATE SET
        last_price = excluded.last_price,
        volume_24h_usd = excluded.volume_24h_usd,
        volume_total_usd = excluded.volume_total_usd,
        captured_at = excluded.captured_at,
        price_as_of = excluded.price_as_of,
        carried_forward = excluded.carried_forward`
  ).bind(day, startedAt, checkedCutoff).run();
  console.log(`marks_daily snapshot ${day}: ${res.meta?.changes ?? '?'} rows`);
  await recordRun(env, runId, 'snapshot', '', startedAt, null, res.meta?.changes ?? null, null);
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
                   finalPrice: number | null, settleTime: string | null, deadline: string | null,
                   recordedAt: string, actor = 'clearmarket-reconcile-cron'): D1PreparedStatement {
  // occurred_at is half the (market_id, occurred_at) PK — never bind NULL (SQLite treats NULLs as
  // distinct, which would let duplicate rows accrue), so fall back deadline -> record time.
  // The basis says which clock occurred_at holds; only a real venue timestamp may claim settlement.
  const occurredAt = settleTime ?? deadline ?? recordedAt;
  const basis = settleTime ? 'venue_settlement' : deadline ? 'deadline' : 'first_observed';
  return env.DB.prepare(
    `INSERT INTO resolution_log (market_id, event_id, platform, event_type, occurred_at, occurred_basis, recorded_at, from_value, to_value, final_price, source, source_ref, actor)
     VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?) ON CONFLICT(market_id, occurred_at) DO NOTHING`
  ).bind(m.market_id, m.event_id, m.platform, eventType, occurredAt, basis, recordedAt,
         fromV, toV, finalPrice, 'platform_api', null, actor);
}

async function reconcileStatus(env: Env, seenOpen: Set<string>, runId: string): Promise<void> {
  const startedAt = new Date().toISOString();
  const { results } = await env.DB.prepare(
    `SELECT market_id, event_id, platform, platform_market_id, close_at FROM markets
     WHERE platform_market_id IS NOT NULL AND status = 'open'`
  ).all<{ market_id: string; event_id: string; platform: string; platform_market_id: string; close_at: string | null }>();

  // Kalshi is reconciled from the hourly R2 snapshot (applyKalshiFinalized) because its settled feed 429s Cloudflare
  // egress; only Polymarket goes through the venue feeds here.
  const unseen = results.filter((r) => r.platform !== 'kalshi' && !seenOpen.has(r.platform_market_id));
  if (!unseen.length) { console.log('reconcile: 0 unseen open markets'); await recordRun(env, runId, 'reconcile', '', startedAt, 0, 0, null); return; }

  // recently-settled feeds -> platform_market_id -> { resolved, price (settlement, 0..1), closeTime,
  // settleTime }. closeTime is deadline-class metadata (endDate/close_time) used for resolve_at;
  // settleTime is the venue's actual settlement timestamp (Kalshi settlement_ts, Poly closedTime)
  // and is the only value allowed into resolution_log as occurred_basis='venue_settlement'.
  type Settle = { resolved: boolean; price: number | null; closeTime: string | null; settleTime: string | null };
  const normCt = (v: unknown): string | null => {
    if (!v) return null;
    let s = String(v).trim().replace(' ', 'T');
    if (s.endsWith('+00')) s = s.slice(0, -3) + 'Z';
    return s;
  };
  const settled = new Map<string, Settle>();
  const cutoffMs = Date.now() - SETTLE_WINDOW_DAYS * 86_400_000;

  // A venue whose settled feed FAILS must not be read as "nothing settled": its unseen markets are skipped
  // this run (no reconciled_at stamp) and the failure is recorded on the run.
  const kalshiFeedOk = true; let polyFeedOk = true;
  // (Kalshi settled-feed pull removed 2026-09-18: unreachable from Workers, and Kalshi unseen markets are excluded above.)

  // Polymarket closed events, newest-first by EVENT endDate. Record ONLY UMA-resolved markets: a closed
  // event whose UMA outcome isn't final yet may still resolve, so we leave those 'open' to re-check next
  // run rather than terminalize them. Stop at PAGE granularity on the event sort key — a still-recent
  // multi-outcome event can nest an old eliminated sub-market, so a per-market endDate must never halt
  // pagination (that silently truncated the feed ~1800 events short of the genuinely recent settlements).
  let pOffset = 0;
  let pStop = false;
  try { for (let i = 0; i < 200 && !pStop; i++) {
    const u = new URL(`${POLY_GAMMA}/events`);
    u.searchParams.set('closed', 'true');
    u.searchParams.set('limit', '100');
    u.searchParams.set('offset', String(pOffset));
    u.searchParams.set('order', 'endDate');
    u.searchParams.set('ascending', 'false');
    let b: any;
    try { b = await fetchJson(u.toString()); }
    catch (e) { if (pOffset > 0 && /HTTP 422/.test(errStr(e))) break; throw e; }   // Gamma 422 past page 1 = end of list
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
        settled.set(m.conditionId, { resolved: true, price, closeTime: m.endDate ?? null, settleTime: normCt(m.closedTime) });
      }
    }
    pOffset += 100;
    if (Number.isFinite(pageMaxEnd) && pageMaxEnd < cutoffMs) pStop = true; // whole page older than the window
  } } catch (e) { polyFeedOk = false; console.error('reconcile: polymarket closed feed failed:', errStr(e)); }

  const nowIso = new Date().toISOString();
  const stmts: D1PreparedStatement[] = [];
  const logStmts: D1PreparedStatement[] = [];
  const counts = { resolved: 0, closed: 0, left: 0, skipped: 0 };

  for (const m of unseen) {
    if ((m.platform === 'kalshi' && !kalshiFeedOk) || (m.platform === 'polymarket' && !polyFeedOk)) { counts.skipped++; continue; }
    const s = settled.get(m.platform_market_id);
    if (s && s.resolved && s.price != null) {
      const outcome = s.price >= 0.5 ? 'YES' : 'NO';
      stmts.push(env.DB.prepare('UPDATE markets SET status=?, last_price=?, last_updated_at=?, resolve_at=COALESCE(?, resolve_at), reconciled_at=?, row_changed_at=? WHERE market_id=?')
        .bind('resolved', s.price, nowIso, s.closeTime, nowIso, nowIso, m.market_id));
      logStmts.push(resLogRow(env, m, 'resolved', 'open', outcome, s.price, s.settleTime, s.closeTime ?? m.close_at, nowIso));
      counts.resolved++;
    } else if (s && s.resolved) {
      // venue says resolved but no parseable settlement price — flip status, keep price, outcome PENDING (no guess)
      stmts.push(env.DB.prepare('UPDATE markets SET status=?, resolve_at=COALESCE(?, resolve_at), reconciled_at=?, row_changed_at=? WHERE market_id=?')
        .bind('resolved', s.closeTime, nowIso, nowIso, m.market_id));
      logStmts.push(resLogRow(env, m, 'resolved', 'open', 'PENDING', null, s.settleTime, s.closeTime ?? m.close_at, nowIso));
      counts.resolved++;
    } else if (s) {
      // Kalshi affirmatively SETTLED with no determinable yes/no outcome (void/cancelled) -> terminal 'closed'.
      // (Polymarket never lands here: the Poly pull only records UMA-resolved markets above.)
      stmts.push(env.DB.prepare('UPDATE markets SET status=?, reconciled_at=?, row_changed_at=? WHERE market_id=?')
        .bind('closed', nowIso, nowIso, m.market_id));
      logStmts.push(resLogRow(env, m, 'status_change', 'open', 'closed', null, s.settleTime, s.closeTime ?? m.close_at, nowIso));
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
  console.log(`reconcile: ${unseen.length} unseen / ${results.length} open -> resolved ${counts.resolved}, closed ${counts.closed}, left-open ${counts.left}, skipped ${counts.skipped}`);
  const feedErr = kalshiFeedOk && polyFeedOk ? null : `settled feed failed (kalshi ${kalshiFeedOk ? 'ok' : 'FAILED'}, polymarket ${polyFeedOk ? 'ok' : 'FAILED'}); ${counts.skipped} unseen markets skipped`;
  await recordRun(env, runId, 'reconcile', '', startedAt, unseen.length, counts.resolved + counts.closed, feedErr);
}

// ---- daily site-side results -> D1 ----------------------------------------
// Two GitHub jobs already fix data every morning but only in the R2 bundle the website renders from:
// the 06:30 UTC past-due sweep (statuses) and the 08:00 UTC eligibility screen. Until 2026-09-17 D1 —
// the API TMX pulls — only learned about either at the monthly reload, so site and API disagreed for
// weeks at a time (6,286 markets the site knew were settled still served as open). The jobs now also
// publish small JSON files to R2; at APPLY_UTC_HOUR the Worker fetches and applies them. Idempotent:
// only still-open rows change, resolution_log inserts are ON CONFLICT DO NOTHING, and a file is applied once.
const DATA_BASE_DEFAULT = 'https://pub-44522f32bfd047a386a961f5a624fd6f.r2.dev';
const DISPATCH_CRON = '45 * * * *';
const APPLY_UTC_HOUR = 15;     // GitHub schedules on this repo start ~5h late (06:30 job ≈ 12:00Z, 08:00 job ≈ 13:00Z); apply after both have landed
const SWEEP_FILE = 'status-sweep-latest.json';
const SCREEN_REGIME = 'ciro-26-0076';

type SweepChange = { market_id: string; status: string; last_price?: number | null; settled_at?: string | null; close_at?: string | null; resolve_at?: string | null };
type ApplyResult = { step: string; applied: number; total: number; file_generated_at: string | null; skipped?: string; error?: string };

async function applySweep(env: Env, runId: string, file = SWEEP_FILE): Promise<ApplyResult> {
  const startedAt = new Date().toISOString();
  const base = env.DATA_BASE ?? DATA_BASE_DEFAULT;
  try {
    const f: any = await fetchJson(`${base}/${file}?t=${Date.now()}`);
    const changes: SweepChange[] = Array.isArray(f?.changes) ? f.changes : [];
    const generatedAt: string | null = f?.generated_at ?? null;
    if (!generatedAt || isNaN(Date.parse(generatedAt))) throw new Error('sweep file has no generated_at');
    if (Date.parse(generatedAt) < Date.now() - 3 * 864e5) throw new Error(`sweep file stale (generated_at=${generatedAt}) — is freshness-daily.yml running?`);
    const last = await env.DB.prepare(`SELECT value FROM feed_meta WHERE key='sweep_last_applied'`).first<{ value: string }>();
    if (last?.value === generatedAt && file === SWEEP_FILE) {
      await recordRun(env, runId, 'sweep_apply', '', startedAt, changes.length, 0, null);
      return { step: 'sweep_apply', applied: 0, total: changes.length, file_generated_at: generatedAt, skipped: 'already applied' };
    }
    // Current D1 truth for the named markets, still-open rows only (chunked: D1 binds cap at 100).
    const cur = new Map<string, { event_id: string; platform: string; status: string; close_at: string | null }>();
    const ids = changes.map((c) => c.market_id).filter(Boolean);
    for (let i = 0; i < ids.length; i += 90) {
      const chunk = ids.slice(i, i + 90);
      const { results } = await env.DB.prepare(
        `SELECT market_id, event_id, platform, status, close_at FROM markets WHERE status IN ('open','closed') AND market_id IN (${chunk.map(() => '?').join(',')})`
      ).bind(...chunk).all<{ market_id: string; event_id: string; platform: string; status: string; close_at: string | null }>();
      for (const r of results) cur.set(r.market_id, r);
    }
    const nowIso = new Date().toISOString();
    const stmts: D1PreparedStatement[] = [];
    const logStmts: D1PreparedStatement[] = [];
    for (const c of changes) {
      const row = cur.get(c.market_id);
      if (!row || (c.status !== 'resolved' && c.status !== 'closed')) continue;
      if (row.status === 'closed' && c.status === 'closed') continue;   // already closed; only a resolution may move it
      const price = c.status === 'resolved' && typeof c.last_price === 'number' ? c.last_price : null;
      // last_updated_at (price_as_of) moves only when a settlement price is actually written.
      // UPDATE and its resolution_log row go into the SAME batch (a D1 batch is one transaction), so a mid-run failure
      // can never leave a resolved market without its outcome row.
      stmts.push(env.DB.prepare(`UPDATE markets SET status=?, last_price=COALESCE(?, last_price), last_updated_at=CASE WHEN ? IS NOT NULL THEN ? ELSE last_updated_at END, reconciled_at=?, row_changed_at=? WHERE market_id=? AND status=?`)
        .bind(c.status, price, price, nowIso, nowIso, nowIso, c.market_id, row.status));
      // to_value follows the existing vocabulary: YES / NO / PENDING for resolved rows, the status word for closes.
      const outcome = c.status === 'resolved' ? (price == null ? 'PENDING' : price >= 0.5 ? 'YES' : 'NO') : 'closed';
      stmts.push(resLogRow(env, { market_id: c.market_id, event_id: row.event_id, platform: row.platform },
        c.status === 'resolved' ? 'resolved' : 'status_change', row.status, outcome, price,
        c.settled_at ?? null, c.close_at ?? c.resolve_at ?? row.close_at, nowIso, 'clearmarket-sweep-apply'));
    }
    for (let i = 0; i < stmts.length; i += 100) await env.DB.batch(stmts.slice(i, i + 100));
    logStmts.length = 0;
    if (file === SWEEP_FILE) await setMeta(env, 'sweep_last_applied', generatedAt);
    await setMeta(env, 'sweep_last_run', nowIso);
    const applied = stmts.length / 2;
    await recordRun(env, runId, 'sweep_apply', '', startedAt, changes.length, applied, null);
    console.log(`sweep apply: ${applied} of ${changes.length} changes applied (file ${generatedAt})`);
    return { step: 'sweep_apply', applied, total: changes.length, file_generated_at: generatedAt };
  } catch (e) {
    const msg = errStr(e); console.error('sweep apply failed:', msg);
    await recordRun(env, runId, 'sweep_apply', '', startedAt, null, null, msg);
    return { step: 'sweep_apply', applied: 0, total: 0, file_generated_at: null, error: msg };
  }
}

// Eligibility screen -> D1. The screen run is deterministic and daily; a record is rewritten only when its
// status/reasons/category/version differ from what D1 holds, stamped with the run's screened_at. So
// screened_at on a record = when THAT record's result last changed; the run date lives in feed_meta.
async function applyScreen(env: Env, runId: string, regime = SCREEN_REGIME): Promise<ApplyResult> {
  const startedAt = new Date().toISOString();
  const base = env.DATA_BASE ?? DATA_BASE_DEFAULT;
  try {
    const [byMarket, summary]: [Record<string, any>, any] = await Promise.all([
      fetchJson(`${base}/eligibility-${regime}.json?t=${Date.now()}`),
      fetchJson(`${base}/eligibility-${regime}-summary.json?t=${Date.now()}`),
    ]);
    const version: string | undefined = summary?.screen_version;
    const screenedAt: string | undefined = summary?.screened_at;
    if (!version || !screenedAt) throw new Error('screen summary lacks screen_version/screened_at');
    const ids = Object.keys(byMarket ?? {});
    if (ids.length < 1000) throw new Error(`screen file suspiciously small (${ids.length} records) — not applied`);
    const norm = (r: any) => JSON.stringify({ s: r?.status ?? null, r: [...(r?.reasons ?? [])].sort(), c: r?.permitted_category ?? r?.bucket ?? null, v: r?.screen_version ?? null });
    const stmts: D1PreparedStatement[] = [];
    for (let i = 0; i < ids.length; i += 90) {
      const chunk = ids.slice(i, i + 90);
      const { results } = await env.DB.prepare(
        `SELECT market_id, eligibility_screens FROM markets WHERE market_id IN (${chunk.map(() => '?').join(',')})`
      ).bind(...chunk).all<{ market_id: string; eligibility_screens: string | null }>();
      for (const r of results) {
        const s = byMarket[r.market_id];
        const next = { regime: s.regime ?? regime, screen_version: version, status: s.status, reasons: s.reasons ?? [],
                       permitted_category: s.permitted_category ?? s.bucket ?? null, screened_at: s.screened_at ?? screenedAt };
        const have = parseJson(r.eligibility_screens, null);
        const haveRec = Array.isArray(have) ? have.find((x: any) => x?.regime === next.regime) : null;
        if (haveRec && norm(haveRec) === norm(next)) continue;
        const others = Array.isArray(have) ? have.filter((x: any) => x?.regime !== next.regime) : [];
        stmts.push(env.DB.prepare('UPDATE markets SET eligibility_screens = ?, row_changed_at = ? WHERE market_id = ?').bind(JSON.stringify([...others, next]), new Date().toISOString(), r.market_id));
      }
    }
    for (let i = 0; i < stmts.length; i += 100) await env.DB.batch(stmts.slice(i, i + 100));
    await setMeta(env, 'screen_last_run', screenedAt);
    await setMeta(env, 'screen_version', version);
    await setMeta(env, 'screen_records', String(ids.length));
    await recordRun(env, runId, 'screen_apply', '', startedAt, ids.length, stmts.length, null);
    console.log(`screen apply: ${stmts.length} of ${ids.length} records changed (screen ${version} @ ${screenedAt})`);
    return { step: 'screen_apply', applied: stmts.length, total: ids.length, file_generated_at: screenedAt };
  } catch (e) {
    const msg = errStr(e); console.error('screen apply failed:', msg);
    await recordRun(env, runId, 'screen_apply', '', startedAt, null, null, msg);
    return { step: 'screen_apply', applied: 0, total: 0, file_generated_at: null, error: msg };
  }
}

// Kalshi finalized -> resolved, from the same hourly snapshot (venue-authoritative status + result). Closes
// the gap the Worker's own settled-feed reconcile cannot (Kalshi 429s Cloudflare) and the daily past-due
// sweep does not reach (markets that settle BEFORE their deadline). Settlement time is not in the snapshot,
// so the resolution_log row carries the venue close_time on a deadline basis, never a fabricated settle time.
async function applyKalshiFinalized(env: Env, runId: string): Promise<ApplyResult> {
  const startedAt = new Date().toISOString();
  try {
    const snap: any = await fetchJson(`${env.DATA_BASE ?? DATA_BASE_DEFAULT}/kalshi-tracked-latest.json?t=${Date.now()}`, undefined, 2);
    if (!Array.isArray(snap?.markets)) throw new Error('snapshot has no markets[]');
    const age = (Date.now() - Date.parse(snap?.generated_at ?? '')) / 60e3;
    if (!(age <= 24 * 60)) throw new Error(`snapshot too old (${Math.round(age)} min)`);
    const fin = new Map<string, { result: string; ct: string | null }>();
    for (const m of snap.markets) {
      const r = String(m.r ?? '').toLowerCase();
      if (m.s === 'finalized' && (r === 'yes' || r === 'no')) fin.set(m.t, { result: r, ct: m.ct ?? null });
    }
    const { results } = await env.DB.prepare(
      `SELECT market_id, event_id, platform_market_id, status, close_at FROM markets WHERE platform='kalshi' AND status IN ('open','closed') AND platform_market_id IS NOT NULL`
    ).all<{ market_id: string; event_id: string; platform_market_id: string; status: string; close_at: string | null }>();
    const nowIso = new Date().toISOString();
    const stmts: D1PreparedStatement[] = []; const logStmts: D1PreparedStatement[] = [];
    for (const row of results) {
      const f = fin.get(row.platform_market_id);
      if (!f) continue;
      const price = f.result === 'yes' ? 1 : 0;
      stmts.push(env.DB.prepare(`UPDATE markets SET status='resolved', last_price=?, last_updated_at=?, reconciled_at=?, row_changed_at=? WHERE market_id=? AND status=?`).bind(price, nowIso, nowIso, nowIso, row.market_id, row.status));
      stmts.push(resLogRow(env, { market_id: row.market_id, event_id: row.event_id, platform: 'kalshi' }, 'resolved', row.status, f.result === 'yes' ? 'YES' : 'NO', price, null, f.ct ?? row.close_at, nowIso, 'clearmarket-kalshi-snapshot'));
    }
    for (let i = 0; i < stmts.length; i += 100) await env.DB.batch(stmts.slice(i, i + 100));
    logStmts.length = 0;
    const applied = stmts.length / 2;
    await recordRun(env, runId, 'kalshi_finalized', '', startedAt, fin.size, applied, null);
    if (applied) console.log(`kalshi finalized: ${applied} markets -> resolved (snapshot ${snap.generated_at})`);
    return { step: 'kalshi_finalized', applied, total: fin.size, file_generated_at: snap.generated_at ?? null };
  } catch (e) {
    const msg = errStr(e); console.error('kalshi finalized failed:', msg);
    await recordRun(env, runId, 'kalshi_finalized', '', startedAt, null, null, msg);
    return { step: 'kalshi_finalized', applied: 0, total: 0, file_generated_at: null, error: msg };
  }
}

// ---- on-time GitHub workflow dispatch --------------------------------------
// GitHub's cron scheduler on this repo starts jobs 20 min to 5 h late and skips hours outright; workflow_dispatch
// events start within seconds. The Worker's second cron (:45) fires the hourly Kalshi snapshot job so the :00
// marks pass finds a fresh file, plus the two daily jobs at their intended hours. The GitHub schedules stay as backup.
const GH_REPO = 'JDSource/clearmarket';
async function dispatchWorkflow(env: Env, runId: string, file: string): Promise<void> {
  const startedAt = new Date().toISOString();
  // No token yet: record the skip WITHOUT an error (an hourly 'degraded' email for a known, pending setup step is noise).
  // Kalshi staleness itself still alarms if GitHub's own schedule lags past the 3h window.
  if (!env.GH_DISPATCH_TOKEN) { await recordRun(env, runId, 'dispatch', file, startedAt, 0, 0, null); return; }
  try {
    const r = await fetch(`https://api.github.com/repos/${GH_REPO}/actions/workflows/${file}/dispatches`, {
      method: 'POST',
      headers: { Authorization: `Bearer ${env.GH_DISPATCH_TOKEN}`, Accept: 'application/vnd.github+json', 'User-Agent': 'clearmarket-dispatch/0.1', 'X-GitHub-Api-Version': '2022-11-28' },
      body: JSON.stringify({ ref: 'main' }),
    });
    if (r.status !== 204) throw new Error(`HTTP ${r.status}: ${(await r.text()).slice(0, 120)}`);
    await recordRun(env, runId, 'dispatch', file, startedAt, 1, 1, null);
  } catch (e) { await recordRun(env, runId, 'dispatch', file, startedAt, null, null, errStr(e)); }
}

// ---- /v1/marks — bulk + incremental pull ----------------------------------
// The way to consume the hourly cadence. Without since= it is the baseline (every market, 1,000 per
// page); with since=<ISO> it returns only markets whose price/volume or status changed after that
// instant. Keyset pagination on (changed_at, market_id) so a walk during the hourly refresh never
// duplicates or drops a row. changed_at = max(price change, status verification); last_checked_at is
// returned but does not by itself count as a change.
// The since=/cursor key is the Worker's own commit clock (row_changed_at), never an observation clock: a Kalshi row
// from the R2 snapshot carries the snapshot's time, which can trail the commit by up to 180 min.
const CHANGED_EXPR = `COALESCE(row_changed_at,'')`;
const b64 = (s: string) => btoa(unescape(encodeURIComponent(s)));
const unb64 = (s: string) => decodeURIComponent(escape(atob(s)));

async function listMarks(env: Env, url: URL): Promise<Response> {
  const p = url.searchParams;
  const limit = Math.min(Math.max(Number(p.get('limit') ?? 500) || 500, 1), 1000);
  const where: string[] = []; const args: any[] = [];
  const since = p.get('since');
  if (since) {
    if (isNaN(Date.parse(since))) return err(400, 'since must be an ISO-8601 timestamp', 'e.g. since=2026-09-17T13:00:00Z');
    where.push(`${CHANGED_EXPR} > ?`); args.push(new Date(since).toISOString());
  }
  const cursor = p.get('cursor');
  if (cursor) {
    let ca = '', mid = '';
    try {
      const parts = unb64(cursor).split('|');
      if (parts.length !== 2 || !parts[1] || (parts[0] && !/^\d{4}-\d{2}-\d{2}T[\d:.]+Z$/.test(parts[0]))) throw new Error('shape');
      [ca, mid] = parts;
    } catch { return err(400, 'bad cursor', 'Use the next_cursor value from the previous page unchanged.'); }
    where.push(`(${CHANGED_EXPR} > ? OR (${CHANGED_EXPR} = ? AND market_id > ?))`); args.push(ca, ca, mid);
  }
  const status = p.get('status');
  if (status) {
    if (!['open', 'resolved', 'closed'].includes(status)) return err(400, 'status must be open, resolved or closed');
    where.push('status = ?'); args.push(status);
  }
  const platform = p.get('platform');
  if (platform) {
    if (!KNOWN_PLATFORMS.includes(platform)) return err(400, `platform must be one of ${KNOWN_PLATFORMS.join(', ')}`);
    where.push('platform = ?'); args.push(platform);
  }
  const sql = `SELECT market_id, event_id, platform, platform_market_id, status, last_price, volume_24h_usd, volume_total_usd,
                      last_updated_at, last_checked_at, reconciled_at, resolve_at, close_at, ${CHANGED_EXPR} AS changed_at
                 FROM markets ${where.length ? 'WHERE ' + where.join(' AND ') : ''}
                ORDER BY changed_at, market_id LIMIT ?`;
  args.push(limit + 1);
  const { results } = await env.DB.prepare(sql).bind(...args).all<any>();
  const more = results.length > limit;
  const rows = more ? results.slice(0, limit) : results;
  const last = rows[rows.length - 1];
  const marks = rows.map((r) => ({
    market_id: r.market_id, event_id: r.event_id, platform: r.platform, platform_market_id: r.platform_market_id,
    status: r.status,
    last_price: num(r.last_price), implied_probability: num(r.last_price),
    volume_24h_usd: num(r.volume_24h_usd), volume_total_usd: num(r.volume_total_usd),
    price_as_of: r.last_updated_at ?? null,       // last time the price changed
    last_checked_at: r.last_checked_at ?? null,   // last time seen in a live venue feed (NULL = not since reload)
    reconciled_at: r.reconciled_at ?? null,       // last time status was verified against the venue
    changed_at: r.changed_at || null,             // when ClearMarket wrote the change (the since= key)
    resolve_at: r.resolve_at ?? null, close_at: r.close_at ?? null,
  }));
  return json({
    as_of: new Date().toISOString(), schema_version: SCHEMA_VERSION, since: since ? new Date(since).toISOString() : null,
    count: marks.length, next_cursor: more && last ? b64(`${last.changed_at ?? ''}|${last.market_id}`) : null,
    docs: 'Baseline: GET /v1/marks (page with next_cursor). Incremental: GET /v1/marks?since=<your previous as_of minus ~15 min> (rows are idempotent by market_id; the overlap covers writes still committing at as_of). changed_at = the ClearMarket write time and moves on price/volume, status and eligibility-screen changes. Filters: status, platform. Max 1000/page. Timestamps UTC.',
    _notice: NOTICE, marks,
  }, 200, { 'Cache-Control': 'no-store' });
}

// ---- /v1/status — feed integrity ------------------------------------------
// One object, computed from D1, that says whether each core pipeline is fresh. Same URL serves the
// hourly GitHub check that emails the operator and any consumer's DevOps poll. Core = prices, daily
// history, status reconcile, sweep apply, eligibility screen. Signal-side feeds are reported as non_core.
const THRESHOLDS = { prices_hours: 2, history_days: 1, reconcile_hours: 30, sweep_hours: 30, screen_days: 45 };
type CheckState = 'ok' | 'stale' | 'degraded';
type Check = { name: string; state: CheckState; as_of: string | null; age_hours: number | null; threshold: string; detail: Record<string, unknown> };

async function statusReport(env: Env): Promise<Response> {
  const now = Date.now();
  const ageH = (iso: string | null | undefined) => (iso && !isNaN(Date.parse(iso)) ? Math.round(((now - Date.parse(iso)) / 3600e3) * 10) / 10 : null);
  const two = isoAgo(THRESHOLDS.prices_hours);
  const [byStatus, openRows, hist, recon, runs, meta, vintage, spot, screenRow] = await Promise.all([
    env.DB.prepare('SELECT status, COUNT(*) n FROM markets GROUP BY status').all<{ status: string; n: number }>(),
    // Per venue: a venue can go dark while the other keeps the aggregate looking fresh (Kalshi did, for weeks).
    env.DB.prepare(`SELECT platform, MAX(last_updated_at) last_change, MAX(last_checked_at) last_checked, SUM(last_checked_at >= ?) checked_recent,
                           SUM(last_updated_at >= ?) changed_recent, SUM(last_checked_at IS NULL) never_checked, COUNT(*) n
                      FROM markets WHERE status='open' GROUP BY platform`).bind(two, two).all<any>(),
    env.DB.prepare(`SELECT day, COUNT(*) n, SUM(COALESCE(carried_forward,0)) carried, SUM(carried_forward IS NULL) unflagged
                      FROM marks_daily WHERE day = (SELECT MAX(day) FROM marks_daily)`).first<any>(),
    env.DB.prepare('SELECT MAX(reconciled_at) last FROM markets').first<{ last: string | null }>(),
    env.DB.prepare(`SELECT run_id, step, venue, started_at, finished_at, fetched, changed, error FROM cron_runs
                     WHERE (step, venue, started_at) IN (SELECT step, venue, MAX(started_at) FROM cron_runs GROUP BY step, venue)
                     ORDER BY step, venue`).all<any>().catch(() => ({ results: [] as any[] })),
    env.DB.prepare('SELECT key, value, updated_at FROM feed_meta').all<{ key: string; value: string | null; updated_at: string }>().catch(() => ({ results: [] as any[] })),
    env.DB.prepare('SELECT MAX(updated_at) v FROM events').first<{ v: string | null }>(),
    env.DB.prepare('SELECT MAX(as_of) as_of FROM spot').first<{ as_of: string | null }>().catch(() => null),
    env.DB.prepare('SELECT eligibility_screens FROM markets WHERE eligibility_screens IS NOT NULL LIMIT 1').first<{ eligibility_screens: string }>(),
  ]);
  const metaMap = new Map<string, string | null>((meta.results as any[]).map((r) => [r.key, r.value]));
  const counts: Record<string, number> = {}; for (const r of byStatus.results) counts[r.status] = r.n;

  const checks: Check[] = [];
  // 1. prices — the hourly promise, judged PER VENUE; the check is as stale as its stalest venue
  const venues: Record<string, any> = {};
  let pricesAsOf: string | null = null, pricesState: CheckState = 'ok';
  const totals = { open_markets: 0, seen_in_live_feed_last_2h: 0, price_changed_last_2h: 0, never_seen_since_reload: 0 };
  for (const v of openRows.results as any[]) {
    const asOf = v.last_checked ?? v.last_change ?? null; const age = ageH(asOf);
    // Kalshi arrives via the hourly R2 snapshot (observation clock = snapshot time), so its budget is that pipeline's window.
    const limitH = v.platform === 'kalshi' ? KALSHI_SNAPSHOT_MAX_AGE_MIN / 60 : THRESHOLDS.prices_hours;
    const st: CheckState = age == null || age > limitH ? 'stale' : 'ok';
    venues[v.platform] = { state: st, as_of: asOf, age_hours: age, threshold_hours: limitH, open_markets: v.n, seen_in_live_feed_last_2h: v.checked_recent ?? 0,
                           price_changed_last_2h: v.changed_recent ?? 0, never_seen_since_reload: v.never_checked ?? 0, last_price_change: v.last_change ?? null };
    if (st === 'stale') pricesState = 'stale';
    if (pricesAsOf == null || (asOf != null && asOf < pricesAsOf)) pricesAsOf = asOf;   // oldest venue clock
    totals.open_markets += v.n ?? 0; totals.seen_in_live_feed_last_2h += v.checked_recent ?? 0;
    totals.price_changed_last_2h += v.changed_recent ?? 0; totals.never_seen_since_reload += v.never_checked ?? 0;
  }
  if (!Object.keys(venues).length) pricesState = 'stale';
  checks.push({ name: 'prices', state: pricesState, as_of: pricesAsOf, age_hours: ageH(pricesAsOf),
    threshold: `per venue: polymarket ${THRESHOLDS.prices_hours}h (live feed), kalshi ${KALSHI_SNAPSHOT_MAX_AGE_MIN / 60}h (hourly snapshot window)`, detail: { ...totals, venues } });
  // 2. daily history — one snapshot per UTC day at 21:00; by the next day's start yesterday must exist
  const expectDay = new Date(now - 864e5).toISOString().slice(0, 10);
  const histOk = !!hist?.day && hist.day >= expectDay;
  checks.push({ name: 'history', state: histOk ? 'ok' : 'stale', as_of: hist?.day ?? null, age_hours: hist?.day ? ageH(`${hist.day}T21:00:00Z`) : null,
    threshold: `snapshot for ${expectDay} or later`, detail: { latest_day: hist?.day ?? null, rows: hist?.n ?? 0, carried_forward_rows: hist?.carried ?? null, unflagged_rows: hist?.unflagged ?? null } });
  // 3. status reconcile (Worker, 06:00 UTC) — judged from the run ledger (sweep/finalized also stamp reconciled_at, so the
  //    column alone cannot tell a stalled reconcile step from a healthy one); falls back to the column until the first run exists.
  const reconRun = (runs.results as any[]).find((r) => r.step === 'reconcile');
  const reconAsOf = reconRun ? (reconRun.finished_at ?? reconRun.started_at) : (recon?.last ?? null);
  const rAge = ageH(reconAsOf);
  checks.push({ name: 'reconcile', state: rAge == null || rAge > THRESHOLDS.reconcile_hours ? 'stale' : 'ok', as_of: reconAsOf, age_hours: rAge,
    threshold: `${THRESHOLDS.reconcile_hours}h`, detail: { source: reconRun ? 'cron_runs' : 'markets.reconciled_at', last_run_error: reconRun?.error ?? null, last_status_verification: recon?.last ?? null } });
  // 4. sweep apply (site-side sweep results into D1, 09:00 UTC)
  const sAsOf = metaMap.get('sweep_last_run') ?? null; const sAge = ageH(sAsOf);
  checks.push({ name: 'sweep_apply', state: sAge == null || sAge > THRESHOLDS.sweep_hours ? 'stale' : 'ok', as_of: sAsOf, age_hours: sAge,
    threshold: `${THRESHOLDS.sweep_hours}h`, detail: { file_generated_at: metaMap.get('sweep_last_applied') ?? null, ...(sAsOf ? {} : { reason: 'never_run' }) } });
  // 5. eligibility screen — run date from feed_meta once applyScreen has run; else the record stamp
  let screenAsOf = metaMap.get('screen_last_run') ?? null, screenVersion = metaMap.get('screen_version') ?? null;
  if (!screenAsOf && screenRow?.eligibility_screens) {
    const rec = parseJson(screenRow.eligibility_screens, null); const r0 = Array.isArray(rec) ? rec[0] : null;
    screenAsOf = r0?.screened_at ?? null; screenVersion = r0?.screen_version ?? null;
  }
  const scAge = ageH(screenAsOf ? `${screenAsOf.slice(0, 10)}T00:00:00Z` : null);
  checks.push({ name: 'screen', state: scAge == null || scAge > THRESHOLDS.screen_days * 24 ? 'stale' : 'ok', as_of: screenAsOf, age_hours: scAge,
    threshold: `${THRESHOLDS.screen_days}d`, detail: { regime: SCREEN_REGIME, screen_version: screenVersion, records: metaMap.get('screen_records') ?? null } });

  // degraded: data still within threshold but the latest run of a step (within 48h) reported an error
  const recentCut = isoAgo(48);
  const latestStart: Record<string, string> = {};
  for (const r of runs.results as any[]) if ((r.started_at ?? '') > (latestStart[r.step] ?? '')) latestStart[r.step] = r.started_at;
  const failing = (runs.results as any[]).filter((r) => r.error && (r.started_at ?? '') >= recentCut && r.started_at === latestStart[r.step]);
  const stepsFor: Record<string, string[]> = { prices: ['marks', 'dispatch'], history: ['snapshot'], reconcile: ['reconcile', 'kalshi_finalized'], sweep_apply: ['sweep_apply'], screen: ['screen_apply'] };
  for (const c of checks) if (c.state === 'ok' && failing.some((r) => stepsFor[c.name].includes(r.step))) c.state = 'degraded';
  const rank: Record<CheckState, number> = { ok: 0, degraded: 1, stale: 2 };
  const overall = checks.reduce<CheckState>((w, c) => (rank[c.state] > rank[w] ? c.state : w), 'ok');

  return json({
    service: 'clearmarket-api', as_of: new Date(now).toISOString(), schema_version: SCHEMA_VERSION,
    state: overall,
    checks,
    dataset: { bundle_vintage: vintage?.v ?? null, markets_by_status: counts, notes: 'bundle_vintage = enrichment reload; grades/links change only then. Prices hourly; statuses daily.' },
    runs: runs.results,
    non_core: { spot: { as_of: spot?.as_of ?? null, age_hours: ageH(spot?.as_of), note: 'CM Signal context feed, not part of the reference dataset' } },
    docs: 'state = worst of checks[]. ok | degraded (fresh, but the latest run of a step reported an error) | stale (a core pipeline is past its threshold). Timestamps UTC.',
  }, 200, { 'Cache-Control': 'no-store' });
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

// MCP server card — the .well-known discovery convention MCP registries probe.
// Observed demand in the miss log (2026-07-18/19): AgenstryBot, AgentRegistryFloor-
// Validation, and AgentSEO all requested /.well-known/mcp.json within 36h of the
// miss log shipping; aliases below are the exact probed variants. Single-sourced
// from mcp.ts exports (built lazily per request to sidestep the index↔mcp module
// cycle at init time). Static payload otherwise — no upkeep beyond mcp.ts itself.
const MCP_MANIFEST_PATHS = new Set([
  '/.well-known/mcp.json', '/.well-known/mcp', '/.well-known/mcp/server-card.json',
  '/mcp/.well-known/mcp', '/mcp.json',
]);
const mcpManifest = () => ({
  name: SERVER_INFO.name,
  title: 'ClearMarket — prediction-market reference layer',
  description:
    'Read-only MCP server for graded prediction-market reference data (Kalshi + Polymarket): ' +
    'Resolution Clarity Grades (A/B/C), committed resolution sources with provenance, ' +
    'cross-venue question linking, live prices, and CM Signal wires. Open, no key, no payment.',
  version: SERVER_INFO.version,
  protocol_version: PROTOCOL_VERSION,
  endpoint: 'https://api.clearmarket.fyi/mcp',
  transport: { type: 'streamable-http', note: 'Stateless JSON-RPC 2.0 over POST; no session required.' },
  authentication: { type: 'none' },
  tools: TOOLS.map((t: any) => ({ name: t.name, description: t.description })),
  docs: 'https://clearmarket.fyi/for-data/',
  terms: 'Attribution required. clearmarket.fyi',
  related: {
    agent_card: 'https://api.clearmarket.fyi/.well-known/agent-card.json',
    x402: 'https://api.clearmarket.fyi/.well-known/x402',
    api_catalog: 'https://api.clearmarket.fyi/.well-known/api-catalog',
    llms_txt: 'https://clearmarket.fyi/llms.txt',
  },
});

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
        { href: 'https://api.clearmarket.fyi/openapi.json', type: 'application/vnd.oai.openapi+json', title: 'OpenAPI 3.1 spec (component schemas = the canonical JSON Schemas)' },
        { href: 'https://clearmarket.fyi/schema.json', type: 'application/json', title: 'ClearMarket 4-table schema (events/markets/marks/resolution_log)' },
      ],
      'service-doc': [
        { href: 'https://clearmarket.fyi/for-data/', type: 'text/html', title: 'ClearMarket for data buyers' },
        { href: 'https://clearmarket.fyi/llms.txt', type: 'text/plain', title: 'LLM-readable index' },
      ],
      'service-meta': [
        { href: 'https://api.clearmarket.fyi/.well-known/agent-card.json', type: 'application/json', title: 'A2A agent card' },
        { href: 'https://api.clearmarket.fyi/.well-known/mcp.json', type: 'application/json', title: 'MCP server card' },
        { href: 'https://api.clearmarket.fyi/.well-known/x402', type: 'application/json', title: 'x402 pricing manifest (free)' },
        { href: 'https://api.clearmarket.fyi/health', type: 'application/json', title: 'Live status + filter vocabulary' },
      ],
    },
  ],
};

// ---- router ------------------------------------------------------------
const worker = {
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
        schema: SCHEMA_VERSION,
        status_url: '/v1/status',
        marks_url: '/v1/marks?since=<ISO>',
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

    if (path === '/v1/status') { logCall(env, ctx, req, 'rest', 'status'); return statusReport(env); }
    if (path === '/v1/marks') { logCall(env, ctx, req, 'rest', 'list_marks', { since: url.searchParams.get('since') }); return listMarks(env, url); }

    // Operator trigger for a pipeline step (backfills, re-runs after a fix). 404 unless ADMIN_TOKEN is configured.
    if (path === '/v1/admin/run') {
      logCall(env, ctx, req, 'rest', 'admin', { step: url.searchParams.get('step'), authed: req.headers.get('Authorization') === `Bearer ${env.ADMIN_TOKEN ?? ''}` });
      if (!env.ADMIN_TOKEN) return err(404, 'Not found', 'Try /health or /v1/events');
      if (req.method !== 'POST') return err(405, 'POST only');
      if (req.headers.get('Authorization') !== `Bearer ${env.ADMIN_TOKEN}`) return err(401, 'Unauthorized');
      const step = url.searchParams.get('step') ?? '';
      const runId = `manual-${new Date().toISOString()}`;
      let out: unknown;
      if (step === 'sweep_apply') out = await applySweep(env, runId, url.searchParams.get('file') ?? undefined);
      else if (step === 'screen_apply') out = await applyScreen(env, runId);
      else if (step === 'kalshi_finalized') out = await applyKalshiFinalized(env, runId);
      else if (step === 'reconcile') {
        const r = await refreshMarks(env, runId);
        if (r.venueOk.polymarket) { await reconcileStatus(env, r.seenOpen, runId); out = { step, done: true, seen: r.seenOpen.size }; }
        else out = { step, done: false, reason: 'polymarket live feed failed this run' };
      }
      else if (step === 'marks') { const r = await refreshMarks(env, runId); out = { step, seen: r.seenOpen.size, venue_ok: r.venueOk }; }
      else if (step === 'snapshot') { await snapshotDaily(env, runId); out = { step, done: true }; }
      else return err(400, 'unknown step', 'sweep_apply | screen_apply | kalshi_finalized | reconcile | marks | snapshot');
      return json({ run_id: runId, result: out });
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
    if (path === '/.well-known/x402' || path === '/.well-known/x402.json') {
      logCall(env, ctx, req, 'rest', 'x402_manifest');
      return json(X402_MANIFEST, 200, { 'cache-control': 'public, max-age=3600' });
    }

    // OpenAPI 3.1 spec — the machine-readable API description codegen tools and agents ask for
    // (observed 404s: /openapi.json from generic clients, /swagger.json probes). Component
    // schemas are the canonical /schema JSON Schemas, imported at build time.
    if (path === '/openapi.json' || path === '/.well-known/openapi.json' || path === '/swagger.json') {
      logCall(env, ctx, req, 'rest', 'openapi', path);
      return json(OPENAPI_SPEC, 200, { 'cache-control': 'public, max-age=3600' });
    }

    // agents.json — directory-facing manifest; AgenstryBot probes six path variants daily.
    if (AGENTS_JSON_PATHS.has(path)) {
      logCall(env, ctx, req, 'rest', 'agents_json', path);
      return json(AGENTS_MANIFEST, 200, { 'cache-control': 'public, max-age=3600' });
    }
    if (path === '/agents.txt') {
      logCall(env, ctx, req, 'rest', 'agents_json', path);
      return new Response(
        'ClearMarket — prediction-market reference layer (open, free, attribution required)\n' +
        'manifest: https://api.clearmarket.fyi/agents.json\n' +
        'openapi:  https://api.clearmarket.fyi/openapi.json\n' +
        'mcp:      https://api.clearmarket.fyi/mcp\n' +
        'a2a:      https://api.clearmarket.fyi/a2a\n' +
        'llms.txt: https://clearmarket.fyi/llms.txt\n',
        { status: 200, headers: { 'Content-Type': 'text/plain; charset=utf-8', 'cache-control': 'public, max-age=3600', ...CORS } },
      );
    }

    // llms.txt on the API host — agent crawlers probe it here (observed 404s from AgentSEO
    // and friends). The canonical file is build-time generated on the site (coverage counts
    // come from the bundle), so proxy it with an edge cache rather than shipping a copy.
    if (path === '/llms.txt' || path === '/.well-known/llms.txt') {
      logCall(env, ctx, req, 'rest', 'llms_txt', path);
      const res = await fetch('https://clearmarket.fyi/llms.txt', {
        cf: { cacheTtl: 3600, cacheEverything: true },
      });
      return new Response(res.body, {
        status: res.status,
        headers: { 'Content-Type': 'text/plain; charset=utf-8', 'cache-control': 'public, max-age=3600', ...CORS },
      });
    }

    if (MCP_MANIFEST_PATHS.has(path)) {
      logCall(env, ctx, req, 'rest', 'mcp_manifest', path);
      return json(mcpManifest(), 200, { 'cache-control': 'public, max-age=3600' });
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

    // Miss log — unknown paths are a demand signal, not noise: agents and
    // assistants request endpoints their priors say should exist here
    // (hallucinated URLs, probed capabilities). The date this log stops being
    // empty of real asks is a market-timing signal. Scanner spam is filtered
    // so the table stays demand data, not a security log.
    if (!SCANNER_NOISE.test(path)) logCall(env, ctx, req, 'miss', 'not_found', path + url.search);
    return err(404, 'Not found', 'Try /health or /v1/events');
  },

  // Hourly cron (0 * * * *). Every hour: refresh prices + stamp last_checked_at. Then by UTC hour:
  //   06 reconcile statuses (Worker, venue-confirmed) · 09 apply the site-side sweep + screen files · 21 EOD snapshot.
  // Each step is isolated: one failing never skips the others, and every outcome lands in cron_runs.
  async scheduled(event: any, env: Env, ctx: any): Promise<void> {
    const when = new Date(event?.scheduledTime ?? Date.now());   // the slot this run is FOR, even if it fired late
    const hour = when.getUTCHours();
    const runId = when.toISOString().slice(0, 13);   // one id per UTC hour
    if (event?.cron === DISPATCH_CRON) {
      ctx.waitUntil((async () => {
        await dispatchWorkflow(env, runId, 'kalshi-marks.yml');
        await dispatchWorkflow(env, runId, 'status-check.yml');   // the alarm itself must not depend on GitHub's lagging scheduler
        if (hour === 6) await dispatchWorkflow(env, runId, 'freshness-daily.yml');
        if (hour === 7) await dispatchWorkflow(env, runId, 'cm-signal-daily.yml');
      })());
      return;
    }
    ctx.waitUntil((async () => {
      let seen: Set<string> | null = null;
      let venueOk: VenueOk = { kalshi: false, polymarket: false };
      try { const r = await refreshMarks(env, runId); seen = r.seenOpen; venueOk = r.venueOk; }
      catch (e) { console.error('refreshMarks failed', e); await recordRun(env, runId, 'marks', '', new Date().toISOString(), null, null, errStr(e)); }

      if (hour === EOD_UTC_HOUR) {
        try { await snapshotDaily(env, runId); }
        catch (e) { console.error('snapshotDaily failed', e); await recordRun(env, runId, 'snapshot', '', new Date().toISOString(), null, null, errStr(e)); }
      }
      if (hour === RECONCILE_UTC_HOUR) {
        if (seen && venueOk.polymarket) {   // Kalshi is excluded inside reconcileStatus (snapshot-reconciled)
          try { await reconcileStatus(env, seen, runId); }
          catch (e) { console.error('reconcileStatus failed', e); await recordRun(env, runId, 'reconcile', '', new Date().toISOString(), null, null, errStr(e)); }
        } else {
          // A failed venue fetch would read as "every market delisted" — never reconcile on a partial snapshot.
          await recordRun(env, runId, 'reconcile', '', new Date().toISOString(), null, null, `skipped: polymarket live feed failed this hour`);
        }
      }
      if (hour === APPLY_UTC_HOUR) {
        await applySweep(env, runId);
        await applyScreen(env, runId);
        await applyKalshiFinalized(env, runId);
        try { await env.DB.prepare('DELETE FROM cron_runs WHERE started_at < ?').bind(isoAgo(24 * 45)).run(); } catch {}
      }
      try { await refreshSpot(env); } catch (e) { console.warn('refreshSpot failed', errStr(e)); }
    })());
  },
};

// Every request goes through one try/catch so a thrown D1/venue error returns JSON with a request id
// instead of Cloudflare's HTML 1101 page (which a consumer's parser cannot read).
export default {
  ...worker,
  async fetch(req: Request, env: Env, ctx: any): Promise<Response> {
    try {
      return await worker.fetch(req, env, ctx);
    } catch (e) {
      const rid = crypto.randomUUID();
      console.error(`request ${rid} ${req.method} ${new URL(req.url).pathname} failed:`, (e as any)?.stack ?? e);
      return json({ error: 'Internal error', request_id: rid, hint: 'Retry. If it persists, email hello@clearmarket.fyi with this request_id.' }, 500, { 'X-Request-Id': rid });
    }
  },
  scheduled: worker.scheduled,
};
