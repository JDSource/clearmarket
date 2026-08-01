---
signal_id: "CMSIG20260801VS04"
signal_slug: "will-donavan-mckinney-be-the-democratic-vol-44699"
headline: "McKinney MI-13 Polymarket: 85% on $45K volume surge"
semantic_title: "Buyers back McKinney for MI-13 on Polymarket at 85%"
telemetry: "85% · $45K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-01T09:55:41+00:00"
event_id: "CM-EVT-KJP3106M36"
event_slug: "mi-13-democratic-primary-winner"
event_question: "Will the Democratic primary winner be determined for Michigan's 13th congressional district by August 4, 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x2cfbd8aabc3519021dc16ab0c7e0f42b0fdac191e64bcc3c42c2319c4c0117f3"
  question_raw: "Will Donavan McKinney be the Democratic Nominee for MI-13?"
  current_price: 0.85
  volume_24h_usd: 44699.440697
  volume_cumulative_usd: 146308.280125
  arbitration_model: "uma_oracle"
  resolves_at: "2026-08-04T00:00:00Z"
bullets:
  - "Polymarket echoes Kalshi at 85% for McKinney's MI-13 Democratic nomination, cross-venue alignment."
  - "24h volume of $45K is 31% of all-time flow; less concentrated than Kalshi but directionally consistent."
  - "Cross-venue consensus at identical pricing reduces arbitrage noise and confirms a genuine market view."
  - "Resolves on primary outcome; Thanedar contract on Polymarket sits at 15%."
atomic_claims:
  - type: "volume_anomaly"
    provenance: "24h + cumulative volume direct from polymarket API; intensity = 24h/cumulative (derived)"
    field_provenance:
      volume_24h_usd:
        tier: "direct"
        method: "polymarket_api"
      intensity:
        tier: "derived"
        method: "arithmetic"
        inputs: ["volume_24h_usd", "volume_cumulative_usd"]
    liquidity_context:
      poly_vol_24h_usd: 44699.440697
sources:
  - label: "ClearMarket market record: Will the Democratic primary winner be determined for Mi"
    url: "https://clearmarket.fyi/events/mi-13-democratic-primary-winner"
    retrieved_at: "2026-08-01T09:55:41+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Identical 85/15 pricing on two separate venues with simultaneous volume spikes tells a desk this is a clean, liquid consensus read, not a single-venue artifact, on McKinney as the overwhelming MI-13 primary favorite.
