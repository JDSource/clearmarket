---
signal_id: "CMSIG20261017VS02"
signal_slug: "will-republican-win-the-house-race-for-w-vol-24726"
headline: "WA-05 GOP House: 88% on $25K volume spike"
semantic_title: "WA-05 Republican bid stays a strong favorite on fresh volume"
telemetry: "88% · $25K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-17T07:48:43+00:00"
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
  - "Kalshi prices the Republican at 88%, near-lock odds leaving limited upside for opposition bets."
  - "$24.7K traded in 24h equals 48% of all-time volume, a sharp single-session concentration."
  - "Eastern Washington's WA-05 has been reliably red; the surge may reflect position-taking ahead of early voting deadlines."
  - "Resolves on 2026 general election night."
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
    retrieved_at: "2026-10-17T07:48:43+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Nearly half of all-time volume arriving at 88% odds suggests traders are either locking in the favorite at scale or a small cohort is taking a long-shot opposition position, either way, the race is drawing fresh attention.
