/**
 * A2A (Agent2Agent) surface — minimal, synchronous, spec-conformant.
 *
 * Directories and agent platforms probe /.well-known/agent-card.json (and a spread of
 * legacy alias paths — all observed as 404s in zone logs before this shipped). The card
 * advertises exactly what exists: one JSON-RPC endpoint (POST /a2a) implementing
 * message/send, returning a completed Task synchronously. streaming/pushNotifications
 * are declared false; unimplemented methods return spec errors per the minimal-
 * conformance guidance. Query logic is the same dispatch the MCP tools use (callTool),
 * so A2A answers stay in lockstep with MCP/REST — no parallel data path.
 *
 * The card is single-sourced from the static Pages copy (esbuild bundles the JSON
 * import), so the api.clearmarket.fyi and clearmarket.fyi copies cannot drift.
 */

import { Env, logCall } from './index';
import { callTool } from './mcp';
import AGENT_CARD from '../../web/public/.well-known/agent-card.json';

export { AGENT_CARD };

// ---- JSON-RPC plumbing (A2A flavor) -------------------------------------
const CORS = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
  'Access-Control-Allow-Headers': 'Authorization, Content-Type',
};
const json = (body: any, status = 200) =>
  new Response(JSON.stringify(body, null, 2), {
    status,
    headers: { 'Content-Type': 'application/json; charset=utf-8', ...CORS },
  });
const rpcResult = (id: any, result: any) => ({ jsonrpc: '2.0', id, result });
const rpcError = (id: any, code: number, message: string) => ({ jsonrpc: '2.0', id, error: { code, message } });

// Meta-words about ClearMarket's own vocabulary (not event topics) plus function words —
// stripped before the token-AND event search so "what is the resolution source for the
// iran deal market" searches as "iran deal".
const STOPWORDS = new Set([
  'the', 'a', 'an', 'of', 'on', 'in', 'for', 'to', 'is', 'are', 'was', 'be', 'been', 'by', 'at', 'it', 'its',
  'this', 'that', 'and', 'or', 'do', 'does', 'did', 'can', 'could', 'will', 'would', 'should', 'i', 'you', 'we',
  'what', 'which', 'who', 'how', 'when', 'with', 'about', 'me', 'my', 'your', 'please', 'tell', 'show', 'find',
  'market', 'markets', 'price', 'prices', 'odds', 'trust', 'trusted', 'resolution', 'source', 'grade', 'graded',
]);

function searchTokens(text: string): string {
  return text
    .toLowerCase()
    .replace(/[^a-z0-9\s-]/g, ' ')
    .split(/\s+/)
    .filter((t) => t.length > 1 && !STOPWORDS.has(t))
    .slice(0, 6)
    .join(' ');
}

// Route a free-text question to the same dispatch MCP uses. Order: id-shaped candidate
// (CM id — uppercased, since D1 TEXT compares are BINARY-collated and canonical ids are
// uppercase — Kalshi-ticker-shaped token, 0x conditionId, or URL) gets an exact lookup;
// a miss falls through to stopword-stripped token search with the id tokens removed.
async function answer(env: Env, text: string): Promise<any> {
  const t = text.trim();

  const cmEvt = t.match(/\bCM-EVT-[A-Za-z0-9_-]+\b/i)?.[0]?.toUpperCase();
  const cmMkt = t.match(/\bCM-MKT-[A-Za-z0-9_-]+\b/i)?.[0]?.toUpperCase();
  const cond = t.match(/\b0x[0-9a-fA-F]{16,}\b/)?.[0];
  // Ticker: the whole input if it's one id-shaped token, else the first mid-sentence
  // token containing letters AND a digit/separator (screens out ordinary words).
  const tick = (/^[A-Za-z][A-Za-z0-9._-]{3,}$/.test(t) && !/\s/.test(t) ? t
    : t.match(/\b[A-Za-z]{2,}[0-9._-][A-Za-z0-9._-]{2,}\b/)?.[0])?.toUpperCase();
  const looksLikeUrl = /^https?:\/\//i.test(t);

  const mktCandidate = cmMkt ?? cond ?? (looksLikeUrl ? t : tick);
  if (mktCandidate) {
    const m = await callTool(env, 'get_market', { market_id: mktCandidate });
    if (m && !m.error) return { result_type: 'market', market: m };
  }
  if (cmEvt) {
    const e = await callTool(env, 'get_event', { slug: cmEvt, detail: 'concise' });
    if (e && !e.error) return { result_type: 'event', event: e };
  }

  // Catalyst-calendar intent (backs the upcoming_catalysts card skill) — checked after id
  // lookups so a ticker containing "cal"/"upcoming" text still resolves as a market first.
  if (/\bcatalysts?\b|\bupcoming\b|\bcalendar\b/i.test(t)) {
    const days = Math.min(90, Math.max(1, Number(t.match(/(\d{1,3})\s*days?/i)?.[1] ?? 30)));
    const c = await callTool(env, 'list_upcoming_catalysts', { days });
    if (c && !c.error) return { result_type: 'catalysts', ...c };
  }

  // Id lookups missed (or none present) — search the remaining words, not the id tokens.
  const residue = [cmEvt, cmMkt, cond, tick].reduce((s, c) => (c ? s.replace(new RegExp(c.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'gi'), ' ') : s), t);
  const q = searchTokens(residue);
  if (!q) {
    return {
      result_type: 'usage',
      usage:
        'Send a market id (CM-MKT-…), a Kalshi ticker, a Polymarket conditionId (0x…), a market URL, or a topic to search (e.g. "fed rate decision"). Full API: https://api.clearmarket.fyi/health · MCP: https://api.clearmarket.fyi/mcp',
    };
  }
  const list = await callTool(env, 'list_events', { q, limit: 5 });
  if (list?.count === 0 && q.includes(' ')) {
    // Token-AND can over-constrain; retry on the two longest tokens before reporting empty.
    const loose = q.split(' ').sort((a, b) => b.length - a.length).slice(0, 2).join(' ');
    const retry = await callTool(env, 'list_events', { q: loose, limit: 5 });
    if (retry?.count > 0) return { result_type: 'search', query: loose, ...retry };
  }
  return { result_type: 'search', query: q, ...list };
}

function extractText(params: any): string | null {
  const parts = params?.message?.parts;
  if (!Array.isArray(parts)) return null;
  // Multi-part messages compose one utterance — join every text part ({kind:'text',text} or bare {text}).
  const text = parts.filter((p: any) => typeof p?.text === 'string' && p.text.trim()).map((p: any) => p.text).join(' ');
  return text.trim() || null;
}

function marketSummary(m: any): string {
  const price = typeof m?.last_price === 'number' ? `, last price ${m.last_price}` : '';
  const src = m?.resolution?.source ? `, resolution source: ${m.resolution.source}` : ', no committed resolution source';
  return `Market ${m?.market_id}: grade ${m?.rcg?.grade ?? 'n/a'}, status ${m?.status ?? 'n/a'}${price}${src}.`;
}

function completedTask(data: any): any {
  const summary =
    data.result_type === 'market'
      ? marketSummary(data.market)
      : data.result_type === 'event'
        ? `Event ${data.event?.event_id}: ${data.event?.question ?? ''}`
        : data.result_type === 'search'
          ? `${data.total ?? data.count ?? 0} graded event(s) matched "${data.query}". For an exact market, send a CM-MKT id, Kalshi ticker, or Polymarket conditionId.`
          : data.result_type === 'catalysts'
            ? `${data.count ?? data.catalysts?.length ?? 0} scheduled catalyst(s) in the next ${data.window_days ?? ''} days.`
            : 'ClearMarket A2A usage.';
  return {
    id: crypto.randomUUID(),
    contextId: crypto.randomUUID(),
    kind: 'task',
    status: { state: 'completed', timestamp: new Date().toISOString() },
    artifacts: [
      {
        artifactId: crypto.randomUUID(),
        name: 'clearmarket-reference-data',
        parts: [
          { kind: 'text', text: summary },
          { kind: 'data', data },
        ],
      },
    ],
    metadata: { source: 'clearmarket.fyi', terms: 'Attribution required. clearmarket.fyi' },
  };
}

export async function handleA2A(req: Request, env: Env, ctx: { waitUntil(p: Promise<any>): void }): Promise<Response> {
  if (req.method === 'OPTIONS') return new Response(null, { status: 204, headers: CORS });
  // GET /a2a → the card, so probing the endpoint itself is self-describing.
  if (req.method === 'GET') return json(AGENT_CARD);
  if (req.method !== 'POST') return json(rpcError(null, -32600, 'Use POST with a JSON-RPC 2.0 body.'), 405);

  let msg: any;
  try { msg = await req.json(); } catch { return json(rpcError(null, -32700, 'Parse error')); }
  // notifications (no id) — ack with 202, no body (JSON-RPC 2.0: MUST NOT reply)
  if (msg && msg.id === undefined) return new Response(null, { status: 202, headers: CORS });
  const { id, method, params } = msg ?? {};

  try {
    // 'message/send' is the JSON-RPC binding name; 'SendMessage' is the v1 proto operation
    // name some clients send verbatim. Accept both, same semantics.
    if (method === 'message/send' || method === 'SendMessage') {
      const text = extractText(params);
      if (!text) {
        // Structurally valid message with only file/data parts = modality mismatch (-32005,
        // ContentTypeNotSupportedError); no parts array at all = invalid params (-32602).
        return Array.isArray(params?.message?.parts)
          ? json(rpcError(id, -32005, 'Only text parts are supported (defaultInputModes: text/plain).'))
          : json(rpcError(id, -32602, 'params.message.parts must include a text part.'));
      }
      logCall(env, ctx, req, 'a2a', 'message/send', text.slice(0, 200));
      return json(rpcResult(id, completedTask(await answer(env, text))));
    }
    if (method === 'message/stream') return json(rpcError(id, -32004, 'Streaming is not supported (capabilities.streaming=false). Use message/send.'));
    if (method === 'tasks/get' || method === 'tasks/cancel') return json(rpcError(id, -32001, 'Tasks complete synchronously and are not persisted.'));
    return json(rpcError(id, -32601, `Method not found: ${method}`));
  } catch (e: any) {
    return json(rpcError(id, -32603, `Internal error: ${e?.message ?? e}`));
  }
}
