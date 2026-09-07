---
signal_id: "CMSIG20260907DV00"
signal_slug: "arc-token-event-k32-p15"
headline: "Arc token launch before 2027: Kalshi 32% vs Polymarket 15%"
semantic_title: "Arc token-launch odds split sharply across venues"
telemetry: "Polymarket 15% vs Kalshi 32%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-09-07T13:55:09+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.15
  volume_cumulative_usd: 156685.06664200002
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.32
bullets:
  - "Kalshi prices Arc token launch at 32%, Polymarket at 15%, a 17pp gap"
  - "Kalshi sits higher; Polymarket carries the larger pool with cumulative volume dwarfing Kalshi's thin book"
  - "Thin Kalshi liquidity may allow a small number of contracts to push odds well above the deeper Polymarket consensus"
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
      kalshi_vol_24h_usd: 32.44
      poly_vol_24h_usd: 368.45
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-09-07T13:55:09+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 17pp spread, paired with Polymarket's far deeper liquidity, suggests the Kalshi price is the less reliable signal, a desk leaning on the larger book would treat 15% as the working prior.
