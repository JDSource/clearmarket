---
signal_id: "CMSIG20261029DV00"
signal_slug: "exponent-token-event-k24-p10"
headline: "Exponent token before 2027: Kalshi 24% vs Polymarket 10%"
semantic_title: "Exponent token launch odds split sharply across venues"
telemetry: "Polymarket 10% vs Kalshi 24%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-29T07:49:05+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Exponent launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x411d2f1251d86d9a4f30186c660745c597d18a19737fd8f7b4ee1483ece9ffde"
  question_raw: "Will Exponent launch a token by December 31, 2026?"
  current_price: 0.1
  volume_cumulative_usd: 359334.40975200007
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-EXPO"
    question_raw: "Will Exponent launch a token before Jan 1, 2027?"
    current_price: 0.24
bullets:
  - "Kalshi prices the launch at 24%, Polymarket at 10%, a 14pp gap with under nine weeks to resolution."
  - "Kalshi is the higher-priced venue; Polymarket carries the overwhelming share of liquidity at over $359K cumulative volume versus roughly $2K on Kalshi."
  - "Polymarket's deep book is the stronger price signal here; Kalshi's elevated print likely reflects a thin, easily skewed market rather than genuine informed conviction."
  - "Resolution mechanic: a confirmed on-chain Exponent token deployment before Jan 1, 2027 settles YES on both contracts."
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
      kalshi_vol_24h_usd: 16.63
      poly_vol_24h_usd: 0.0
sources:
  - label: "ClearMarket cross-venue record: Will Exponent launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/exponent-token-event-y-2026"
    retrieved_at: "2026-10-29T07:49:05+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With Polymarket holding more than 99% of combined volume, its 10% print should be treated as the reference price; the Kalshi 24% reads as noise from an illiquid contract and offers a theoretical but execution-constrained arbitrage for any desk able to operate on both venues.
