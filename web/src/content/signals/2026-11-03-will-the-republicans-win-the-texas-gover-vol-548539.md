---
signal_id: "CMSIG20261103VS05"
signal_slug: "will-the-republicans-win-the-texas-gover-vol-548539"
headline: "Texas GOP governor (PM): 64% on $549K volume"
semantic_title: "GOP Texas governor price holds at 64% on Polymarket volume"
telemetry: "64% · $549K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-03T15:46:45+00:00"
event_id: "CM-EVT-HCY4NZ1SN4"
event_slug: "texas-governor-winner-2026"
event_question: "Will the Texas Governor election be won by the Republican candidate?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xcd953913ecd5bf5387092bf447fe13190871b2bc9436c85b0918b4767c3fa58a"
  question_raw: "Will the Republicans win the Texas governor race in 2026?"
  current_price: 0.637
  volume_24h_usd: 548539.539742
  volume_cumulative_usd: 2015537.7634270005
  arbitration_model: "uma_oracle"
bullets:
  - "Polymarket prices the Republican Texas governor at 64%, roughly in line with Kalshi's 67% on the same race."
  - "$549K in 24h is 27% of all-time for this contract, consistent with broad midterm attention."
  - "The slight cross-venue price gap between Kalshi and Polymarket may attract arbitrage activity."
  - "Resolves on the 2026 Texas gubernatorial election result."
atomic_claims:
  - type: "volume_anomaly"
    provenance: "24h + cumulative volume direct from polymarket API; intensity = 24h/cumulative (derived)"
    field_provenance:
      volume_24h_usd:
        tier: "direct"
        method: "polymarket_api"
      intensity:
        tier: "derived"
        method: "arithmetic"
        inputs: ["volume_24h_usd", "volume_cumulative_usd"]
    liquidity_context:
      poly_vol_24h_usd: 548539.539742
sources:
  - label: "ClearMarket market record: Will the Texas Governor election be won by the Republic"
    url: "https://clearmarket.fyi/events/texas-governor-winner-2026"
    retrieved_at: "2026-11-03T15:46:45+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The Kalshi-Polymarket spread on the same Texas governor question is a live arbitrage signal; a desk running both venues should check whether the gap exceeds transaction costs.
