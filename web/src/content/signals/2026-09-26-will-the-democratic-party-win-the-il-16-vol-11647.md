---
signal_id: "CMSIG20260926VS04"
signal_slug: "will-the-democratic-party-win-the-il-16-vol-11647"
headline: "Democrats IL-16 House: 0% on $12K surge"
semantic_title: "Democrats IL-16 odds sit at zero through a volume push"
telemetry: "0% · $12K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-26T07:47:58+00:00"
event_id: "CM-EVT-F04Q02GR20"
event_slug: "il-16-house-election-winner"
event_question: "Will the Illinois 16th Congressional District elect a new House representative in 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xe1f250d7363697296cbc5b845a4e9268e93ba29269b7465e69da60a418b4bf2c"
  question_raw: "Will the Democratic Party win the IL-16 House seat?"
  current_price: 0.001
  volume_24h_usd: 11647.789965999998
  volume_cumulative_usd: 37279.89739800001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "0% on Polymarket effectively rules out a Democratic win in IL-16 for 2026."
  - "24h volume of $12K equals 31% of all-time activity, a large single-day share for a contract already at zero."
  - "Volume into a zeroed contract may reflect late settlement positioning or a dispute over resolution criteria."
  - "Resolves on the certified IL-16 2026 House election result."
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
      poly_vol_24h_usd: 11647.789965999998
sources:
  - label: "ClearMarket market record: Will the Illinois 16th Congressional District elect a n"
    url: "https://clearmarket.fyi/events/il-16-house-election-winner"
    retrieved_at: "2026-09-26T07:47:58+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Significant volume against a 0% price in a House seat contract suggests either resolution-criteria arbitrage or a trader testing whether any path to YES remains, desks should review the contract's resolution rules.
