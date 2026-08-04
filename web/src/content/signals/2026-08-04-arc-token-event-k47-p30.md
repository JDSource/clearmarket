---
signal_id: "CMSIG20260804DV00"
signal_slug: "arc-token-event-k47-p30"
headline: "Arc token launch before 2027: Kalshi 47% vs Polymarket 30%"
semantic_title: "Arc token launch odds split sharply across venues"
telemetry: "Polymarket 30% vs Kalshi 47%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-08-04T10:34:23+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.3
  volume_cumulative_usd: 129854.59262199997
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.47
bullets:
  - "Kalshi prices 47%, Polymarket 30%, a 17pp gap on the same binary claim."
  - "Kalshi sits higher; Polymarket carries far deeper liquidity on both sides."
  - "Thin Kalshi volume likely inflates the yes side; Polymarket's deeper book may reflect a more informed consensus."
  - "Resolves YES if Arc publicly launches a token on any chain before Jan 1, 2027."
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
      kalshi_vol_24h_usd: 71.65
      poly_vol_24h_usd: 22.132700999999997
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-08-04T10:34:23+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 17pp spread and the stark volume imbalance suggest Kalshi's elevated yes price is a thin-market artifact rather than a genuine belief difference, making Polymarket's 30% the more credible anchor for a desk assessing this claim.
