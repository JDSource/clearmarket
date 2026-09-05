---
signal_id: "CMSIG20260905DV01"
signal_slug: "globalfoundries-us-government-stake-k84-p93"
headline: "US govt stake in GlobalFoundries: Kalshi 84% vs Polymarket 93%"
semantic_title: "US federal stake in GlobalFoundries carries a premium on one venue"
telemetry: "Kalshi 84% vs Polymarket 93%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-09-05T11:35:42+00:00"
event_id: "CM-EVT-TDJHRGQTY1"
event_slug: "kxusacompanystake-27jan01"
event_question: "Will any part of the United States federal government take a stake of above 0% in GlobalFoundries?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXUSACOMPANYSTAKE-27JAN01-GFS"
  question_raw: "Will any part of the United States federal government take a stake of above 0% in GlobalFoundries?"
  current_price: 0.84
  volume_cumulative_usd: 28319.21
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-01T15:00:00Z"
related_markets:
  - platform: "polymarket"
    platform_market_id: "0x29de69eea09afcb0cde8301eca3e6fcabf826dcb8a8dafacc0d20f3404a735ff"
    question_raw: "Will the US federal government take a stake in GlobalFoundries Inc.?"
    current_price: 0.93
bullets:
  - "Polymarket prices 93%, Kalshi 84%, a 9pp spread on an already high-probability claim."
  - "Kalshi holds the lower price with $28,319 volume; Polymarket higher with $7,535."
  - "Kalshi's larger, more liquid book pricing lower may reflect stricter read of 'above 0% stake' resolution language."
  - "Resolves YES if any US federal entity acquires any ownership stake in GlobalFoundries before 2027."
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
      kalshi_vol_24h_usd: 67.2
      poly_vol_24h_usd: 80.0
sources:
  - label: "ClearMarket cross-venue record: Will any part of the United States federal government take a"
    url: "https://clearmarket.fyi/compare/globalfoundries-us-government-stake-y-2026"
    retrieved_at: "2026-09-05T11:35:42+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With both venues above 80% but 9pp apart, the divergence likely turns on resolution-language interpretation, a desk should scrutinize the exact contract definitions before assuming the gap represents a clean arbitrage.
