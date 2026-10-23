---
signal_id: "CMSIG20261023VS02"
signal_slug: "will-the-republicans-win-the-idaho-senat-vol-105362"
headline: "Idaho Senate GOP Polymarket: 97% on $105K spike"
semantic_title: "Traders back Idaho GOP lock on polymarket at near-certainty"
telemetry: "97% · $105K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-23T07:49:03+00:00"
event_id: "CM-EVT-HW8FT0L534"
event_slug: "idaho-senate-election-winner"
event_question: "Will the Republicans win the Idaho Senate race in 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x22e986868fae24a9e7b6fff86e063cc90843c85c4a9dd65b2628bbf5663997c7"
  question_raw: "Will the Republicans win the Idaho Senate race in 2026?"
  current_price: 0.969
  volume_24h_usd: 105362.516704
  volume_cumulative_usd: 245897.37426199997
  arbitration_model: "uma_oracle"
bullets:
  - "97% price on polymarket echoes Kalshi's read, GOP Idaho win treated as a near-certainty across venues."
  - "$105,363 in 24h volume is 43% of all-time, mirroring the Kalshi spike on the same race today."
  - "Cross-venue volume surge on the same contract suggests coordinated positioning or an arbitrage desk active on both books."
  - "Resolves on 2026 Idaho Senate general election."
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
      poly_vol_24h_usd: 105362.516704
sources:
  - label: "ClearMarket market record: Will the Republicans win the Idaho Senate race in 2026?"
    url: "https://clearmarket.fyi/events/idaho-senate-election-winner"
    retrieved_at: "2026-10-23T07:49:03+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Simultaneous spikes on both Kalshi and polymarket for the same Idaho race in the same session points to multi-venue arbitrage activity, a desk should check for any residual price discrepancy between the two.
