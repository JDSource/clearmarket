/* Static wire-list endpoint: GET /signals.json
 *
 * The machine-readable list of every published CM Signal wire, newest first.
 * Static (built from the content collection) — no Worker, no /v1/ namespace.
 * Sibling to the /signals/ HTML index (named /signals.json to avoid the
 * index.astro route collision). Each entry links to its full per-wire record.
 */
import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';

export const GET: APIRoute = async () => {
  const signals = await getCollection('signals');
  const items = signals
    .map((s) => s.data)
    .sort((a: any, b: any) => (a.published_at < b.published_at ? 1 : -1))
    .map((d: any) => {
      const venues = Array.from(
        new Set([d.primary_market?.platform, ...(d.related_markets ?? []).map((m: any) => m.platform)].filter(Boolean)),
      );
      return {
        record_id: d.signal_id,
        record_slug: d.signal_slug,
        published_at: d.published_at,
        headline: d.headline,
        category_tag: d.category_tag,
        detection_path: d.detection_path,
        target_event_id: d.event_id ?? null,
        target_event_slug: d.event_slug ?? null,
        linked_event_ids: d.linked_event_ids ?? [],
        venues,
        html: `https://clearmarket.fyi/signals/${d.signal_slug}/`,
        json: `https://clearmarket.fyi/signals/${d.signal_slug}.json`,
      };
    });

  const body = {
    $schema: 'https://clearmarket.fyi/schema/signal-list/v1.json',
    generated_from: 'static_build',
    count: items.length,
    license: 'https://creativecommons.org/licenses/by/4.0/',
    feeds: {
      html: 'https://clearmarket.fyi/signals/',
      rss: 'https://clearmarket.fyi/signals/rss.xml',
      per_wire_json: 'https://clearmarket.fyi/signals/{record_slug}.json',
    },
    signals: items,
  };

  return new Response(JSON.stringify(body, null, 2), {
    status: 200,
    headers: {
      'Content-Type': 'application/json; charset=utf-8',
      'Cache-Control': 'public, max-age=300',
      'Access-Control-Allow-Origin': '*',
    },
  });
};
