---
signal_id: "CMSIG20261101DV00"
signal_slug: "exponent-token-event-k30-p12"
headline: "Exponent token before 2027: Kalshi 30% vs Polymarket 12%"
semantic_title: "Exponent token launch odds split sharply across venues"
telemetry: "Polymarket 12% vs Kalshi 30%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-11-01T07:50:04+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Exponent launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x411d2f1251d86d9a4f30186c660745c597d18a19737fd8f7b4ee1483ece9ffde"
  question_raw: "Will Exponent launch a token by December 31, 2026?"
  current_price: 0.12
  volume_cumulative_usd: 359387.40975200007
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-EXPO"
    question_raw: "Will Exponent launch a token before Jan 1, 2027?"
    current_price: 0.3
bullets:
  - "Kalshi prices Exponent token launch at 30%, Polymarket at 12%, an 18pp gap"
  - "Kalshi is higher; Polymarket carries the dominant liquidity at $359K vs $2.6K"
  - "Thin Kalshi volume may reflect a small, optimistic pool with low price discovery; Polymarket's deeper book likely more credible"
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
      kalshi_vol_24h_usd: 53.06
      poly_vol_24h_usd: 53.0
sources:
  - label: "ClearMarket cross-venue record: Will Exponent launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/exponent-token-event-y-2026"
    retrieved_at: "2026-11-01T07:50:04+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 18pp spread, set against a near-100-to-1 volume imbalance, strongly suggests Kalshi's 30% reflects thin-market noise rather than informed conviction, Polymarket's 12% is the more defensible anchor for any desk pricing this risk.
