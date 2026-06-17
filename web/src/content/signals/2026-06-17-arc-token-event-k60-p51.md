---
signal_id: "CMSIG20260617DV00"
signal_slug: "arc-token-event-k60-p51"
headline: "Arc token launch before 2027: Kalshi 60% vs Polymarket 51%"
semantic_title: "Arc token launch before 2027 splits sharply across venues"
telemetry: "Polymarket 51% vs Kalshi 60%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-06-17T12:14:49+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.51
  volume_cumulative_usd: 22023.804401999998
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.6
bullets:
  - "Kalshi prices 60%, Polymarket 51%, a 9pp gap on the same binary claim."
  - "Kalshi sits higher; Polymarket carries significantly deeper liquidity on this contract."
  - "Thin Kalshi book may reflect a smaller, more crypto-native crowd willing to price token launches generously."
  - "Resolution hinges on a verifiable mainnet or public token launch by Dec 31, 2026."
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
      poly_vol_24h_usd: 2844.5519550000004
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-06-17T12:14:49+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 9pp spread on a sub-six-month horizon suggests Kalshi's shallow book is not fully arbitraged, leaving a potential edge for desks that can access both venues.
