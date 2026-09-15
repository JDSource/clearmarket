---
signal_id: "CMSIG20260915VS00"
signal_slug: "will-any-ai-model-reach-1520-overall-are-vol-46185"
headline: "AI Arena 1520: 77% on $46K volume surge"
semantic_title: "Traders back AI hitting 1520 Arena Score by Sept 30"
telemetry: "77% · $46K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-15T13:06:46+00:00"
event_id: "CM-EVT-61DHJLFR26"
event_slug: "will-any-ai-model-reach-overall-arena-score-by-september-30"
event_question: "AI model highest Overall Arena Score, September 30, 2026"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x6a98ff5d9296b7130ba3c6d5978e0777b98f0550341706bef86f7eb390def16b"
  question_raw: "Will any AI model reach 1520 Overall Arena Score by September 30, 2026?"
  current_price: 0.77
  volume_24h_usd: 46185.692593000014
  volume_cumulative_usd: 141244.153645
  arbitration_model: "uma_oracle"
  resolves_at: "2026-09-30T00:00:00Z"
bullets:
  - "Polymarket prices a 77% chance any model clears the 1520 Overall Arena Score threshold before month-end."
  - "24h volume of $46K equals 33% of all-time handle, a sharp single-day concentration with two weeks left."
  - "Fresh activity likely tracks a recent benchmark release or lab announcement putting the threshold within reach."
  - "Resolves Sept 30, 2026, the tight window compresses risk and draws attention as the deadline nears."
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
      poly_vol_24h_usd: 46185.692593000014
sources:
  - label: "ClearMarket market record: AI model highest Overall Arena Score, September 30, 202"
    url: "https://clearmarket.fyi/events/will-any-ai-model-reach-overall-arena-score-by-september-30"
    retrieved_at: "2026-09-15T13:06:46+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The heavy late-cycle volume into a 77% price signals desks are treating the remaining two weeks as a near-certainty event, worth monitoring for any benchmark release that could snap this to near-100% or collapse it.
