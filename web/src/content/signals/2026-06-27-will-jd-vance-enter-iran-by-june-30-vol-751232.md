---
signal_id: "CMSIG20260627VS00"
signal_slug: "will-jd-vance-enter-iran-by-june-30-vol-751232"
headline: "Vance Iran visit by June 30: 0% on $751K surge"
semantic_title: "Traders write off a Vance Iran entry by June 30"
telemetry: "0% · $751K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-27T10:03:08+00:00"
event_id: "CM-EVT-QF15YF74T9"
event_slug: "who-will-enter-iran-by-june-30"
event_question: "Will someone enter Iran by June 30?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x77eafa497fe8ff7a41f540e2920e8897540b01f06b82477d168c4a21a7f9e57a"
  question_raw: "Will JD Vance enter Iran by June 30?"
  current_price: 0.002
  volume_24h_usd: 751232.3859969998
  volume_cumulative_usd: 2618619.220146999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-06-30T00:00:00Z"
bullets:
  - "Polymarket prices zero probability, market treats the scenario as expired fiction."
  - "29% of all-time volume, $751K in 24h, signals a final flush of residual longs."
  - "Three days to deadline with no diplomatic groundwork; attention spike likely confirms closure."
  - "Contract resolves June 30, zero price means capital is collecting, not wagering."
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
      poly_vol_24h_usd: 751232.3859969998
sources:
  - label: "ClearMarket market record: Will someone enter Iran by June 30?"
    url: "https://clearmarket.fyi/events/who-will-enter-iran-by-june-30"
    retrieved_at: "2026-06-27T10:03:08+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should read this as a crowded, near-unanimous close-out trade, late holders liquidating into a hard deadline with no credible path to resolution.
