---
signal_id: "CMSIG20260831DV00"
signal_slug: "arc-token-event-k41-p26"
headline: "Arc token launch before Jan 1 2027: Kalshi 41% vs Polymarket 26%"
semantic_title: "Arc token launch before 2027 trades far apart across venues"
telemetry: "Polymarket 26% vs Kalshi 41%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-08-31T15:48:40+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.26
  volume_cumulative_usd: 153185.978557
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.41
bullets:
  - "Kalshi prices Arc token launch at 41%, Polymarket at 26%, a 15pp gap"
  - "Kalshi is the higher venue; liquidity heavily favors Polymarket ($153K vs $5K cumulative volume)"
  - "Thin Kalshi volume likely reflects a small, less-informed sample skewing optimistic; Polymarket's deeper book carries more price credibility"
  - "Resolves YES if Arc publicly launches a token before January 1, 2027"
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
      kalshi_vol_24h_usd: 70.94
      poly_vol_24h_usd: 0.0
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-08-31T15:48:40+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 15pp spread, combined with a 30-to-1 volume imbalance favoring Polymarket, suggests Kalshi's higher price is a thin-market artifact rather than a genuine informational signal, a desk leaning on the deeper book would shade toward 26%.
