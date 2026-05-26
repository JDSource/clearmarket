import type { APIRoute } from 'astro';
import { getAllEvents, SPECIMEN_GENERATED_AT, SCHEMA_VERSION } from '../../../lib/specimens';

const SITE = 'https://clearmarket.fyi';

export const GET: APIRoute = () => {
  const body = {
    name: 'ClearMarket API',
    version: 'v0.2.0-beta',
    schema_version: SCHEMA_VERSION,
    description:
      'Reference data for prediction markets. Free tier: 4-table normalized records (events, markets, marks, resolution_log) covering canonical events from Kalshi and Polymarket.',
    status: 'beta — static cached responses, refreshed daily from sample specimens',
    snapshot_at: SPECIMEN_GENERATED_AT,
    event_count: getAllEvents().length,
    endpoints: {
      events_list: `${SITE}/api/v1/events.json`,
      event_detail: `${SITE}/api/v1/events/{slug}.json`,
      event_markets: `${SITE}/api/v1/events/{slug}/markets.json`,
    },
    schema: {
      events: 'https://raw.githubusercontent.com/JDSource/clearmarket/main/schema/events.schema.json',
      markets: 'https://raw.githubusercontent.com/JDSource/clearmarket/main/schema/markets.schema.json',
      marks: 'https://raw.githubusercontent.com/JDSource/clearmarket/main/schema/marks.schema.json',
      resolution_log:
        'https://raw.githubusercontent.com/JDSource/clearmarket/main/schema/resolution_log.schema.json',
    },
    rate_limit: {
      policy: 'free tier — soft cap ~100 requests/day per IP, enforced at CDN edge',
      headers: 'see Cache-Control on each response; CDN-Cache-Status indicates hit/miss',
    },
    repository: 'https://github.com/JDSource/clearmarket',
    contact: 'hello@clearmarket.fyi',
  };
  return new Response(JSON.stringify(body, null, 2), {
    headers: { 'Content-Type': 'application/json; charset=utf-8' },
  });
};
