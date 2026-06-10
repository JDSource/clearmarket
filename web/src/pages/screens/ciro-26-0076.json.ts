// Machine-readable parallel of /screens/ciro-26-0076/ (four-format rule).
// Serves the screen summary + per-status market-id lists; per-market records
// travel on the market objects themselves (eligibility_screens field).
import type { APIRoute } from 'astro';
import { getScreenSummary, getMarketIdsByStatus } from '../../lib/eligibility';

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
    markets: {
      eligible: getMarketIdsByStatus('eligible'),
      review: getMarketIdsByStatus('review'),
      not_eligible_count: summary.funnel.not_eligible,
    },
  };
  return new Response(JSON.stringify(body, null, 2), {
    headers: { 'Content-Type': 'application/json; charset=utf-8' },
  });
};
