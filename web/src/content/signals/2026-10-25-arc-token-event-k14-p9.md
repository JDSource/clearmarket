---
signal_id: "CMSIG20261025DV01"
signal_slug: "arc-token-event-k14-p9"
headline: "Arc token launch before 2027: Kalshi 14% vs Polymarket 9%"
semantic_title: "Arc token-by-2027 carries a modest premium across venues"
telemetry: "Polymarket 9% vs Kalshi 14%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-25T12:57:37+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.09
  volume_cumulative_usd: 184557.302986
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.14
bullets:
  - "Kalshi sits at 14%, Polymarket at 9%, a 5pp spread with roughly 67 days remaining."
  - "Kalshi is higher; Polymarket leads on liquidity with $184K cumulative volume vs $3K on Kalshi."
  - "As with Exponent, Kalshi's thin book likely explains the upward drift; Polymarket's 9% reflects a far broader participant base."
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
      kalshi_vol_24h_usd: 16.74
      poly_vol_24h_usd: 0.0
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-10-25T12:57:37+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 5pp gap is narrower but driven by the same structural imbalance, Kalshi's sub-$5K market is prone to wide spreads, and desks should treat Polymarket's 9% as the benchmark while monitoring whether Kalshi volume builds enough to close the gap organically.
