---
signal_id: "CMSIG20260714VS03"
signal_slug: "will-the-rate-of-cpi-inflation-be-above-vol-22275"
headline: "June CPI above 3.8%: 29% on $22K Kalshi inflow"
semantic_title: "Above-3.8% June CPI absorbs heavy capital near resolution"
telemetry: "29% · $22K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-14T09:55:02+00:00"
event_id: "CM-EVT-FC6YNQPJV4"
event_slug: "kxcpiyoy-26jun"
event_question: "Will inflation in June 2026 be measured by year-over-year CPI?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPIYOY-26JUN-T3.8"
  question_raw: "Will the rate of CPI inflation be above 3.8% for the year ending in June 2026?"
  current_price: 0.29
  volume_24h_usd: 22275.43
  volume_cumulative_usd: 78584.58
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-10-13T14:00:00Z"
bullets:
  - "29% price means the market assigns meaningful but minority odds to a sharper 3.8%+ inflation print."
  - "$22,275 in 24h, 28% of all-time volume, clusters with the 3.6% contract in a twin-threshold play."
  - "Paired positioning across 3.6% and 3.8% levels signals traders stress-testing the upper CPI tail."
  - "Both Kalshi CPI contracts resolve on the same BLS June data release, collapsing timing uncertainty."
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
      kalshi_vol_24h_usd: 22275.43
sources:
  - label: "ClearMarket market record: Will inflation in June 2026 be measured by year-over-ye"
    url: "https://clearmarket.fyi/events/kxcpiyoy-26jun"
    retrieved_at: "2026-07-14T09:55:02+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The coordinated surge across two CPI threshold contracts suggests a macro desk is actively pricing the distribution of the June inflation print, with meaningful weight retained on an upside surprise above 3.8%.
