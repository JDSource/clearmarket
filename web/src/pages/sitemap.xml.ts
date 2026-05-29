import { getAllEvents } from '../lib/universe';
const SITE = 'https://clearmarket.fyi';
export async function GET() {
  const urls = [`${SITE}/`, ...getAllEvents().map((e) => `${SITE}/events/${e.slug}/`)];
  const body = `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${urls.map((u) => `  <url><loc>${u}</loc></url>`).join('\n')}\n</urlset>\n`;
  return new Response(body, { headers: { 'Content-Type': 'application/xml' } });
}
