---
signal_id: "CMSIG20260922VS02"
signal_slug: "will-democratic-win-the-house-race-for-t-vol-44490"
headline: "Democrat TX-28 House: 86% on $44K Kalshi surge"
semantic_title: "Heavy trading backs Democrats holding TX-28"
telemetry: "86% · $44K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-22T13:04:04+00:00"
event_id: "CM-EVT-BJ7C9T9VL1"
event_slug: "housetx28-26"
event_question: "TX-28 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSETX28-26-D"
  question_raw: "Will Democratic win the House race for TX-28?"
  current_price: 0.86
  volume_24h_usd: 44490.14
  volume_cumulative_usd: 121941.98
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "At 86%, Kalshi prices a Democratic hold in Texas's 28th district as the strong base case."
  - "36% of all-time volume arrived in 24 hours, the heaviest single-day share for this contract."
  - "TX-28 drew national attention after incumbent litigation; fresh volume suggests positioning ahead of a near-term catalyst."
  - "Resolves on 2026 general election result."
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
      kalshi_vol_24h_usd: 44490.14
sources:
  - label: "ClearMarket market record: TX-28 House winner?"
    url: "https://clearmarket.fyi/events/housetx28-26"
    retrieved_at: "2026-09-22T13:04:04+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

An 86% price absorbing more than a third of all-time handle in one day tells a desk that traders are loading conviction on the Democratic side ahead of an expected resolution trigger in TX-28.
