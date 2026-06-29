---
signal_id: "CMSIG20260629VS04"
signal_slug: "will-the-h200-compute-per-hour-price-be-vol-17657"
headline: "H200 above $4.79 by Jun 30: 96% on $18K"
semantic_title: "H200 compute pricing above $4.79 commands near-certain flows"
telemetry: "96% · $18K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-29T01:47:13+00:00"
event_id: "CM-EVT-XQHHCRQHC2"
event_slug: "kxh200q-26jun30"
event_question: "Will the price of NVIDIA H200 compute decrease by June 30, 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXH200Q-26JUN30-4.790"
  question_raw: "Will the H200 compute per hour price be above $4.79 by Jun 30?"
  current_price: 0.96
  volume_24h_usd: 17657.22
  volume_cumulative_usd: 38107.32
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-07-01T03:59:59Z"
bullets:
  - "Kalshi prices 96%, market treats H200 hourly compute staying above $4.79 as effectively resolved."
  - "$18K in 24h is 46% of all-time volume; concentrated positioning ahead of tomorrow's deadline."
  - "Current cloud GPU spot rates well above threshold; 96% reflects observable market data, not speculation."
  - "Resolves June 30, any observable pricing data confirming the rate closes the contract at near-par."
atomic_claims:
  - type: "volume_anomaly"
    provenance: "24h + cumulative volume direct from kalshi API; intensity = 24h/cumulative (derived)"
    field_provenance:
      volume_24h_usd:
        tier: "direct"
        method: "kalshi_api"
      intensity:
        tier: "derived"
        method: "arithmetic"
        inputs: ["volume_24h_usd", "volume_cumulative_usd"]
    liquidity_context:
      kalshi_vol_24h_usd: 17657.22
sources:
  - label: "ClearMarket market record: Will the price of NVIDIA H200 compute decrease by June "
    url: "https://clearmarket.fyi/events/kxh200q-26jun30"
    retrieved_at: "2026-06-29T01:47:13+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

This contract trades as a near-certainty arbitrage on observable GPU pricing data; desk relevance lies in the implied signal that H200 compute costs remain structurally elevated, sustaining AI infrastructure cost assumptions.
