/* Static per-event wire list: GET /signals/for-event/<event_id>.json
 *
 * Closes the discovery loop the PRD specifies (§6.5.3): given a CM event_id,
 * return every CM Signal wire that targets or links to it. Pre-generated at
 * build time (events are a finite known set), so no Worker / no /v1/ namespace.
 * The event page renders the same data inline; this is the machine surface.
 */
import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';
import { displayTitle, composeTelemetry } from '../../../lib/signal-display';
import { resolveSignalStatus } from '../../../lib/universe';

function refersTo(data: any, id: string): boolean {
  return data.event_id === id || (data.linked_event_ids ?? []).includes(id);
}

export async function getStaticPaths() {
  const signals = await getCollection('signals');
  const ids = new Set<string>();
  for (const s of signals) {
    if (s.data.event_id) ids.add(s.data.event_id);
    for (const e of s.data.linked_event_ids ?? []) ids.add(e);
  }
  return [...ids].map((id) => ({ params: { id } }));
}

export const GET: APIRoute = async ({ params }) => {
  const id = params.id as string;
  const signals = await getCollection('signals');
  const items = signals
    .map((s) => s.data)
    .filter((d: any) => refersTo(d, id))
    .sort((a: any, b: any) => (a.published_at < b.published_at ? 1 : -1))
    .map((d: any) => ({
      record_id: d.signal_id,
      record_slug: d.signal_slug,
      published_at: d.published_at,
      // Settlement state of the primary market at build time (full detail in the per-wire json).
      status: (({ state, outcome }) => ({ state, outcome }))(
        resolveSignalStatus(d.event_id, d.primary_market?.platform_market_id, d.primary_market?.resolves_at),
      ),
      semantic_title: displayTitle(d),
      telemetry: composeTelemetry(d),
      headline: d.headline,
      category_tag: d.category_tag,
      detection_path: d.detection_path,
      role: d.event_id === id ? 'primary' : 'linked',
      html: `https://clearmarket.fyi/signals/${d.signal_slug}/`,
      json: `https://clearmarket.fyi/signals/${d.signal_slug}.json`,
    }));

  const body = {
    $schema: 'https://clearmarket.fyi/schema/signal-list/v1.json',
    event_id: id,
    count: items.length,
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
