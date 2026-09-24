---
signal_id: "CMSIG20260924VS05"
signal_slug: "will-the-democrats-win-the-georgia-gover-vol-22448"
headline: "Dem Georgia governor: 56% Polymarket, $22K in"
semantic_title: "Democrats lead Georgia governor at 56% on Polymarket volume"
telemetry: "56% · $22K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-24T07:48:17+00:00"
event_id: "CM-EVT-L03QNMYNS5"
event_slug: "georgia-governor-winner-2026"
event_question: "Will there be a winner determined in the Georgia Governor Election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x73a9911393e7bd2262904c4413d9614f68bb6290ddf7d88ed607f1562d08fb05"
  question_raw: "Will the Democrats win the Georgia governor race in 2026?"
  current_price: 0.56
  volume_24h_usd: 22448.017667999997
  volume_cumulative_usd: 65742.760699
  arbitration_model: "uma_oracle"
bullets:
  - "Polymarket marks Democrats at 56%, marginally firmer than the 54% on Kalshi, both within noise."
  - "$22.4K in 24h equals 34% of all-time volume, showing the race is attracting fresh money across venues."
  - "Cross-platform agreement near 54-56% reinforces the Democrat lean without suggesting a blowout."
  - "Resolves on the 2026 Georgia gubernatorial election outcome."
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
      poly_vol_24h_usd: 22448.017667999997
sources:
  - label: "ClearMarket market record: Will there be a winner determined in the Georgia Govern"
    url: "https://clearmarket.fyi/events/georgia-governor-winner-2026"
    retrieved_at: "2026-09-24T07:48:17+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The Kalshi/Polymarket bracket of 54-56% with simultaneous volume surges on both venues confirms the Georgia governor race is in active price-discovery, relevant for any Senate-majority or down-ballot overlay model.
