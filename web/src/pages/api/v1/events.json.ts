import type { APIRoute } from 'astro';
import {
  getAllEvents,
  getMarketsForEvent,
  SPECIMEN_GENERATED_AT,
  SCHEMA_VERSION,
} from '../../../lib/specimens';

const SITE = 'https://clearmarket.fyi';

export const GET: APIRoute = () => {
  const events = getAllEvents().map((e) => {
    const markets = getMarketsForEvent(e.event_id);
    return {
      event_id: e.event_id,
      slug: e.slug,
      question: e.question,
      category: e.category,
      tags: e.tags,
      venues_covered: e.venues_covered,
      market_count: markets.length,
      primary_market_id: e.primary_market_id,
      catalyst_dates: e.catalyst_dates,
      current_primary_mark: e.current_primary_mark
        ? {
            snapshot_date: e.current_primary_mark.snapshot_date,
            yes_last_price: e.current_primary_mark.yes_last_price,
            implied_probability: e.current_primary_mark.implied_probability,
            volume_24h_usd: e.current_primary_mark.volume_24h_usd,
            volume_total_usd: e.current_primary_mark.volume_total_usd,
            stale_flag: e.current_primary_mark.stale_flag,
          }
        : null,
      _links: {
        self: `${SITE}/api/v1/events/${e.slug}.json`,
        markets: `${SITE}/api/v1/events/${e.slug}/markets.json`,
      },
    };
  });

  const body = {
    schema_version: SCHEMA_VERSION,
    snapshot_at: SPECIMEN_GENERATED_AT,
    count: events.length,
    events,
  };

  return new Response(JSON.stringify(body, null, 2), {
    headers: { 'Content-Type': 'application/json; charset=utf-8' },
  });
};
