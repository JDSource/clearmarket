---
signal_id: "CMSIG20260709VS02"
signal_slug: "will-mostafa-pourmohammadi-be-head-of-st-vol-395304"
headline: "Pourmohammadi Iran head of state: 0% on $395K"
semantic_title: "Capital stacks against Pourmohammadi leading Iran by year-end"
telemetry: "0% · $395K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-09T10:57:00+00:00"
event_id: "CM-EVT-RHBS1Y2385"
event_slug: "iran-leader-end-of-2026"
event_question: "Will Iran's leader change by the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xaa53ce562be767321e2f0cba9f7b3207fde7d2204dbb7f9b5d804996eba7de7c"
  question_raw: "Will Mostafa Pourmohammadi be head of state in Iran end of 2026?"
  current_price: 0.001
  volume_24h_usd: 395304.462333
  volume_cumulative_usd: 578964.820455
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Zero percent price, market flatly rejects Pourmohammadi as Iran's end-2026 head of state."
  - "$395K in 24h represents 68% of all-time volume; one of the highest single-day concentration ratios in this batch."
  - "Spike mirrors the Mousavian zero-out, pointing to systematic clearing of Iran succession long-tail names."
  - "End-2026 resolution; parallel flows across multiple Iran candidates suggest coordinated book cleanup."
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
      poly_vol_24h_usd: 395304.462333
sources:
  - label: "ClearMarket market record: Will Iran's leader change by the end of 2026?"
    url: "https://clearmarket.fyi/events/iran-leader-end-of-2026"
    retrieved_at: "2026-07-09T10:57:00+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The high share of all-time volume hitting at zero, in tandem with the Mousavian contract, tells desks that the market is systematically eliminating secondary Iran succession candidates in a single session.
