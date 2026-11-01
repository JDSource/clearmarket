---
signal_id: "CMSIG20261101DV00"
signal_slug: "exponent-token-event-k28-p14"
headline: "Exponent token launch before 2027: Kalshi 28% vs Polymarket 14%"
semantic_title: "Exponent token-before-2027 trades far apart across venues"
telemetry: "Polymarket 14% vs Kalshi 28%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-11-01T14:44:10+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Exponent launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x411d2f1251d86d9a4f30186c660745c597d18a19737fd8f7b4ee1483ece9ffde"
  question_raw: "Will Exponent launch a token by December 31, 2026?"
  current_price: 0.14
  volume_cumulative_usd: 359398.40975200007
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-EXPO"
    question_raw: "Will Exponent launch a token before Jan 1, 2027?"
    current_price: 0.28
bullets:
  - "Kalshi prices Exponent token launch at 28%, Polymarket at 14%, a 14pp gap"
  - "Kalshi is the higher-priced venue; Polymarket carries the dominant liquidity at $359K cumulative vs $2.5K on Kalshi"
  - "Thin Kalshi volume likely distorts its price upward; Polymarket's deep book makes its 14% the more liquid-backed signal"
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
      kalshi_vol_24h_usd: 54.14
      poly_vol_24h_usd: 64.0
sources:
  - label: "ClearMarket cross-venue record: Will Exponent launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/exponent-token-event-y-2026"
    retrieved_at: "2026-11-01T14:44:10+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 14pp spread almost certainly reflects a liquidity imbalance rather than genuine information, Polymarket's price at $359K in volume is the more credible anchor, and a desk should treat Kalshi's 28% as noise from a thin book.
