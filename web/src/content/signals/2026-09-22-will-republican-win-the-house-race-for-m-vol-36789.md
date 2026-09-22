---
signal_id: "CMSIG20260922VS03"
signal_slug: "will-republican-win-the-house-race-for-m-vol-36789"
headline: "Republican MT-1 House: 69% on $37K volume spike"
semantic_title: "Republican stays favored in MT-1 as heavy trading tests 69%"
telemetry: "69% · $37K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-22T07:48:31+00:00"
event_id: "CM-EVT-QWGZDJ1DQ6"
event_slug: "housemt1-26"
event_question: "MT-01 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSEMT1-26-R"
  question_raw: "Will Republican win the House race for MT-1?"
  current_price: 0.69
  volume_24h_usd: 36789.02
  volume_cumulative_usd: 88726.0
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices a Republican win in MT-1 at 69%, a solid but contested favorite, leaving Democrats a real path."
  - "$36.8K in 24h is 41% of all-time volume on this contract, the market is repricing with urgency."
  - "MT-1 is a bellwether swing seat; volume at this scale suggests polling, fundraising data, or candidate news is moving through the market."
  - "Resolves on 2026 midterm results for MT-1."
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
      kalshi_vol_24h_usd: 36789.02
sources:
  - label: "ClearMarket market record: MT-01 House winner?"
    url: "https://clearmarket.fyi/events/housemt1-26"
    retrieved_at: "2026-09-22T07:48:31+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Forty-one percent of all-time volume in a single session on a contested House race is a strong signal that material district-level information is circulating and warrants immediate tracking.
