---
signal_id: "CMSIG20260923VS01"
signal_slug: "will-democratic-win-the-house-race-for-p-vol-54292"
headline: "PA-7 House Dem: 82% on $54K volume spike"
semantic_title: "Buyers back the Democrat in PA-7 at 82%"
telemetry: "82% · $54K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-23T13:18:01+00:00"
event_id: "CM-EVT-6S7C40J637"
event_slug: "housepa7-26"
event_question: "Will the winner of Pennsylvania's 7th congressional district House race be determined by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSEPA7-26-D"
  question_raw: "Will Democratic win the House race for PA-7?"
  current_price: 0.82
  volume_24h_usd: 54292.81
  volume_cumulative_usd: 185902.5
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices Democrats at 82% in PA-7, a strong favorite reading with meaningful residual GOP risk."
  - "24h volume of $54K is 29% of all-time, making today one of the most active single sessions on this contract."
  - "PA-7 has been a swing-district bellwether; fresh volume at 82% suggests new polling or candidate news is driving reassessment."
  - "Resolves on the November 2026 PA-7 House general election result."
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
      kalshi_vol_24h_usd: 54292.81
sources:
  - label: "ClearMarket market record: Will the winner of Pennsylvania's 7th congressional dis"
    url: "https://clearmarket.fyi/events/housepa7-26"
    retrieved_at: "2026-09-23T13:18:01+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A $54K single-day surge on a contested House seat approaching 82% is a signal that district-level intelligence, polling, fundraising, or candidate developments, may be hitting the market ahead of public release.
