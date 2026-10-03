---
signal_id: "CMSIG20261003VS00"
signal_slug: "will-the-republicans-win-the-kansas-sena-vol-135502"
headline: "Kansas Senate GOP: 62% on $136K volume surge"
semantic_title: "Republicans hold the edge in Kansas Senate at 62%"
telemetry: "62% · $136K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-03T13:00:25+00:00"
event_id: "CM-EVT-V8Y5SZ7SK0"
event_slug: "kansas-senate-election-winner"
event_question: "Kansas Senate Election Winner"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xb8b5349814450b8bba2ecdda2eeb9f48bd3c795bfb858bedf7a383712b877743"
  question_raw: "Will the Republicans win the Kansas Senate race in 2026?"
  current_price: 0.62
  volume_24h_usd: 135502.152359
  volume_cumulative_usd: 408926.2270259999
  arbitration_model: "uma_oracle"
bullets:
  - "Polymarket prices Republicans at 62%, a clear but not decisive lean toward a GOP hold."
  - "24h volume of $135K is 33% of all-time, signaling a sharp burst of fresh attention on this race."
  - "Paired spike with the Democratic side (Spike 1) suggests the Kansas Senate is drawing contested two-sided flow."
  - "Resolves on 2026 Kansas Senate election outcome."
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
      poly_vol_24h_usd: 135502.152359
sources:
  - label: "ClearMarket market record: Kansas Senate Election Winner"
    url: "https://clearmarket.fyi/events/kansas-senate-election-winner"
    retrieved_at: "2026-10-03T13:00:25+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Heavy two-sided volume across both Kansas Senate contracts signals desks are re-evaluating competitiveness; the 62/38 split is tighter than a safe red-state hold and warrants fresh positioning review.
