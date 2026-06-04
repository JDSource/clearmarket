/* RSS 2.0 feed for ClearMarket Signal wire items.
 *
 * Route: /signals/rss.xml
 *
 * Auto-discovered by Perplexity, NewsBot, Inoreader, and other indexers via the
 * <link rel="alternate"> tag in the signals page <head>. Feeds the GEO/AEO loop
 * (regular publication cadence is a freshness signal for AI citation systems).
 *
 * Generated at build time from the same content collection as the page.
 * Build item #11 in the v0.2 queue per outputs/clearmarket/now.md.
 */
import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';
import { displayTitle, composeTelemetry, dedupeActiveWires } from '../../lib/signal-display';

const SITE_URL = 'https://clearmarket.fyi';

function xmlEscape(s: string): string {
  return s
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&apos;');
}

function rfc822(iso: string): string {
  return new Date(iso).toUTCString();
}

export const GET: APIRoute = async () => {
  const signals = dedupeActiveWires(await getCollection('signals'));
  const sorted = signals.sort((a, b) =>
    new Date(b.data.published_at).getTime() - new Date(a.data.published_at).getTime()
  );

  const lastBuild = sorted.length > 0 ? rfc822(sorted[0].data.published_at) : rfc822(new Date().toISOString());

  const items = sorted.map((s) => {
    const url = `${SITE_URL}/signals/${s.data.signal_slug}/`;
    // Clean semantic title in the feed title (the indexed surface); telemetry leads the description.
    const telem = composeTelemetry(s.data);
    const description = [telem, s.data.bullets[0] ?? ''].filter(Boolean).join(' — ');
    return `    <item>
      <title>${xmlEscape(displayTitle(s.data))}</title>
      <link>${url}</link>
      <description>${xmlEscape(description)}</description>
      <pubDate>${rfc822(s.data.published_at)}</pubDate>
      <guid isPermaLink="true">${url}</guid>
      <category>${xmlEscape(s.data.detection_path)}</category>
      <category>${xmlEscape(s.data.category_tag)}</category>
    </item>`;
  }).join('\n');

  const rss = `<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>ClearMarket Signal — wire feed</title>
    <link>${SITE_URL}/signals/</link>
    <description>Atomic wire bulletins on prediction-market activity. Cross-venue spreads, benchmark drift, news-cycle coverage, and volume spikes across Polymarket, Kalshi, and other venues.</description>
    <language>en-US</language>
    <atom:link href="${SITE_URL}/signals/rss.xml" rel="self" type="application/rss+xml" />
    <lastBuildDate>${lastBuild}</lastBuildDate>
    <generator>ClearMarket Signal v0.2.0</generator>
${items}
  </channel>
</rss>
`;

  return new Response(rss, {
    status: 200,
    headers: {
      'Content-Type': 'application/rss+xml; charset=utf-8',
      'Cache-Control': 'public, max-age=300',
    },
  });
};
