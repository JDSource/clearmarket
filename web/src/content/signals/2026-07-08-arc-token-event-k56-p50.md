---
signal_id: "CMSIG20260708DV03"
signal_slug: "arc-token-event-k56-p50"
headline: "Arc token launch before Jan 1, 2027: Kalshi 56% vs Polymarket 50%"
semantic_title: "Arc token launch odds track a modest premium across venues"
telemetry: "Polymarket 50% vs Kalshi 56%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-07-08T10:15:03+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.5
  volume_cumulative_usd: 58987.8137210001
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.56
bullets:
  - "Kalshi prices Arc token launch at 56%, Polymarket at 50%, a 6pp spread on a crypto-adjacent claim."
  - "Kalshi is higher; both pools are relatively thin, with Polymarket carrying the larger cumulative volume."
  - "Modest gap may reflect differing crowd familiarity with Arc's roadmap; neither venue shows commanding liquidity to declare a clear anchor."
  - "Resolves YES if Arc publicly launches a token on any network before Jan 1, 2027."
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
      kalshi_vol_24h_usd: 0.55
      poly_vol_24h_usd: 1426.747842
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-07-08T10:15:03+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 6pp divergence on low combined volume is within noise tolerance, desks should monitor for a volume-weighted convergence rather than acting on the spread as a structural signal.
