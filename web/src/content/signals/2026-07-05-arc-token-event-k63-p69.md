---
signal_id: "CMSIG20260705DV04"
signal_slug: "arc-token-event-k63-p69"
headline: "Arc token launch before Jan 1, 2027: Kalshi 63% vs Polymarket 69%"
semantic_title: "Arc token launch tracks a modest premium across venues"
telemetry: "Polymarket 69% vs Kalshi 63%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-07-05T10:08:50+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.69
  volume_cumulative_usd: 56313.17587900011
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.63
bullets:
  - "Kalshi prices Arc token launch at 63%, Polymarket at 69%, a 6pp gap"
  - "Polymarket is the higher-priced venue; its volume exceeds Kalshi's by roughly twenty-to-one"
  - "Both venues sit above 60%, indicating broad cross-platform consensus that a launch is more likely than not; the gap is narrow"
  - "Resolution hinges on Arc's official token generation or launch event before Jan 1, 2027"
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
      kalshi_vol_24h_usd: 84.11
      poly_vol_24h_usd: 1366.9601310000003
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-07-05T10:08:50+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 6pp spread at elevated probability levels is modest enough that the venues are broadly in agreement, the primary divergence risk for a desk is resolution-criteria interpretation, not directional disagreement.
