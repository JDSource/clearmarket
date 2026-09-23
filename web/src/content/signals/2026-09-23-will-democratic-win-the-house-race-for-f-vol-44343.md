---
signal_id: "CMSIG20260923VS04"
signal_slug: "will-democratic-win-the-house-race-for-f-vol-44343"
headline: "Democrat FL-14 House: 67% on $44K volume push"
semantic_title: "Democrats lead in FL-14 with odds holding above 50%"
telemetry: "67% · $44K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-23T07:48:28+00:00"
event_id: "CM-EVT-H89NH9QH14"
event_slug: "kxhouserace-fl14-26"
event_question: "Will a winner be determined in the FL-14 House race by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-FL14-26-D"
  question_raw: "Will Democratic win the House race for FL-14?"
  current_price: 0.67
  volume_24h_usd: 44343.08
  volume_cumulative_usd: 120947.78
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "At 67%, Kalshi prices a Democratic win in Florida's 14th congressional district as the more likely outcome."
  - "24h volume of $44K is 37% of all-time handle, a notable single-session surge in a competitive House race."
  - "FL-14 has emerged as a targeted pickup opportunity; fresh volume may reflect new polling, candidate news, or national party spending signals."
  - "Contract resolves on the certified November 2026 House election result for FL-14."
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
      kalshi_vol_24h_usd: 44343.08
sources:
  - label: "ClearMarket market record: Will a winner be determined in the FL-14 House race by "
    url: "https://clearmarket.fyi/events/kxhouserace-fl14-26"
    retrieved_at: "2026-09-23T07:48:28+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk tracking House majority scenarios should log FL-14 as an actively contested seat where fresh money is backing the Democratic side, consistent with broader signals on Florida suburban district competitiveness.
