---
signal_id: "CMSIG2026101005"
signal_slug: "oct-2026-nonfarm-payrolls-implied-40k-50k-prediction-market-2026-10-10"
headline: "Oct 2026 nonfarm payrolls implied 40K-50K: prediction market"
semantic_title: "October payroll adds priced in the 40K to 50K range"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-10T00:00:00.000Z"
event_id: "CM-EVT-6CSLHX0K76"
event_slug: "kxpayrolls-26oct"
event_question: "October 2026 nonfarm payrolls added"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPAYROLLS-26OCT-T50000"
  question_raw: "Will above 50000 jobs be added in October 2026?"
  current_price: 0.49
  volume_24h_usd: 9.43
  arbitration_model: "kalshi_staff"
  resolution_source: "BLS"
  resolves_at: "2027-02-05T15:00:00Z"
bullets:
  - "The ladder implies October payroll adds in the 40,000-50,000 range: 55% above 40,000 but only 49% above 50,000, reflecting persistent labor market weakness."
  - "September's 29,000 print against a 90,000 forecast anchors the subdued baseline; the market is not pricing a sharp bounce toward prior trend levels."
  - "With 29% probability above 100,000 and 36% above 90,000, the ladder treats a return to pre-miss levels in October as a minority outcome."
  - "Resolution is via the Bureau of Labor Statistics October employment situation report; steep downward revisions in September add uncertainty to the October baseline."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The US economy added only 29,000 jobs in September, well below the 90,000 estimate, signaling a weakening labor market."
    publisher: "5thnews.com"
    published_at: "2026-10-10T00:00:00.000Z"
    source_url: "https://www.5thnews.com/finance/us-economy-added-29000-jobs-in-september-a-slower-pace-than-expected/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "5thnews.com"
        source_url: "https://www.5thnews.com/finance/us-economy-added-29000-jobs-in-september-a-slower-pace-than-expected/"
        retrieved_at: "2026-10-12T07:49:04+00:00"
  - type: "pm_response"
    notes: "The prediction market ladder on October payrolls is the only active contract with current pricing directly relevant to the September jobs miss narrative."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "5thnews.com: US economy added 29,000 jobs in September, a slower pace than expected"
    url: "https://www.5thnews.com/finance/us-economy-added-29000-jobs-in-september-a-slower-pace-than-expected/"
    published_at: "2026-10-10T00:00:00.000Z"
    retrieved_at: "2026-10-12T07:49:04+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
