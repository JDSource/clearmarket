---
signal_id: "CMSIG20261006VS04"
signal_slug: "will-republican-win-the-house-race-for-v-vol-11477"
headline: "GOP VA-05 House win: 77% on $11K volume pop"
semantic_title: "Buyers back the GOP hold on VA-05 at 77%"
telemetry: "77% · $11K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-06T14:43:21+00:00"
event_id: "CM-EVT-J5Q1GQ0MF2"
event_slug: "kxhouserace-va05-26"
event_question: "Will a winner be determined in the Virginia 5th Congressional District House race?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-VA05-26-R"
  question_raw: "Will Republican win the House race for VA-05?"
  current_price: 0.77
  volume_24h_usd: 11477.92
  volume_cumulative_usd: 42251.19
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "Kalshi prices a Republican win in Virginia's 5th district at 77%, a solid favorite read."
  - "24h volume is 27% of all-time, a moderate but notable uptick for a House district race."
  - "Attention may reflect early polling, candidate filing deadlines, or redistricting clarity."
  - "Resolves on 2026 midterm election night."
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
      kalshi_vol_24h_usd: 11477.92
sources:
  - label: "ClearMarket market record: Will a winner be determined in the Virginia 5th Congres"
    url: "https://clearmarket.fyi/events/kxhouserace-va05-26"
    retrieved_at: "2026-10-06T14:43:21+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 77% price with a volume uptick in a House district race suggests desks are actively pricing VA-05 as a safe Republican hold, but the surge warrants watching for any district-level news that could shift that view.
