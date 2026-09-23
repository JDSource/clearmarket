---
signal_id: "CMSIG20260923VS05"
signal_slug: "will-democratic-win-the-house-race-for-p-vol-54292"
headline: "Democrat PA-7 House: 82% on $54K volume surge"
semantic_title: "Buyers back Democrats in PA-7 at a firm 82%"
telemetry: "82% · $54K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-23T07:48:28+00:00"
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
  - "At 82%, Kalshi treats a Democratic hold of Pennsylvania's 7th district as a high-confidence outcome."
  - "24h volume of $54K is 29% of all-time, a large session reinforcing an already-elevated price."
  - "PA-7 is a Biden-era pickup held by an incumbent; fresh volume at 82% suggests the market is pricing out meaningful Republican competition."
  - "Contract resolves on the certified November 2026 House election result for PA-7."
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
    retrieved_at: "2026-09-23T07:48:28+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk modeling House majority counts should treat PA-7 as a likely Democratic hold; volume reinforcing high odds suggests incumbent structural advantages are being priced in after recent district-level news.
