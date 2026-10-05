---
signal_id: "CMSIG20261005DV01"
signal_slug: "us-economy-soft-landing-k32-p27"
headline: "Economy 'good/excellent' at end of 2026: Kalshi 33% vs Polymarket 27%"
semantic_title: "U.S. economy outlook for end-2026 backs higher odds on one desk"
telemetry: "Polymarket 27% vs Kalshi 33%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-05T07:48:26+00:00"
event_id: "CM-EVT-ZRG5DFDMZ8"
event_slug: "kxeconpath-26"
event_question: "State of the economy at the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x50e3ee8f93a464d04ea2cea6efff45c902f43642aedbf43f7afdc899e10f71d8"
  question_raw: "Will the US economy be in a soft landing at the end of 2026?"
  current_price: 0.27
  volume_cumulative_usd: 47047.880713
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXECONPATH-26-SOFT"
    question_raw: "State of the economy at the end of 2026?"
    current_price: 0.329
bullets:
  - "Kalshi prices a positive economy outcome at 33%, Polymarket at 27%, a 6pp gap on the same claim."
  - "Kalshi holds the higher price; Kalshi cumulative volume $9,665 vs Polymarket $47,048."
  - "Polymarket's roughly 5x greater volume makes its 27% the better-tested price; Kalshi's smaller pool may reflect audience composition skewing optimistic."
  - "Resolution depends on the specific survey or index methodology each venue uses to define 'good' or 'excellent' economic conditions at year-end 2026."
atomic_claims:
  - type: "cross_venue_spread"
    provenance: "CM cross-venue link (question_id CMX-534611296D); prices direct from venue APIs"
    field_provenance:
      kalshi_price:
        tier: "direct"
        method: "kalshi_api"
      poly_price:
        tier: "direct"
        method: "polymarket_clob_api"
      divergence_pp:
        tier: "derived"
        method: "arithmetic"
        inputs: ["kalshi_price", "poly_price"]
    liquidity_context:
      kalshi_vol_24h_usd: 0.95
      poly_vol_24h_usd: 7.14
sources:
  - label: "ClearMarket cross-venue record: State of the economy at the end of 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-soft-landing-y-2026"
    retrieved_at: "2026-10-05T07:48:26+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 6pp divergence on a macro sentiment claim with mismatched liquidity depth signals that a desk should weight Polymarket's 27% as the more credible anchor while monitoring whether Kalshi's higher read reflects a genuine information gap or simply a thinner, noisier book.
