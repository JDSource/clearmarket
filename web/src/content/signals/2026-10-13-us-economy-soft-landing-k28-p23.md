---
signal_id: "CMSIG20261013DV02"
signal_slug: "us-economy-soft-landing-k28-p23"
headline: "U.S. economy in recession end-2026: Kalshi 29% vs Polymarket 23%"
semantic_title: "Economy-in-recession odds stay apart across venues"
telemetry: "Polymarket 23% vs Kalshi 29%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-13T07:49:40+00:00"
event_id: "CM-EVT-ZRG5DFDMZ8"
event_slug: "kxeconpath-26"
event_question: "State of the economy at the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x50e3ee8f93a464d04ea2cea6efff45c902f43642aedbf43f7afdc899e10f71d8"
  question_raw: "Will the US economy be in a soft landing at the end of 2026?"
  current_price: 0.23
  volume_cumulative_usd: 48304.530012
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXECONPATH-26-SOFT"
    question_raw: "State of the economy at the end of 2026?"
    current_price: 0.29
bullets:
  - "Kalshi prices a recessionary economy at end of 2026 at 29%; Polymarket prices it at 23%, a 6pp gap."
  - "Kalshi is higher on roughly $8.6K volume; Polymarket's lower price is backed by approximately $48K in cumulative volume."
  - "Resolution ambiguity may explain part of the gap, the two venues may use different economic indicators or definition thresholds to judge 'state of economy.'"
  - "Resolves based on official or designated economic condition readings at or before end of 2026."
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
      kalshi_vol_24h_usd: 31.04
      poly_vol_24h_usd: 929.038483
sources:
  - label: "ClearMarket cross-venue record: State of the economy at the end of 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-soft-landing-y-2026"
    retrieved_at: "2026-10-13T07:49:40+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 6pp divergence on a macro claim with differing resolution criteria across venues means a desk should scrutinize each contract's exact resolution rules before treating the spread as a clean arbitrage opportunity.
