---
signal_id: "CMSIG20261031DV01"
signal_slug: "arc-token-event-k10-p4"
headline: "Arc token launch before 2027: Kalshi 10% vs Polymarket 4%"
semantic_title: "Arc token-by-2027 carries a premium on the smaller desk"
telemetry: "Polymarket 4% vs Kalshi 10%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-31T07:50:02+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.04
  volume_cumulative_usd: 192917.47753599996
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.1
bullets:
  - "Kalshi prices 10%, Polymarket 4%, a 6pp gap on the same binary outcome"
  - "Kalshi is higher; Polymarket carries roughly $193K in cumulative volume vs ~$2K on Kalshi"
  - "With two months left in the horizon, Polymarket's deeper liquidity makes its 4% the more credible anchor"
  - "Resolves YES if Arc publicly launches a token before Jan 1, 2027"
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
      kalshi_vol_24h_usd: 2.7
      poly_vol_24h_usd: 621.42
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-10-31T07:50:02+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 6pp spread where virtually all traded volume sits on the lower-priced venue points to a thin Kalshi market mispricing upward, a desk should treat Polymarket's 4% as the reference price.
