---
signal_id: "CMSIG20261028VS07"
signal_slug: "will-democratic-win-the-house-race-for-p-vol-20005"
headline: "Democrat PA-8 House: 86% on $20K volume return"
semantic_title: "Democrats hold 86% in PA-8 as fresh volume returns to the race"
telemetry: "86% · $20K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-28T07:50:03+00:00"
event_id: "CM-EVT-RB6J9TCV17"
event_slug: "housepa8-26"
event_question: "PA-08 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSEPA8-26-D"
  question_raw: "Will Democratic win the House race for PA-8?"
  current_price: 0.86
  volume_24h_usd: 20005.4
  volume_cumulative_usd: 73808.0
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "86% pricing establishes the Democratic candidate as a heavy favorite in Pennsylvania's 8th district."
  - "Kalshi recorded $20K in 24h, 27% of all-time volume, a moderate but notable single-session reactivation."
  - "PA-8 returning to volume after a quieter stretch suggests polling, candidate news, or House majority modeling."
  - "Resolves on certified PA-8 House election result."
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
      kalshi_vol_24h_usd: 20005.4
sources:
  - label: "ClearMarket market record: PA-08 House winner?"
    url: "https://clearmarket.fyi/events/housepa8-26"
    retrieved_at: "2026-10-28T07:50:03+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A fresh $20K session on a high-conviction 86% contract in PA-8 suggests desks are revisiting Pennsylvania House seats as part of broader majority-margin recalculation, monitor alongside WI-3 and NC-03 for House control signals.
