---
signal_id: "CMSIG20261102VS05"
signal_slug: "will-republicans-win-the-senate-race-in-vol-60983"
headline: "Louisiana Senate GOP: 88% on $61K volume surge"
semantic_title: "Louisiana GOP Senate seat trades as a near-sure thing"
telemetry: "88% · $61K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-02T17:45:32+00:00"
event_id: "CM-EVT-862GRMT4M0"
event_slug: "kxsenatela-26nov"
event_question: "Will there be a Louisiana Senate winner by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXSENATELA-26NOV-R"
  question_raw: "Will Republicans win the Senate race in Louisiana?"
  current_price: 0.88
  volume_24h_usd: 60983.93
  volume_cumulative_usd: 151786.44
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices Republicans at 88% in Louisiana, a heavy favorite reflecting the state's deep-red partisan lean."
  - "24h volume of $61K is 40% of all-time contract flow, the largest single-day share of any session to date."
  - "A 40% all-time share in one day implies a sudden catalyst, likely spillover attention from broader Senate map repricing."
  - "Resolves on the 2026 Louisiana Senate race result."
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
      kalshi_vol_24h_usd: 60983.93
sources:
  - label: "ClearMarket market record: Will there be a Louisiana Senate winner by January 4, 2"
    url: "https://clearmarket.fyi/events/kxsenatela-26nov"
    retrieved_at: "2026-11-02T17:45:32+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Forty percent of all-time volume arriving in a single session on an 88% contract suggests this is a satellite hedge within a broader Senate-map basket, not a standalone directional trade.
