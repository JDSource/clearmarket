---
signal_id: "CMSIG20261003VS02"
signal_slug: "will-democratic-win-the-house-race-for-w-vol-15845"
headline: "Democrat WA-3 House: 89% on $16K inflow"
semantic_title: "Buyers back the Democrat in WA-3 House race"
telemetry: "89% · $16K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-03T07:48:19+00:00"
event_id: "CM-EVT-H6TY7G52C4"
event_slug: "housewa3-26"
event_question: "Will the winner of the Washington 3rd congressional district House race be determined by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSEWA3-26-D"
  question_raw: "Will Democratic win the House race for WA-3?"
  current_price: 0.89
  volume_24h_usd: 15845.89
  volume_cumulative_usd: 38814.41
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi contract prices Democratic win in Washington's 3rd Congressional District at 89%, a strong lean toward the Democrat."
  - "24h volume of $16K equals 41% of all-time contract volume, an unusually concentrated single-session surge."
  - "WA-3 flipped Republican in 2022 and back Democratic in 2024; heavy trading at 89% suggests a catalyst, likely new polling or fundraising data, is driving conviction."
  - "Resolves on 2026 general election certified result for WA-3."
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
      kalshi_vol_24h_usd: 15845.89
sources:
  - label: "ClearMarket market record: Will the winner of the Washington 3rd congressional dis"
    url: "https://clearmarket.fyi/events/housewa3-26"
    retrieved_at: "2026-10-03T07:48:19+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should flag this as a race where new on-the-ground data may be ahead of public release, 41% of all-time volume in one day is a strong signal to monitor upcoming district-level polling.
