---
signal_id: "CMSIG20260923VS06"
signal_slug: "will-democratic-win-the-house-race-for-i-vol-17629"
headline: "Democrat IA-3 House: 76% on $18K; 62% of lifetime"
semantic_title: "Trading picks up on Democrats winning IA-3 at 76%"
telemetry: "76% · $18K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-23T07:48:28+00:00"
event_id: "CM-EVT-2VB36981K2"
event_slug: "houseia3-26"
event_question: "IA-03 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSEIA3-26-D"
  question_raw: "Will Democratic win the House race for IA-3?"
  current_price: 0.76
  volume_24h_usd: 17629.58
  volume_cumulative_usd: 28282.27
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "At 76%, Kalshi prices a Democratic win in Iowa's 3rd district as the clear favored outcome."
  - "24h volume of $18K represents 62% of all-time handle, the contract's activity is overwhelmingly concentrated in this single session."
  - "A 62% lifetime-volume single-day surge on a district race signals either a major catalyst, redistricting news, candidate development, or polling, or a market just gaining traction."
  - "Contract resolves on the certified November 2026 House election result for IA-3."
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
      kalshi_vol_24h_usd: 17629.58
sources:
  - label: "ClearMarket market record: IA-03 House winner?"
    url: "https://clearmarket.fyi/events/houseia3-26"
    retrieved_at: "2026-09-23T07:48:28+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should treat the 62% lifetime-in-one-day volume as a discovery signal, this contract is newly liquid, meaning price formation is still early and could shift materially as more participants engage.
