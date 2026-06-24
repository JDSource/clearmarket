---
signal_id: "CMSIG2026062308"
signal_slug: "june-u-3-unemployment-above-4-2-kalshi-63-2026-06-23"
headline: "June U-3 unemployment above 4.2%: Kalshi 63%"
semantic_title: "June unemployment rate consensus centers on 4.2-4.3 percent range"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-23T02:03:38.000Z"
event_id: "CM-EVT-FJGT56DTV2"
event_slug: "kxu3-26jun"
event_question: "June 2026 U-3 unemployment rate"
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
  - "Kalshi ladder implies June unemployment in the 4.2-4.3% range: 63% above 4.2%, dropping sharply to 31% above 4.3%."
  - "Falling weekly claims are a modest downside signal for unemployment, but the market still prices near-even odds above 4.2%."
  - "The long-horizon contract (CM-EVT-RBY62SKLC0) shows only 23% chance unemployment breaches 5.0% before 2027, limiting tail-risk concern."
  - "Resolves via the Bureau of Labor Statistics Employment Situation report; the official U-3 figure, not claims data, determines settlement."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Weekly jobless claims fell, signaling continued labor market resilience despite ongoing hiring challenges."
    publisher: "csuiteera.com"
    published_at: "2026-06-23T02:03:38.000Z"
    source_url: "https://csuiteera.com/us-jobless-claims-fall/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "csuiteera.com"
        source_url: "https://csuiteera.com/us-jobless-claims-fall/"
        retrieved_at: "2026-06-24T10:45:49+00:00"
  - type: "pm_response"
    notes: "Kalshi's June unemployment ladder shows a tight modal range of 4.2-4.3%, with the claims improvement leaving the distribution largely unchanged at current pricing."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "csuiteera.com: US Jobless Claims Fall As Labor Market Remains Resilient | C Suit Era"
    url: "https://csuiteera.com/us-jobless-claims-fall/"
    published_at: "2026-06-23T02:03:38.000Z"
    retrieved_at: "2026-06-24T10:45:49+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
