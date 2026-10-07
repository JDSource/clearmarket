---
signal_id: "CMSIG20261007VS06"
signal_slug: "will-republican-win-the-house-race-for-v-vol-11804"
headline: "VA-05 GOP House: 78% on $11K inflow"
semantic_title: "Buyers back the Republican in Virginia's VA-05 race"
telemetry: "78% · $12K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-07T07:48:37+00:00"
event_id: "CM-EVT-J5Q1GQ0MF2"
event_slug: "kxhouserace-va05-26"
event_question: "Will a winner be determined in the Virginia 5th Congressional District House race?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-VA05-26-R"
  question_raw: "Will Republican win the House race for VA-05?"
  current_price: 0.78
  volume_24h_usd: 11804.83
  volume_cumulative_usd: 43064.23
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "78% odds make the Republican the clear favorite in Virginia's 5th congressional district."
  - "24h volume of $11K is 27% of all-time, a notable single-session share for a House district contract."
  - "Fresh flow at 78% suggests the race is drawing renewed attention, possibly from polling or fundraising data."
  - "Resolves on certified VA-05 House race result."
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
      kalshi_vol_24h_usd: 11804.83
sources:
  - label: "ClearMarket market record: Will a winner be determined in the Virginia 5th Congres"
    url: "https://clearmarket.fyi/events/kxhouserace-va05-26"
    retrieved_at: "2026-10-07T07:48:37+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 78% price with a fresh volume uptick in a competitive Virginia district warrants a desk's attention as a proxy for suburban Republican strength heading into November.
