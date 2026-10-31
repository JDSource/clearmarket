---
signal_id: "CMSIG20261031VS05"
signal_slug: "will-an-independent-win-the-nebraska-sen-vol-300256"
headline: "Nebraska Senate independent: 25% on $300K Polymarket flow"
semantic_title: "Betting picks up on an independent Nebraska Senate upset at 25%"
telemetry: "25% · $300K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-31T14:16:49+00:00"
event_id: "CM-EVT-CY3W5Z2793"
event_slug: "nebraska-senate-election-winner"
event_question: "Nebraska Senate Election Winner  "
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5554740293afa7aafd5fed10fd2de43a898e2884c1f98bd65185e703f371b9db"
  question_raw: "Will an independent win the Nebraska Senate race in 2026?"
  current_price: 0.25
  volume_24h_usd: 300256.24702699995
  volume_cumulative_usd: 760707.693021
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices an independent Nebraska Senate win at 25%, a meaningful long-shot."
  - "$300K in 24h equals 39% of all-time contract volume, the second-highest all-time share here."
  - "With the GOP leg at 76%, the market implies a near-zero Democratic path and an active independent race."
  - "Resolves on Nebraska 2026 Senate result; independent candidate fundraising or polling could reprice fast."
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
      poly_vol_24h_usd: 300256.24702699995
sources:
  - label: "ClearMarket market record: Nebraska Senate Election Winner  "
    url: "https://clearmarket.fyi/events/nebraska-senate-election-winner"
    retrieved_at: "2026-10-31T14:16:49+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 25% independent line drawing 39% of its all-time volume in one session signals a desk that traders are actively stress-testing the GOP consensus, the Nebraska race has a live three-way dynamic worth monitoring.
