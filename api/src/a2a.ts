/**
 * A2A (Agent2Agent) surface — minimal, synchronous, spec-conformant.
 *
 * Directories and agent platforms probe /.well-known/agent-card.json (and a spread of
 * legacy alias paths — all observed as 404s in zone logs before this shipped). The card
 * advertises exactly what exists: one JSON-RPC endpoint (POST /a2a) implementing
 * message/send, returning a completed Task synchronously. streaming/pushNotifications
 * are declared false; unimplemented methods return -32601 per the spec's minimal-
 * conformance guidance. Query logic is the same dispatch the MCP tools use (callTool),
 * so A2A answers stay in lockstep with MCP/REST — no parallel data path.
 */

import { Env, logCall } from './index';
import { callTool } from './mcp';

const A2A_URL = 'https://api.clearmarket.fyi/a2a';

// The JSON shapes below (kind/task, lowercase status states, parts with kind:'text'|'data')
// follow the A2A JSON-RPC binding as implemented by the 0.2/0.3-generation SDKs — which is
// what A2A clients and card validators in the wild actually speak.
export const AGENT_CARD = {
  protocolVersion: '0.3.0',
  name: 'ClearMarket',
  description:
    'Reference layer for prediction markets. Judges whether a Kalshi or Polymarket price can be trusted: every market carries a Resolution Clarity Grade (A/B/C), the committed resolution source is named with provenance where one exists (the absence is graded too — that gap is the point), and the same question across venues is linked by a venue-independent question_id with live cross-venue prices (also_on). Read-only reference data; not trading advice.',
  url: A2A_URL,
  preferredTransport: 'JSONRPC',
  additionalInterfaces: [{ url: A2A_URL, transport: 'JSONRPC' }],
  provider: { organization: 'ClearMarket', url: 'https://clearmarket.fyi' },
  version: '1.0.0',
  documentationUrl: 'https://clearmarket.fyi/for-data/',
  capabilities: { streaming: false, pushNotifications: false, stateTransitionHistory: false },
  securitySchemes: {},
  security: [],
  defaultInputModes: ['text/plain'],
  defaultOutputModes: ['application/json', 'text/plain'],
  skills: [
    {
      id: 'market_trust_lookup',
      name: 'Market trust lookup',
      description:
        'Given a market id (CM-MKT-…), a Kalshi ticker, or a market URL: the Resolution Clarity Grade, the committed resolution source and its provenance, settlement status, latest price, and cross-venue twins.',
      tags: ['prediction-markets', 'resolution', 'provenance', 'reference-data'],
      examples: ['KXCPIYOY-26', 'What is the resolution source for CM-MKT-…?'],
    },
    {
      id: 'event_search',
      name: 'Graded event search',
      description:
        'Free-text search across ~2,400 graded prediction-market events on Kalshi and Polymarket. Returns per-event grade mix, venues, prices, and the canonical CM ids to cite.',
      tags: ['prediction-markets', 'search', 'events'],
      examples: ['fed rate decision', 'iran nuclear deal'],
    },
  ],
};

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

// Route a free-text question to the same dispatch MCP uses. Order: explicit CM/venue id or
// URL (exact lookup) -> token search over events. Lookup misses fall through to search.
async function answer(env: Env, text: string): Promise<any> {
  const t = text.trim();

  const cmMkt = t.match(/\bCM-MKT-[A-Za-z0-9_-]+\b/i)?.[0];
  const looksLikeTicker = /^[A-Z][A-Z0-9._-]{3,}$/.test(t);
  const looksLikeUrl = /^https?:\/\//i.test(t);
  if (cmMkt || looksLikeTicker || looksLikeUrl) {
    const m = await callTool(env, 'get_market', { market_id: cmMkt ?? t });
    if (m && !m.error) return { result_type: 'market', market: m };
  }

  const cmEvt = t.match(/\bCM-EVT-[A-Za-z0-9_-]+\b/i)?.[0];
  if (cmEvt) {
    const e = await callTool(env, 'get_event', { slug: cmEvt, detail: 'concise' });
    if (e && !e.error) return { result_type: 'event', event: e };
  }

  const q = searchTokens(t);
  if (!q) {
    return {
      result_type: 'usage',
      usage:
        'Send a market id (CM-MKT-…), a Kalshi ticker, a market URL, or a topic to search (e.g. "fed rate decision"). Full API: https://api.clearmarket.fyi/health · MCP: https://api.clearmarket.fyi/mcp',
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
  for (const p of parts) {
    if (typeof p?.text === 'string' && p.text.trim()) return p.text; // covers {kind:'text',text} and bare {text}
  }
  return null;
}

function completedTask(data: any): any {
  const summary =
    data.result_type === 'market'
      ? `Market ${data.market?.market_id}: grade ${data.market?.resolution_clarity_grade ?? 'n/a'}, status ${data.market?.status ?? 'n/a'}.`
      : data.result_type === 'event'
        ? `Event ${data.event?.event_id}: ${data.event?.question ?? ''}`
        : data.result_type === 'search'
          ? `${data.total ?? data.count ?? 0} graded event(s) matched "${data.query}".`
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
  const { id, method, params } = msg ?? {};

  try {
    // 'message/send' is the JSON-RPC binding name; 'SendMessage' is the v1 proto operation
    // name some clients send verbatim. Accept both, same semantics.
    if (method === 'message/send' || method === 'SendMessage') {
      const text = extractText(params);
      if (!text) return json(rpcError(id, -32602, 'params.message.parts must include a text part.'));
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
