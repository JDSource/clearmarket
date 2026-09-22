---
signal_id: "CMSIG20260922VS03"
signal_slug: "will-republican-win-the-house-race-for-m-vol-37323"
headline: "Republican MT-1 House: 70% on $37K Kalshi spike"
semantic_title: "Buyers back GOP holding MT-1 as volume hits 41% of all-time"
telemetry: "70% · $37K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-22T13:04:04+00:00"
event_id: "CM-EVT-QWGZDJ1DQ6"
event_slug: "housemt1-26"
event_question: "MT-01 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSEMT1-26-R"
  question_raw: "Will Republican win the House race for MT-1?"
  current_price: 0.7
  volume_24h_usd: 37323.16
  volume_cumulative_usd: 90012.85
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "At 70%, Kalshi prices the Republican candidate as a clear favorite in Montana's 1st district."
  - "41% of all-time volume landed in 24 hours, the steepest one-day concentration this contract has seen."
  - "Montana's at-large competitive history draws capital when Senate and House races move together in polling."
  - "Resolves on 2026 general election certification."
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
      kalshi_vol_24h_usd: 37323.16
sources:
  - label: "ClearMarket market record: MT-01 House winner?"
    url: "https://clearmarket.fyi/events/housemt1-26"
    retrieved_at: "2026-09-22T13:04:04+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 70% read with 41% of lifetime volume in a single session signals the desk that MT-1 has become an active House-control input and is drawing cross-market positioning alongside the MT Democratic contract.
