---
signal_id: "CMSIG20260702VS03"
signal_slug: "will-s-bastien-lecornu-be-the-next-leade-vol-1140815"
headline: "Lecornu next out: 0% on $1.1M Polymarket flow"
semantic_title: "Market fades Lecornu as the next European leader out before 2027"
telemetry: "0% · $1.1M 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-02T10:35:06+00:00"
event_id: "CM-EVT-2FLCV9PNS4"
event_slug: "next-leader-out-of-power-before-2027-no-orban"
event_question: "Will a current leader lose power before 2027, excluding Viktor Orbán?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xa922643c642c7d0a8541a60bbd70f11e97dc16b3dfb4cf98c46217f7bfa3e916"
  question_raw: "Will Sébastien Lecornu be the next leader out before 2027?"
  current_price: 0.001
  volume_24h_usd: 1140815.993833
  volume_cumulative_usd: 2655687.6576199997
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "0% price signals traders see no viable path to a Lecornu departure as the next listed exit."
  - "$1.14M in 24h, 43% of all-time, makes this one of the largest single-day flows in the contract."
  - "Lecornu's elevated volume relative to Trump's adds a France-specific angle: likely tied to recent political noise."
  - "Part of the same coordinated multi-leg G7 leadership basket liquidation seen across Polymarket today."
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
      poly_vol_24h_usd: 1140815.993833
sources:
  - label: "ClearMarket market record: Will a current leader lose power before 2027, excluding"
    url: "https://clearmarket.fyi/events/next-leader-out-of-power-before-2027-no-orban"
    retrieved_at: "2026-07-02T10:35:06+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The disproportionate volume on Lecornu versus other legs may reflect France-specific political event risk that briefly lifted speculative longs before traders returned the contract to zero, worth monitoring for Élysée succession chatter.
