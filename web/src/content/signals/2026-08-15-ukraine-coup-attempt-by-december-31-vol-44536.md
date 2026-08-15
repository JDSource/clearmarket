---
signal_id: "CMSIG20260815VS03"
signal_slug: "ukraine-coup-attempt-by-december-31-vol-44536"
headline: "Ukraine coup by Dec 31: 8% on $45K surge"
semantic_title: "Ukraine coup odds hold low at 8% through a volume rise"
telemetry: "8% · $45K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-15T08:22:27+00:00"
event_id: "CM-EVT-YXSZTFG520"
event_slug: "ukraine-coup-attempt-by-june-30"
event_question: "Will there be a coup attempt in Ukraine by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x71ee8e53f370ab5630f8a68f8a40d4e4cbbad222138f208de574056e80ab8473"
  question_raw: "Ukraine coup attempt by December 31?"
  current_price: 0.08
  volume_24h_usd: 44536.53
  volume_cumulative_usd: 151304.65645799998
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "8% price reflects the market firmly discounting a coup attempt in Ukraine before year-end, despite active war conditions."
  - "29% of all-time Polymarket volume arrived in 24 hours, showing meaningful but not record-setting renewed attention on the contract."
  - "Fresh capital at a low price implies traders are either reaffirming conviction or responding to a geopolitical event that raised the question again."
  - "Contract resolves December 31, 2026."
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
      poly_vol_24h_usd: 44536.53
sources:
  - label: "ClearMarket market record: Will there be a coup attempt in Ukraine by 2026?"
    url: "https://clearmarket.fyi/events/ukraine-coup-attempt-by-june-30"
    retrieved_at: "2026-08-15T08:22:27+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A low-price, moderate-volume surge on a geopolitical tail-risk contract is worth flagging, it often precedes news flow; desks running Ukraine exposure should check for any credible political instability reporting driving the fresh attention.
