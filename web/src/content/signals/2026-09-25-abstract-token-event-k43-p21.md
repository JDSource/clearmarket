---
signal_id: "CMSIG20260925DV00"
signal_slug: "abstract-token-event-k43-p21"
headline: "Abstract token before 2027: Kalshi 43% vs Polymarket 21%"
semantic_title: "Abstract token launch odds split sharply across venues"
telemetry: "Polymarket 21% vs Kalshi 43%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-09-25T13:14:13+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Abstract launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xd008c45c5320e7453b4e7725bda285cd822a3a61adef14759f2aadf0778c64b6"
  question_raw: "Will Abstract launch a token by December 31, 2026"
  current_price: 0.21
  volume_cumulative_usd: 377366.03204799996
  arbitration_model: "uma_oracle"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ABST"
    question_raw: "Will Abstract launch a token before Jan 1, 2027?"
    current_price: 0.43
bullets:
  - "Kalshi prices the launch at 43%, Polymarket at 21%, a 22pp gap with roughly three months left on the clock."
  - "Kalshi sits higher; Polymarket carries the dominant liquidity at over $377K cumulative volume versus Kalshi's $2.5K."
  - "Thin Kalshi volume makes its 43% read fragile, the Polymarket price, backed by far deeper participation, likely reflects broader consensus."
  - "Resolves YES if Abstract publicly launches a native token before Jan 1, 2027."
atomic_claims:
  - type: "cross_venue_spread"
    provenance: "CM cross-venue link (question_id CMX-3E5461019B); prices direct from venue APIs"
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
      kalshi_vol_24h_usd: 6.58
      poly_vol_24h_usd: 50.17
sources:
  - label: "ClearMarket cross-venue record: Will Abstract launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/abstract-token-event-y-2026"
    retrieved_at: "2026-09-25T13:14:13+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 22pp gap is almost certainly a Kalshi liquidity artifact, with under $2.5K traded there, a handful of contracts can skew the price materially, while Polymarket's deep book at 21% is the more credible signal for a desk sizing a position.
