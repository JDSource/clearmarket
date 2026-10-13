---
signal_id: "CMSIG20261013DV02"
signal_slug: "us-economy-soft-landing-k28-p23"
headline: "U.S. economy 'good' at end of 2026: Kalshi 29% vs Polymarket 23%"
semantic_title: "U.S. economy end-of-2026 outlook carries a premium on one venue"
telemetry: "Polymarket 23% vs Kalshi 29%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-13T15:33:55+00:00"
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
  - "Kalshi prices a positive economic outcome at 29%, Polymarket at 23%, a 6pp divergence on the same year-end claim."
  - "Kalshi is the higher-priced venue; Polymarket leads on liquidity with $48K vs Kalshi's $8K cumulative volume."
  - "Kalshi's higher read may reflect a more optimistic user base or looser resolution framing; Polymarket's definition of 'good' may be more stringent."
  - "Resolution hinges on how each platform operationalizes the economy's state, differing source criteria could independently justify the spread."
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
      kalshi_vol_24h_usd: 11.6
      poly_vol_24h_usd: 100.73
sources:
  - label: "ClearMarket cross-venue record: State of the economy at the end of 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-soft-landing-y-2026"
    retrieved_at: "2026-10-13T15:33:55+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

This divergence is notable because resolution-definition ambiguity, not just liquidity imbalance, is a credible driver of the 6pp gap, meaning a desk should closely compare each platform's stated resolution criteria before treating either price as the cleaner signal.
