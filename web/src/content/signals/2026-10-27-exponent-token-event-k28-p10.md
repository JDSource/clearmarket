---
signal_id: "CMSIG20261027DV00"
signal_slug: "exponent-token-event-k28-p10"
headline: "Exponent token before 2027: Kalshi 29% vs Polymarket 10%"
semantic_title: "Exponent token launch trades far apart across venues"
telemetry: "Polymarket 10% vs Kalshi 29%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-27T07:49:44+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Exponent launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x411d2f1251d86d9a4f30186c660745c597d18a19737fd8f7b4ee1483ece9ffde"
  question_raw: "Will Exponent launch a token by December 31, 2026?"
  current_price: 0.1
  volume_cumulative_usd: 359334.4097520001
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-EXPO"
    question_raw: "Will Exponent launch a token before Jan 1, 2027?"
    current_price: 0.29
bullets:
  - "Kalshi prices Exponent token launch at 29%, Polymarket at 10%, a 19pp gap"
  - "Kalshi sits higher with $2,316 cumulative volume; Polymarket carries $359,334, far deeper"
  - "Thin Kalshi liquidity likely inflates its price; Polymarket's deeper book is the more credible signal"
  - "Resolves YES if Exponent publicly launches a token before Jan 1, 2027"
atomic_claims:
  - type: "cross_venue_spread"
    provenance: "CM cross-venue link (question_id CMX-B8681B67DA); prices direct from venue APIs"
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
      kalshi_vol_24h_usd: 24.13
      poly_vol_24h_usd: 12.0
sources:
  - label: "ClearMarket cross-venue record: Will Exponent launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/exponent-token-event-y-2026"
    retrieved_at: "2026-10-27T07:49:44+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 19pp spread almost certainly reflects Kalshi's shallow liquidity rather than genuine information, making Polymarket's 10% the more reliable reference for a desk pricing this outcome.
