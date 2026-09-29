---
signal_id: "CMSIG20260929VS02"
signal_slug: "will-kostadin-kostadinov-win-the-next-b-vol-18452"
headline: "Kostadinov Bulgaria pres: 1% on $18K volume pop"
semantic_title: "Kostadinov Bulgarian presidency bid trades at long-shot odds"
telemetry: "1% · $18K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-29T07:47:54+00:00"
event_id: "CM-EVT-C541X65QT7"
event_slug: "bulgaria-presidential-election"
event_question: "Will Bulgaria hold a presidential election by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xa9e24f23e61265a798a2e484c0ead96255e6cd94034dfc0ab58343aa907cc390"
  question_raw: "Will Kostadin Kostadinov win the next  Bulgarian presidential election?"
  current_price: 0.008
  volume_24h_usd: 18452.993998
  volume_cumulative_usd: 72325.07790799999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-30T00:00:00Z"
bullets:
  - "Polymarket prices Kostadin Kostadinov at just 1% to win the next Bulgarian presidential election, a near-zero probability outcome."
  - "$18.5K traded in 24 hours, representing 26% of all-time contract volume, meaningful fresh attention on an otherwise thin market."
  - "Volume into a 1% contract suggests either hedging against a tail scenario or speculative positioning on a far-right upset narrative gaining traction."
  - "Resolution tied to the Bulgarian presidential election result."
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
      poly_vol_24h_usd: 18452.993998
sources:
  - label: "ClearMarket market record: Will Bulgaria hold a presidential election by 2026?"
    url: "https://clearmarket.fyi/events/bulgaria-presidential-election"
    retrieved_at: "2026-09-29T07:47:54+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Fresh volume into a 1% contract on a European far-right candidate warrants a brief check for geopolitical desks tracking Balkans political risk, though current odds assign near-zero weight to the outcome.
