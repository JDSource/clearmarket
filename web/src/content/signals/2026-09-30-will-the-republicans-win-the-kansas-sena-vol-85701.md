---
signal_id: "CMSIG20260930VS02"
signal_slug: "will-the-republicans-win-the-kansas-sena-vol-85701"
headline: "GOP Kansas Senate: 73% on $86K spike"
semantic_title: "Republicans hold firm as Kansas Senate favorite"
telemetry: "73% · $86K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-30T14:33:50+00:00"
event_id: "CM-EVT-V8Y5SZ7SK0"
event_slug: "kansas-senate-election-winner"
event_question: "Kansas Senate Election Winner"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xb8b5349814450b8bba2ecdda2eeb9f48bd3c795bfb858bedf7a383712b877743"
  question_raw: "Will the Republicans win the Kansas Senate race in 2026?"
  current_price: 0.73
  volume_24h_usd: 85701.69502200001
  volume_cumulative_usd: 254214.20586400008
  arbitration_model: "uma_oracle"
bullets:
  - "Polymarket has Republicans winning the Kansas Senate seat at 73%, a solid but not locked-in lead."
  - "24h volume of $86K represents 34% of all-time, a sharp single-session attention jump."
  - "Fresh volume into a race previously considered safe suggests new competitive information or polling is circulating."
  - "Resolves on the 2026 Kansas Senate general election result."
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
      poly_vol_24h_usd: 85701.69502200001
sources:
  - label: "ClearMarket market record: Kansas Senate Election Winner"
    url: "https://clearmarket.fyi/events/kansas-senate-election-winner"
    retrieved_at: "2026-09-30T14:33:50+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A one-day volume share of 34% in a race priced at 73% Republican suggests desks should watch for incoming polling or candidate news that may be tightening the margin.
