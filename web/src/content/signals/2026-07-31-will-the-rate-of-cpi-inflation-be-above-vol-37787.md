---
signal_id: "CMSIG20260731VS01"
signal_slug: "will-the-rate-of-cpi-inflation-be-above-vol-37787"
headline: "July CPI above 3.3%: 59% on $37K surge"
semantic_title: "Betting picks up on July CPI holding above 3.3%"
telemetry: "59% · $38K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-31T10:35:22+00:00"
event_id: "CM-EVT-XP5XZNK7W3"
event_slug: "kxcpiyoy-26jul"
event_question: "The rate of CPI inflation for the year ending in July 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPIYOY-26JUL-T3.3"
  question_raw: "Will the rate of CPI inflation be above 3.3% for the year ending in July 2026?"
  current_price: 0.59
  volume_24h_usd: 37787.53
  volume_cumulative_usd: 74292.99
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-11-11T14:00:00Z"
bullets:
  - "At 59%, Kalshi leans toward annual CPI through July topping the 3.3% threshold."
  - "$37K in 24h represents 51% of all-time volume, majority of lifetime activity in one day."
  - "Surge likely front-runs the imminent July CPI print due imminently."
  - "Resolves on official BLS CPI release for the year ending July 2026."
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
      kalshi_vol_24h_usd: 37787.53
sources:
  - label: "ClearMarket market record: The rate of CPI inflation for the year ending in July 2"
    url: "https://clearmarket.fyi/events/kxcpiyoy-26jul"
    retrieved_at: "2026-07-31T10:35:22+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A majority of all-time liquidity arriving the day before the expected print tells a desk that informed traders are pricing sticky inflation; 59% is a live signal, not noise.
