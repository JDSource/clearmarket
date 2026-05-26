/* Static parallel JSON endpoint for wire items.
 *
 * Route: /signals/[slug].json — returns the canonical wire-item record as JSON.
 * Satisfies the four-format rule (HTML + JSON-LD + parallel .json + llms.txt row)
 * without waiting for the Cloudflare Worker (build item #6) to ship.
 *
 * Astro prerenders one file per signal at build time. The Worker can replace
 * these later for dynamic queries (filters, pagination) — for v1 launch, static
 * is enough.
 */
import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';

// Short-form definitions of the 4 provenance tiers. Embedded in every wire
// record so the JSON payload is a self-contained unit of proof — consumers
// (AI agents, ETL pipelines, MCP clients) can interpret the tier vocabulary
// without a secondary HTTP fetch to /schema/provenance/v1.
const PROVENANCE_REGISTRY = {
  direct: 'Unaltered extraction from primary venue/source API (e.g., polymarket_clob_api, kalshi_api, BLS, FRED). Highest trust tier.',
  mediated: 'Information fetched via grounded agentic retrieval (e.g., perplexity_grounded). MUST carry source_url to the underlying primary source.',
  derived: 'Algorithmic computation from listed inputs. Chain only as fresh as the oldest input timestamp (see as_of).',
  editorial: 'Interpretive classification produced by a versioned LLM prompt template (prompts auditable in github.com/JDSource/clearmarket/prompts).',
};

export async function getStaticPaths() {
  const signals = await getCollection('signals');
  return signals.map((s) => ({
    params: { slug: s.data.signal_slug },
    props: { signal: s },
  }));
}

export const GET: APIRoute = ({ props }) => {
  const { signal } = props as any;
  const data = signal.data;

  // Canonical wire-item record — same shape as the inline JSON on the signal page,
  // same data the Worker will eventually serve via api.clearmarket.fyi/v1/signals/[slug].
  const record = {
    $schema: 'https://clearmarket.fyi/schema/signal/v1.json',
    record_id: data.signal_id,
    record_slug: data.signal_slug,
    schema_version: 'v0.2.0',
    provenance_version: '0.2.0',
    published_at: data.published_at,
    headline: data.headline,
    category_tag: data.category_tag,
    secondary_tags: data.secondary_tags ?? [],
    detection_path: data.detection_path,
    pre_news_classification: data.pre_news_classification,
    target_event_id: data.event_id,
    target_event_slug: data.event_slug,
    event_question: data.event_question,
    linked_event_ids: data.linked_event_ids ?? [],
    primary_market: data.primary_market,
    related_markets: data.related_markets ?? [],
    bullets: data.bullets,
    atomic_claims: data.atomic_claims ?? [],
    sources: data.sources ?? [],
    field_provenance: data.field_provenance ?? null,
    canonical_urls: {
      html: `https://clearmarket.fyi/signals/${data.signal_slug}/`,
      json: `https://clearmarket.fyi/signals/${data.signal_slug}.json`,
    },
    license: 'https://creativecommons.org/licenses/by/4.0/',
    _provenance_registry: PROVENANCE_REGISTRY,
    _provenance_canonical: 'https://clearmarket.fyi/schema/provenance/v1',
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
