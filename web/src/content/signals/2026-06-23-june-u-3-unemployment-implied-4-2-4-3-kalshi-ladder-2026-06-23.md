---
signal_id: "CMSIG2026062305"
signal_slug: "june-u-3-unemployment-implied-4-2-4-3-kalshi-ladder-2026-06-23"
headline: "June U-3 unemployment implied 4.2-4.3%: Kalshi ladder"
semantic_title: "June unemployment above 4.2 percent sits near even odds in distribution"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-23T02:03:38.000Z"
event_id: "CM-EVT-FJGT56DTV2"
event_slug: "kxu3-26jun"
event_question: "June 2026 US unemployment rate (U-3)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXU3-26JUN-T4.3"
  question_raw: "Will the unemployment rate (U-3) be above 4.3% in June?"
  current_price: 0.31
  volume_24h_usd: 0.96
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2026-07-02T14:00:00Z"
bullets:
  - "Kalshi ladder implies the June unemployment rate in the 4.2-4.3% range: 63% above 4.2%, only 31% above 4.3%."
  - "Falling weekly claims are consistent with the market's modal view near 4.2%, but the low-hire dynamic from the St. Louis Fed research supports the rate staying elevated above 4.0%."
  - "The tail above 4.4% is priced at only 11%, suggesting the market rules out a significant labor deterioration by June."
  - "Resolves via Bureau of Labor Statistics June employment situation report."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "US jobless claims fell in the latest week, reinforcing a resilient but low-hire, low-fire labor market backdrop."
    publisher: "csuiteera.com"
    published_at: "2026-06-23T02:03:38.000Z"
    source_url: "https://csuiteera.com/us-jobless-claims-fall/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "csuiteera.com"
        source_url: "https://csuiteera.com/us-jobless-claims-fall/"
        retrieved_at: "2026-06-23T10:59:18+00:00"
  - type: "pm_response"
    notes: "Kalshi's distribution pins consensus around 4.2-4.3%, aligning with resilient but stagnant labor market conditions reported this week."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "csuiteera.com: US Jobless Claims Fall As Labor Market Remains Resilient | C Suit Era"
    url: "https://csuiteera.com/us-jobless-claims-fall/"
    published_at: "2026-06-23T02:03:38.000Z"
    retrieved_at: "2026-06-23T10:59:18+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
