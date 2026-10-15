---
signal_id: "CMSIG20261015VS01"
signal_slug: "will-the-republican-party-win-the-ny-23-vol-34993"
headline: "NY-23 (R): 97% on $35K, 63% of all-time vol"
semantic_title: "Traders pile into NY-23 Republican hold at near-certain odds"
telemetry: "97% · $35K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-15T07:48:38+00:00"
event_id: "CM-EVT-K34TZHDVH7"
event_slug: "ny-23-house-election-winner"
event_question: "NY-23 House Election Winner"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x8aceb4fc5afb4b23dd93b7f0845ea50bb28226d8bca67d5dfabd2647cd663155"
  question_raw: "Will the Republican Party win the NY-23 House seat?"
  current_price: 0.973
  volume_24h_usd: 34993.443272
  volume_cumulative_usd: 55559.56950899999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "At 97%, Polymarket has the Republican candidate as a virtual lock for the NY-23 House seat."
  - "$35K in 24h represents 63% of the contract's entire all-time volume, an unusually concentrated burst."
  - "Late-cycle volume at near-ceiling odds suggests a specific catalyst confirming Republican strength, or late arbitrage closing residual risk."
  - "Contract resolves on NY-23 House election result."
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
      poly_vol_24h_usd: 34993.443272
sources:
  - label: "ClearMarket market record: NY-23 House Election Winner"
    url: "https://clearmarket.fyi/events/ny-23-house-election-winner"
    retrieved_at: "2026-10-15T07:48:38+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Two-thirds of all-time liquidity landing in one day at 97% tells a desk this race is being officially retired as a contest, focus shifts to adjacent competitive seats.
