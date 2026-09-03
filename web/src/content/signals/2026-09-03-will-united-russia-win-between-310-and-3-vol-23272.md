---
signal_id: "CMSIG20260903VS03"
signal_slug: "will-united-russia-win-between-310-and-3-vol-23272"
headline: "United Russia 310-324 seats: 24% on $23K flow"
semantic_title: "United Russia 310-324 seat band trades under 25%"
telemetry: "24% · $23K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-03T12:31:50+00:00"
event_id: "CM-EVT-MCHQSDBHW5"
event_slug: "how-many-seats-will-united-russia-win-in-the-next-russian-legislative-election"
event_question: "How many seats will United Russia win in the next Russian legislative election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x8e41c5c2c887553ea7cce7f3644b50c62c8ab55238b50e939048f6d71aae6d4c"
  question_raw: "Will United Russia win between 310 and 324 seats in the next Russian State Duma election?"
  current_price: 0.239
  volume_24h_usd: 23272.316056
  volume_cumulative_usd: 47087.138290999996
  arbitration_model: "uma_oracle"
  resolves_at: "2026-09-20T00:00:00Z"
bullets:
  - "Polymarket prices the specific seat band at 24%, traders lean toward a result outside this narrow range."
  - "24h volume of $23K is 49% of all-time flow, nearly half of all lifetime trading in one session."
  - "Russian State Duma election campaign activity or polling shifts appear to be driving fresh positioning."
  - "Resolves on the official seat count for United Russia in the next State Duma election."
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
      poly_vol_24h_usd: 23272.316056
sources:
  - label: "ClearMarket market record: How many seats will United Russia win in the next Russi"
    url: "https://clearmarket.fyi/events/how-many-seats-will-united-russia-win-in-the-next-russian-legislative-election"
    retrieved_at: "2026-09-03T12:31:50+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Nearly half of lifetime volume hitting in one session at sub-25% odds indicates traders are actively hedging or speculating on the seat distribution, likely in response to new polling or electoral developments.
