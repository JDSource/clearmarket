---
signal_id: "CMSIG2026102907"
signal_slug: "negative-us-gdp-growth-2026-polymarket-3-2026-10-29"
headline: "Negative US GDP growth 2026: Polymarket 3%"
semantic_title: "Negative US GDP growth in 2026 stays a long shot"
telemetry: "Polymarket 3%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "lagging"
published_at: "2026-10-29T00:00:00.000Z"
event_id: "CM-EVT-36YHF72CQ8"
event_slug: "negative-gdp-growth-in-2026"
event_question: "Will there be negative GDP growth in 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xd8c1b0a73653b1fb4fb6e8d13d0063d25810870d7ddf83e61fffb4de4522edf1"
  question_raw: "Negative GDP growth in 2026?"
  current_price: 0.029
  volume_24h_usd: 0.0
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-29T00:00:00Z"
bullets:
  - "Polymarket prices negative US GDP growth in 2026 at just 3%, consistent with a strong Q3 beat of 3.4% annualized growth."
  - "The Q3 print directly undercuts any recession narrative; the Polymarket contract is aligned with the data, not at odds with it."
  - "Persistent above-target inflation complicates the picture but does not threaten growth-positive resolution of this contract."
  - "Polymarket resolves via UMA oracle; with Q3 final data already at 3.4%, the full-year negative GDP outcome would require a severe Q4 contraction."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Q3 2026 US GDP grew 3.4%, beating forecasts, while September PCE inflation accelerated above the Fed's 2% target, providing a final pre-election economic snapshot."
    publisher: "Stephan Bisaha"
    published_at: "2026-10-29T00:00:00.000Z"
    source_url: "https://www.npr.org/2026/10/29/nx-s1-6020539/two-reports-give-insight-on-the-economy-ahead-of-election-day"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Stephan Bisaha"
        source_url: "https://www.npr.org/2026/10/29/nx-s1-6020539/two-reports-give-insight-on-the-economy-ahead-of-election-day"
        retrieved_at: "2026-10-30T14:47:28+00:00"
  - type: "pm_response"
    notes: "Polymarket's 3% pricing on negative 2026 GDP is effectively a tail-risk residual after a strong Q3 print; the market is fully aligned with the bullish growth data."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Stephan Bisaha: Two reports give insight on the economy ahead of Election Day : NPR"
    url: "https://www.npr.org/2026/10/29/nx-s1-6020539/two-reports-give-insight-on-the-economy-ahead-of-election-day"
    published_at: "2026-10-29T00:00:00.000Z"
    retrieved_at: "2026-10-30T14:47:28+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
