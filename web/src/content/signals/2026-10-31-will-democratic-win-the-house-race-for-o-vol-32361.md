---
signal_id: "CMSIG20261031VS06"
signal_slug: "will-democratic-win-the-house-race-for-o-vol-32361"
headline: "OH-9 Dem House win: 81% on $32K volume push"
semantic_title: "Buyers back Democrats heavily in OH-9 at 81%"
telemetry: "81% · $32K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-31T07:49:19+00:00"
event_id: "CM-EVT-TC43SYMZM4"
event_slug: "houseoh9-26"
event_question: "Will the Republican candidate win the Ohio's 9th congressional district House race?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSEOH9-26-D"
  question_raw: "Will Democratic win the House race for OH-9?"
  current_price: 0.81
  volume_24h_usd: 32361.57
  volume_cumulative_usd: 84117.56
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices Democrats at 81% in OH-9, near-consensus favorite, reflecting incumbent structural strength."
  - "$32K in 24h is 38% of all-time volume, a meaningful late surge for a lower-liquidity district contract."
  - "High confidence pricing suggests late money is closing out Republican hedges rather than opening new positions."
  - "Resolves on OH-9 2026 House election result."
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
      kalshi_vol_24h_usd: 32361.57
sources:
  - label: "ClearMarket market record: Will the Republican candidate win the Ohio's 9th congre"
    url: "https://clearmarket.fyi/events/houseoh9-26"
    retrieved_at: "2026-10-31T07:49:19+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

An 81% price with a 38% daily volume share in a lower-dollar contract indicates the OH-9 result is treated as near-certain, desks can use this as a baseline for broader Ohio downballot modeling.
