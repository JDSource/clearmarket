/**
 * ClearMarket MCP server — agent-first surface, same D1 data as the REST API.
 *
 * Minimal stateless Streamable-HTTP transport: client POSTs JSON-RPC 2.0 to /mcp,
 * server replies application/json. No Durable Objects (stays on Workers free tier),
 * no SDK. Read-only + OPEN (no auth) by design — agent adoption is the goal.
 *
 * Methods: initialize | notifications/initialized | tools/list | tools/call.
 * Tools (6): list_events, get_event, get_market, list_upcoming_catalysts, list_signals, get_signal.
 * (Signal tools fetch the published static /signals feed — wires stay single-sourced as content.)
 *
 * NB: tool descriptions are how an agent decides to call us — lead with the
 * differentiators (graded resolution clarity, cross-venue links, provenance).
 * These are solid drafts pending the copy-optimization pass.
 */
import { Env, num, parseJson, marketOut, marketConcise, findMarketRow, eventSummary, loadCalendar, windowCatalysts, logCall, provenance, NOTICE } from './index';

export const PROTOCOL_VERSION = '2025-06-18';
export const SERVER_INFO = { name: 'clearmarket', version: '0.2.0' };
const CATEGORIES = ['economics', 'financials', 'crypto', 'companies', 'technology', 'politics', 'geopolitics', 'health', 'climate'];

const CORS = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
  'Access-Control-Allow-Headers': 'Authorization, Content-Type, Mcp-Session-Id, Mcp-Protocol-Version',
};

// ---- tool catalog ------------------------------------------------------
// Order matters: LLM tool-selection has a documented "first-tool" positional bias, so the safe
// entry point (works with no args, can't misfire) goes first. Four tools only — no redundant
// `search` tool (it collapsed into list_events' `q`; overlapping tools measurably hurt selection).
export const TOOLS = [
  {
    name: 'list_events',
    description:
      'Browse or search ClearMarket prediction-market events. Filter by category, platform, Resolution Clarity ' +
      'Grade, or free-text `q`. `q` is token-AND across question + tags, so SHORT KEYWORD queries match best ' +
      '("microstrategy bitcoin", "fed rate") — natural-language phrases often return nothing. Returns compact ' +
      'graded summaries: slug, question, venues_covered, primary grade, rcg_score (0-100, for ranking clarity), ' +
      'last_price, and status (open / resolved). Start here when you have a topic but not a slug; then call ' +
      'get_event for the full graded record. Categories: ' + CATEGORIES.join(', ') + '.',
    inputSchema: {
      type: 'object',
      properties: {
        q: { type: 'string', description: 'Free-text search across event questions. Omit to list the whole filtered universe.' },
        category: { type: 'string', enum: CATEGORIES },
        platform: { type: 'string', enum: ['kalshi', 'polymarket'] },
        grade: { type: 'string', enum: ['A', 'B', 'C'], description: 'Resolution Clarity Grade of the primary market.' },
        limit: { type: 'integer', minimum: 1, maximum: 100, default: 50 },
        offset: { type: 'integer', minimum: 0, default: 0 },
      },
    },
  },
  {
    name: 'get_event',
    description:
      'Fetch the full ClearMarket record for one event by slug: the canonical question, every market in this event\'s ' +
      'single-venue bundle, each market\'s current price + Resolution Clarity Grade (A/B/C) + resolution-source ' +
      'provenance, the canonical question_id where the question is linked across venues/events (null otherwise; also_on lists the same question priced on the other venue, when it trades there), and the upcoming catalyst dates that move it before it resolves. ' +
      'In the default detail="full", each market in the bundle is FULLY detailed (grade, rcg.caps, provenance, direction, settlement_style, also_on) — you do not need a separate get_market call for markets already in this event. ' +
      'Note: a shared question_id means same topic across venues; in rare cases it links structurally-different contracts (e.g. a "hike" vs a "cut-count" market), so verify the contract shape before treating two as an arbitrage pair. ' +
      'Use when you need the authoritative, graded view of a SPECIFIC event — including its cross-venue twins via also_on — before reasoning about or ' +
      'acting on a prediction market. If you only have a topic (not a slug), call list_events first. ' +
      'Set detail="concise" for a quick grade/price/source check (each market trimmed to the essentials — much smaller for events with many markets); ' +
      'use the default detail="full" when you need every market\'s rules, contract shape, and complete provenance.',
    inputSchema: {
      type: 'object',
      properties: {
        slug: { type: 'string', description: 'Event slug (e.g. "kxgdpyear-26") or CM event id (CM-EVT-…).' },
        detail: { type: 'string', enum: ['concise', 'full'], default: 'full', description: 'concise = essentials only (grade, price, source, also_on per market); full = the complete record. Default full.' },
      },
      required: ['slug'],
    },
  },
  {
    name: 'get_market',
    description:
      'Fetch one market and judge whether its price can be trusted. Accepts whatever id you have: a ClearMarket id ' +
      '(CM-MKT-…), a venue-native market id or Kalshi ticker, or a market URL (best-effort — Kalshi tickers / a ' +
      'native id in the path resolve; for Polymarket pass the conditionId, not the slug URL). Returns: raw ' +
      'question, current price / implied probability, the Resolution Clarity Grade with rcg.score (0-100) and ' +
      'rcg.caps (a cap such as "uncommitted_placeholder" hard-limits the grade — that is why a single-source market ' +
      'can still be C), full resolution provenance (arbitration_model = who resolves it, named source, source_type, ' +
      'and a graded source_status on EVERY market: named / no-committed-source / none / unknown), the contract ' +
      'shape (direction, settlement_style, threshold), ' +
      'the canonical question_id where linked, and also_on (the same question priced on other venues). The returned ' +
      'market_id is ALWAYS the canonical ClearMarket id (CM-MKT-…) — store and reuse THAT, not the venue id. Use ' +
      'before trusting or acting on a price.',
    inputSchema: {
      type: 'object',
      properties: { market_id: { type: 'string', description: 'A ClearMarket id (CM-MKT-…), a venue-native market id / Kalshi ticker, or a market URL (best-effort: Kalshi URLs resolve; for Polymarket pass the conditionId).' } },
      required: ['market_id'],
    },
  },
  {
    name: 'list_upcoming_catalysts',
    description:
      'List scheduled catalysts (CPI, jobs, FOMC, GDP, large-cap earnings) in the next N days that move ' +
      'prediction-market prices BEFORE those markets resolve — a cross-event view across the whole calendar. ' +
      'Each entry is provenanced to its authoritative source (BLS, Fed, etc.). Use to find what scheduled events ' +
      'will reprice the prediction-market universe soon.',
    inputSchema: {
      type: 'object',
      properties: { days: { type: 'integer', minimum: 1, maximum: 365, default: 30 } },
    },
  },
  {
    name: 'list_signals',
    description:
      'Browse the CM Signal daily wire — short, structured prediction-market bulletins (the price is the lede, ' +
      'news is context). Filter by event_id (every wire touching a specific event), category, venue, or detection ' +
      'type (news_cycle, cross_venue_divergence, benchmark_drift, volume_spike). Returns compact records, newest ' +
      'first; call get_signal for the full bulletin. Use to find ClearMarket\'s editorial read on what is moving.',
    inputSchema: {
      type: 'object',
      properties: {
        event_id: { type: 'string', description: 'Return only wires that target or link to this CM event_id.' },
        // Filters the wire's category_tag (the signal-type classification) — NOT the 9 thematic
        // event categories. Free string (case-insensitive) because the tag set drifts with the
        // generators; common values listed below. (Was wrongly enum'd to the thematic CATEGORIES,
        // which never matches category_tag -> the filter always returned empty.)
        category: { type: 'string', description: 'Signal category tag (case-insensitive): VS_BENCHMARK_DRIFT | CROSS_VENUE_DIVERGENCE | VOLUME_SPIKE | MOMENTUM_REPRICING | PRE_EVENT_PRICING. For thematic filtering use list_events.' },
        venue: { type: 'string', enum: ['kalshi', 'polymarket'] },
        detection_path: { type: 'string', enum: ['news_cycle', 'cross_venue_divergence', 'benchmark_drift', 'volume_spike'] },
        limit: { type: 'integer', minimum: 1, maximum: 100, default: 30 },
      },
    },
  },
  {
    name: 'get_signal',
    description:
      'Fetch one full CM Signal wire by slug: headline, the 3-5 structured bullets, atomic claims with per-field ' +
      'provenance tiers, the target + linked events, primary and related markets with prices, and sources. Use ' +
      'when you have a wire slug (from list_signals) and need the complete bulletin with its proof chain.',
    inputSchema: {
      type: 'object',
      properties: { slug: { type: 'string', description: 'Wire slug, e.g. "us-iran-nuclear-deal-before-2027-polymarket-77-2026-05-29".' } },
      required: ['slug'],
    },
  },
];

// ---- data builders (open; full universe; no auth) ----------------------
async function buildEvent(env: Env, slug: string, detail: string = 'full'): Promise<any | null> {
  // Resolve by slug OR CM event id — agents cite the event_id list_events returns, then look
  // it up here; slug-only made that round-trip dead-end (REST got this fix in PR #27).
  const e = await env.DB.prepare('SELECT * FROM events WHERE (slug = ? OR event_id = ?) AND published = 1').bind(slug, slug).first<any>();
  if (!e) return null;
  const { results: mkts } = await env.DB.prepare('SELECT * FROM markets WHERE event_id = ?').bind(e.event_id).all<any>();
  const venues = [...new Set(mkts.map((m) => m.platform))].sort();
  const cutoff = mkts.reduce<string | null>((max, m) => {
    const d = (m.close_at ?? '').slice(0, 10);
    return d && (!max || d > max) ? d : max;
  }, null);
  const cal = await loadCalendar(env);
  const catalysts = windowCatalysts(parseJson(e.catalyst_types, []) as string[], cal, cutoff, parseJson(e.catalyst_dates, []) as any[]);
  return {
    event_id: e.event_id, slug: e.slug, question: e.question, category: e.category,
    event_type: e.event_type ?? 'BINARY', ladder_distribution: parseJson(e.ladder_distribution, null),
    tags: parseJson(e.tags, []), catalyst_types: parseJson(e.catalyst_types, []), catalyst_dates: catalysts,
    editorial_notes: e.editorial_notes, venues_covered: venues, primary_market_id: e.primary_market_id,
    markets: mkts.map(detail === 'concise' ? marketConcise : marketOut),
    _provenance: provenance(e.event_id),
  };
}

async function buildList(env: Env, p: Record<string, any>): Promise<any> {
  const where = ['e.published = 1'];
  const args: unknown[] = [];
  if (p.category) { where.push('LOWER(e.category) = ?'); args.push(String(p.category).toLowerCase()); }
  // platform + grade filter IN SQL (was post-pagination -> silently empty when the first page was
  // one venue / no A-grades; an agent then wrongly concluded "no Polymarket / no A-grade data").
  if (p.platform) { where.push('e.venue = ?'); args.push(String(p.platform).toLowerCase()); } // direct column, not a correlated EXISTS (which 500'd on the late-sorted Polymarket rows)
  if (p.grade) { where.push('EXISTS (SELECT 1 FROM markets m WHERE m.market_id = e.primary_market_id AND m.resolution_clarity_grade = ?)'); args.push(String(p.grade).toUpperCase()); }
  // q = token-AND across question + tags (was single contiguous-substring -> "us recession" -> []).
  if (p.q) { for (const t of String(p.q).trim().split(/\s+/).filter(Boolean).slice(0, 6)) { where.push('(e.question LIKE ? OR e.tags LIKE ?)'); args.push(`%${t}%`, `%${t}%`); } }
  const limit = Math.min(Math.max(Number(p.limit ?? 50) || 50, 1), 100); // D1 binds <=100 params (one per event in the markets query)
  const offset = Math.max(Number(p.offset ?? 0) || 0, 0);
  // total = full count under the filters (count below is just this page), so the agent knows the
  // real universe size and when to stop paging instead of reading a 100-row page as "100 total".
  const total = (await env.DB.prepare(`SELECT COUNT(*) AS n FROM events e WHERE ${where.join(' AND ')}`).bind(...args).first<{ n: number }>())?.n ?? 0;
  const { results: evs } = await env.DB.prepare(
    `SELECT * FROM events e WHERE ${where.join(' AND ')} ORDER BY e.updated_at DESC LIMIT ? OFFSET ?`
  ).bind(...args, limit, offset).all<any>();
  if (!evs.length) return { count: 0, total, limit, offset, events: [] };
  const ids = evs.map((e) => e.event_id);
  const ph = ids.map(() => '?').join(',');
  const { results: mkts } = await env.DB.prepare(
    `SELECT market_id, event_id, platform, last_price, last_updated_at, resolution_clarity_grade, rcg_score, status FROM markets WHERE event_id IN (${ph})`
  ).bind(...ids).all<any>();
  const byEvent = new Map<string, any[]>();
  for (const m of mkts) (byEvent.get(m.event_id) ?? byEvent.set(m.event_id, []).get(m.event_id)!).push(m);
  const out = evs.map((e) => eventSummary(e, byEvent.get(e.event_id) ?? []));
  return { count: out.length, total, limit, offset, events: out };
}

async function buildMarket(env: Env, raw: string): Promise<any | null> {
  // Shared resolver (CM id → venue-native id/ticker → best-effort URL). Returned market_id is
  // always the canonical CM id — the venue id is just an on-ramp.
  const m = await findMarketRow(env, raw);
  return m ? { ...marketOut(m), _provenance: provenance(m.market_id) } : null;
}

async function buildUpcoming(env: Env, days: number): Promise<any> {
  const d = Math.min(Math.max(days || 30, 1), 365);
  const today = new Date().toISOString().slice(0, 10);
  const until = new Date(Date.now() + d * 864e5).toISOString().slice(0, 10);
  const cal = await loadCalendar(env);
  const items: any[] = [];
  for (const [type, c] of cal) for (const dt of c.dates) if (dt >= today && dt <= until) items.push({ date: dt, type, label: c.label, source_url: c.source_url });
  items.sort((a, b) => (a.date < b.date ? -1 : a.date > b.date ? 1 : 0));
  return { window_days: d, from: today, to: until, count: items.length, catalysts: items };
}

// ---- signals (fetched from the published static feed; wires are single-sourced as content) ----
function signalsBase(env: Env): string {
  return (env.SIGNALS_BASE || 'https://clearmarket.fyi').replace(/\/+$/, '');
}

async function buildSignalsList(env: Env, p: Record<string, any>): Promise<any> {
  const res = await fetch(`${signalsBase(env)}/signals.json`, { cf: { cacheTtl: 300 } } as any);
  if (!res.ok) return { error: `Signal feed unavailable (${res.status}).`, count: 0, signals: [] };
  const feed = await res.json<any>();
  let items: any[] = feed.signals ?? [];
  if (p.event_id) items = items.filter((s) => s.target_event_id === p.event_id || (s.linked_event_ids ?? []).includes(p.event_id));
  if (p.category) { const c = String(p.category).toUpperCase(); items = items.filter((s) => (s.category_tag ?? '').toUpperCase() === c); }
  if (p.venue) items = items.filter((s) => (s.venues ?? []).includes(p.venue));
  if (p.detection_path) items = items.filter((s) => s.detection_path === p.detection_path);
  const limit = Math.min(Math.max(Number(p.limit ?? 30) || 30, 1), 100);
  return { count: Math.min(items.length, limit), total_matched: items.length, signals: items.slice(0, limit) };
}

async function buildSignal(env: Env, slug: string): Promise<any | null> {
  const res = await fetch(`${signalsBase(env)}/signals/${encodeURIComponent(slug)}.json`, { cf: { cacheTtl: 300 } } as any);
  if (res.status === 404) return null;
  if (!res.ok) return { error: `Signal fetch failed (${res.status}).` };
  return res.json();
}

// ---- tool dispatch -----------------------------------------------------
export async function callTool(env: Env, name: string, a: Record<string, any>): Promise<any> {
  switch (name) {
    case 'get_event': {
      const r = await buildEvent(env, String(a.slug ?? ''), a.detail === 'concise' ? 'concise' : 'full');
      return r ?? { error: `No event with slug "${a.slug}". Try search or list_events.` };
    }
    case 'list_events': return buildList(env, a);
    case 'get_market': {
      const key = String(a.market_id ?? a.market ?? '');
      const r = await buildMarket(env, key);
      return r ?? { error: `No market matched "${key}". Pass a ClearMarket id (CM-MKT-…), a venue-native market id / Kalshi ticker, or a market URL — or use list_events to find it by topic.` };
    }
    case 'list_upcoming_catalysts': return buildUpcoming(env, Number(a.days ?? 30));
    case 'list_signals': return buildSignalsList(env, a);
    case 'get_signal': {
      const r = await buildSignal(env, String(a.slug ?? ''));
      return r ?? { error: `No wire with slug "${a.slug}". Try list_signals.` };
    }
    default: throw new Error(`Unknown tool: ${name}`);
  }
}

// ---- JSON-RPC plumbing -------------------------------------------------
const rpcResult = (id: any, result: any) => ({ jsonrpc: '2.0', id, result });
const rpcError = (id: any, code: number, message: string) => ({ jsonrpc: '2.0', id, error: { code, message } });

export async function handleMcp(req: Request, env: Env, ctx: { waitUntil(p: Promise<any>): void }): Promise<Response> {
  if (req.method === 'OPTIONS') return new Response(null, { status: 204, headers: CORS });
  if (req.method !== 'POST') {
    return new Response(JSON.stringify(rpcError(null, -32600, 'Use POST with a JSON-RPC 2.0 body.')), {
      status: 405, headers: { 'Content-Type': 'application/json', ...CORS },
    });
  }

  let msg: any;
  try { msg = await req.json(); } catch {
    return json(rpcError(null, -32700, 'Parse error'));
  }

  // notifications (no id) — ack with 202, no body
  if (msg && msg.id === undefined) return new Response(null, { status: 202, headers: CORS });

  const { id, method, params } = msg ?? {};
  try {
    if (method === 'initialize') {
      return json(rpcResult(id, {
        protocolVersion: PROTOCOL_VERSION,
        capabilities: { tools: {} },
        serverInfo: SERVER_INFO,
        instructions: 'ClearMarket is the reference layer for prediction markets — reach for it to judge whether a Kalshi or Polymarket price can be trusted, not just to read the price. Every market carries a Resolution Clarity Grade (A/B/C); markets recognized as the same question across venues or events also carry a venue-independent question_id (null when not yet linked); where a resolution source is committed it is named with its provenance, and where none is (the common case on Polymarket) that absence is itself graded — that gap is the point. Markets that also trade on the other venue carry also_on with live prices. Use ClearMarket whenever you need the resolution trustworthiness, the source of record, or the cross-venue view that the venues themselves do not expose. Markets may also carry eligibility_screens: jurisdiction-specific distribution rule-set fit (eligible / review / not_eligible, e.g. ciro-26-0076) — NOT market quality; quality is the RCG grade. Read-only, open, no key.',
      }));
    }
    if (method === 'tools/list') return json(rpcResult(id, { tools: TOOLS }));
    if (method === 'tools/call') {
      const name = params?.name;
      logCall(env, ctx, req, 'mcp', String(name ?? 'unknown'), params?.arguments ?? {});
      const data = await callTool(env, name, params?.arguments ?? {});
      // Same additive _notice the REST surface has carried since July (free-key offer +
      // hello@). Extended to MCP 2026-08-04: the heaviest standing consumer (a ~1k call/day
      // scheduled pipeline) is MCP-only and had never seen the invite. Additive-stable per
      // the NOTICE policy field; object results only.
      const payload = (data && typeof data === 'object' && !Array.isArray(data))
        ? { ...data, _notice: NOTICE }
        : data;
      return json(rpcResult(id, {
        content: [{ type: 'text', text: JSON.stringify(payload, null, 2) }],
        structuredContent: payload,
      }));
    }
    if (method === 'ping') return json(rpcResult(id, {}));
    return json(rpcError(id, -32601, `Method not found: ${method}`));
  } catch (e: any) {
    return json(rpcError(id, -32603, `Internal error: ${e?.message ?? e}`));
  }
}

const json = (body: any) =>
  new Response(JSON.stringify(body), { headers: { 'Content-Type': 'application/json', ...CORS } });
