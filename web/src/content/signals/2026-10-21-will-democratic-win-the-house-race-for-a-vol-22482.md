---
signal_id: "CMSIG20261021VS00"
signal_slug: "will-democratic-win-the-house-race-for-a-vol-22482"
headline: "AZ-6 House seat: 86% as Kalshi logs $22K surge"
semantic_title: "Democrats stay heavy favorites in AZ-6 House race"
telemetry: "86% · $22K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-21T07:48:52+00:00"
event_id: "CM-EVT-2G9FBHFVL0"
event_slug: "houseaz6-26"
event_question: "AZ-06 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSEAZ6-26-D"
  question_raw: "Will Democratic win the House race for AZ-6?"
  current_price: 0.86
  volume_24h_usd: 22482.73
  volume_cumulative_usd: 31175.68
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "86% implies Democrats are near-locks in AZ-6 with little competitive uncertainty priced in."
  - "24h volume of $22K represents 72% of all-time handle, a near-exhaustive single-day flush."
  - "Late-cycle volume at this share of all-time suggests a final positioning push ahead of Nov. results."
  - "Resolves on certified House race outcome for Arizona's 6th congressional district."
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
      kalshi_vol_24h_usd: 22482.73
sources:
  - label: "ClearMarket market record: AZ-06 House winner?"
    url: "https://clearmarket.fyi/events/houseaz6-26"
    retrieved_at: "2026-10-21T07:48:52+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The outsized share of all-time volume in one session signals a terminal conviction trade, desks should watch for any late polling or candidate news that could compress the final few points of risk.
