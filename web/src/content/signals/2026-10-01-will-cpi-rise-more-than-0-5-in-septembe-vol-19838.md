---
signal_id: "CMSIG20261001VS05"
signal_slug: "will-cpi-rise-more-than-0-5-in-septembe-vol-19838"
headline: "CPI above 0.5% Sept 2026: 54% on $20K volume"
semantic_title: "Odds split evenly on CPI topping 0.5% in September"
telemetry: "54% · $20K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-01T15:04:01+00:00"
event_id: "CM-EVT-F9NPW9F1V9"
event_slug: "kxcpi-26sep"
event_question: "Will CPI in September be above expectations?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPI-26SEP-T0.5"
  question_raw: "Will CPI rise more than 0.5% in September 2026?"
  current_price: 0.54
  volume_24h_usd: 19838.71
  volume_cumulative_usd: 63041.46
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-13T13:56:00Z"
bullets:
  - "Kalshi prices a 54% chance September 2026 CPI rises more than 0.5%, a coin-flip with a marginal upside lean."
  - "24h volume of $20K is 31% of all-time, consistent with pre-data positioning as the September CPI release approaches."
  - "A 54/46 split signals genuine two-way uncertainty; neither disinflationary nor re-acceleration thesis has the floor."
  - "Resolves on the September CPI print; the tight price makes this a high-sensitivity contract to any data surprise."
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
      kalshi_vol_24h_usd: 19838.71
sources:
  - label: "ClearMarket market record: Will CPI in September be above expectations?"
    url: "https://clearmarket.fyi/events/kxcpi-26sep"
    retrieved_at: "2026-10-01T15:04:01+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The near-50% price combined with a 31%-of-all-time volume day signals the market has no strong prior on September inflation, desks should flag this as a binary event-risk contract with meaningful repricing potential on the data.
