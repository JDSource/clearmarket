---
signal_id: "CMSIG20260911VS05"
signal_slug: "will-the-10-year-treasury-yield-hit-5-2-vol-15210"
headline: "10Y yield 5.2% before 2027: 28% on $15K"
semantic_title: "10-year yield hitting 5.2% before 2027 stays a long shot"
telemetry: "28% · $15K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-11T12:33:13+00:00"
event_id: "CM-EVT-4F238D6VR7"
event_slug: "how-high-will-10-year-treasury-yield-go-before-2027"
event_question: "What is the maximum 10-year Treasury yield before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x29ab857c87a22182c1ebb51c80f4ad5110c11676f78fac95af1942bceccbfed1"
  question_raw: "Will the 10-year Treasury yield hit 5.2% before 2027?"
  current_price: 0.279
  volume_24h_usd: 15210.09846
  volume_cumulative_usd: 50687.931711000005
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket holds the 5.2% threshold at 28%, traders assign roughly one-in-four odds to a significant rates spike before year-end."
  - "30% of all-time volume traded in 24h, suggesting a macro catalyst, CPI print, Fed communication, or Treasury supply news, refreshed interest."
  - "At 28%, the market is pricing this as a tail risk, not a base case, but the volume shows it is not being ignored."
  - "Contract resolves if the 10-year yield closes at or above 5.2% at any point before January 1, 2027."
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
      poly_vol_24h_usd: 15210.09846
sources:
  - label: "ClearMarket market record: What is the maximum 10-year Treasury yield before 2027?"
    url: "https://clearmarket.fyi/events/how-high-will-10-year-treasury-yield-go-before-2027"
    retrieved_at: "2026-09-11T12:33:13+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 28% probability with a fresh volume pulse on rates spike risk is a useful cross-check for fixed-income desks, it suggests the market is holding a non-trivial tail on the long end but has not repriced it as consensus.
