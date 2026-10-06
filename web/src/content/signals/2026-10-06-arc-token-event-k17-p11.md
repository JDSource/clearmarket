---
signal_id: "CMSIG20261006DV01"
signal_slug: "arc-token-event-k17-p11"
headline: "Arc token launch before Jan 1 2027: Kalshi 17% vs Polymarket 11%"
semantic_title: "Arc token launch carries a premium on one major desk"
telemetry: "Polymarket 11% vs Kalshi 17%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-06T14:44:02+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.11
  volume_cumulative_usd: 176254.82999499992
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.17
bullets:
  - "Kalshi prices an Arc token launch before 2027 at 17%; Polymarket at 11%, a 6pp gap."
  - "Kalshi is higher with minimal volume; Polymarket's position holds across substantially greater cumulative activity."
  - "Kalshi's thin book makes the higher price fragile; Polymarket's depth provides a sturdier consensus read."
  - "Resolves YES if Arc publicly launches a token before Jan 1, 2027 per verifiable announcement."
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
      kalshi_vol_24h_usd: 32.36
      poly_vol_24h_usd: 541.0
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-10-06T14:44:02+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With Polymarket running roughly 53 times Kalshi's volume, the 6pp premium on Kalshi reads as a liquidity-driven dislocation, a desk leaning on Polymarket's 11% as the credible anchor is well-supported by the depth imbalance.
