---
signal_id: "CMSIG20260921VS03"
signal_slug: "will-the-democrats-win-the-south-carolin-vol-62887"
headline: "Dems SC Senate: 13% on $63K volume pop"
semantic_title: "Democrats stay a long shot in the South Carolina Senate race"
telemetry: "13% · $63K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-21T07:48:00+00:00"
event_id: "CM-EVT-44DJH0XML6"
event_slug: "south-carolina-senate-election-winner"
event_question: "Will a winner be declared in the South Carolina Senate election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x4de72138204727d2821bff847d8158819ab5b591db1b5b263676126cbb3a0430"
  question_raw: "Will the Democrats win the South Carolina Senate race in 2026?"
  current_price: 0.13
  volume_24h_usd: 62887.972853
  volume_cumulative_usd: 219624.86793500005
  arbitration_model: "uma_oracle"
bullets:
  - "Polymarket has Democrats at 13% in South Carolina, a heavy underdog reading in a reliably Republican state."
  - "$63K in 24h volume equals 29% of all-time, placing this among the contract's busiest sessions."
  - "Simultaneous spikes across multiple red-state Senate races point to a broader 2026 Senate-cycle repricing event."
  - "Resolves on 2026 South Carolina Senate general election result."
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
      poly_vol_24h_usd: 62887.972853
sources:
  - label: "ClearMarket market record: Will a winner be declared in the South Carolina Senate "
    url: "https://clearmarket.fyi/events/south-carolina-senate-election-winner"
    retrieved_at: "2026-09-21T07:48:00+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Concurrent volume across SC, KS, and OH Senate contracts suggests a systematic sweep of 2026 Senate pricing, desks should look for a common catalyst such as a new forecaster model update or a polling release affecting the whole cycle.
