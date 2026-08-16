---
signal_id: "CMSIG2026081403"
signal_slug: "us-recession-by-year-end-2026-polymarket-53-2026-08-14"
headline: "US recession by year-end 2026: Polymarket 53%"
semantic_title: "Recession by end of 2026 stays near 50% despite soft-landing talk"
telemetry: "Polymarket 53%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-14T15:41:15.000Z"
event_id: "CM-EVT-Z32WPK4K45"
event_slug: "us-economic-state-at-the-end-of-2026"
event_question: "Will the US economy be in recession at the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x50e3ee8f93a464d04ea2cea6efff45c902f43642aedbf43f7afdc899e10f71d8"
  question_raw: "Will the US economy be in a soft landing at the end of 2026?"
  current_price: 0.53
  volume_24h_usd: 0.0
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
bullets:
  - "The Polymarket contract on a US recession by end of 2026 sits at 53%, keeping odds just above even despite the week's soft-landing narrative."
  - "Soft retail sales, cooling PPI, and subdued jobless claims are consistent with a soft landing, yet the contract above 50% shows the market has not embraced that outcome fully."
  - "Cross-market: Kalshi's separate US recession contract (Bureau of Economic Analysis resolution) prices the probability at just 4%, a stark gap versus Polymarket's 53%, likely reflecting differing resolution definitions and timelines."
  - "Resolves via Polymarket's UMA oracle based on official US GDP data."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Fed September rate-hike expectations dropped to 30% as cooling inflation, jobs, and retail spending fueled soft-landing optimism, with the S&P 500 topping 7,800."
    publisher: "tradingkey.com"
    published_at: "2026-08-14T15:41:15.000Z"
    source_url: "https://www.tradingkey.com/analysis/stocks/us-stocks/262108725-fed-september-hike-cools-soft-landing-sp500-7800-tradingkey"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "tradingkey.com"
        source_url: "https://www.tradingkey.com/analysis/stocks/us-stocks/262108725-fed-september-hike-cools-soft-landing-sp500-7800-tradingkey"
        retrieved_at: "2026-08-16T08:23:09+00:00"
  - type: "pm_response"
    notes: "Polymarket at 53% and Kalshi at 4% on US recession reflect materially different resolution criteria; readers should weigh both venues with that definitional gap in mind."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "tradingkey.com: Fed September Rate Hike Expectations Drop to 30% as Inflation, Jobs, a"
    url: "https://www.tradingkey.com/analysis/stocks/us-stocks/262108725-fed-september-hike-cools-soft-landing-sp500-7800-tradingkey"
    published_at: "2026-08-14T15:41:15.000Z"
    retrieved_at: "2026-08-16T08:23:09+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
