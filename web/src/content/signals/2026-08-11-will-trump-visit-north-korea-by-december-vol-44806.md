---
signal_id: "CMSIG20260811VS02"
signal_slug: "will-trump-visit-north-korea-by-december-vol-44806"
headline: "Trump North Korea visit: 8% on $45K surge"
semantic_title: "A Trump visit to North Korea by year-end stays a long shot at 8%"
telemetry: "8% · $45K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-11T08:50:18+00:00"
event_id: "CM-EVT-4GRY31QS88"
event_slug: "will-trump-visit-north-korea-by-june-30"
event_question: "Will Trump visit North Korea by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x4e53d90b756b3820270df8c51acb5ddd48ce090c3c7fa05e162c9d897b8688d6"
  question_raw: "Will Trump visit North Korea by December 31?"
  current_price: 0.084
  volume_24h_usd: 44806.38465000001
  volume_cumulative_usd: 94932.340307
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Market prices a Trump visit to North Korea by December 31 at just 8%, heavily discounted."
  - "$45K in 24h volume, 47% of all-time, flags renewed geopolitical attention on the contract."
  - "Volume spike likely driven by diplomatic news flow or DPRK-related headline risk without confirming details."
  - "Resolves YES only if Trump physically visits North Korea before January 1, 2027."
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
      poly_vol_24h_usd: 44806.38465000001
sources:
  - label: "ClearMarket market record: Will Trump visit North Korea by 2026?"
    url: "https://clearmarket.fyi/events/will-trump-visit-north-korea-by-june-30"
    retrieved_at: "2026-08-11T08:50:18+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 47% all-time volume draw at 8% odds indicates the market is actively re-testing the probability on new diplomatic noise without shifting consensus, desks covering Korea policy should monitor for the catalyst behind today's attention.
