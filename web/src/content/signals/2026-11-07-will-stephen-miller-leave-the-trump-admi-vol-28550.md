---
signal_id: "CMSIG20261107VS06"
signal_slug: "will-stephen-miller-leave-the-trump-admi-vol-28550"
headline: "Miller leaves Trump admin: 3% on $29K Polymarket inflow"
semantic_title: "Miller administration exit odds stay near zero as trading picks up"
telemetry: "3% · $29K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-07T07:49:22+00:00"
event_id: "CM-EVT-KZSP2MGN63"
event_slug: "who-will-leave-trump-administration-before-2027"
event_question: "Will anyone leave the Trump Administration before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x8e2c840905e4089910b2797984e2331e23be0b0071ddcb67c466a120faf05b60"
  question_raw: "Will Stephen Miller leave the Trump administration before 2027?"
  current_price: 0.031
  volume_24h_usd: 28550.727003
  volume_cumulative_usd: 47317.728451
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "3% price on the broader admin exit contract echoes the near-certainty on Spike 0."
  - "Polymarket logs $29K in 24h, 60% of all-time, reinforcing coordinated cross-venue flow."
  - "Pairing with Kalshi's 97% NO (Spike 0) shows consistent cross-venue conviction."
  - "Resolves end of 2026; near-zero pricing reflects no credible exit pathway."
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
      poly_vol_24h_usd: 28550.727003
sources:
  - label: "ClearMarket market record: Will anyone leave the Trump Administration before 2027?"
    url: "https://clearmarket.fyi/events/who-will-leave-trump-administration-before-2027"
    retrieved_at: "2026-11-07T07:49:22+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The cross-venue alignment between Kalshi and Polymarket on Miller, both near-certain retention, tells a desk the market has absorbed any rumour and dismissed it decisively.
