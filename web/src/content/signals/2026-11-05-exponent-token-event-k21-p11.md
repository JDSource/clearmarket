---
signal_id: "CMSIG20261105DV00"
signal_slug: "exponent-token-event-k21-p11"
headline: "Exponent token before Jan 1 2027: Kalshi 21% vs Polymarket 11%"
semantic_title: "Exponent token launch odds split sharply across venues"
telemetry: "Polymarket 11% vs Kalshi 21%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-11-05T16:03:50+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Exponent launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x411d2f1251d86d9a4f30186c660745c597d18a19737fd8f7b4ee1483ece9ffde"
  question_raw: "Will Exponent launch a token by December 31, 2026?"
  current_price: 0.11
  volume_cumulative_usd: 360124.339752
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-EXPO"
    question_raw: "Will Exponent launch a token before Jan 1, 2027?"
    current_price: 0.21
bullets:
  - "Kalshi prices the launch at 21%, nearly double Polymarket's 11%, a 10pp gap with under two months to resolution."
  - "Kalshi carries the higher odds on thin cumulative volume; Polymarket holds the lower price with far deeper liquidity."
  - "Polymarket's larger crowd likely reflects broader market awareness of Exponent's public roadmap; Kalshi's thin book may be driven by fewer, less-informed positions."
  - "Resolution hinges on a verifiable public token launch by Exponent before Jan 1, 2027, a binary, date-bound trigger."
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
      kalshi_vol_24h_usd: 43.13
      poly_vol_24h_usd: 0.0
sources:
  - label: "ClearMarket cross-venue record: Will Exponent launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/exponent-token-event-y-2026"
    retrieved_at: "2026-11-05T16:03:50+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The wide gap and extreme volume asymmetry suggest Kalshi's elevated odds are unreliable signal, a desk would lean on Polymarket's deeper-liquidity 11% as the more credible fair-value anchor with roughly eight weeks left on the clock.
