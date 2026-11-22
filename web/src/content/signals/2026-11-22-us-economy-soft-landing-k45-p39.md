---
signal_id: "CMSIG20261122DV01"
signal_slug: "us-economy-soft-landing-k45-p39"
headline: "Economy 'good' end-2026: Kalshi 46% vs Polymarket 40%"
semantic_title: "U.S. economy end-2026 outlook trades higher on Kalshi"
telemetry: "Polymarket 40% vs Kalshi 46%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-11-22T07:48:35+00:00"
event_id: "CM-EVT-ZRG5DFDMZ8"
event_slug: "kxeconpath-26"
event_question: "State of the economy at the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x50e3ee8f93a464d04ea2cea6efff45c902f43642aedbf43f7afdc899e10f71d8"
  question_raw: "Will the US economy be in a soft landing at the end of 2026?"
  current_price: 0.396
  volume_cumulative_usd: 66351.80522100002
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXECONPATH-26-SOFT"
    question_raw: "State of the economy at the end of 2026?"
    current_price: 0.459
bullets:
  - "Kalshi prices a positive economic outcome at 46%, Polymarket at 40%, a 6pp spread into year-end."
  - "Kalshi is the higher-side venue; Polymarket holds roughly twice the cumulative volume."
  - "The gap may reflect differing resolution criteria or question wording between platforms, not pure sentiment divergence."
  - "Resolves on an assessment of U.S. economic conditions at end of 2026; exact resolver and rubric vary by venue."
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
      kalshi_vol_24h_usd: 4.82
      poly_vol_24h_usd: 0.0
sources:
  - label: "ClearMarket cross-venue record: State of the economy at the end of 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-soft-landing-y-2026"
    retrieved_at: "2026-11-22T07:48:35+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 6pp divergence on a macro-sentiment contract with moderate volume on both sides points to ambiguous resolution language as the likely culprit, desks should map each platform's exact resolver before treating the spread as tradeable.
