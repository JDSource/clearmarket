---
signal_id: "CMSIG20260922VS02"
signal_slug: "will-democratic-win-the-house-race-for-t-vol-44490"
headline: "Democrat TX-28 House: 86% on $44K volume surge"
semantic_title: "Democrats hold a strong lead in TX-28 as volume picks up"
telemetry: "86% · $44K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-22T07:48:31+00:00"
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
  - "Kalshi prices a Democratic win in TX-28 at 86%, a heavy favorite with meaningful residual Republican risk."
  - "$44.5K in 24h represents 36% of all-time contract volume, a notable single-day concentration."
  - "TX-28 has a history of close races; fresh volume at this price may reflect new polling or candidate news narrowing the field."
  - "Resolves on 2026 midterm election results for the TX-28 House seat."
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
    retrieved_at: "2026-09-22T07:48:31+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 36% all-time volume day on a House race priced at 86% suggests new district-level data or candidate developments that election-desk models should reprice against.
