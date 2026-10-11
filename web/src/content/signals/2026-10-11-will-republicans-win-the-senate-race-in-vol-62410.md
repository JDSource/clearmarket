---
signal_id: "CMSIG20261011VS00"
signal_slug: "will-republicans-win-the-senate-race-in-vol-62410"
headline: "TN Senate GOP: 93% on $62K surge"
semantic_title: "Tennessee Senate GOP hold stays a strong bet"
telemetry: "93% · $62K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-11T07:48:50+00:00"
event_id: "CM-EVT-T9PVHWGH35"
event_slug: "senatetn-26"
event_question: "Will the Tennessee Senate race be decided by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "SENATETN-26-R"
  question_raw: "Will Republicans win the Senate race in Tennessee?"
  current_price: 0.934
  volume_24h_usd: 62410.92
  volume_cumulative_usd: 160195.08
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices Republicans at 93%, near-certain hold with little room for surprise."
  - "39% of all-time volume hit in 24h, signaling sharp renewed focus on this race."
  - "Fresh capital flowing into a near-settled race suggests bettors are locking in late conviction ahead of midterm season."
  - "Resolves on 2026 midterm election night."
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
      kalshi_vol_24h_usd: 62410.92
sources:
  - label: "ClearMarket market record: Will the Tennessee Senate race be decided by January 4,"
    url: "https://clearmarket.fyi/events/senatetn-26"
    retrieved_at: "2026-10-11T07:48:50+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Heavy late-stage volume on a 93% contract suggests the desk is watching Tennessee as a floor test for Republican Senate defense heading into November.
