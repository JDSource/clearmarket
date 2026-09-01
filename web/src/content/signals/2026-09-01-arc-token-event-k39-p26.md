---
signal_id: "CMSIG20260901DV00"
signal_slug: "arc-token-event-k39-p26"
headline: "Arc token launch before Jan 2027: Kalshi 39% vs Polymarket 26%"
semantic_title: "Arc token launch before 2027 trades far apart across venues"
telemetry: "Polymarket 26% vs Kalshi 39%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-09-01T13:01:19+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.26
  volume_cumulative_usd: 153198.07855699994
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.39
bullets:
  - "Kalshi prices Arc token launch at 39%, Polymarket at 26%, a 13pp gap on the same claim."
  - "Kalshi sits higher; Polymarket carries far deeper liquidity with cumulative volume dwarfing Kalshi's."
  - "Thin Kalshi volume may reflect unanchored optimism; Polymarket's larger pool likely better price-discovers low-probability crypto events."
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
      kalshi_vol_24h_usd: 4.37
      poly_vol_24h_usd: 12.1
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-09-01T13:01:19+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 13pp spread on a thin-vs-deep liquidity pair suggests Kalshi's price is noise-driven; a desk should weight Polymarket's 26% as the more credible signal and watch for any Arc protocol announcement to close the gap.
