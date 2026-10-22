---
signal_id: "CMSIG20261022VS01"
signal_slug: "will-the-republicans-win-the-ohio-govern-vol-133492"
headline: "Ohio GOP governor: 20% on $133K volume"
semantic_title: "Ohio governor odds stay well below 25% for Republicans"
telemetry: "20% · $133K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-22T13:25:36+00:00"
event_id: "CM-EVT-KSRSHVHX02"
event_slug: "ohio-governor-winner-2026"
event_question: "Will a specific candidate win the Ohio gubernatorial election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x650e3ebc043ddbcfa1d1ffda0c5830f19da7389827889fb5db3474bde5b007fb"
  question_raw: "Will the Republicans win the Ohio governor race in 2026?"
  current_price: 0.2
  volume_24h_usd: 133492.127556
  volume_cumulative_usd: 392431.668192
  arbitration_model: "uma_oracle"
bullets:
  - "Polymarket prices Republican win at 20%, implying Democrats are clear favorites in this open-seat race."
  - "$133K in 24h is 34% of all-time volume, a major one-day surge on a governor market."
  - "Fresh attention on Ohio suggests new polling, candidate developments, or realignment chatter driving reassessment."
  - "Resolves after November 2026 general election."
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
      poly_vol_24h_usd: 133492.127556
sources:
  - label: "ClearMarket market record: Will a specific candidate win the Ohio gubernatorial el"
    url: "https://clearmarket.fyi/events/ohio-governor-winner-2026"
    retrieved_at: "2026-10-22T13:25:36+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A third of lifetime volume in one day on a market where Republicans sit at 20% flags that a desk is either accumulating Democratic exposure or stress-testing a state-level gubernatorial model after new data.
