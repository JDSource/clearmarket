---
signal_id: "CMSIG20261014VS01"
signal_slug: "will-republican-win-the-house-race-for-m-vol-75727"
headline: "MN-01 GOP seat: 77% on $75K volume surge"
semantic_title: "Republican hold in MN-01 draws heavy backing at 75%+"
telemetry: "77% · $76K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-14T07:48:34+00:00"
event_id: "CM-EVT-0HH4XXLY85"
event_slug: "kxhouserace-mn01-26"
event_question: "Will MN-01 House winner be determined by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-MN01-26-R"
  question_raw: "Will Republican win the House race for MN-01?"
  current_price: 0.77
  volume_24h_usd: 75727.56
  volume_cumulative_usd: 134769.76
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "77% price reflects strong but not certain Republican favoritism in this competitive southern Minnesota district."
  - "24h volume of $75K is 56% of all-time handle, a major single-session commitment to the current odds."
  - "Mid-October timing aligns with final polling drops and closing ad-spend reports shaping trader conviction."
  - "Resolves on 2026 midterm election night; any late polling shift would move this price quickly."
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
      kalshi_vol_24h_usd: 75727.56
sources:
  - label: "ClearMarket market record: Will MN-01 House winner be determined by January 4, 202"
    url: "https://clearmarket.fyi/events/kxhouserace-mn01-26"
    retrieved_at: "2026-10-14T07:48:34+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 56% all-time share in one session on Kalshi indicates a coordinated reassessment of MN-01's competitiveness, desks should watch for fresh district-level polling or fundraising disclosures.
