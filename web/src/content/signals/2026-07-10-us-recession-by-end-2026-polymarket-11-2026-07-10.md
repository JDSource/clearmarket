---
signal_id: "CMSIG2026071003"
signal_slug: "us-recession-by-end-2026-polymarket-11-2026-07-10"
headline: "US recession by end 2026: Polymarket 11%"
semantic_title: "Recession by year-end consensus holds at deep discount"
telemetry: "Polymarket 11%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-10T09:40:23.000Z"
event_id: "CM-EVT-943Z5Y3NP4"
event_slug: "us-recession-by-end-of-2026"
event_question: "Will the United States enter a recession by the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xfdc73f10edf0266756686f35b5712cffa828b0940fc015e0426c76c934c2105d"
  question_raw: "US recession by end of 2026?"
  current_price: 0.11
  volume_24h_usd: 723.955603
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
bullets:
  - "The Polymarket contract prices only 11% probability on a US recession declared by end of 2026, resolved via UMA oracle."
  - "RSM's easing-supply-shock narrative aligns with the market's low recession pricing; the two readings reinforce rather than contradict each other."
  - "Kalshi's parallel contract (CM-EVT-L7017DJDX1) also sits at 11% via Bureau of Economic Analysis, showing cross-venue consensus with no gap to arbitrage."
  - "Resolves via UMA oracle using BEA GDP data; back-to-back negative real GDP quarters is the conventional trigger, making the Q3-Q4 2026 prints the key datapoints."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "RSM's midyear update argued supply shocks are easing, consistent with a soft-landing scenario heading into the second half of 2026."
    publisher: "Joseph Brusuelas"
    published_at: "2026-07-10T09:40:23.000Z"
    source_url: "https://realeconomy.rsmus.com/u-s-midyear-economic-update-supply-shocks-ease/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Joseph Brusuelas"
        source_url: "https://realeconomy.rsmus.com/u-s-midyear-economic-update-supply-shocks-ease/"
        retrieved_at: "2026-07-11T09:24:13+00:00"
  - type: "pm_response"
    notes: "Polymarket and Kalshi both price 11% on recession this year, confirming cross-venue alignment; no venue gap exists at current marks."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Joseph Brusuelas: RSM’s U.S. midyear economic update: Supply shocks ease"
    url: "https://realeconomy.rsmus.com/u-s-midyear-economic-update-supply-shocks-ease/"
    published_at: "2026-07-10T09:40:23.000Z"
    retrieved_at: "2026-07-11T09:24:13+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
