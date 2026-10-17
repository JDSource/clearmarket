---
signal_id: "CMSIG20261017VS02"
signal_slug: "will-republican-win-the-house-race-for-w-vol-24726"
headline: "WA-05 Republican: 88% on $25K volume spike"
semantic_title: "Heavy trading backs Republican in WA-05 at 88%"
telemetry: "88% · $25K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-17T11:58:01+00:00"
event_id: "CM-EVT-Z9PH16L5M4"
event_slug: "kxhouserace-wa05-26"
event_question: "Will the winner of Washington's 5th congressional district House seat be determined by 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-WA05-26-R"
  question_raw: "Will Republican win the House race for WA-05?"
  current_price: 0.88
  volume_24h_usd: 24726.79
  volume_cumulative_usd: 51271.44
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "Kalshi prices Republican at 88%, a near-lockup that leaves just 12% tail risk for an upset."
  - "24h volume of $25K is 48% of all-time, nearly half of all trading concentrated in this single session."
  - "Concentrated flow at a high-conviction price level suggests new information is confirming, not challenging, the favorite."
  - "Resolves on November 2026 election night."
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
      kalshi_vol_24h_usd: 24726.79
sources:
  - label: "ClearMarket market record: Will the winner of Washington's 5th congressional distr"
    url: "https://clearmarket.fyi/events/kxhouserace-wa05-26"
    retrieved_at: "2026-10-17T11:58:01+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A near-consensus price drawing half its all-time volume in one day points to event-driven confirmation trading that desks should cross-check against latest district polling.
