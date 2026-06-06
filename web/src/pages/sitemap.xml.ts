import { getCollection } from 'astro:content';
import { getAllEvents } from '../lib/universe';

const SITE = 'https://clearmarket.fyi';

// Generated at build time from the same sources the pages build from, so the sitemap can never
// list a URL that wasn't built (no stale 404s). The daily cron rebuild regenerates this with each
// day's new events + ~25 new signal wires automatically — no manual maintenance.
export async function GET() {
  const signals = await getCollection('signals');

  const entries: { loc: string; lastmod?: string }[] = [
    { loc: `${SITE}/` },
    { loc: `${SITE}/events/` },
    { loc: `${SITE}/signals/` },
    { loc: `${SITE}/methodology/` },
    { loc: `${SITE}/api/` },
    // Event pages — one per tradable event, each carrying Dataset JSON-LD.
    ...getAllEvents().map((e) => ({
      loc: `${SITE}/events/${e.slug}/`,
      lastmod: ((e as any).updated_at || '').slice(0, 10) || undefined,
    })),
    // Signal wire items — each carrying Dataset + ClaimReview JSON-LD. Dedupe by signal_slug so
    // we advertise exactly the pages signals/[slug].astro builds (Astro collapses duplicate slugs
    // to one page; without dedupe the sitemap would list phantom duplicate URLs).
    ...[...new Map(signals.map((s) => [s.data.signal_slug, s])).values()].map((s) => ({
      loc: `${SITE}/signals/${s.data.signal_slug}/`,
      lastmod: (s.data.published_at || '').slice(0, 10) || undefined,
    })),
  ];

  const body = `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${entries
    .map((u) => `  <url><loc>${u.loc}</loc>${u.lastmod ? `<lastmod>${u.lastmod}</lastmod>` : ''}</url>`)
    .join('\n')}\n</urlset>\n`;
  return new Response(body, { headers: { 'Content-Type': 'application/xml' } });
}
