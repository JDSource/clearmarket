/**
 * OpenAPI 3.1 spec for the public REST surface, served at /openapi.json (+ probed aliases)
 * so agents and codegen tools can wire themselves in without reading the human docs.
 *
 * Component schemas are the CANONICAL JSON Schemas from /schema (Zod-first pipeline exports,
 * draft 2020-12 — the dialect OpenAPI 3.1 embeds natively), imported at build time so the
 * spec cannot drift from the published data shapes. Paths/params are maintained here by hand;
 * they change rarely and each route in index.ts is the source of truth.
 *
 * agents.json (also here) is the directory-facing manifest AgenstryBot & co. probe daily —
 * it points at this spec plus the MCP/A2A/llms.txt surfaces rather than describing anything itself.
 */
import EVENT_SCHEMA from '../../schema/events.schema.json';
import MARKET_SCHEMA from '../../schema/markets.schema.json';
import MARK_SCHEMA from '../../schema/marks.schema.json';
import RESOLUTION_LOG_SCHEMA from '../../schema/resolution_log.schema.json';

const CATEGORIES = ['economics', 'financials', 'crypto', 'companies', 'technology', 'politics', 'geopolitics', 'health', 'climate'];
const PLATFORMS = ['kalshi', 'polymarket'];
const GRADES = ['A', 'B', 'C'];

// Embed a canonical schema as a RESPONSE component: drop $schema (3.1 sets the dialect
// document-wide) and drop `additionalProperties: false` — the canonical files describe the
// strict data contract, but API responses decorate rows with serve-time fields (_provenance,
// _notice, venues_covered, current_primary_mark, …). A validating client must not reject those.
const responseShape = (s: any) => {
  const { $schema, additionalProperties, ...rest } = s;
  return {
    ...rest,
    description:
      (rest.description ? rest.description + ' ' : '') +
      'API responses add serve-time fields beyond this canonical schema (_provenance, _notice, and per-endpoint extras).',
  };
};

export const OPENAPI_SPEC = {
  openapi: '3.1.0',
  info: {
    title: 'ClearMarket API',
    version: '0.2.0',
    description:
      'Reference data layer for prediction markets: cross-venue event linking, Resolution Clarity Grades (A/B/C), ' +
      'committed resolution sources with provenance, jurisdiction eligibility screens, live marks, and CM Signal wires ' +
      'across Kalshi and Polymarket. Open access, no key required (optional free key raises rate limits). ' +
      'Attribution required: clearmarket.fyi. Same data via MCP (https://api.clearmarket.fyi/mcp) and ' +
      'A2A (https://api.clearmarket.fyi/a2a).',
    contact: { name: 'ClearMarket', url: 'https://clearmarket.fyi/for-data/' },
  },
  servers: [{ url: 'https://api.clearmarket.fyi' }],
  externalDocs: { description: 'Human docs, schema tour, and grading methodology', url: 'https://clearmarket.fyi/for-data/' },
  paths: {
    '/': {
      get: {
        operationId: 'serviceInfo',
        summary: 'Service status, coverage counts, and valid filter values',
        description: 'Returns live event/market counts plus the valid category/platform/grade filter vocabulary so a client can discover query values without guessing.',
        responses: { '200': { description: 'Service info', content: { 'application/json': { schema: { type: 'object' } } } } },
      },
    },
    '/v1/events': {
      get: {
        operationId: 'listEvents',
        summary: 'List graded events',
        parameters: [
          { name: 'category', in: 'query', schema: { type: 'string', enum: CATEGORIES } },
          { name: 'platform', in: 'query', schema: { type: 'string', enum: PLATFORMS } },
          { name: 'grade', in: 'query', description: 'Resolution Clarity Grade of the primary market', schema: { type: 'string', enum: GRADES } },
          { name: 'q', in: 'query', description: 'Token-AND search across question and tags', schema: { type: 'string' } },
          { name: 'status', in: 'query', description: 'active = has at least one open market; resolved = none', schema: { type: 'string', enum: ['all', 'active', 'resolved'], default: 'all' } },
          { name: 'limit', in: 'query', schema: { type: 'integer', maximum: 100, default: 50 } },
          { name: 'offset', in: 'query', schema: { type: 'integer', default: 0 } },
        ],
        responses: {
          '200': {
            description: 'Paged event list. Unknown filter values return an empty page plus a notice naming the valid set.',
            content: { 'application/json': { schema: {
              type: 'object',
              properties: { count: { type: 'integer', description: 'rows in this page' }, total: { type: 'integer', description: 'full count under the active filters' }, limit: { type: 'integer' }, offset: { type: 'integer' }, events: { type: 'array', items: { $ref: '#/components/schemas/Event' } } },
              additionalProperties: true,
            } } },
          },
        },
      },
    },
    '/v1/events/{slug}': {
      get: {
        operationId: 'getEvent',
        summary: 'One event with all linked markets, cross-venue prices, catalysts, and resolution detail',
        parameters: [
          { name: 'slug', in: 'path', required: true, description: 'Event slug OR ClearMarket event_id — both resolve', schema: { type: 'string' } },
          { name: 'detail', in: 'query', schema: { type: 'string', enum: ['full', 'concise'], default: 'full' } },
        ],
        responses: {
          '200': { description: 'Event fields FLATTENED at the top level (not wrapped in an `event` key), plus linked markets and resolution log', content: { 'application/json': { schema: {
            allOf: [
              { $ref: '#/components/schemas/Event' },
              { type: 'object', properties: {
                markets: { type: 'array', items: { $ref: '#/components/schemas/Market' } },
                resolution_log: { type: 'array', items: { $ref: '#/components/schemas/ResolutionLogEntry' } },
              } },
            ],
          } } } },
          '404': { description: 'Unknown slug/event_id' },
        },
      },
    },
    '/v1/markets/{id}': {
      get: {
        operationId: 'getMarket',
        summary: 'One market by ClearMarket market_id',
        parameters: [{ name: 'id', in: 'path', required: true, schema: { type: 'string' } }],
        responses: {
          '200': { description: 'Market', content: { 'application/json': { schema: { $ref: '#/components/schemas/Market' } } } },
          '404': { description: 'Unknown market_id' },
        },
      },
    },
    '/v1/markets/movers': {
      get: {
        operationId: 'listMovers',
        summary: 'Day-over-day volume movers across all tracked markets',
        parameters: [
          { name: 'min_mult', in: 'query', description: 'Minimum volume multiple vs prior day', schema: { type: 'number', minimum: 1, default: 2 } },
          { name: 'limit', in: 'query', schema: { type: 'integer', maximum: 200, default: 50 } },
        ],
        responses: { '200': { description: 'Movers (empty with a notice when adjacent daily snapshots are unavailable)', content: { 'application/json': { schema: { type: 'object' } } } } },
      },
    },
    '/v1/catalysts/upcoming': {
      get: {
        operationId: 'listUpcomingCatalysts',
        summary: 'Scheduled catalysts (FOMC, CPI, earnings, elections…) in the next N days',
        parameters: [{ name: 'days', in: 'query', schema: { type: 'integer', minimum: 1, maximum: 365, default: 30 } }],
        responses: { '200': { description: 'Dated catalyst calendar with source URLs', content: { 'application/json': { schema: { type: 'object' } } } } },
      },
    },
    '/v1/signals': {
      get: {
        operationId: 'listSignals',
        summary: 'CM Signal wire index (analytics bulletins built on the reference layer)',
        responses: { '200': { description: 'Wire index', content: { 'application/json': { schema: { type: 'object' } } } } },
      },
    },
    '/v1/signals/{slug}': {
      get: {
        operationId: 'getSignal',
        summary: 'One CM Signal bulletin',
        parameters: [{ name: 'slug', in: 'path', required: true, schema: { type: 'string' } }],
        responses: { '200': { description: 'Bulletin JSON' }, '404': { description: 'Unknown wire' } },
      },
    },
    '/v1/spot': {
      get: {
        operationId: 'getSpot',
        summary: 'Reference spot prices (USD) for coins referenced by crypto markets',
        responses: { '200': { description: 'Spot table with as-of timestamps' } },
      },
    },
    '/v1/keys': {
      post: {
        operationId: 'createKey',
        summary: 'Create a free API key (optional — anonymous access works; a key raises the daily limit)',
        requestBody: { required: true, content: { 'application/json': { schema: { type: 'object', required: ['email'], properties: { email: { type: 'string', format: 'email' } } } } } },
        responses: { '201': { description: 'Key issued; send as `Authorization: Bearer <key>` or `?key=`' }, '400': { description: 'Invalid email' } },
      },
    },
  },
  components: {
    schemas: {
      Event: responseShape(EVENT_SCHEMA),
      Market: responseShape(MARKET_SCHEMA),
      Mark: responseShape(MARK_SCHEMA),
      ResolutionLogEntry: responseShape(RESOLUTION_LOG_SCHEMA),
    },
  },
} as const;

// Directory-facing manifest. No single "agents.json" standard has won, so this stays minimal:
// identity + where the machine-usable surfaces live. Directories that want detail follow openapi.
export const AGENTS_MANIFEST = {
  name: 'ClearMarket',
  description:
    'Reference data layer for prediction markets — graded resolution clarity (A/B/C), committed resolution sources, cross-venue linking, live marks, and signal wires for Kalshi + Polymarket. Open, free, attribution required.',
  url: 'https://clearmarket.fyi',
  openapi: 'https://api.clearmarket.fyi/openapi.json',
  interfaces: {
    rest: { base: 'https://api.clearmarket.fyi/v1', spec: 'https://api.clearmarket.fyi/openapi.json', auth: 'none (optional free key)' },
    mcp: { endpoint: 'https://api.clearmarket.fyi/mcp', transport: 'streamable-http', manifest: 'https://api.clearmarket.fyi/.well-known/mcp.json' },
    a2a: { endpoint: 'https://api.clearmarket.fyi/a2a', agent_card: 'https://api.clearmarket.fyi/.well-known/agent-card.json' },
  },
  llms_txt: 'https://clearmarket.fyi/llms.txt',
  api_catalog: 'https://api.clearmarket.fyi/.well-known/api-catalog',
  x402: 'https://api.clearmarket.fyi/.well-known/x402',
  terms: 'Attribution required. clearmarket.fyi',
};
