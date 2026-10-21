---
signal_id: "CMSIG20261021DV00"
signal_slug: "arc-token-event-k14-p9"
headline: "Arc token before Jan 1 2027: Kalshi 14% vs Polymarket 9%"
semantic_title: "Arc token launch odds run higher on one venue"
telemetry: "Polymarket 9% vs Kalshi 14%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-21T07:49:13+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.09
  volume_cumulative_usd: 184489.53965199998
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.14
bullets:
  - "Kalshi prices Arc token launch at 14%, Polymarket at 9%, a 5pp gap with under 10 weeks left."
  - "Kalshi is higher; Polymarket carries the deeper book at $184K cumulative volume vs Kalshi's $3K."
  - "Thin Kalshi liquidity makes its 14% print fragile, the well-traded Polymarket line likely reflects broader informed consensus."
  - "Resolution hinges on a publicly announced Arc token launch before January 1, 2027."
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
      kalshi_vol_24h_usd: 0.0
      poly_vol_24h_usd: 4379.888889
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-10-21T07:49:13+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With Polymarket holding 98% of the combined volume, its 9% print is the more reliable anchor, and the Kalshi premium likely reflects thin-market noise rather than a genuine information edge.
