---
signal_id: "CMSIG20260908VS04"
signal_slug: "will-united-russia-win-between-280-and-2-vol-11106"
headline: "United Russia 280, 294 seats: 1% on $11K volume"
semantic_title: "Odds stay near zero on United Russia claiming 280, 294 Duma seats"
telemetry: "1% · $11K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-08T12:34:41+00:00"
event_id: "CM-EVT-MCHQSDBHW5"
event_slug: "how-many-seats-will-united-russia-win-in-the-next-russian-legislative-election"
event_question: "How many seats will United Russia win in the next Russian legislative election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x070312637ff200867e1316b2a4e31c7f2492610c78dd0851608c23f6ef9f3d7a"
  question_raw: "Will United Russia win between 280 and 294 seats in the next Russian State Duma election?"
  current_price: 0.013
  volume_24h_usd: 11106.92
  volume_cumulative_usd: 32548.895462999993
  arbitration_model: "uma_oracle"
  resolves_at: "2026-09-20T00:00:00Z"
bullets:
  - "Polymarket prices this band at just 1%, the market strongly discounts a result this low for United Russia."
  - "$11.1K in 24h equals 34% of all-time volume, running parallel to the 295, 309 band spike."
  - "Near-zero pricing with double-digit all-time volume share suggests traders are closing out or hedging positions rather than initiating new longs."
  - "Resolves on the official United Russia seat count in the next State Duma."
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
      poly_vol_24h_usd: 11106.92
sources:
  - label: "ClearMarket market record: How many seats will United Russia win in the next Russi"
    url: "https://clearmarket.fyi/events/how-many-seats-will-united-russia-win-in-the-next-russian-legislative-election"
    retrieved_at: "2026-09-08T12:34:41+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

At 1% and rising volume, a desk should treat this as a hedge or tail-risk contract, the activity is more diagnostic of how traders are structuring Duma-outcome exposure than a directional bet on this band.
