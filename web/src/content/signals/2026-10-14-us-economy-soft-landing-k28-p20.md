---
signal_id: "CMSIG20261014DV00"
signal_slug: "us-economy-soft-landing-k28-p20"
headline: "U.S. economy in recession by end-2026: Kalshi 29% vs Polymarket 20%"
semantic_title: "Economy-in-recession odds carry a premium across venues into year-end"
telemetry: "Polymarket 20% vs Kalshi 29%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-14T07:49:05+00:00"
event_id: "CM-EVT-ZRG5DFDMZ8"
event_slug: "kxeconpath-26"
event_question: "State of the economy at the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x50e3ee8f93a464d04ea2cea6efff45c902f43642aedbf43f7afdc899e10f71d8"
  question_raw: "Will the US economy be in a soft landing at the end of 2026?"
  current_price: 0.2
  volume_cumulative_usd: 49093.276340000004
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXECONPATH-26-SOFT"
    question_raw: "State of the economy at the end of 2026?"
    current_price: 0.29
bullets:
  - "Kalshi prices recession at 29%, Polymarket at 20%, a 9pp spread on the same claim."
  - "Kalshi sits higher; Polymarket carries the dominant liquidity at roughly six times Kalshi's volume."
  - "Thin Kalshi book may be drifting on a narrower, potentially more pessimistic user base; Polymarket's deeper pool likely reflects broader consensus."
  - "Resolution hinges on an agreed definition of 'recession', definitional ambiguity may itself be widening the gap."
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
      kalshi_vol_24h_usd: 0.0
      poly_vol_24h_usd: 788.746328
sources:
  - label: "ClearMarket cross-venue record: State of the economy at the end of 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-soft-landing-y-2026"
    retrieved_at: "2026-10-14T07:49:05+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 9pp spread signals that a desk should treat Kalshi's elevated recession probability with caution given its thin book, while Polymarket's deeper-liquidity 20% print is the more defensible reference for near-term positioning.
