---
signal_id: "CMSIG20260929VS00"
signal_slug: "will-the-unemployment-rate-u-3-be-abov-vol-40477"
headline: "Sept unemployment above 3.9%: 94% on $40K surge"
semantic_title: "Traders back U-3 staying above 3.9% this September"
telemetry: "94% · $40K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-29T14:35:01+00:00"
event_id: "CM-EVT-720DZC17Y9"
event_slug: "kxu3-26sep"
event_question: "Will the unemployment rate (U-3) be above 4.0% in September?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXU3-26SEP-T3.9"
  question_raw: "Will the unemployment rate (U-3) be above 3.9% in September?"
  current_price: 0.94
  volume_24h_usd: 40477.11
  volume_cumulative_usd: 107120.37
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-01T14:00:00Z"
bullets:
  - "Kalshi prices 94% odds that September U-3 prints above 3.9%, implying near-certainty of an elevated read."
  - "24h volume of $40K represents 38% of all-time contract volume, a heavy single-session commitment."
  - "September jobs data drops imminently; fresh positioning suggests consensus expects no surprise labor-market cooling."
  - "Contract resolves on BLS official U-3 release for September 2026."
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
      kalshi_vol_24h_usd: 40477.11
sources:
  - label: "ClearMarket market record: Will the unemployment rate (U-3) be above 4.0% in Septe"
    url: "https://clearmarket.fyi/events/kxu3-26sep"
    retrieved_at: "2026-09-29T14:35:01+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The concentrated volume surge just ahead of the September BLS release signals desks are locking in high-conviction exposure to an above-3.9% print, with little appetite to fade the bearish labor-market read.
