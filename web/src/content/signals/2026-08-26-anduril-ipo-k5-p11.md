---
signal_id: "CMSIG20260826DV03"
signal_slug: "anduril-ipo-k5-p11"
headline: "Anduril IPO before 2027: Kalshi 5% vs Polymarket 11%"
semantic_title: "Anduril IPO before 2027 trades far apart on the major desks"
telemetry: "Polymarket 11% vs Kalshi 5%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-08-26T08:38:56+00:00"
event_id: "CM-EVT-858NYLKF97"
event_slug: "kxipo-26"
event_question: "Anduril IPO before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xb7a72d5e5e4ad1dd7664fec7b7c3031a66d149d186e9c5180351780eb1323566"
  question_raw: "Anduril IPO before 2027?"
  current_price: 0.11
  volume_cumulative_usd: 356897.763034
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXIPO-26-ANDURIL"
    question_raw: "Who will IPO before 2027?"
    current_price: 0.05
bullets:
  - "Polymarket prices an Anduril IPO this year at 11%, Kalshi at just 5%, a 6pp gap on a low-probability claim."
  - "Polymarket is the higher side with roughly twenty-eight times Kalshi's cumulative volume."
  - "On a tail-probability claim this small, a 6pp gap is proportionally large, Kalshi's thin liquidity may be compressing the price toward zero artificially."
  - "Resolution requires a confirmed public listing or IPO completion by Anduril before January 1, 2027."
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
      kalshi_vol_24h_usd: 6.44
      poly_vol_24h_usd: 265.93695
sources:
  - label: "ClearMarket cross-venue record: Anduril IPO before 2027?"
    url: "https://clearmarket.fyi/compare/anduril-ipo-y-2026"
    retrieved_at: "2026-08-26T08:38:56+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 6pp divergence at the low-single-digit probability range is proportionally extreme, suggesting Kalshi's shallow order book is distorting the price downward, desks should treat Polymarket's 11% as the more reliable anchor.
