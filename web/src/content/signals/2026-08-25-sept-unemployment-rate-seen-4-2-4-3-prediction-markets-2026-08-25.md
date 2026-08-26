---
signal_id: "CMSIG2026082503"
signal_slug: "sept-unemployment-rate-seen-4-2-4-3-prediction-markets-2026-08-25"
headline: "Sept unemployment rate seen 4.2-4.3%: prediction markets"
semantic_title: "September unemployment rate odds hold near 4.2-4.3%"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-25T00:00:00.000Z"
event_id: "CM-EVT-720DZC17Y9"
event_slug: "kxu3-26sep"
event_question: "September 2026 U-3 unemployment rate"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXU3-26SEP-T4.3"
  question_raw: "Will the unemployment rate (U-3) be above 4.3% in September?"
  current_price: 0.3
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-01-01T14:00:00Z"
bullets:
  - "The prediction market ladder implies September unemployment in the 4.2-4.3% range, with 52% above 4.2% but only 30% above 4.3%."
  - "Wolfe Research's 4.16% unemployment call sits just below the market's modal range, meaning the market is slightly more pessimistic than the Wolfe forecast."
  - "The 88% probability above 4.0% is consistent with the broader narrative of a labor market softening but not collapsing."
  - "Compare the August unemployment ladder (CM-EVT-CN1M891289), which implies 4.0-4.1% for the current month, confirming a market expectation of gradual deterioration into September."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Wolfe Research forecasts August nonfarm payrolls of 65,000, above the 55,000 consensus, with unemployment expected to tick up to 4.16%."
    publisher: "roic.ai"
    published_at: "2026-08-25T00:00:00.000Z"
    source_url: "https://www.roic.ai/news/wolfe-research-sees-august-payrolls-beating-expectations-but-feds-focus-remains-inflation-08-25-2026"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "roic.ai"
        source_url: "https://www.roic.ai/news/wolfe-research-sees-august-payrolls-beating-expectations-but-feds-focus-remains-inflation-08-25-2026"
        retrieved_at: "2026-08-26T08:38:02+00:00"
  - type: "pm_response"
    notes: "Prediction market ladder prices September U-3 unemployment in the 4.2-4.3% range, slightly above Wolfe's 4.16% call, with volume elevated on the August contract."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "roic.ai: Wolfe Research Sees August Payrolls Beating Expectations, But Fed's Fo"
    url: "https://www.roic.ai/news/wolfe-research-sees-august-payrolls-beating-expectations-but-feds-focus-remains-inflation-08-25-2026"
    published_at: "2026-08-25T00:00:00.000Z"
    retrieved_at: "2026-08-26T08:38:02+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
