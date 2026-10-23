---
signal_id: "CMSIG20261023VS04"
signal_slug: "will-republican-win-the-house-race-for-w-vol-23070"
headline: "Rep WA-05 House: 85% on $23K in new trading"
semantic_title: "Republicans keep strong odds in WA-05 through fresh volume"
telemetry: "85% · $23K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-23T13:04:13+00:00"
event_id: "CM-EVT-Z9PH16L5M4"
event_slug: "kxhouserace-wa05-26"
event_question: "Will the winner of Washington's 5th congressional district House seat be determined by 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-WA05-26-R"
  question_raw: "Will Republican win the House race for WA-05?"
  current_price: 0.85
  volume_24h_usd: 23070.62
  volume_cumulative_usd: 76816.17
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "Kalshi prices the Republican candidate at 85% in WA-05, market treats this as a solid Republican hold."
  - "24h volume of $23K is 30% of all-time total, a notable single-day share for a race near consensus."
  - "Fresh activity at 85% suggests limited challenge to the Republican thesis but confirms ongoing positioning interest."
  - "Resolves on Washington 5th District House race result."
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
      kalshi_vol_24h_usd: 23070.62
sources:
  - label: "ClearMarket market record: Will the winner of Washington's 5th congressional distr"
    url: "https://clearmarket.fyi/events/kxhouserace-wa05-26"
    retrieved_at: "2026-10-23T13:04:13+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Steady volume into a high-conviction 85% Republican contract on WA-05 indicates desks are using this seat as a reliable anchor in House majority scenario modeling.
