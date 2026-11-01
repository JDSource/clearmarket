---
signal_id: "CMSIG20261101DV01"
signal_slug: "arc-token-event-k14-p4"
headline: "Arc token launch before 2027: Kalshi 14% vs Polymarket 4%"
semantic_title: "Arc token launch odds build a wide split across venues"
telemetry: "Polymarket 4% vs Kalshi 14%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-11-01T14:44:10+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.045
  volume_cumulative_usd: 194350.59727499998
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.14
bullets:
  - "Kalshi prices an Arc token launch at 14%, Polymarket at 4%, a 10pp gap"
  - "Kalshi is the higher-priced venue; Polymarket holds dominant liquidity at $194K cumulative vs $3.2K on Kalshi"
  - "Polymarket's deep book makes its 4% reading far more reliable; Kalshi's 14% likely overstates the probability due to sparse trading"
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
      kalshi_vol_24h_usd: 0.94
      poly_vol_24h_usd: 1095.238914
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-11-01T14:44:10+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 10pp gap where one venue has sixty times the volume of the other is a liquidity story, not a view divergence, Polymarket's 4% is the operative market price, and Kalshi's elevated reading offers no actionable edge given its minimal book depth.
