import type { APIRoute, GetStaticPaths } from 'astro';
import {
  getAllEvents,
  getEventBySlug,
  getMarketsForEvent,
  getMarksForEvent,
  getResolutionLogForEvent,
  SPECIMEN_GENERATED_AT,
  SCHEMA_VERSION,
} from '../../../../lib/specimens';

const SITE = 'https://clearmarket.fyi';

export const getStaticPaths: GetStaticPaths = () => {
  return getAllEvents().map((e) => ({ params: { slug: e.slug } }));
};

export const GET: APIRoute = ({ params }) => {
  const slug = params.slug as string;
  const event = getEventBySlug(slug);
  if (!event) {
    return new Response(JSON.stringify({ error: 'not_found', slug }), {
      status: 404,
      headers: { 'Content-Type': 'application/json; charset=utf-8' },
    });
  }

  const markets = getMarketsForEvent(event.event_id);
  const marks = getMarksForEvent(event.event_id);
  const resolution_log = getResolutionLogForEvent(event.event_id);

  const body = {
    schema_version: SCHEMA_VERSION,
    snapshot_at: SPECIMEN_GENERATED_AT,
    event,
    markets,
    marks,
    resolution_log,
    _links: {
      self: `${SITE}/api/v1/events/${event.slug}.json`,
      markets: `${SITE}/api/v1/events/${event.slug}/markets.json`,
      collection: `${SITE}/api/v1/events.json`,
    },
  };

  return new Response(JSON.stringify(body, null, 2), {
    headers: { 'Content-Type': 'application/json; charset=utf-8' },
  });
};
