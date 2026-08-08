---
signal_id: "CMSIG20260808DV03"
signal_slug: "globalfoundries-us-government-stake-k80-p85"
headline: "U.S. govt stake in GlobalFoundries: Kalshi 80% vs Polymarket 85%"
semantic_title: "GlobalFoundries stake odds stay near 25% short across venues"
telemetry: "Kalshi 80% vs Polymarket 85%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-08-08T08:36:39+00:00"
event_id: "CM-EVT-TDJHRGQTY1"
event_slug: "kxusacompanystake-27jan01"
event_question: "Will any part of the United States federal government take a stake of above 0% in GlobalFoundries?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXUSACOMPANYSTAKE-27JAN01-GFS"
  question_raw: "Will any part of the United States federal government take a stake of above 0% in GlobalFoundries?"
  current_price: 0.8
  volume_cumulative_usd: 21823.65
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-01T15:00:00Z"
related_markets:
  - platform: "polymarket"
    platform_market_id: "0x29de69eea09afcb0cde8301eca3e6fcabf826dcb8a8dafacc0d20f3404a735ff"
    question_raw: "Will the US federal government take a stake in GlobalFoundries Inc.?"
    current_price: 0.852
bullets:
  - "Kalshi prices a government stake above 0% at 80%, Polymarket at 85%, a 5pp gap at high probability"
  - "Polymarket is higher; Kalshi holds roughly 3.7x more cumulative volume, giving it stronger liquidity backing"
  - "At these elevated levels, the spread is narrow; Kalshi's deeper book may reflect more conservative pricing of remaining legal or procedural risk"
  - "Resolves YES on any confirmed federal government acquisition of any equity stake, however small, in GlobalFoundries"
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
      kalshi_vol_24h_usd: 3.78
      poly_vol_24h_usd: 0.0
sources:
  - label: "ClearMarket cross-venue record: Will any part of the United States federal government take a"
    url: "https://clearmarket.fyi/compare/globalfoundries-us-government-stake-y-2026"
    retrieved_at: "2026-08-08T08:36:39+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Both venues are pricing this as a high-probability near-certainty, and the 5pp gap is modest at these levels, a desk should focus on the residual tail risk and resolution mechanics rather than the spread itself.
