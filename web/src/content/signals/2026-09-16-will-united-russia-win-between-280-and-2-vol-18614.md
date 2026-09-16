---
signal_id: "CMSIG20260916VS06"
signal_slug: "will-united-russia-win-between-280-and-2-vol-18614"
headline: "United Russia 280-294 Duma seats: 9% on $19K"
semantic_title: "United Russia landing 280, 294 Duma seats also priced as unlikely"
telemetry: "9% · $19K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-16T13:03:41+00:00"
event_id: "CM-EVT-MCHQSDBHW5"
event_slug: "how-many-seats-will-united-russia-win-in-the-next-russian-legislative-election"
event_question: "How many seats will United Russia win in the next Russian legislative election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x070312637ff200867e1316b2a4e31c7f2492610c78dd0851608c23f6ef9f3d7a"
  question_raw: "Will United Russia win between 280 and 294 seats in the next Russian State Duma election?"
  current_price: 0.089
  volume_24h_usd: 18614.805306
  volume_cumulative_usd: 72885.65901200003
  arbitration_model: "uma_oracle"
  resolves_at: "2026-09-20T00:00:00Z"
bullets:
  - "Polymarket prices this adjacent seat-band at 9%, nearly identical to the 295, 309 band, both treated as low-probability outcomes."
  - "26% of all-time volume, $18.6K, arrived in 24h, tracking in tandem with the sister contract above."
  - "Coordinated volume across adjacent bands signals systematic seat-distribution modeling, not random speculation."
  - "Resolution hinges on official Duma election results; the market's probability mass appears concentrated outside both these ranges."
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
      poly_vol_24h_usd: 18614.805306
sources:
  - label: "ClearMarket market record: How many seats will United Russia win in the next Russi"
    url: "https://clearmarket.fyi/events/how-many-seats-will-united-russia-win-in-the-next-russian-legislative-election"
    retrieved_at: "2026-09-16T13:03:41+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The near-identical pricing and simultaneous volume across two adjacent Duma seat-band contracts points to structured position-building on Russian electoral outcomes, desks should treat both contracts as a single geopolitical risk signal.
