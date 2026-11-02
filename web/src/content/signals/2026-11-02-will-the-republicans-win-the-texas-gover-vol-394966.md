---
signal_id: "CMSIG20261102VS01"
signal_slug: "will-the-republicans-win-the-texas-gover-vol-394966"
headline: "Texas GOP governor: 62% on $395K volume spike"
semantic_title: "Buyers back Texas GOP governor odds above 50%"
telemetry: "62% · $395K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-02T17:45:32+00:00"
event_id: "CM-EVT-HCY4NZ1SN4"
event_slug: "texas-governor-winner-2026"
event_question: "Will the Texas Governor election be won by the Republican candidate?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xcd953913ecd5bf5387092bf447fe13190871b2bc9436c85b0918b4767c3fa58a"
  question_raw: "Will the Republicans win the Texas governor race in 2026?"
  current_price: 0.621
  volume_24h_usd: 394966.795953
  volume_cumulative_usd: 1501645.3603610003
  arbitration_model: "uma_oracle"
bullets:
  - "Polymarket prices Republicans at 62%, a clear but not commanding favorite for the Texas governorship in 2026."
  - "24h volume of $395K represents 26% of all-time contract flow, indicating a meaningful surge of fresh attention."
  - "Texas Democrats have made incremental inroads statewide; 62% implies the market is not treating this as a lock."
  - "Resolves on the 2026 Texas gubernatorial election outcome."
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
      poly_vol_24h_usd: 394966.795953
sources:
  - label: "ClearMarket market record: Will the Texas Governor election be won by the Republic"
    url: "https://clearmarket.fyi/events/texas-governor-winner-2026"
    retrieved_at: "2026-11-02T17:45:32+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Active two-way flow on a 62% favorite suggests the desk community sees legitimate contest risk in Texas and is not willing to let this trade go unhedged into the midterm cycle.
