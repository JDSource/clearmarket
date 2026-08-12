---
signal_id: "CMSIG2026081103"
signal_slug: "oct-payrolls-implied-at-70k-80k-prediction-market-2026-08-11"
headline: "Oct payrolls implied at 70K-80K: prediction market"
semantic_title: "October payrolls outlook holds near 50% at the 70-80K range"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-11T00:00:00.000Z"
event_id: "CM-EVT-6CSLHX0K76"
event_slug: "kxpayrolls-26oct"
event_question: "Nonfarm payrolls change, October 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPAYROLLS-26OCT-T80000"
  question_raw: "Will above 80000 jobs be added in October 2026?"
  current_price: 0.45
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "BLS"
  resolves_at: "2027-02-05T15:00:00Z"
bullets:
  - "The prediction market ladder implies October 2026 payrolls in the 70,000-80,000 range, with the 70K rung at 50% and the 80K rung at 45%."
  - "July's 23,000 job loss sits well below this implied range, suggesting the market does not yet fully extrapolate the July weakness into October."
  - "May revised to 63,000 and June to 20,000 already reflect a softening trend; October pricing above zero implies a partial rebound expectation."
  - "Resolves via the Bureau of Labor Statistics nonfarm payrolls release for October 2026; revisions to prior months could shift the effective benchmark."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "U.S. employers shed 23,000 jobs in July, with prior months also revised sharply lower, raising fears of sustained labor market weakness."
    publisher: "Dani Tietz"
    published_at: "2026-08-11T00:00:00.000Z"
    source_url: "https://mahometdaily.com/u-s-payrolls-slip-by-23000-in-july-as-health-care-gains-offset-public-education-retail-losses/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Dani Tietz"
        source_url: "https://mahometdaily.com/u-s-payrolls-slip-by-23000-in-july-as-health-care-gains-offset-public-education-retail-losses/"
        retrieved_at: "2026-08-12T09:07:43+00:00"
  - type: "pm_response"
    notes: "This ladder carries priced data; the distribution is centered well above zero, implying markets treat July as a trough rather than a trend."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Dani Tietz: U.S. payrolls slip by 23,000 in July as health care gains offset publi"
    url: "https://mahometdaily.com/u-s-payrolls-slip-by-23000-in-july-as-health-care-gains-offset-public-education-retail-losses/"
    published_at: "2026-08-11T00:00:00.000Z"
    retrieved_at: "2026-08-12T09:07:43+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
