/* Static parallel JSON endpoint for events — the primary entity.
 *
 * Route: /events/[slug].json — returns the canonical event record (event + its
 * markets, each with grade / resolution / provenance / cross-venue key) as JSON.
 * Satisfies the four-format rule (HTML + JSON-LD + parallel .json + llms.txt row)
 * for events, mirroring /signals/[slug].json. Prerendered one-file-per-event at
 * build time; the Cloudflare Worker's /v1/events/:slug is the dynamic equivalent.
 */
import type { APIRoute } from 'astro';
import { getAllEvents, getEventBySlug, getMarketsForEvent, getMarksForEvent, getResolutionLogForEvent, SCHEMA_VERSION } from '../../lib/universe';

export async function getStaticPaths() {
  return getAllEvents().map((e) => ({ params: { slug: e.slug } }));
}

export const GET: APIRoute = ({ params }) => {
  const slug = params.slug as string;
  const event = getEventBySlug(slug);
  if (!event) {
    return new Response(JSON.stringify({ error: 'not_found', slug }), {
      status: 404,
      headers: { 'Content-Type': 'application/json; charset=utf-8', 'Access-Control-Allow-Origin': '*' },
    });
  }

  const markets = getMarketsForEvent(event.event_id);
  const marks = getMarksForEvent(event.event_id);
  const markByMkt: Record<string, any> = {};
  for (const m of marks as any[]) markByMkt[m.market_id] = m;

  const record = {
    $schema: 'https://clearmarket.fyi/schema/event/v1.json',
    schema_version: SCHEMA_VERSION,
    event_id: event.event_id,
    slug: event.slug,
    question: event.question,
    category: event.category,
    event_type: (event as any).event_type ?? 'BINARY',
    ladder_distribution: (event as any).ladder_distribution ?? null,
    tags: (event as any).tags ?? [],
    venues_covered: (event as any).venues_covered ?? [],
    primary_market_id: (event as any).primary_market_id ?? null,
    catalyst_types: (event as any).catalyst_types ?? [],
    markets: (markets as any[]).map((m) => {
      const mk = markByMkt[m.market_id];
      return {
        market_id: m.market_id,
        platform: m.platform,
        platform_market_id: m.platform_market_id,
        question_raw: m.question_raw,
        contract_type: m.contract_type,
        close_at: m.close_at,
        resolve_at: m.resolve_at,
        status: m.status,
        resolution_clarity_grade: m.resolution_clarity_grade,
        rcg_score: m.rcg_score,
        resolution_source: m.resolution_source,
        resolution_source_type: m.resolution_source_type,
        source_commitment: m.source_commitment,
        settlement_style: m.settlement_style,
        direction: m.direction,
        threshold: m.threshold,
        cross_venue_id: m.claim_sig ?? null,
        last_price: mk?.last_price ?? m.last_price ?? null,
        volume_total_usd: m.volume_total_usd ?? null,
      };
    }),
    resolution_log: getResolutionLogForEvent(event.event_id).map((r) => ({
      market_id: r.market_id,
      platform: r.platform,
      outcome: r.to_value,
      resolved_at: r.occurred_at,
      final_price: r.final_price,
      recorded_at: r.recorded_at,
      source: r.source,
      source_ref: r.source_ref,
    })),
    canonical_urls: {
      html: `https://clearmarket.fyi/events/${event.slug}/`,
      json: `https://clearmarket.fyi/events/${event.slug}.json`,
      api: `https://api.clearmarket.fyi/v1/events/${event.slug}`,
    },
    license: 'https://creativecommons.org/licenses/by/4.0/',
  };

  return new Response(JSON.stringify(record, null, 2), {
    status: 200,
    headers: {
      'Content-Type': 'application/json; charset=utf-8',
      'Cache-Control': 'public, max-age=300',
      'Access-Control-Allow-Origin': '*',
    },
  });
};
