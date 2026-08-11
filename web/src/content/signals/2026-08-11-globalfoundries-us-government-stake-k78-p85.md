---
signal_id: "CMSIG20260811DV00"
signal_slug: "globalfoundries-us-government-stake-k78-p85"
headline: "US gov't stake in GlobalFoundries before 2027: Kalshi 78% vs Polymarket 85%"
semantic_title: "US federal stake in GlobalFoundries splits across venues"
telemetry: "Kalshi 78% vs Polymarket 85%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-08-11T08:50:46+00:00"
event_id: "CM-EVT-TDJHRGQTY1"
event_slug: "kxusacompanystake-27jan01"
event_question: "Will any part of the United States federal government take a stake of above 0% in GlobalFoundries?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXUSACOMPANYSTAKE-27JAN01-GFS"
  question_raw: "Will any part of the United States federal government take a stake of above 0% in GlobalFoundries?"
  current_price: 0.78
  volume_cumulative_usd: 21481.77
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-01T15:00:00Z"
related_markets:
  - platform: "polymarket"
    platform_market_id: "0x29de69eea09afcb0cde8301eca3e6fcabf826dcb8a8dafacc0d20f3404a735ff"
    question_raw: "Will the US federal government take a stake in GlobalFoundries Inc.?"
    current_price: 0.852
bullets:
  - "Kalshi prices the claim at 78%; Polymarket at 85%, a 7pp spread on the same resolution trigger."
  - "Polymarket is higher at 85% on $5,872 cumulative volume; Kalshi lower at 78% on $21,482."
  - "Thin Polymarket liquidity may inflate its price; Kalshi's deeper pool likely reflects steadier consensus."
  - "Resolution hinges on any formal equity stake above 0% by any federal entity before Jan 1, 2027."
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
      kalshi_vol_24h_usd: 170.31
      poly_vol_24h_usd: 0.0
sources:
  - label: "ClearMarket cross-venue record: Will any part of the United States federal government take a"
    url: "https://clearmarket.fyi/compare/globalfoundries-us-government-stake-y-2026"
    retrieved_at: "2026-08-11T08:50:46+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 7pp gap, with Polymarket higher on far less volume, suggests the lower-liquidity venue is running hot, a desk leaning on Kalshi's deeper book as the more reliable signal here.
