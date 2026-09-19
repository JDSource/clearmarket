---
signal_id: "CMSIG20260919VS03"
signal_slug: "will-united-russia-win-between-340-and-3-vol-40594"
headline: "United Russia 340-354 seats: 30% on $41K"
semantic_title: "United Russia holding 340-354 Duma seats looks unlikely"
telemetry: "30% · $41K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-19T12:15:36+00:00"
event_id: "CM-EVT-MCHQSDBHW5"
event_slug: "how-many-seats-will-united-russia-win-in-the-next-russian-legislative-election"
event_question: "How many seats will United Russia win in the next Russian legislative election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5ee38949a4ba69f716052e5139b03953e2ecf79e8130d583f92acd87e3c1ca68"
  question_raw: "Will United Russia win between 340 and 354 seats in the next Russian State Duma election?"
  current_price: 0.3
  volume_24h_usd: 40594.427544000006
  volume_cumulative_usd: 149642.020962
  arbitration_model: "uma_oracle"
  resolves_at: "2026-09-20T00:00:00Z"
bullets:
  - "Polymarket prices United Russia landing in the 340-354 seat band at just 30%, the market leans against this range."
  - "24h volume of $41K is 27% of all-time, a meaningful session for an emerging geopolitical contract."
  - "Low odds suggest traders expect United Russia to either overshoot or undershoot this specific seat bracket."
  - "Resolves on official Russian State Duma election results."
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
      poly_vol_24h_usd: 40594.427544000006
sources:
  - label: "ClearMarket market record: How many seats will United Russia win in the next Russi"
    url: "https://clearmarket.fyi/events/how-many-seats-will-united-russia-win-in-the-next-russian-legislative-election"
    retrieved_at: "2026-09-19T12:15:36+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Volume clustering at 30% on a narrow seat-count band tells desks that positioning is shifting toward outcomes outside this range, likely toward a higher United Russia total given typical electoral dynamics.
