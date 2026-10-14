---
signal_id: "CMSIG20261014VS03"
signal_slug: "will-the-democrats-win-the-ohio-governor-vol-55796"
headline: "Ohio governor Dem win: 72% on $55K fresh inflow"
semantic_title: "Ohio governor race tilts Democratic as odds hold near 75%"
telemetry: "72% · $56K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-14T07:48:34+00:00"
event_id: "CM-EVT-KSRSHVHX02"
event_slug: "ohio-governor-winner-2026"
event_question: "Will a specific candidate win the Ohio gubernatorial election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x3babe91f8d2fac44027f9ba7f0f1a59e61b72419828e6e517f96bbcf4e132498"
  question_raw: "Will the Democrats win the Ohio governor race in 2026?"
  current_price: 0.72
  volume_24h_usd: 55796.59811100001
  volume_cumulative_usd: 215545.32605900007
  arbitration_model: "uma_oracle"
bullets:
  - "72% price puts Democrats as clear favorites in Ohio's 2026 gubernatorial race, a notable stance in a swing state."
  - "24h volume of $55K is only 26% of all-time, meaning sustained prior interest exists and today adds a meaningful layer."
  - "Mid-October catalyst likely includes candidate debate performance, endorsements, or new polling crossing traders' desks."
  - "Resolves on November 2026 election night; Republican path to recovery would require a significant environment shift."
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
      poly_vol_24h_usd: 55796.59811100001
sources:
  - label: "ClearMarket market record: Will a specific candidate win the Ohio gubernatorial el"
    url: "https://clearmarket.fyi/events/ohio-governor-winner-2026"
    retrieved_at: "2026-10-14T07:48:34+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Steady all-time base plus a fresh 26% single-day layer signals ongoing informed accumulation, desks should treat the 72% price as a live, liquid read on Ohio's political environment heading into the final stretch.
