---
signal_id: "CMSIG20260813VS03"
signal_slug: "will-luiz-in-cio-lula-da-silva-finish-in-vol-77668"
headline: "Lula 2nd place R1: 7% on $78K Polymarket surge"
semantic_title: "Traders back long odds against Lula placing second in round one"
telemetry: "7% · $78K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-13T09:08:38+00:00"
event_id: "CM-EVT-Z8ZNQ1C002"
event_slug: "brazil-presidential-election-first-round-2nd-place"
event_question: "Will the second-place finisher in the first round of the 2026 Brazil Presidential Election be determined?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x8ee27c276a1bee094293751285d8a6697674b023196cb21fdd14bf3ca12f6ec0"
  question_raw: "Will Luiz Inácio Lula da Silva finish in second place in the first round of the 2026 Brazilian presidential election?"
  current_price: 0.073
  volume_24h_usd: 77668.03118600001
  volume_cumulative_usd: 240909.98506199993
  arbitration_model: "uma_oracle"
  resolves_at: "2026-10-04T00:00:00Z"
bullets:
  - "Polymarket prices Lula finishing second in the first round at just 7%, a deep-underdog scenario."
  - "$78K in 24 hours is 32% of all-time volume, signaling fresh eyes on Brazil's 2026 electoral math."
  - "A 7% price with rising volume suggests the market is stress-testing incumbent resilience amid opposition noise."
  - "Resolves on official first-round results of the Brazilian presidential election."
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
      poly_vol_24h_usd: 77668.03118600001
sources:
  - label: "ClearMarket market record: Will the second-place finisher in the first round of th"
    url: "https://clearmarket.fyi/events/brazil-presidential-election-first-round-2nd-place"
    retrieved_at: "2026-08-13T09:08:38+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Volume into a 7% outcome on a major EM election signals a desk should review Brazil political risk exposure, the market is assigning meaningful but low probability to a historic upset scenario.
