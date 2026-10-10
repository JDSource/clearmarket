---
signal_id: "CMSIG20261010DV00"
signal_slug: "arc-token-event-k21-p11"
headline: "Arc token launch before 2027: Kalshi 21% vs Polymarket 11%"
semantic_title: "Arc token launch odds run wide across venues"
telemetry: "Polymarket 11% vs Kalshi 21%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-10T07:49:03+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.11
  volume_cumulative_usd: 177074.989995
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.21
bullets:
  - "Kalshi prices the launch at 21%, nearly double Polymarket's 11%, a 10pp spread."
  - "Kalshi sits higher with cumulative volume near $4K; Polymarket carries the deep book at $177K."
  - "Thin Kalshi liquidity amplifies noise, the larger Polymarket market likely reflects broader consensus on a sub-12-week window."
  - "Resolves YES if Arc publicly announces a token launch before Jan 1, 2027."
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
      kalshi_vol_24h_usd: 136.72
      poly_vol_24h_usd: 766.16
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-10-10T07:49:03+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With less than three months to resolution and a 10pp gap, the well-capitalized Polymarket side at 11% is the more reliable signal, the Kalshi premium most plausibly reflects thin liquidity rather than a genuine information edge.
