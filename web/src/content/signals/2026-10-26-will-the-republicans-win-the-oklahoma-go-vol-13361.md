---
signal_id: "CMSIG20261026VS07"
signal_slug: "will-the-republicans-win-the-oklahoma-go-vol-13361"
headline: "GOP Oklahoma governor 2026: 91% on $13K"
semantic_title: "Oklahoma governor race draws fresh bets on a 91% Republican hold"
telemetry: "91% · $13K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-26T07:48:41+00:00"
event_id: "CM-EVT-1DTWM6K041"
event_slug: "oklahoma-governor-winner-2026"
event_question: "Will the Oklahoma governor election be won by the Republican candidate?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x45165a4a2a03b178007446496ec61a551125ec2bc56eae79d444b68b322af3cd"
  question_raw: "Will the Republicans win the Oklahoma governor race in 2026?"
  current_price: 0.91
  volume_24h_usd: 13361.274611
  volume_cumulative_usd: 47214.118712
  arbitration_model: "uma_oracle"
bullets:
  - "Republicans priced at 91%, market treats the Oklahoma governorship as a near-certain hold."
  - "28% of all-time Polymarket volume arrived in 24 hours, a moderate but notable spike."
  - "Fresh attention on a high-confidence contract may reflect a candidate filing deadline or primary development."
  - "Resolves on the certified 2026 Oklahoma gubernatorial election result."
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
      poly_vol_24h_usd: 13361.274611
sources:
  - label: "ClearMarket market record: Will the Oklahoma governor election be won by the Repub"
    url: "https://clearmarket.fyi/events/oklahoma-governor-winner-2026"
    retrieved_at: "2026-10-26T07:48:41+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A volume bump on a 91% contract in a non-competitive state suggests a primary or candidate-qualification event drove attention, a desk can use this as a low-risk reference point for Republican state-level strength heading into the 2026 cycle.
