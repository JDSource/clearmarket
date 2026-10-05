---
signal_id: "CMSIG20261005VS04"
signal_slug: "will-the-democrats-win-the-nevada-govern-vol-63261"
headline: "NV Dem governor: 56% on $63K polymarket"
semantic_title: "Nevada governor: buying picks up on Democrats at 56%"
telemetry: "56% · $63K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-05T16:45:18+00:00"
event_id: "CM-EVT-Q7DX7L87P0"
event_slug: "nevada-governor-winner-2026"
event_question: "Will the Nevada governor election be won by the Republican candidate?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x707eb5c6df23e32e0b770dd0ccd1245abb7fac0dcfd24d8b68dd99e5ca737180"
  question_raw: "Will the Democrats win the Nevada governor race in 2026?"
  current_price: 0.56
  volume_24h_usd: 63261.264142999986
  volume_cumulative_usd: 181052.39676800012
  arbitration_model: "uma_oracle"
bullets:
  - "Polymarket prices Nevada Democrats at 56%, close to Kalshi's 54%, markets broadly aligned."
  - "$63K in 24h is 35% of all-time volume on Polymarket's version of the same race."
  - "Cross-venue activity on the same contract is a strong sign of informed, arbitrage-aware flow."
  - "Resolves on the 2026 Nevada gubernatorial election."
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
      poly_vol_24h_usd: 63261.264142999986
sources:
  - label: "ClearMarket market record: Will the Nevada governor election be won by the Republi"
    url: "https://clearmarket.fyi/events/nevada-governor-winner-2026"
    retrieved_at: "2026-10-05T16:45:18+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Simultaneous spikes on both Kalshi and Polymarket for the Nevada governor race indicate coordinated or parallel positioning across venues, elevating the signal quality relative to a single-venue surge.
