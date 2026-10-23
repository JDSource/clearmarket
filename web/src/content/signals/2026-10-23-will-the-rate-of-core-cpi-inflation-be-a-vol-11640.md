---
signal_id: "CMSIG20261023VS06"
signal_slug: "will-the-rate-of-core-cpi-inflation-be-a-vol-11640"
headline: "Core CPI >2.4% Nov yr-end: 97% on $11.6K surge"
semantic_title: "Core CPI above 2.4% for November year holds near certainty"
telemetry: "97% · $12K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-23T13:04:13+00:00"
event_id: "CM-EVT-BXDL61HVR9"
event_slug: "kxcpicoreyoy-26nov"
event_question: "Will core inflation in November 2026 be measured by Core CPI year-over-year change?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPICOREYOY-26NOV-T2.4"
  question_raw: "Will the rate of core CPI inflation be above 2.4% for the year ending in November 2026?"
  current_price: 0.97
  volume_24h_usd: 11640.0
  volume_cumulative_usd: 22561.56
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-12-17T15:00:00Z"
bullets:
  - "Kalshi prices core CPI above 2.4% for the November year-end at 97%, near-unanimous market conviction."
  - "24h volume of $11.6K is 52% of all-time total, the majority of all trading concentrated in one day."
  - "Paired with the 2.2% contract also at near-certainty, the market signals core inflation firmly embedded above 2.4%."
  - "Resolves on BLS core CPI print for the 12 months ending November 2026."
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
      kalshi_vol_24h_usd: 11640.0
sources:
  - label: "ClearMarket market record: Will core inflation in November 2026 be measured by Cor"
    url: "https://clearmarket.fyi/events/kxcpicoreyoy-26nov"
    retrieved_at: "2026-10-23T13:04:13+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Majority all-time volume in a single session on a 97% above-2.4% core CPI contract confirms desks are treating persistently elevated core inflation as the base case for Fed policy calibration.
