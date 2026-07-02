---
signal_id: "CMSIG20260702VS04"
signal_slug: "will-benjamin-netanyahu-be-the-next-lead-vol-673163"
headline: "Netanyahu next out: 0% on $673K Polymarket surge"
semantic_title: "Heavy flows absorb Netanyahu tail risk, price to zero before 2027"
telemetry: "0% · $673K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-02T10:35:06+00:00"
event_id: "CM-EVT-2FLCV9PNS4"
event_slug: "next-leader-out-of-power-before-2027-no-orban"
event_question: "Will a current leader lose power before 2027, excluding Viktor Orbán?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x1cd1a66943b214de90027ce888621fc4e53f5c46351809e51dbad0635b7fe9b7"
  question_raw: "Will Benjamin Netanyahu be the next leader out before 2027?"
  current_price: 0.001
  volume_24h_usd: 673163.598915
  volume_cumulative_usd: 1211413.4634779997
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "0% price means Polymarket participants assign no probability to Netanyahu being the next listed leader out."
  - "$673K in 24h, 56% of all-time, is the highest all-time share of any leg in this basket today."
  - "Israel-Gaza ceasefire developments and coalition dynamics likely drove speculative positioning into this contract."
  - "Full reset to zero amid elevated geopolitical noise suggests structured arb fully overwhelmed directional flow."
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
      poly_vol_24h_usd: 673163.598915
sources:
  - label: "ClearMarket market record: Will a current leader lose power before 2027, excluding"
    url: "https://clearmarket.fyi/events/next-leader-out-of-power-before-2027-no-orban"
    retrieved_at: "2026-07-02T10:35:06+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The highest all-time-volume share in the basket for Netanyahu, despite, or because of, active Middle East news flow, signals that any speculative risk premium was arbitraged away quickly, leaving desks with clean books on this leg.
