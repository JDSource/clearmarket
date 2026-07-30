---
signal_id: "CMSIG20260730DV00"
signal_slug: "arc-token-event-k60-p39"
headline: "Arc token launch before Jan 1 2027: Kalshi 60% vs Polymarket 39%"
semantic_title: "Arc token-before-2027 odds split sharply across venues"
telemetry: "Polymarket 39% vs Kalshi 60%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-07-30T10:22:05+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.39
  volume_cumulative_usd: 103552.772895
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.6
bullets:
  - "Kalshi prices Arc token launch at 60%, Polymarket at 39%, a 21pp gap"
  - "Kalshi is the higher-priced venue ($3,908 cumulative volume) vs Polymarket's deeper $103,553 book"
  - "Thin Kalshi liquidity likely driving the premium; Polymarket's larger pool may reflect more informed consensus"
  - "Resolves YES if Arc publicly launches a token before January 1, 2027"
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
      poly_vol_24h_usd: 2642.971706
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-07-30T10:22:05+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 21pp spread and wide liquidity imbalance suggest Kalshi's elevated price reflects a thin, potentially uninformed book, a desk with a directional view would look to Polymarket's deeper market as the more reliable anchor.
