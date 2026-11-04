---
signal_id: "CMSIG20261104DV01"
signal_slug: "arc-token-event-k15-p4"
headline: "Arc token before 2027: Kalshi 15% vs Polymarket 4%"
semantic_title: "Arc token launch carries a wide premium on one venue"
telemetry: "Polymarket 4% vs Kalshi 15%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-11-04T07:49:20+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.04
  volume_cumulative_usd: 203666.911788
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.15
bullets:
  - "Kalshi at 15%, Polymarket at 4%, an 11pp spread with resolution due Jan 1, 2027."
  - "Kalshi prices higher; Polymarket holds $204K in cumulative volume against Kalshi's $3.5K."
  - "Severe liquidity disparity points to Polymarket as the reference price; Kalshi's reading may reflect a small, less-informed participant pool."
  - "Resolves YES only on a confirmed Arc token launch before the year-end deadline."
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
      kalshi_vol_24h_usd: 12.66
      poly_vol_24h_usd: 6746.314513
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-11-04T07:49:20+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

An 11pp gap alongside a roughly 60-to-1 volume ratio strongly favors Polymarket's 4% as the credible baseline, leaving Kalshi's elevated print looking like a thin-market artifact rather than genuine signal.
