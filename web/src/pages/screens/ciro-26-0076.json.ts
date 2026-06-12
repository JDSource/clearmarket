// Machine-readable parallel of /screens/ciro-26-0076/ (four-format rule).
// Serves the screen summary + full per-market records (status/reasons/cluster/
// bucket) so the JSON surface honors decision 8 ("status + reasons free on all
// surfaces") on its own — the API/MCP eligibility_screens field is the richer
// twin once deployed, not a prerequisite.
import type { APIRoute } from 'astro';
import { getScreenSummary, getAllEligibility } from '../../lib/eligibility';

export const GET: APIRoute = () => {
  const summary = getScreenSummary();
  if (!summary) {
    return new Response(JSON.stringify({ error: 'screen unavailable in this build' }), {
      status: 503,
      headers: { 'Content-Type': 'application/json; charset=utf-8' },
    });
  }
  const body = {
    ...summary,
    disclaimer:
      'ClearMarket eligibility screens are reference data supporting a dealer’s own determination. They are not a compliance opinion. A status describes fit against this rule-set only and says nothing about a market’s quality or tradability elsewhere.',
    primary_source:
      'https://www.ciro.ca/newsroom/publications/application-ciro-requirements-event-contracts',
    markets: Object.fromEntries(
      Object.entries(getAllEligibility()).map(([id, r]) => [
        id,
        { status: r.status, reasons: r.reasons, bucket: r.bucket ?? null, ...(r.cluster ? { cluster: r.cluster } : {}) },
      ])
    ),
  };
  return new Response(JSON.stringify(body, null, 2), {
    headers: { 'Content-Type': 'application/json; charset=utf-8' },
  });
};
