---
signal_id: "CMSIG20261101VS07"
signal_slug: "will-the-republican-party-hold-between-1-vol-10183"
headline: "GOP 190, 194 seats: 17% on $10K surge"
semantic_title: "Republican 190, 194 seat band stays a long shot despite fresh volume"
telemetry: "17% · $10K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-01T14:43:30+00:00"
event_id: "CM-EVT-HZZP4JMQ30"
event_slug: "republican-house-seats-after-the-2026-midterm-elections"
event_question: "Will Republicans win more than 218 House seats in the 2026 midterm elections?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x18cc1dd29f0b816135d5337cebae4d1f8b42a2c8b951e893936f35fd235ecc94"
  question_raw: "Will the Republican Party hold between 190 and 194 House seats after the 2026 midterm elections?"
  current_price: 0.17
  volume_24h_usd: 10183.357645
  volume_cumulative_usd: 34151.53883500001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "At 17% on Polymarket, a Republican final count landing in the narrow 190, 194 band is an unlikely but priced outcome."
  - "$10K in 24h is 30% of all-time volume, moderate Election Day interest in fine-grained House seat-count positioning."
  - "This contract pairs with the sub-190 spike (Spike 3), together mapping the full distribution of a wave scenario."
  - "Resolves on the final certified 2026 Republican House seat total."
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
      poly_vol_24h_usd: 10183.357645
sources:
  - label: "ClearMarket market record: Will Republicans win more than 218 House seats in the 2"
    url: "https://clearmarket.fyi/events/republican-house-seats-after-the-2026-midterm-elections"
    retrieved_at: "2026-11-01T14:43:30+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Low probability but active Election Day flow in the 190, 194 band tells a desk traders are building out a full House-composition distribution, not just binary control bets.
