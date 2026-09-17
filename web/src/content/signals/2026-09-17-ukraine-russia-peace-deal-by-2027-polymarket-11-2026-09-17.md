---
signal_id: "CMSIG2026091704"
signal_slug: "ukraine-russia-peace-deal-by-2027-polymarket-11-2026-09-17"
headline: "Ukraine-Russia peace deal by 2027: Polymarket 11%"
semantic_title: "Ukraine-Russia peace deal before 2027 stays a long shot"
telemetry: "Polymarket 11%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-17T00:00:00.000Z"
event_id: "CM-EVT-DCQYWYX424"
event_slug: "ukraine-signs-peace-deal-with-russia-before-2027"
event_question: "Will Ukraine sign a peace deal with Russia before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x4167e22670f31e5f93d132f78108f3fae809bd15cadf78983eff096845ed1415"
  question_raw: "Ukraine signs peace deal with Russia before 2027?"
  current_price: 0.11
  volume_24h_usd: 6889.236746
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract on Ukraine signing a peace deal with Russia before 2027 prices at 11%."
  - "Russia's explicit warning that sanctions complicate negotiations is consistent with the market's low-probability stance on a near-term deal."
  - "A companion Polymarket contract on a ceasefire in 2026 prices at 15%, slightly above the full peace deal contract, reflecting the gap between a pause and a settlement."
  - "The Polymarket contract resolves via UMA oracle; a formal signed peace agreement would be required for YES, not a ceasefire or partial truce."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Russia warned that new US sanctions, if signed by Trump, would make a Ukraine peace deal harder to achieve."
    publisher: "reuters.com"
    published_at: "2026-09-17T00:00:00.000Z"
    source_url: "https://www.reuters.com/world/europe/russia-says-new-us-sanctions-if-signed-by-trump-would-make-ukraine-peace-deal-2026-09-17/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "reuters.com"
        source_url: "https://www.reuters.com/world/europe/russia-says-new-us-sanctions-if-signed-by-trump-would-make-ukraine-peace-deal-2026-09-17/"
        retrieved_at: "2026-09-17T13:04:18+00:00"
  - type: "pm_response"
    notes: "Polymarket at 11% resolves via UMA oracle; Russia's sanctions warning reinforces the market's skeptical pricing."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "reuters.com: Russia says new US sanctions, if signed by Trump, would make  Ukraine"
    url: "https://www.reuters.com/world/europe/russia-says-new-us-sanctions-if-signed-by-trump-would-make-ukraine-peace-deal-2026-09-17/"
    published_at: "2026-09-17T00:00:00.000Z"
    retrieved_at: "2026-09-17T13:04:18+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
