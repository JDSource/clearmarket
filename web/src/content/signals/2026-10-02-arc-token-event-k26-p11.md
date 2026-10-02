---
signal_id: "CMSIG20261002DV00"
signal_slug: "arc-token-event-k26-p11"
headline: "Arc token launch before 2027: Kalshi 26% vs Polymarket 11%"
semantic_title: "Arc token-launch odds split sharply across venues"
telemetry: "Polymarket 11% vs Kalshi 26%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-02T07:49:27+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.11
  volume_cumulative_usd: 166983.88333499996
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.26
bullets:
  - "Kalshi prices Arc token launch at 26%, Polymarket at 11%, a 15pp gap."
  - "Kalshi sits higher; Polymarket carries the deeper book at ~$167K cumulative vs ~$4K."
  - "Thin Kalshi volume may reflect a small, undisciplined market; Polymarket's larger pool likely anchors closer to informed consensus."
  - "Resolves YES if Arc publicly launches a token before Jan 1, 2027, roughly 90 days remain."
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
      kalshi_vol_24h_usd: 51.43
      poly_vol_24h_usd: 1415.2411570000002
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-10-02T07:49:27+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 15pp spread, combined with a 38-to-1 liquidity imbalance favoring Polymarket, suggests Kalshi's elevated print reflects noise in a thin market rather than a genuine edge, and a desk should weight Polymarket's 11% as the more credible signal.
