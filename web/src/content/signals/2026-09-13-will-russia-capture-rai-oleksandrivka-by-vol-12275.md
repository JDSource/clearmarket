---
signal_id: "CMSIG20260913VS00"
signal_slug: "will-russia-capture-rai-oleksandrivka-by-vol-12275"
headline: "Russia/Rai-Oleksandrivka: 55% on $12K surge"
semantic_title: "Traders back Russia taking Rai-Oleksandrivka by year-end"
telemetry: "55% · $12K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-13T13:04:59+00:00"
event_id: "CM-EVT-V5Z6YFM7W2"
event_slug: "will-russia-capture-rai-oleksandrivka-by-june-30"
event_question: "Will Russia capture Rai-Oleksandrivka in 2026? (multi-deadline series)"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xbd395d67357a1862b014dfad77cb770824a64734949e789ea631509a4e1879d6"
  question_raw: "Will Russia capture Rai-Oleksandrivka by December 31?"
  current_price: 0.55
  volume_24h_usd: 12275.490971
  volume_cumulative_usd: 36944.702286
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Market prices a 55% chance Russia captures the town by Dec 31, a lean-positive read on near-term Russian advance."
  - "24h volume of $12,275 equals 33% of all-time handle, outsized single-session deployment signals fresh conviction."
  - "Renewed attention likely tracks battlefield reporting or Ukrainian line movements drawing capital to retest the majority threshold."
  - "Resolves Dec 31; any confirmed capture or credible front-line shift before year-end is the key trigger."
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
      poly_vol_24h_usd: 12275.490971
sources:
  - label: "ClearMarket market record: Will Russia capture Rai-Oleksandrivka in 2026? (multi-d"
    url: "https://clearmarket.fyi/events/will-russia-capture-rai-oleksandrivka-by-june-30"
    retrieved_at: "2026-09-13T13:04:59+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A one-third-of-lifetime volume day on a front-line territorial contract tells a desk that geopolitical desks are actively repricing eastern Ukraine battlefield risk into year-end, worth monitoring alongside energy and defense names.
