---
signal_id: "CMSIG20260815DV04"
signal_slug: "us-economy-soft-landing-k59-p53"
headline: "U.S. economy strong at end of 2026: Kalshi 59% vs Polymarket 53%"
semantic_title: "U.S. economy outlook at year-end holds apart across venues"
telemetry: "Polymarket 53% vs Kalshi 59%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-08-15T08:23:11+00:00"
event_id: "CM-EVT-ZRG5DFDMZ8"
event_slug: "kxeconpath-26"
event_question: "State of the economy at the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x50e3ee8f93a464d04ea2cea6efff45c902f43642aedbf43f7afdc899e10f71d8"
  question_raw: "Will the US economy be in a soft landing at the end of 2026?"
  current_price: 0.53
  volume_cumulative_usd: 30768.274219
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXECONPATH-26-SOFT"
    question_raw: "State of the economy at the end of 2026?"
    current_price: 0.591
bullets:
  - "Kalshi puts the odds of a strong economy at year-end at 59%; Polymarket at 53%, a 6pp gap."
  - "Kalshi is the higher venue; volume is $12.6K on Kalshi and $30.8K on Polymarket."
  - "The 6pp spread near the 50% threshold is meaningful; resolution criteria may differ slightly between venues."
  - "Resolves based on defined economic indicators or official designations at end of 2026."
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
      kalshi_vol_24h_usd: 977.99
      poly_vol_24h_usd: 4.99
sources:
  - label: "ClearMarket cross-venue record: State of the economy at the end of 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-soft-landing-y-2026"
    retrieved_at: "2026-08-15T08:23:11+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 6pp split straddling the midpoint on a macro claim is material for a desk, the divergence may reflect different resolution oracles between platforms, worth confirming before taking a position.
