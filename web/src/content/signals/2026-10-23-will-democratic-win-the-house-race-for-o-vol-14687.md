---
signal_id: "CMSIG20261023VS03"
signal_slug: "will-democratic-win-the-house-race-for-o-vol-14687"
headline: "Dem OH-10 House: 30% on $14.7K, majority all-time vol"
semantic_title: "Republicans lead in OH-10 as buyers test the Democratic odds"
telemetry: "30% · $15K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-23T13:04:13+00:00"
event_id: "CM-EVT-TY2DWD9XJ0"
event_slug: "kxhouserace-oh10-26"
event_question: "OH-10 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-OH10-26-D"
  question_raw: "Will Democratic win the House race for OH-10?"
  current_price: 0.3
  volume_24h_usd: 14687.21
  volume_cumulative_usd: 26614.99
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "Kalshi prices the Democratic candidate at 30% in OH-10, market favors the Republican in this race."
  - "24h volume of $14.7K is 55% of all-time total, meaning more than half of all trading landed in a single day."
  - "Fresh volume into a 30% contract signals active debate over whether Democrats can outperform in this district."
  - "Resolves on Ohio 10th District House race result."
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
      kalshi_vol_24h_usd: 14687.21
sources:
  - label: "ClearMarket market record: OH-10 House winner?"
    url: "https://clearmarket.fyi/events/kxhouserace-oh10-26"
    retrieved_at: "2026-10-23T13:04:13+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A majority-of-all-time volume burst into a 30% Democratic contract in OH-10 suggests desks are actively pricing tail risk of a Democratic overperformance in a Republican-leaning seat.
