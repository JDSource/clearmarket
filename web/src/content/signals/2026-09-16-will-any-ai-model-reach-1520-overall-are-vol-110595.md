---
signal_id: "CMSIG20260916VS00"
signal_slug: "will-any-ai-model-reach-1520-overall-are-vol-110595"
headline: "AI Arena 1520 score: 100% on $111K surge"
semantic_title: "AI Arena 1520 by Sept 30 looks like a done deal"
telemetry: "100% · $111K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-16T13:03:41+00:00"
event_id: "CM-EVT-61DHJLFR26"
event_slug: "will-any-ai-model-reach-overall-arena-score-by-september-30"
event_question: "AI model highest Overall Arena Score, September 30, 2026"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x6a98ff5d9296b7130ba3c6d5978e0777b98f0550341706bef86f7eb390def16b"
  question_raw: "Will any AI model reach 1520 Overall Arena Score by September 30, 2026?"
  current_price: 0.999
  volume_24h_usd: 110595.006441
  volume_cumulative_usd: 251839.16008599993
  arbitration_model: "uma_oracle"
  resolves_at: "2026-09-30T00:00:00Z"
bullets:
  - "Polymarket prices this at 100%, implying the market treats the outcome as already resolved."
  - "44% of all-time volume, $110.6K, landed in 24h, the largest single-day commitment on record."
  - "A model crossing 1520 overall may already be documented or imminent, drawing last-minute confirming flow."
  - "Resolves Sept 30, 2026; any 100% contract carrying this much fresh volume warrants immediate verification of claim status."
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
      poly_vol_24h_usd: 110595.006441
sources:
  - label: "ClearMarket market record: AI model highest Overall Arena Score, September 30, 202"
    url: "https://clearmarket.fyi/events/will-any-ai-model-reach-overall-arena-score-by-september-30"
    retrieved_at: "2026-09-16T13:03:41+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A near-certain contract drawing 44% of lifetime volume in one session is a strong signal the resolution event has effectively occurred or been publicly confirmed, desks should verify claim status before assuming residual edge.
