---
signal_id: "CMSIG20261011VS00"
signal_slug: "will-republicans-win-the-senate-race-in-vol-62229"
headline: "TN Senate GOP win: 92% on $62K surge"
semantic_title: "Tennessee Senate stays a GOP lock at 92%"
telemetry: "92% · $62K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-11T14:36:40+00:00"
event_id: "CM-EVT-T9PVHWGH35"
event_slug: "senatetn-26"
event_question: "Will the Tennessee Senate race be decided by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "SENATETN-26-R"
  question_raw: "Will Republicans win the Senate race in Tennessee?"
  current_price: 0.916
  volume_24h_usd: 62229.97
  volume_cumulative_usd: 158894.91
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices a Republican Tennessee Senate win at 92%, near-certainty territory."
  - "24h volume of $62K is 39% of all-time handle, a significant single-day commitment."
  - "Heavy fresh volume into a high-conviction line suggests traders are positioning ahead of midterm consolidation."
  - "Resolves after 2026 Tennessee Senate race results are certified."
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
      kalshi_vol_24h_usd: 62229.97
sources:
  - label: "ClearMarket market record: Will the Tennessee Senate race be decided by January 4,"
    url: "https://clearmarket.fyi/events/senatetn-26"
    retrieved_at: "2026-10-11T14:36:40+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A large share of lifetime volume landing on a 92% line signals desks are using this as a near-certain midterm leg, likely in paired portfolio trades rather than speculative bets.
