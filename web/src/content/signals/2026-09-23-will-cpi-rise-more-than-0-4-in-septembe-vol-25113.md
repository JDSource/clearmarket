---
signal_id: "CMSIG20260923VS07"
signal_slug: "will-cpi-rise-more-than-0-4-in-septembe-vol-25113"
headline: "CPI >0.4% Sept 2026: 88% on $25K volume burst"
semantic_title: "A hot September CPI print above 0.4% is the heavy favorite"
telemetry: "88% · $25K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-23T07:48:28+00:00"
event_id: "CM-EVT-F9NPW9F1V9"
event_slug: "kxcpi-26sep"
event_question: "Will CPI in September be above expectations?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPI-26SEP-T0.4"
  question_raw: "Will CPI rise more than 0.4% in September 2026?"
  current_price: 0.88
  volume_24h_usd: 25113.05
  volume_cumulative_usd: 63941.57
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-13T13:56:00Z"
bullets:
  - "At 88%, Kalshi prices a September 2026 CPI monthly gain above 0.4% as a near-certainty, reflecting firm inflation expectations."
  - "24h volume of $25K is 39% of all-time, a concentrated surge likely tied to pre-release positioning or fresh economic data."
  - "With the print days away, traders are loading up on the high-inflation outcome; 88% implies the market sees a hot number as the base case."
  - "Contract resolves on the official BLS CPI release for September 2026."
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
      kalshi_vol_24h_usd: 25113.05
sources:
  - label: "ClearMarket market record: Will CPI in September be above expectations?"
    url: "https://clearmarket.fyi/events/kxcpi-26sep"
    retrieved_at: "2026-09-23T07:48:28+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk running rates or macro books should treat 88% on a >0.4% CPI as a strong consensus signal ahead of the print, worth cross-referencing with fed funds positioning for a potential hawkish surprise trade.
