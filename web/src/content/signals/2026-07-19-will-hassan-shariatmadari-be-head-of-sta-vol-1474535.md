---
signal_id: "CMSIG20260719VS00"
signal_slug: "will-hassan-shariatmadari-be-head-of-sta-vol-1474535"
headline: "Shariatmadari Iran head of state: 0% on $1.47M surge"
semantic_title: "Capital writes off Shariatmadari as Iran head of state"
telemetry: "0% · $1.5M 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-19T09:49:33+00:00"
event_id: "CM-EVT-RHBS1Y2385"
event_slug: "iran-leader-end-of-2026"
event_question: "Will Iran's leader change by the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x7d9928e23aefb2209696048829b614f49e387d5a77327aa887d0724952fd1156"
  question_raw: "Will Hassan Shariatmadari be head of state in Iran end of 2026?"
  current_price: 0.001
  volume_24h_usd: 1474535.0000000023
  volume_cumulative_usd: 1760177.8277880051
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Market prices zero probability, crowd treats Shariatmadari as effectively eliminated from contention."
  - "$1.47M traded in 24h, representing 84% of all-time contract volume, near-total position flush."
  - "Massive one-day dominance of lifetime flow signals a decisive information event driving consensus to zero."
  - "Contract resolves end of 2026; current pricing implies no credible path to power within the horizon."
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
      poly_vol_24h_usd: 1474535.0000000023
sources:
  - label: "ClearMarket market record: Will Iran's leader change by the end of 2026?"
    url: "https://clearmarket.fyi/events/iran-leader-end-of-2026"
    retrieved_at: "2026-07-19T09:49:33+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The near-total liquidation of all-time volume into a single session at 0% signals a hard informational close on this contract, desks should treat Iranian succession risk through alternative names.
