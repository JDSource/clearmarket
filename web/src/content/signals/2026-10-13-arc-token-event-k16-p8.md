---
signal_id: "CMSIG20261013DV00"
signal_slug: "arc-token-event-k16-p8"
headline: "Arc token launch before Jan 2027: Kalshi 16% vs Polymarket 8%"
semantic_title: "Arc token launch before 2027 prices far apart across venues"
telemetry: "Polymarket 8% vs Kalshi 16%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-13T15:33:55+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.08
  volume_cumulative_usd: 177766.38280899994
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.16
bullets:
  - "Kalshi prices the launch at 16%, Polymarket at 8%, an 8pp spread on identical claim terms."
  - "Kalshi is the higher-priced venue; Polymarket carries vastly deeper liquidity at $177K+ cumulative volume vs Kalshi's $3K."
  - "Thin Kalshi volume likely inflates its price; Polymarket's deeper market is generally considered the more calibrated read here."
  - "Resolution requires a confirmed public Arc token launch before January 1, 2027."
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
      kalshi_vol_24h_usd: 77.24
      poly_vol_24h_usd: 197.71
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-10-13T15:33:55+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With Kalshi's cumulative volume a fraction of Polymarket's, the 8pp gap almost certainly reflects a thin, illiquid market on the high side rather than a genuine information asymmetry, the desk should treat Polymarket's 8% as the sharper signal.
