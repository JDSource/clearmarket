---
signal_id: "CMSIG20261014VS03"
signal_slug: "will-the-democrats-win-the-ohio-governor-vol-63838"
headline: "Dem Ohio governor win: 71% on $63K volume surge"
semantic_title: "Democrats favored in Ohio governor race as buyers back 71%"
telemetry: "71% · $64K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-14T13:17:59+00:00"
event_id: "CM-EVT-KSRSHVHX02"
event_slug: "ohio-governor-winner-2026"
event_question: "Will a specific candidate win the Ohio gubernatorial election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x3babe91f8d2fac44027f9ba7f0f1a59e61b72419828e6e517f96bbcf4e132498"
  question_raw: "Will the Democrats win the Ohio governor race in 2026?"
  current_price: 0.71
  volume_24h_usd: 63838.61533000001
  volume_cumulative_usd: 225588.00605900004
  arbitration_model: "uma_oracle"
bullets:
  - "Polymarket prices 71%, odds favor Democrats but leave meaningful room for a Republican upset."
  - "$63K in 24h is 28% of all-time volume on a $225K contract, reflecting sustained ongoing interest."
  - "Ohio's competitive governor race is attracting fresh capital as the 2026 midterm cycle heats up."
  - "Resolves on 2026 Ohio gubernatorial election result."
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
      poly_vol_24h_usd: 63838.61533000001
sources:
  - label: "ClearMarket market record: Will a specific candidate win the Ohio gubernatorial el"
    url: "https://clearmarket.fyi/events/ohio-governor-winner-2026"
    retrieved_at: "2026-10-14T13:17:59+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Sustained volume on a 71% Democratic contract in a swing state suggests active two-sided hedging; a desk should treat this as a live battleground with real price discovery still underway.
