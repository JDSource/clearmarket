---
signal_id: "CMSIG20260809DV03"
signal_slug: "anduril-ipo-k4-p10"
headline: "Anduril IPO before 2027: Kalshi 4% vs Polymarket 10%"
semantic_title: "Anduril IPO long odds trade further apart on the major desks"
telemetry: "Polymarket 10% vs Kalshi 4%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-08-09T08:38:03+00:00"
event_id: "CM-EVT-858NYLKF97"
event_slug: "kxipo-26"
event_question: "Anduril IPO before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xb7a72d5e5e4ad1dd7664fec7b7c3031a66d149d186e9c5180351780eb1323566"
  question_raw: "Anduril IPO before 2027?"
  current_price: 0.1
  volume_cumulative_usd: 356344.2860840002
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXIPO-26-ANDURIL"
    question_raw: "Who will IPO before 2027?"
    current_price: 0.04
bullets:
  - "Polymarket puts Anduril IPO odds at 10%, Kalshi at 4%, a 6pp gap on low base rates"
  - "Polymarket is the higher venue; volume is $356K vs $10K, roughly 35x deeper"
  - "At single-digit probabilities, a 6pp gap is proportionally large; Polymarket's liquidity depth makes it the stronger reference"
  - "Resolves YES on a completed Anduril IPO before Jan 1, 2027"
atomic_claims:
  - type: "cross_venue_spread"
    provenance: "CM cross-venue link (question_id CMX-D39E0284B8); prices direct from venue APIs"
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
      kalshi_vol_24h_usd: 4.88
      poly_vol_24h_usd: 0.0
sources:
  - label: "ClearMarket cross-venue record: Anduril IPO before 2027?"
    url: "https://clearmarket.fyi/compare/anduril-ipo-y-2026"
    retrieved_at: "2026-08-09T08:38:03+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 6pp gap between 4% and 10% is a 2.5x relative difference, material at low probabilities, but the lopsided liquidity means Polymarket's 10% is the market price of record, and Kalshi's 4% likely reflects an undertraded contract.
