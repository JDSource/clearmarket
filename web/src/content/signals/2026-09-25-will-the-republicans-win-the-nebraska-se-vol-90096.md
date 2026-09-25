---
signal_id: "CMSIG20260925VS01"
signal_slug: "will-the-republicans-win-the-nebraska-se-vol-90096"
headline: "Nebraska Senate GOP: 70% on $90K inflow"
semantic_title: "Buyers back Nebraska Senate Republicans at 70%"
telemetry: "70% · $90K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-25T07:48:30+00:00"
event_id: "CM-EVT-CY3W5Z2793"
event_slug: "nebraska-senate-election-winner"
event_question: "Nebraska Senate Election Winner  "
primary_market:
  platform: "polymarket"
  platform_market_id: "0x71e9f5312aac62bdc9b87fa8d171fa929eca6243d815298c4c7d61303f7d53dd"
  question_raw: "Will the Republicans win the Nebraska Senate race in 2026?"
  current_price: 0.7
  volume_24h_usd: 90096.103047
  volume_cumulative_usd: 240463.26102099995
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices Republican victory at 70%, competitive but not safe territory for the GOP."
  - "$90K in 24h volume represents 37% of all-time, the largest single-day surge for this contract."
  - "Nebraska Senate drawing fresh capital alongside Kansas suggests broad reassessment of plains-state races."
  - "Resolves on the Nebraska Senate general election in November 2026."
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
      poly_vol_24h_usd: 90096.103047
sources:
  - label: "ClearMarket market record: Nebraska Senate Election Winner  "
    url: "https://clearmarket.fyi/events/nebraska-senate-election-winner"
    retrieved_at: "2026-09-25T07:48:30+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The largest daily volume print on this contract, arriving alongside the Kansas spike, points to coordinated Senate-map repricing that desks should track together.
