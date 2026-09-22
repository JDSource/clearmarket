---
signal_id: "CMSIG20260922VS05"
signal_slug: "will-russia-enter-sloviansk-by-december-vol-38106"
headline: "Russia in Sloviansk by Dec 31: 15% on $38K volume"
semantic_title: "Odds hold Russia out of Sloviansk by year-end at 15%"
telemetry: "15% · $38K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-22T13:04:04+00:00"
event_id: "CM-EVT-7G3FWY0RL4"
event_slug: "which-cities-will-russia-enter-by-december-31"
event_question: "Will Russia enter any additional cities by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xd4aa5c6bd2a179244d98ba714dba4441e4bf5f99f27a657b8d967f8f67cfe041"
  question_raw: "Will Russia enter Sloviansk by December 31, 2026?"
  current_price: 0.15
  volume_24h_usd: 38106.428371
  volume_cumulative_usd: 125333.16902900003
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "At 15%, Polymarket prices Russian entry into Sloviansk before December 31 as a low-probability tail."
  - "30% of all-time volume arrived in 24 hours, mirroring the Dopropillia contract's pattern, suggesting paired positioning."
  - "The gap between Dopropillia (97%) and Sloviansk (15%) maps a market-implied advance corridor traders are pricing explicitly."
  - "Resolves December 31, 2026."
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
      poly_vol_24h_usd: 38106.428371
sources:
  - label: "ClearMarket market record: Will Russia enter any additional cities by December 31?"
    url: "https://clearmarket.fyi/events/which-cities-will-russia-enter-by-december-31"
    retrieved_at: "2026-09-22T13:04:04+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Running this alongside Spike 0 gives a desk a market-implied frontline gradient, capital is pricing Dopropillia as done and Sloviansk as a distant next step, useful framing for geopolitical risk staging.
