---
signal_id: "CMSIG20261012VS01"
signal_slug: "will-the-democratic-party-win-the-ny-23-vol-15683"
headline: "Dem NY-23 House win: 2% on $15K volume"
semantic_title: "Democrats priced out of NY-23 as odds stay at 2%"
telemetry: "2% · $16K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-12T17:18:20+00:00"
event_id: "CM-EVT-K34TZHDVH7"
event_slug: "ny-23-house-election-winner"
event_question: "NY-23 House Election Winner"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x6098d023d47306dbb9d9b41675038f09b47718e4e833e46599bef3ae338dbb35"
  question_raw: "Will the Democratic Party win the NY-23 House seat?"
  current_price: 0.024
  volume_24h_usd: 15683.045715
  volume_cumulative_usd: 31233.217899
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices Democratic odds of winning NY-23 at 2%, near-total Republican lock."
  - "24h volume of $15.7K is 50% of all-time, showing fresh attention on a heavily one-sided contract."
  - "NY-23 has lean-Republican fundamentals; volume surge likely reflects hedging or late confirmation trades."
  - "Resolves on certified House election result for NY-23."
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
      poly_vol_24h_usd: 15683.045715
sources:
  - label: "ClearMarket market record: NY-23 House Election Winner"
    url: "https://clearmarket.fyi/events/ny-23-house-election-winner"
    retrieved_at: "2026-10-12T17:18:20+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Heavy volume on a 2% contract signals a desk should watch for any late-breaking news that could reprice a seemingly settled race, or confirm the market is efficiently absorbing final closing bets.
