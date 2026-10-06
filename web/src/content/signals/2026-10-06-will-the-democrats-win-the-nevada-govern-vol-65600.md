---
signal_id: "CMSIG20261006VS03"
signal_slug: "will-the-democrats-win-the-nevada-govern-vol-65600"
headline: "Nevada Dem governor: 55% on $66K volume"
semantic_title: "Democrats hold a modest lead in Nevada governor betting on Polymarket"
telemetry: "55% · $66K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-06T07:48:59+00:00"
event_id: "CM-EVT-Q7DX7L87P0"
event_slug: "nevada-governor-winner-2026"
event_question: "Will the Nevada governor election be won by the Republican candidate?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x707eb5c6df23e32e0b770dd0ccd1245abb7fac0dcfd24d8b68dd99e5ca737180"
  question_raw: "Will the Democrats win the Nevada governor race in 2026?"
  current_price: 0.55
  volume_24h_usd: 65600.70243599999
  volume_cumulative_usd: 183980.8735230001
  arbitration_model: "uma_oracle"
bullets:
  - "Polymarket prices Democrats at 55%, a clearer lean than the Kalshi contract, though still within a competitive range."
  - "$66K traded in 24h accounts for 36% of all-time volume on this contract."
  - "Simultaneous spikes on both the Kalshi and Polymarket Nevada governor contracts suggest new polling or candidate news is pulling cross-venue attention."
  - "Resolves on the 2026 Nevada gubernatorial election outcome."
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
      poly_vol_24h_usd: 65600.70243599999
sources:
  - label: "ClearMarket market record: Will the Nevada governor election be won by the Republi"
    url: "https://clearmarket.fyi/events/nevada-governor-winner-2026"
    retrieved_at: "2026-10-06T07:48:59+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Cross-venue volume spikes on the same underlying race give a desk a live arbitrage signal, Polymarket at 55% vs. Kalshi at 51% implies a 4-point spread worth monitoring for convergence.
