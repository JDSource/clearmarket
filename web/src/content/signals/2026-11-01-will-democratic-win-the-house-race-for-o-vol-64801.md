---
signal_id: "CMSIG20261101VS04"
signal_slug: "will-democratic-win-the-house-race-for-o-vol-64801"
headline: "OH-9 House Dems: 82% on $65K Kalshi surge"
semantic_title: "Buyers back Democrats in OH-9 as odds climb to 82%"
telemetry: "82% · $65K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-01T07:49:22+00:00"
event_id: "CM-EVT-TC43SYMZM4"
event_slug: "houseoh9-26"
event_question: "Will the Republican candidate win the Ohio's 9th congressional district House race?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSEOH9-26-D"
  question_raw: "Will Democratic win the House race for OH-9?"
  current_price: 0.82
  volume_24h_usd: 64801.29
  volume_cumulative_usd: 149957.34
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "At 82%, Kalshi assigns Democrats a strong hold on the OH-9 House seat."
  - "$65K in 24h, 43% of all-time, is the largest single-day session by a wide margin."
  - "OH-9 draws attention as Republicans weigh targeting Marcy Kaptur's long-held seat in redistricting aftermath."
  - "Resolves on the November 2026 election result."
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
      kalshi_vol_24h_usd: 64801.29
sources:
  - label: "ClearMarket market record: Will the Republican candidate win the Ohio's 9th congre"
    url: "https://clearmarket.fyi/events/houseoh9-26"
    retrieved_at: "2026-11-01T07:49:22+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

43% of all-time volume in one session on an 82% Democratic contract suggests the market is confidently re-pricing GOP upside in OH-9 as limited, but someone is willing to take the other side.
