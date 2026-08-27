---
signal_id: "CMSIG20260827VS04"
signal_slug: "will-the-republicans-win-the-pennsylvani-vol-17585"
headline: "GOP PA governor: 2% on $18K Polymarket flow"
semantic_title: "Republican PA governor odds slip to near-zero"
telemetry: "2% · $18K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-27T18:47:16+00:00"
event_id: "CM-EVT-X8GH8VFYN1"
event_slug: "pennsylvania-governor-winner-2026"
event_question: "Will the Pennsylvania Governor election be won by the Democratic candidate?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xb3529e4cbcc5756ae7d5662ad1d6ddd8dd97b53bd459e2684af9bb8c4dbf582c"
  question_raw: "Will the Republicans win the Pennsylvania governor race in 2026?"
  current_price: 0.02
  volume_24h_usd: 17585.47
  volume_cumulative_usd: 41596.693185000004
  arbitration_model: "uma_oracle"
bullets:
  - "Polymarket prices Republicans at just 2%, market sees almost no path to a GOP Pennsylvania governorship."
  - "24h volume of $18K is 42% of all-time, a sharp single-day spike for a near-zero contract."
  - "Flow at 2% typically reflects either arbitrage against the Kalshi 95% Democrat contract or speculative long-shot buying."
  - "Resolves on the 2026 Pennsylvania governor election outcome."
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
      poly_vol_24h_usd: 17585.47
sources:
  - label: "ClearMarket market record: Will the Pennsylvania Governor election be won by the D"
    url: "https://clearmarket.fyi/events/pennsylvania-governor-winner-2026"
    retrieved_at: "2026-08-27T18:47:16+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Heavy volume into a 2% contract is a cross-venue arbitrage signal, desks should check the spread against the Kalshi Democratic equivalent and assess whether a structural pricing gap exists.
