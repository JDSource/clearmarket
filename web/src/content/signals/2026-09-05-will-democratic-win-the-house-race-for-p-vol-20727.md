---
signal_id: "CMSIG20260905VS02"
signal_slug: "will-democratic-win-the-house-race-for-p-vol-20727"
headline: "Democrat PA-7 House win: 82% on $20K volume spike"
semantic_title: "Buyers back the Democrat in PA-7 as odds stay above 75%"
telemetry: "82% · $21K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-05T11:35:07+00:00"
event_id: "CM-EVT-6S7C40J637"
event_slug: "housepa7-26"
event_question: "Will the winner of Pennsylvania's 7th congressional district House race be determined by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSEPA7-26-D"
  question_raw: "Will Democratic win the House race for PA-7?"
  current_price: 0.82
  volume_24h_usd: 20727.26
  volume_cumulative_usd: 81131.76
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices a Democratic win in Pennsylvania's 7th district at 82%, well above the 75% threshold, a strong lean."
  - "24h volume of $20.7K is 26% of all-time flow, a notable single-day concentration for a House-level contract."
  - "PA-7 is a competitive suburban Philadelphia seat; fresh volume at this price suggests new polling or campaign-finance data is moving traders."
  - "Resolves on the certified winner of the PA-7 general election."
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
      kalshi_vol_24h_usd: 20727.26
sources:
  - label: "ClearMarket market record: Will the winner of Pennsylvania's 7th congressional dis"
    url: "https://clearmarket.fyi/events/housepa7-26"
    retrieved_at: "2026-09-05T11:35:07+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A fresh 26% of lifetime volume at 82% indicates desks are adding conviction to the Democratic lean, likely in response to updated district-level data or opponent vulnerability signals.
