---
signal_id: "CMSIG20260714DV00"
signal_slug: "arc-token-event-k63-p56"
headline: "Arc token launch before 2027: Kalshi 63% vs Polymarket 57%"
semantic_title: "Arc token-launch odds split across the major prediction desks"
telemetry: "Polymarket 57% vs Kalshi 63%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-07-14T09:55:35+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.57
  volume_cumulative_usd: 60555.3761600001
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.63
bullets:
  - "Kalshi prices Arc token launch at 63%, Polymarket at 57%, a 6pp spread."
  - "Kalshi is the higher-conviction venue; Polymarket carries far deeper liquidity on this contract."
  - "Thin Kalshi volume may reflect a concentrated, informed cohort; Polymarket's crowd consensus sits lower."
  - "Resolves YES if Arc publicly launches a token before Jan 1, 2027."
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
      kalshi_vol_24h_usd: 101.43
      poly_vol_24h_usd: 191.0
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-07-14T09:55:35+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 6pp gap on a thin-vs-deep liquidity pair suggests Kalshi's price is driven by a small number of high-conviction participants, making Polymarket's 57% the more robust consensus reference for a desk.
