---
signal_id: "CMSIG20261101VS03"
signal_slug: "will-the-republican-party-hold-below-190-vol-64964"
headline: "GOP below 190 seats: 43% on $65K surge"
semantic_title: "Odds stay near 50% on Republicans falling below 190 seats"
telemetry: "43% · $65K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-01T14:43:30+00:00"
event_id: "CM-EVT-HZZP4JMQ30"
event_slug: "republican-house-seats-after-the-2026-midterm-elections"
event_question: "Will Republicans win more than 218 House seats in the 2026 midterm elections?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xa2e43598547f2e90e3eee195812c8814202b9b66f6c540d7e15a265cbe93f68f"
  question_raw: "Will the Republican Party hold below 190 House seats after the 2026 midterm elections?"
  current_price: 0.43
  volume_24h_usd: 64964.88390900001
  volume_cumulative_usd: 163925.43355999998
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "At 43% on Polymarket, the market sees a Republican sub-190 House outcome as slightly less likely than not."
  - "$65K in 24h is 40% of all-time volume, reflecting Election Day demand for macro House-composition exposure."
  - "The 190-seat threshold is a marker of a historic Democratic wave; 43% prices that scenario as live but not favored."
  - "Resolves on the final certified 2026 House seat count for Republicans."
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
      poly_vol_24h_usd: 64964.88390900001
sources:
  - label: "ClearMarket market record: Will Republicans win more than 218 House seats in the 2"
    url: "https://clearmarket.fyi/events/republican-house-seats-after-the-2026-midterm-elections"
    retrieved_at: "2026-11-01T14:43:30+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Near-even odds on a sub-190 Republican seat count, with 40% of all-time volume hitting today, signals desks are actively hedging against a larger-than-expected Democratic House surge.
