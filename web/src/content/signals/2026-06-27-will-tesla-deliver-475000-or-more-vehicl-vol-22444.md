---
signal_id: "CMSIG20260627VS06"
signal_slug: "will-tesla-deliver-475000-or-more-vehicl-vol-22444"
headline: "Tesla Q2 deliveries ≥475K: 11% on $22K"
semantic_title: "Tesla Q2 delivery miss risk priced at 89% against 475K target"
telemetry: "11% · $22K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-27T01:36:27+00:00"
event_id: "CM-EVT-TKB6WQH0P3"
event_slug: "how-many-tesla-deliveries-in-q2-2026"
event_question: "Will Tesla deliver between 350000 and 375000 vehicles in Q2 2026"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x4926438a8bcd51e07989a94a7efafff86a0c66101a5f0f51dc0a252425c41b4b"
  question_raw: "Will Tesla deliver 475000 or more vehicles in Q2 2026"
  current_price: 0.112
  volume_24h_usd: 22444.178305000012
  volume_cumulative_usd: 38462.889547000006
  arbitration_model: "uma_oracle"
  resolves_at: "2026-06-30T00:00:00Z"
bullets:
  - "11% probability implies the market expects Tesla to fall short of 475K Q2 deliveries."
  - "$22K in 24h is 58% of all-time contract volume, significant late-quarter positioning."
  - "Q2 ends June 30; delivery data release imminent, compressing time value sharply."
  - "Low price and high volume share suggest 'No' holders are locking in gains ahead of the print."
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
      poly_vol_24h_usd: 22444.178305000012
sources:
  - label: "ClearMarket market record: Will Tesla deliver between 350000 and 375000 vehicles i"
    url: "https://clearmarket.fyi/events/how-many-tesla-deliveries-in-q2-2026"
    retrieved_at: "2026-06-27T01:36:27+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With Q2 closing today and delivery data due imminently, the 11% price and heavy volume share indicate the market has already largely adjudicated the miss, equity desks should watch for the official print as a near-term catalyst.
