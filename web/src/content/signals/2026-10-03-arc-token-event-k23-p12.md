---
signal_id: "CMSIG20261003DV00"
signal_slug: "arc-token-event-k23-p12"
headline: "Arc token launch before Jan 2027: Kalshi 23% vs Polymarket 12%"
semantic_title: "Arc token-before-2027 odds split sharply across venues"
telemetry: "Polymarket 12% vs Kalshi 23%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-03T13:00:57+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.12
  volume_cumulative_usd: 167029.883335
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.23
bullets:
  - "Kalshi prices Arc token launch at 23%, Polymarket at 12%, an 11pp gap with under three months to resolution."
  - "Kalshi is the higher-priced venue; Polymarket carries substantially deeper liquidity at over $167K cumulative volume vs Kalshi's $3.9K."
  - "Thin Kalshi volume makes its 23% print fragile, the Polymarket crowd, trading with far more capital at stake, assigns roughly half the probability."
  - "Resolution: any verified public Arc token launch before Jan 1, 2027 settles YES; no launch by year-end settles NO."
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
      kalshi_vol_24h_usd: 32.27
      poly_vol_24h_usd: 26.0
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-10-03T13:00:57+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 11pp gap likely reflects Kalshi's shallow book amplifying noise rather than genuine information advantage, Polymarket's deeper market at 12% is the more credible anchor for a desk sizing a position.
