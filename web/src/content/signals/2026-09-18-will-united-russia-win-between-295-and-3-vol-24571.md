---
signal_id: "CMSIG20260918VS07"
signal_slug: "will-united-russia-win-between-295-and-3-vol-24571"
headline: "United Russia 295-309 seats: 6% on $25K surge"
semantic_title: "United Russia 295-309 seat band stays a long shot at 6%"
telemetry: "6% · $25K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-18T12:39:43+00:00"
event_id: "CM-EVT-MCHQSDBHW5"
event_slug: "how-many-seats-will-united-russia-win-in-the-next-russian-legislative-election"
event_question: "How many seats will United Russia win in the next Russian legislative election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a9bb5f9c32f57b1683bec4170da0a1116876f2bf0665a1ec9bf6c6db76d2f57"
  question_raw: "Will United Russia win between 295 and 309 seats in the next Russian State Duma election?"
  current_price: 0.058
  volume_24h_usd: 24571.685631999997
  volume_cumulative_usd: 97859.94900699997
  arbitration_model: "uma_oracle"
  resolves_at: "2026-09-20T00:00:00Z"
bullets:
  - "6% price marks the 295-309 seat band as a heavy underdog, the market prices a weaker United Russia result as unlikely."
  - "25% of all-time volume in one session, alongside Spike 4, shows capital rotating across seat-count brackets."
  - "Low price with non-trivial volume suggests traders are selling this band as the higher brackets absorb conviction."
  - "Resolves on certified seat totals from the next Russian State Duma election."
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
      poly_vol_24h_usd: 24571.685631999997
sources:
  - label: "ClearMarket market record: How many seats will United Russia win in the next Russi"
    url: "https://clearmarket.fyi/events/how-many-seats-will-united-russia-win-in-the-next-russian-legislative-election"
    retrieved_at: "2026-09-18T12:39:43+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Volume across both the 295-309 and 325-339 seat bands in the same session tells a desk the market is actively repricing the full United Russia seat distribution, with flow leaning toward the higher bracket.
