---
signal_id: "CMSIG20261015VS03"
signal_slug: "will-the-republican-party-win-the-ny-23-vol-34973"
headline: "NY-23 GOP win: 96% on $34.9K Polymarket surge"
semantic_title: "NY-23 Republican hold attracts heavy odds near certainty"
telemetry: "96% · $35K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-15T13:03:58+00:00"
event_id: "CM-EVT-K34TZHDVH7"
event_slug: "ny-23-house-election-winner"
event_question: "NY-23 House Election Winner"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x8aceb4fc5afb4b23dd93b7f0845ea50bb28226d8bca67d5dfabd2647cd663155"
  question_raw: "Will the Republican Party win the NY-23 House seat?"
  current_price: 0.964
  volume_24h_usd: 34973.631151
  volume_cumulative_usd: 55560.339509
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Republicans priced at 96% in NY-23, the market treats this seat as effectively decided."
  - "$35K in 24h is 63% of all-time, a notable concentration for what appears a non-competitive race."
  - "Volume near certainty often reflects arbitrage flow or late hedgers covering opposite exposure in adjacent races."
  - "Resolves on 2026 NY-23 House election result."
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
      poly_vol_24h_usd: 34973.631151
sources:
  - label: "ClearMarket market record: NY-23 House Election Winner"
    url: "https://clearmarket.fyi/events/ny-23-house-election-winner"
    retrieved_at: "2026-10-15T13:03:58+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

High-confidence volume on a near-certain outcome suggests this is likely arb or portfolio-level House-composition hedging rather than new directional opinion, useful as a calibration point for broader House control models.
