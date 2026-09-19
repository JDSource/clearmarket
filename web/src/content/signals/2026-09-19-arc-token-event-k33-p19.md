---
signal_id: "CMSIG20260919DV00"
signal_slug: "arc-token-event-k33-p19"
headline: "Will Arc launch a token before 2027? Kalshi 33% vs Polymarket 19%"
semantic_title: "Arc token launch before 2027 splits sharply across venues"
telemetry: "Polymarket 19% vs Kalshi 33%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-09-19T07:48:36+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.19
  volume_cumulative_usd: 162157.66180799998
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.33
bullets:
  - "Kalshi prices the Arc token launch at 33%, Polymarket at 19%, a 14pp gap."
  - "Kalshi is the higher-conviction venue; Polymarket carries far deeper liquidity at over $162K traded vs Kalshi's $5K."
  - "Thin Kalshi volume likely amplifies the spread, Polymarket's larger pool suggests its 19% is the better-anchored price."
  - "Resolves YES if Arc publicly launches a token before January 1, 2027."
atomic_claims:
  - type: "cross_venue_spread"
    provenance: "CM cross-venue link (question_id CMX-F36B8880EB); prices direct from venue APIs"
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
      kalshi_vol_24h_usd: 11.64
      poly_vol_24h_usd: 645.1363529999999
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-09-19T07:48:36+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 14pp gap with a 32x liquidity imbalance signals Kalshi's higher price is likely a thin-market artifact; Polymarket's 19% is the more defensible reference for any desk sizing a position.
