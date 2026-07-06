---
signal_id: "CMSIG2026070606"
signal_slug: "us-negative-gdp-growth-in-2026-polymarket-8-2026-07-06"
headline: "US negative GDP growth in 2026: Polymarket 8%"
semantic_title: "US negative GDP in 2026 remains a low-conviction fringe bet"
telemetry: "Polymarket 8%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "lagging"
published_at: "2026-07-06T06:59:15.688Z"
event_id: "CM-EVT-36YHF72CQ8"
event_slug: "negative-gdp-growth-in-2026"
event_question: "Will the United States experience negative GDP growth in 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xd8c1b0a73653b1fb4fb6e8d13d0063d25810870d7ddf83e61fffb4de4522edf1"
  question_raw: "Negative GDP growth in 2026?"
  current_price: 0.078
  volume_24h_usd: 81.588102
  arbitration_model: "uma_oracle"
  resolution_source: "bea.gov"
  resolves_at: "2027-01-29T00:00:00Z"
bullets:
  - "Polymarket prices only an 8% chance the United States records negative GDP growth in 2026."
  - "Despite June payrolls missing badly at 57,000, the market treats a full-year GDP contraction as a tail risk, not a base case."
  - "At 8%, the market is not fading the weak labor data outright, it is absorbing it while keeping recession pricing low."
  - "Resolves via the Bureau of Economic Analysis (bea.gov) full-year GDP report; negative growth requires two or more quarters of contraction to register annually."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Ongoing U.S. economic data including the weak June jobs report has kept recession fears in circulation."
    publisher: "tradingeconomics.com"
    published_at: "2026-07-06T06:59:15.688Z"
    source_url: "https://tradingeconomics.com/united-states/news"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "tradingeconomics.com"
        source_url: "https://tradingeconomics.com/united-states/news"
        retrieved_at: "2026-07-06T12:00:14+00:00"
  - type: "pm_response"
    notes: "Polymarket at 8% shows the recession pricing remains firmly in tail territory despite the labor market deterioration evident in June's payroll print."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "tradingeconomics.com: United States News - Trading Economics"
    url: "https://tradingeconomics.com/united-states/news"
    published_at: "2026-07-06T06:59:15.688Z"
    retrieved_at: "2026-07-06T12:00:14+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
