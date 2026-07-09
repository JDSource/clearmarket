---
signal_id: "CMSIG20260709DV00"
signal_slug: "arc-token-event-k80-p56"
headline: "Arc token launch before 2027: Kalshi 80% vs Polymarket 56%"
semantic_title: "Arc token-launch odds split sharply across venues before 2027"
telemetry: "Polymarket 56% vs Kalshi 80%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-07-09T10:57:41+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.56
  volume_cumulative_usd: 59194.554193000105
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.8
bullets:
  - "Kalshi at 80%, Polymarket at 56%, a 24pp spread on the same binary claim."
  - "Kalshi prices the higher probability; Polymarket carries the deeper liquidity by a wide margin."
  - "Thin Kalshi volume likely reflects a narrow, high-conviction participant base, potentially inflating YES prices absent sufficient sell-side pressure."
  - "Contract resolves on any confirmed Arc token public launch before Jan 1, 2027."
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
      kalshi_vol_24h_usd: 2.03
      poly_vol_24h_usd: 206.74047200000004
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-07-09T10:57:41+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 24pp gap with a steep liquidity imbalance suggests Kalshi's 80% is poorly price-discovered; desks should weight the deeper Polymarket market at 56% as the more reliable signal.
