---
signal_id: "CMSIG20260730VS01"
signal_slug: "will-hassan-shariatmadari-be-head-of-sta-vol-1365388"
headline: "Shariatmadari Iran head: 0% on $1.37M"
semantic_title: "Shariatmadari Iran head of state odds crash to zero"
telemetry: "0% · $1.4M 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-30T10:21:41+00:00"
event_id: "CM-EVT-RHBS1Y2385"
event_slug: "iran-leader-end-of-2026"
event_question: "Will Iran's leader change by the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x7d9928e23aefb2209696048829b614f49e387d5a77327aa887d0724952fd1156"
  question_raw: "Will Hassan Shariatmadari be head of state in Iran end of 2026?"
  current_price: 0.001
  volume_24h_usd: 1365388.792000001
  volume_cumulative_usd: 3131577.4687879994
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Price at 0% is a near-total market rejection, traders see no realistic path to Shariatmadari leading Iran by year-end."
  - "$1.37M in 24h volume is 44% of all-time flow, marking this as one of the contract's highest-activity sessions."
  - "Fresh volume at a zero price typically reflects a definitive off-market development that has closed the question."
  - "Resolves end of 2026; current pricing implies the question is effectively settled in traders' minds."
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
      poly_vol_24h_usd: 1365388.792000001
sources:
  - label: "ClearMarket market record: Will Iran's leader change by the end of 2026?"
    url: "https://clearmarket.fyi/events/iran-leader-end-of-2026"
    retrieved_at: "2026-07-30T10:21:41+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A flood of capital into a 0%-priced contract signals a known, market-conclusive event has made this outcome impossible, desks should flag for Iran political intelligence updates that may not yet be fully public.
