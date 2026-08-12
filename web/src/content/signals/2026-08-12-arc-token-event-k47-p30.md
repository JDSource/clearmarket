---
signal_id: "CMSIG20260812DV00"
signal_slug: "arc-token-event-k47-p30"
headline: "Will Arc launch a token before 2027? Kalshi 47% vs Polymarket 30%"
semantic_title: "Arc token launch before 2027 splits sharply across venues"
telemetry: "Polymarket 30% vs Kalshi 47%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-08-12T09:08:57+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.3
  volume_cumulative_usd: 146718.069708
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.47
bullets:
  - "Kalshi prices the Arc token launch at 47%, Polymarket at 30%, a 17pp gap"
  - "Kalshi is the higher venue; Polymarket carries roughly 37x the cumulative volume"
  - "Thin Kalshi liquidity may inflate its price; Polymarket's deeper book likely reflects broader consensus"
  - "Resolves YES if Arc publicly launches any token before Jan 1, 2027"
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
      kalshi_vol_24h_usd: 247.28
      poly_vol_24h_usd: 3258.857379
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-08-12T09:08:57+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 17pp spread, paired with a lopsided volume imbalance, flags Kalshi's higher price as a thin-market artifact, a desk leaning on resolution clarity would weight Polymarket's 30% more heavily.
