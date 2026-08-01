---
signal_id: "CMSIG20260801DV03"
signal_slug: "us-economy-soft-landing-k61-p56"
headline: "US economy 'moderate growth' end-2026: Kalshi 62% vs Polymarket 56%"
semantic_title: "Moderate-growth economy call stays split across the major desks"
telemetry: "Polymarket 56% vs Kalshi 62%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-08-01T09:56:15+00:00"
event_id: "CM-EVT-ZRG5DFDMZ8"
event_slug: "kxeconpath-26"
event_question: "State of the economy at the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x50e3ee8f93a464d04ea2cea6efff45c902f43642aedbf43f7afdc899e10f71d8"
  question_raw: "Will the US economy be in a soft landing at the end of 2026?"
  current_price: 0.56
  volume_cumulative_usd: 29795.856674000002
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXECONPATH-26-SOFT"
    question_raw: "State of the economy at the end of 2026?"
    current_price: 0.615
bullets:
  - "Kalshi prices moderate-growth outcome at 62%, Polymarket at 56%, a 5pp spread"
  - "Kalshi higher on ~$11K volume; Polymarket deeper at ~$30K, nearly 3x more liquid"
  - "Polymarket's lower price on the modal outcome may reflect broader outcome-bracket competition within its market"
  - "Resolution depends on how each venue defines 'moderate growth' versus adjacent economic-state buckets"
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
      kalshi_vol_24h_usd: 0.96
      poly_vol_24h_usd: 206.8
sources:
  - label: "ClearMarket cross-venue record: State of the economy at the end of 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-soft-landing-y-2026"
    retrieved_at: "2026-08-01T09:56:15+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 5pp split on the highest-probability outcome bucket signals that outcome-category definitions differ across venues, and a desk should map each contract's resolution criteria before treating this as a clean arbitrage.
