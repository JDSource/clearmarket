---
signal_id: "CMSIG20260818VS02"
signal_slug: "will-randy-fine-be-the-republican-nomine-vol-54343"
headline: "Fine FL-06 GOP nom: 98% on $54K volume pop"
semantic_title: "Randy Fine FL-06 GOP slot holds near-certain at 98%"
telemetry: "98% · $54K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-18T08:31:22+00:00"
event_id: "CM-EVT-JM46D114M2"
event_slug: "kxflprimary-06r26"
event_question: "Will the Republican nominee for Florida's 6th congressional district be determined by August 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFLPRIMARY-06R26-RFIN"
  question_raw: "Will Randy Fine be the Republican nominee for FL-06?"
  current_price: 0.98
  volume_24h_usd: 54343.08
  volume_cumulative_usd: 145150.01
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-08-18T14:00:00Z"
bullets:
  - "Kalshi prices Fine at 98%, market leaves only 2 cents of residual uncertainty on the nomination."
  - "37% of all-time volume in 24h ($54K), highest daily share this contract has recorded."
  - "Volume spike alongside the Donalds surge suggests a broad Florida primary resolution event."
  - "Resolves on certified Republican nominee for Florida's 6th congressional district."
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
      kalshi_vol_24h_usd: 54343.08
sources:
  - label: "ClearMarket market record: Will the Republican nominee for Florida's 6th congressi"
    url: "https://clearmarket.fyi/events/kxflprimary-06r26"
    retrieved_at: "2026-08-18T08:31:22+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 37% all-time share on a tight 98% print suggests a primary-day or canvassing-board event has triggered final position squaring, the FL-06 nomination is effectively closed for pricing purposes.
