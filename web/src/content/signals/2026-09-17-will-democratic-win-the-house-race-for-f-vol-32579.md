---
signal_id: "CMSIG20260917VS06"
signal_slug: "will-democratic-win-the-house-race-for-f-vol-32579"
headline: "Dem FL-14 House: 63% on $33K inflow"
semantic_title: "Democrats hold a 63% edge in FL-14 on fresh volume"
telemetry: "63% · $33K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-17T13:05:20+00:00"
event_id: "CM-EVT-H89NH9QH14"
event_slug: "kxhouserace-fl14-26"
event_question: "Will a winner be determined in the FL-14 House race by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-FL14-26-D"
  question_raw: "Will Democratic win the House race for FL-14?"
  current_price: 0.63
  volume_24h_usd: 32579.38
  volume_cumulative_usd: 68751.81
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "Kalshi prices Democrats at 63% to win Florida's 14th Congressional District, a moderate lean."
  - "$33K in 24h, 47% of all-time volume, marks a meaningful acceleration in FL-14 trading."
  - "FL-14 sits in a competitive suburban corridor; fresh attention may follow candidate news or polling."
  - "Contract resolves on November 2026 general election results."
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
      kalshi_vol_24h_usd: 32579.38
sources:
  - label: "ClearMarket market record: Will a winner be determined in the FL-14 House race by "
    url: "https://clearmarket.fyi/events/kxhouserace-fl14-26"
    retrieved_at: "2026-09-17T13:05:20+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A near-majority of all-time volume in one session suggests FL-14 has been re-rated as a genuine Democratic opportunity, relevant for House majority scenario desks.
