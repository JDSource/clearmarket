import type { APIRoute, GetStaticPaths } from 'astro';
import {
  getAllEvents,
  getEventBySlug,
  getMarketsForEvent,
  SPECIMEN_GENERATED_AT,
  SCHEMA_VERSION,
} from '../../../../../lib/specimens';

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

  const body = {
    schema_version: SCHEMA_VERSION,
    snapshot_at: SPECIMEN_GENERATED_AT,
    event_id: event.event_id,
    event_slug: event.slug,
    count: markets.length,
    markets,
    _links: {
      self: `${SITE}/api/v1/events/${event.slug}/markets.json`,
      event: `${SITE}/api/v1/events/${event.slug}.json`,
    },
  };

  return new Response(JSON.stringify(body, null, 2), {
    headers: { 'Content-Type': 'application/json; charset=utf-8' },
  });
};
