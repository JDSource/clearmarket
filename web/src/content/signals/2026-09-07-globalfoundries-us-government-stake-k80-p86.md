---
signal_id: "CMSIG20260907DV01"
signal_slug: "globalfoundries-us-government-stake-k80-p86"
headline: "US gov stake in GlobalFoundries before 2027: Kalshi 80% vs Polymarket 86%"
semantic_title: "US government GlobalFoundries stake carries a premium on one venue"
telemetry: "Kalshi 80% vs Polymarket 86%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-09-07T13:55:09+00:00"
event_id: "CM-EVT-TDJHRGQTY1"
event_slug: "kxusacompanystake-27jan01"
event_question: "Will any part of the United States federal government take a stake of above 0% in GlobalFoundries?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXUSACOMPANYSTAKE-27JAN01-GFS"
  question_raw: "Will any part of the United States federal government take a stake of above 0% in GlobalFoundries?"
  current_price: 0.8
  volume_cumulative_usd: 27341.62
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-01T15:00:00Z"
related_markets:
  - platform: "polymarket"
    platform_market_id: "0x29de69eea09afcb0cde8301eca3e6fcabf826dcb8a8dafacc0d20f3404a735ff"
    question_raw: "Will the US federal government take a stake in GlobalFoundries Inc.?"
    current_price: 0.863
bullets:
  - "Polymarket prices the outcome at 86%, Kalshi at 80%, a 6pp gap"
  - "Polymarket is higher; Kalshi holds the larger cumulative volume, giving its 80% more weight by liquidity"
  - "Polymarket's thinner book may reflect late-breaking deal optimism not yet absorbed by Kalshi's bigger crowd"
  - "Resolves YES if any US federal entity acquires any equity stake above 0% in GlobalFoundries before 2027"
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
      kalshi_vol_24h_usd: 247.62
      poly_vol_24h_usd: 76.91
sources:
  - label: "ClearMarket cross-venue record: Will any part of the United States federal government take a"
    url: "https://clearmarket.fyi/compare/globalfoundries-us-government-stake-y-2026"
    retrieved_at: "2026-09-07T13:55:09+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With both venues above 75% and Kalshi's deeper book anchoring the lower number, a desk should treat the outcome as heavily favored but note the 6pp gap flags residual uncertainty about timing or deal structure before year-end.
