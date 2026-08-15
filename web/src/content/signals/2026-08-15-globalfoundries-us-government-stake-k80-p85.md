---
signal_id: "CMSIG20260815DV05"
signal_slug: "globalfoundries-us-government-stake-k80-p85"
headline: "U.S. gov stake in GlobalFoundries: Kalshi 80% vs Polymarket 85%"
semantic_title: "U.S. stake in GlobalFoundries stays near 75% but builds higher on one venue"
telemetry: "Kalshi 80% vs Polymarket 85%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-08-15T08:23:11+00:00"
event_id: "CM-EVT-TDJHRGQTY1"
event_slug: "kxusacompanystake-27jan01"
event_question: "Will any part of the United States federal government take a stake of above 0% in GlobalFoundries?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXUSACOMPANYSTAKE-27JAN01-GFS"
  question_raw: "Will any part of the United States federal government take a stake of above 0% in GlobalFoundries?"
  current_price: 0.8
  volume_cumulative_usd: 22545.38
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-01T15:00:00Z"
related_markets:
  - platform: "polymarket"
    platform_market_id: "0x29de69eea09afcb0cde8301eca3e6fcabf826dcb8a8dafacc0d20f3404a735ff"
    question_raw: "Will the US federal government take a stake in GlobalFoundries Inc.?"
    current_price: 0.851
bullets:
  - "Polymarket prices U.S. government equity stake in GlobalFoundries at 85%; Kalshi at 80%, a 5pp gap."
  - "Polymarket is the higher venue; Kalshi volume is $22.5K vs Polymarket's $6.1K, Kalshi has the larger book here."
  - "With Kalshi holding the deeper book and lower price, Polymarket's thin market may be nudging the odds upward."
  - "Resolves YES if any U.S. federal entity acquires above 0% equity in GlobalFoundries before 2027."
atomic_claims:
  - type: "cross_venue_spread"
    provenance: "CM cross-venue link (question_id CMX-64E6FFD2DB); prices direct from venue APIs"
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
      kalshi_vol_24h_usd: 343.2
      poly_vol_24h_usd: 229.0
sources:
  - label: "ClearMarket cross-venue record: Will any part of the United States federal government take a"
    url: "https://clearmarket.fyi/compare/globalfoundries-us-government-stake-y-2026"
    retrieved_at: "2026-08-15T08:23:11+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The volume dynamic inverts here, Kalshi's larger book prices the claim lower, suggesting Polymarket's 85% reflects a thinner, potentially less tested crowd, and desks may prefer Kalshi's 80% as the better-supported read.
