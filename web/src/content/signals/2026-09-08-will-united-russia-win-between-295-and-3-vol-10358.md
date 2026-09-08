---
signal_id: "CMSIG20260908VS03"
signal_slug: "will-united-russia-win-between-295-and-3-vol-10358"
headline: "United Russia 295, 309 seats: 5% on $10K surge"
semantic_title: "Heavy trading tests United Russia's 295, 309 seat range at slim odds"
telemetry: "5% · $10K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-08T12:34:41+00:00"
event_id: "CM-EVT-MCHQSDBHW5"
event_slug: "how-many-seats-will-united-russia-win-in-the-next-russian-legislative-election"
event_question: "How many seats will United Russia win in the next Russian legislative election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a9bb5f9c32f57b1683bec4170da0a1116876f2bf0665a1ec9bf6c6db76d2f57"
  question_raw: "Will United Russia win between 295 and 309 seats in the next Russian State Duma election?"
  current_price: 0.05
  volume_24h_usd: 10358.720291
  volume_cumulative_usd: 27696.337788999994
  arbitration_model: "uma_oracle"
  resolves_at: "2026-09-20T00:00:00Z"
bullets:
  - "Polymarket prices this seat-band at 5%, traders see a higher or lower outcome as far more likely."
  - "$10.4K in 24h is 37% of all-time volume, a notable spike for a low-probability band contract."
  - "Volume alongside the adjacent 280, 294 band suggests traders are mapping probability across multiple Duma outcome buckets ahead of the election."
  - "Contract resolves on United Russia's official seat count in the next State Duma election."
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
      poly_vol_24h_usd: 10358.720291
sources:
  - label: "ClearMarket market record: How many seats will United Russia win in the next Russi"
    url: "https://clearmarket.fyi/events/how-many-seats-will-united-russia-win-in-the-next-russian-legislative-election"
    retrieved_at: "2026-09-08T12:34:41+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Simultaneous spikes across adjacent seat-band contracts signal a desk-level effort to build a probability distribution over Duma outcomes, worth tracking for geopolitical positioning ahead of the Russian election.
