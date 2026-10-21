---
signal_id: "CMSIG20261021DV00"
signal_slug: "exponent-token-event-k28-p15"
headline: "Exponent token before 2027: Kalshi 29% vs Polymarket 15%"
semantic_title: "Exponent token launch splits sharply across venues"
telemetry: "Polymarket 15% vs Kalshi 29%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-21T13:25:45+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Exponent launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x411d2f1251d86d9a4f30186c660745c597d18a19737fd8f7b4ee1483ece9ffde"
  question_raw: "Will Exponent launch a token by December 31, 2026?"
  current_price: 0.15
  volume_cumulative_usd: 357823.21353400004
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-EXPO"
    question_raw: "Will Exponent launch a token before Jan 1, 2027?"
    current_price: 0.29
bullets:
  - "Kalshi prices the launch at 29%, Polymarket at 15%, a 14pp gap on the same claim."
  - "Kalshi is the higher venue; Polymarket carries vastly deeper liquidity on the lower side."
  - "Thin volume on Kalshi leaves it more vulnerable to noise; Polymarket's deeper book likely reflects broader informed consensus."
  - "Resolves YES if Exponent publicly launches a token before Jan 1, 2027."
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
      kalshi_vol_24h_usd: 65.75
      poly_vol_24h_usd: 586.6659169999999
sources:
  - label: "ClearMarket cross-venue record: Will Exponent launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/exponent-token-event-y-2026"
    retrieved_at: "2026-10-21T13:25:45+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 14pp spread on a sub-ten-week horizon suggests Kalshi's price is unreliable due to minimal activity, Polymarket's deeper book at 15% is the more defensible anchor for any desk sizing a position.
