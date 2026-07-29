---
signal_id: "CMSIG20260729DV00"
signal_slug: "arc-token-event-k60-p37"
headline: "Arc token launch before 2027: Kalshi 60% vs Polymarket 37%"
semantic_title: "Arc token-launch odds split sharply across venues"
telemetry: "Polymarket 37% vs Kalshi 60%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-07-29T10:36:27+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.37
  volume_cumulative_usd: 100909.80118900012
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.6
bullets:
  - "Kalshi prices Arc token launch at 60%, Polymarket at 37%, a 23pp gap."
  - "Kalshi sits higher; Polymarket carries the deeper book with cumulative volume roughly 26x larger."
  - "Thin Kalshi liquidity may let a small number of trades push odds well above the better-informed Polymarket consensus."
  - "Resolves YES if Arc publicly launches a token before Jan 1, 2027; no launch = NO."
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
      kalshi_vol_24h_usd: 6.52
      poly_vol_24h_usd: 2397.5099999999998
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-07-29T10:36:27+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 23pp spread, combined with a lopsided liquidity ratio, suggests Kalshi's higher print reflects a thin, potentially mispriced market rather than genuine informational disagreement, a desk should weight Polymarket's 37% as the more reliable anchor.
