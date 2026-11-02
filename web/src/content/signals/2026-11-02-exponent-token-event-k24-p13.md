---
signal_id: "CMSIG20261102DV00"
signal_slug: "exponent-token-event-k24-p13"
headline: "Exponent token launch before 2027: Kalshi 24% vs Polymarket 13%"
semantic_title: "Exponent token-before-2027 pricing splits sharply across venues"
telemetry: "Polymarket 13% vs Kalshi 24%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-11-02T17:46:21+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Exponent launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x411d2f1251d86d9a4f30186c660745c597d18a19737fd8f7b4ee1483ece9ffde"
  question_raw: "Will Exponent launch a token by December 31, 2026?"
  current_price: 0.13
  volume_cumulative_usd: 359883.33975200006
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-EXPO"
    question_raw: "Will Exponent launch a token before Jan 1, 2027?"
    current_price: 0.24
bullets:
  - "Kalshi prices the launch at 24%, Polymarket at 13%, an 11pp gap with under two months to resolution."
  - "Kalshi is higher; liquidity heavily skewed to Polymarket, which carries the dominant volume."
  - "Thin Kalshi volume may reflect a small, less-informed pool; Polymarket's deeper market likely provides the sharper signal."
  - "Resolves YES only if Exponent publicly launches a token before Jan 1, 2027."
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
      kalshi_vol_24h_usd: 70.43
      poly_vol_24h_usd: 484.93
sources:
  - label: "ClearMarket cross-venue record: Will Exponent launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/exponent-token-event-y-2026"
    retrieved_at: "2026-11-02T17:46:21+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 11pp spread on a near-term binary with heavy Polymarket volume suggests Kalshi's price is unreliable noise, a desk should weight the Polymarket read and flag potential arb given low Kalshi transaction costs.
