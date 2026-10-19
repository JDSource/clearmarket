---
signal_id: "CMSIG20261019DV00"
signal_slug: "exponent-token-event-k31-p11"
headline: "Exponent token before 2027: Kalshi 31% vs Polymarket 11%"
semantic_title: "Exponent token launch odds split sharply across venues"
telemetry: "Polymarket 11% vs Kalshi 31%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-19T15:15:40+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Exponent launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x411d2f1251d86d9a4f30186c660745c597d18a19737fd8f7b4ee1483ece9ffde"
  question_raw: "Will Exponent launch a token by December 31, 2026?"
  current_price: 0.11
  volume_cumulative_usd: 357236.54761700006
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-EXPO"
    question_raw: "Will Exponent launch a token before Jan 1, 2027?"
    current_price: 0.31
bullets:
  - "Kalshi prices Exponent token launch at 31%, Polymarket at 11%, a 20pp gap"
  - "Kalshi runs higher on $2K cumulative volume; Polymarket holds lower on $357K"
  - "Polymarket's deeper liquidity and larger crowd likely reflects stronger resolution-signal consensus; Kalshi's thin book may overstate probability"
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
      kalshi_vol_24h_usd: 33.5
      poly_vol_24h_usd: 263.426358
sources:
  - label: "ClearMarket cross-venue record: Will Exponent launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/exponent-token-event-y-2026"
    retrieved_at: "2026-10-19T15:15:40+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 20pp spread, flipped by a 175x liquidity imbalance favoring Polymarket, strongly suggests Kalshi's thin-volume 31% is an unreliable outlier, a desk should weight Polymarket's 11% as the more credible anchor.
