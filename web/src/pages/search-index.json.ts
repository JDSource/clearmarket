// Build-time search index — one compact row per event, auto-derived from the universe (no hand-
// maintained list). The header search box fetches this once and filters client-side. Each row:
//   s = event slug (nav target), t = display title, q = lowercased search blob
//       (title + tags + category + every venue market-id, so pasting KXIPO-26-STRIPE or a 0x… id hits).
import type { APIRoute } from 'astro';
import { getAllEvents, getMarketsForEvent, isEventLive } from '../lib/universe';
import { eventDisplayQuestion } from '../lib/labels';

export const GET: APIRoute = () => {
  const index = getAllEvents().map((e) => {
    const mkts = getMarketsForEvent(e.event_id);
    const ids = mkts
      .map((m) => m.platform_market_id)
      .filter(Boolean)
      .join(' ');
    const tags = (e.tags ?? []).join(' ');
    const title = eventDisplayQuestion(e.question, mkts);
    return {
      s: e.slug,
      t: title,
      q: `${title} ${tags} ${e.category} ${ids}`.toLowerCase(),
      r: isEventLive(e) ? 0 : 1, // resolved flag — consumers rank these lower
    };
  });
  // Active first so the typeahead dropdown + index filter surface live events before resolved ones.
  index.sort((a, b) => a.r - b.r);
  return new Response(JSON.stringify(index), {
    headers: { 'content-type': 'application/json', 'cache-control': 'public, max-age=3600' },
  });
};
