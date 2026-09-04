---
signal_id: "CMSIG20260904DV01"
signal_slug: "globalfoundries-us-government-stake-k88-p93"
headline: "US gov stake in GlobalFoundries before 2027: Kalshi 88% vs Polymarket 93%"
semantic_title: "US government GlobalFoundries stake builds a premium on Polymarket"
telemetry: "Kalshi 88% vs Polymarket 93%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-09-04T12:29:39+00:00"
event_id: "CM-EVT-TDJHRGQTY1"
event_slug: "kxusacompanystake-27jan01"
event_question: "Will any part of the United States federal government take a stake of above 0% in GlobalFoundries?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXUSACOMPANYSTAKE-27JAN01-GFS"
  question_raw: "Will any part of the United States federal government take a stake of above 0% in GlobalFoundries?"
  current_price: 0.88
  volume_cumulative_usd: 29597.34
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-01T15:00:00Z"
related_markets:
  - platform: "polymarket"
    platform_market_id: "0x29de69eea09afcb0cde8301eca3e6fcabf826dcb8a8dafacc0d20f3404a735ff"
    question_raw: "Will the US federal government take a stake in GlobalFoundries Inc.?"
    current_price: 0.93
bullets:
  - "Polymarket prices the US government taking a GlobalFoundries stake at 93%; Kalshi at 88%, a 5pp gap."
  - "Polymarket is higher; Kalshi carries the larger cumulative volume, giving it the deeper liquidity base."
  - "Polymarket's thinner book may be pricing in a broader definition of 'stake,' including loan or grant instruments."
  - "Resolves YES if any federal entity acquires above 0% equity or equivalent ownership interest in GlobalFoundries before 2027."
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
      kalshi_vol_24h_usd: 1614.79
      poly_vol_24h_usd: 212.48
sources:
  - label: "ClearMarket cross-venue record: Will any part of the United States federal government take a"
    url: "https://clearmarket.fyi/compare/globalfoundries-us-government-stake-y-2026"
    retrieved_at: "2026-09-04T12:29:39+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With both venues above 85% and Kalshi holding deeper volume, the 5pp gap likely reflects definitional ambiguity around what constitutes a qualifying federal 'stake'; a desk should probe resolution criteria before leaning into the Polymarket side.
