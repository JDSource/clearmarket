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
import { Env, num, parseJson, marketOut, eventSummary, loadCalendar, windowCatalysts, logCall, provenance } from './index';

const PROTOCOL_VERSION = '2025-06-18';
const SERVER_INFO = { name: 'clearmarket', version: '0.2.0' };
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
const TOOLS = [
  {
    name: 'list_events',
    description:
      'Browse or search ClearMarket prediction-market events. Filter by category, platform, Resolution Clarity ' +
      'Grade, or free-text (set `q` to search event questions, e.g. "recession", "bitcoin 150k", "fed rate"). ' +
      'Returns compact graded summaries (slug, question, venues covered, primary grade, price). Start here when you ' +
      'have a topic but not a slug; then call get_event for the full graded record. ' +
      'Categories: ' + CATEGORIES.join(', ') + '.',
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
      'Fetch the full ClearMarket record for one event by slug: the canonical question, every linked market across ' +
      'Kalshi and Polymarket, each market\'s current price + Resolution Clarity Grade (A/B/C) + resolution-source ' +
      'provenance, cross-venue links (claim_sig), and the upcoming catalyst dates that move it before it resolves. ' +
      'Use when you need the authoritative, graded, cross-venue view of a SPECIFIC event before reasoning about or ' +
      'acting on a prediction market. If you only have a topic (not a slug), call list_events first.',
    inputSchema: {
      type: 'object',
      properties: { slug: { type: 'string', description: 'Event slug, e.g. "kxgdpyear-26".' } },
      required: ['slug'],
    },
  },
  {
    name: 'get_market',
    description:
      'Fetch one market by market_id: raw question, current price / implied probability, the Resolution Clarity Grade ' +
      'with the factors behind it, full resolution-source provenance (who resolves it, named source, source type & quality), ' +
      'and the cross-venue claim_sig. Use when you have a specific market and need its resolution trustworthiness and ' +
      'provenance before trusting its price.',
    inputSchema: {
      type: 'object',
      properties: { market_id: { type: 'string', description: 'Market id, e.g. "CM-MKT-001828".' } },
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
async function buildEvent(env: Env, slug: string): Promise<any | null> {
  const e = await env.DB.prepare('SELECT * FROM events WHERE slug = ? AND published = 1').bind(slug).first<any>();
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
    markets: mkts.map(marketOut),
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
    `SELECT market_id, event_id, platform, last_price, resolution_clarity_grade, rcg_score FROM markets WHERE event_id IN (${ph})`
  ).bind(...ids).all<any>();
  const byEvent = new Map<string, any[]>();
  for (const m of mkts) (byEvent.get(m.event_id) ?? byEvent.set(m.event_id, []).get(m.event_id)!).push(m);
  const out = evs.map((e) => eventSummary(e, byEvent.get(e.event_id) ?? []));
  return { count: out.length, total, limit, offset, events: out };
}

async function buildMarket(env: Env, id: string): Promise<any | null> {
  const m = await env.DB.prepare('SELECT * FROM markets WHERE market_id = ?').bind(id).first<any>();
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
async function callTool(env: Env, name: string, a: Record<string, any>): Promise<any> {
  switch (name) {
    case 'get_event': {
      const r = await buildEvent(env, String(a.slug ?? ''));
      return r ?? { error: `No event with slug "${a.slug}". Try search or list_events.` };
    }
    case 'list_events': return buildList(env, a);
    case 'get_market': {
      const r = await buildMarket(env, String(a.market_id ?? ''));
      return r ?? { error: `No market with id "${a.market_id}".` };
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
        instructions: 'ClearMarket: the reference layer for prediction markets. Graded resolution clarity, cross-venue links, and provenance for Kalshi + Polymarket. Read-only, open.',
      }));
    }
    if (method === 'tools/list') return json(rpcResult(id, { tools: TOOLS }));
    if (method === 'tools/call') {
      const name = params?.name;
      logCall(env, ctx, req, 'mcp', String(name ?? 'unknown'), params?.arguments ?? {});
      const data = await callTool(env, name, params?.arguments ?? {});
      return json(rpcResult(id, {
        content: [{ type: 'text', text: JSON.stringify(data, null, 2) }],
        structuredContent: data,
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
