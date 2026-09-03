---
signal_id: "CMSIG20260903VS05"
signal_slug: "will-any-ai-model-reach-1520-overall-are-vol-20743"
headline: "AI Arena 1520 by Sept 30: 93% on $20K volume"
semantic_title: "Traders back AI hitting 1520 score before September 30"
telemetry: "93% · $21K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-03T12:31:50+00:00"
event_id: "CM-EVT-61DHJLFR26"
event_slug: "will-any-ai-model-reach-overall-arena-score-by-september-30"
event_question: "AI model highest Overall Arena Score, September 30, 2026"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x6a98ff5d9296b7130ba3c6d5978e0777b98f0550341706bef86f7eb390def16b"
  question_raw: "Will any AI model reach 1520 Overall Arena Score by September 30, 2026?"
  current_price: 0.932
  volume_24h_usd: 20743.757672999996
  volume_cumulative_usd: 50373.283349
  arbitration_model: "uma_oracle"
  resolves_at: "2026-09-30T00:00:00Z"
bullets:
  - "Polymarket prices the September 30 deadline at 93%, near-consensus that the threshold will be crossed imminently."
  - "24h volume of $20K is 41% of all-time flow, a substantial single-session concentration."
  - "This contract shares thematic overlap with the January 2027 version, suggesting a specific model release is the catalyst."
  - "Resolves if any AI model achieves a 1520 Overall Arena Score by September 30, 2026."
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
      poly_vol_24h_usd: 20743.757672999996
sources:
  - label: "ClearMarket market record: AI model highest Overall Arena Score, September 30, 202"
    url: "https://clearmarket.fyi/events/will-any-ai-model-reach-overall-arena-score-by-september-30"
    retrieved_at: "2026-09-03T12:31:50+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Paired with the January 2027 contract seeing similar volume, the convergence of activity at 93% points to an imminent benchmark event that desks tracking AI sector developments should flag immediately.
