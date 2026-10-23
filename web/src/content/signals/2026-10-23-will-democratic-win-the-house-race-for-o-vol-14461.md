---
signal_id: "CMSIG20261023VS07"
signal_slug: "will-democratic-win-the-house-race-for-o-vol-14461"
headline: "OH-10 House Dem: 30% on $14K Kalshi surge"
semantic_title: "OH-10 House odds stay below 50% as fresh volume tests the line"
telemetry: "30% · $14K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-23T07:49:03+00:00"
event_id: "CM-EVT-TY2DWD9XJ0"
event_slug: "kxhouserace-oh10-26"
event_question: "OH-10 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-OH10-26-D"
  question_raw: "Will Democratic win the House race for OH-10?"
  current_price: 0.3
  volume_24h_usd: 14461.39
  volume_cumulative_usd: 26389.16
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "30% price on Kalshi keeps Democrats as an underdog in OH-10, below the 50% line."
  - "$14,461 in 24h is 55% of all-time, more than half the contract's total lifetime volume in one session."
  - "Ohio-10 is a competitive suburban district; fresh volume just below 50% odds may signal a tightening race narrative."
  - "Resolves on 2026 OH-10 House general election."
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
      kalshi_vol_24h_usd: 14461.39
sources:
  - label: "ClearMarket market record: OH-10 House winner?"
    url: "https://clearmarket.fyi/events/kxhouserace-oh10-26"
    retrieved_at: "2026-10-23T07:49:03+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 55% all-time daily volume flush into a 30% Democratic contract in OH-10 is worth tracking for desks running House majority models, this level of activity at the 30% mark may precede a polling or fundraising development that moves the line.
