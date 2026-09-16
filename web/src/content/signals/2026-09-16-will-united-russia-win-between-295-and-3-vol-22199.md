---
signal_id: "CMSIG20260916VS05"
signal_slug: "will-united-russia-win-between-295-and-3-vol-22199"
headline: "United Russia 295-309 Duma seats: 8% on $22K"
semantic_title: "United Russia winning 295, 309 Duma seats trades at just 8%"
telemetry: "8% · $22K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-16T13:03:41+00:00"
event_id: "CM-EVT-MCHQSDBHW5"
event_slug: "how-many-seats-will-united-russia-win-in-the-next-russian-legislative-election"
event_question: "How many seats will United Russia win in the next Russian legislative election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a9bb5f9c32f57b1683bec4170da0a1116876f2bf0665a1ec9bf6c6db76d2f57"
  question_raw: "Will United Russia win between 295 and 309 seats in the next Russian State Duma election?"
  current_price: 0.075
  volume_24h_usd: 22199.885993
  volume_cumulative_usd: 67067.703866
  arbitration_model: "uma_oracle"
  resolves_at: "2026-09-20T00:00:00Z"
bullets:
  - "Polymarket prices this specific seat-band at 8%, implying the market expects United Russia's haul to land elsewhere."
  - "$22.2K in 24h is 33% of all-time volume, clustering attention on Russian Duma seat-distribution contracts."
  - "Paired with the 280, 294 band contract at 9%, traders appear to be mapping out the full seat distribution."
  - "Duma election context is the resolution driver; watch for official Russian electoral commission guidance."
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
      poly_vol_24h_usd: 22199.885993
sources:
  - label: "ClearMarket market record: How many seats will United Russia win in the next Russi"
    url: "https://clearmarket.fyi/events/how-many-seats-will-united-russia-win-in-the-next-russian-legislative-election"
    retrieved_at: "2026-09-16T13:03:41+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Parallel volume spikes across adjacent Duma seat-band contracts suggest traders are actively triangulating the expected United Russia seat count, useful for desks modeling Russian political risk scenarios.
