---
signal_id: "CMSIG20260926DV00"
signal_slug: "arc-token-event-k24-p15"
headline: "Arc token launch before Jan 1 2027: Kalshi 24% vs Polymarket 15%"
semantic_title: "Arc token-before-2027 odds run higher on one desk"
telemetry: "Polymarket 15% vs Kalshi 24%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-09-26T07:48:20+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.15
  volume_cumulative_usd: 164423.35927099994
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.24
bullets:
  - "Kalshi prices the launch at 24%, Polymarket at 15%, a 9pp gap with under 100 days left on the clock."
  - "Kalshi sits higher; Polymarket carries vastly deeper liquidity at roughly 43x the cumulative volume."
  - "Thin Kalshi book may amplify noise; Polymarket's larger crowd likely reflects a more stable consensus against a launch."
  - "Resolves YES on any official Arc token launch event confirmed before Jan 1, 2027."
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
      kalshi_vol_24h_usd: 15.06
      poly_vol_24h_usd: 171.08
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-09-26T07:48:20+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 9pp spread almost certainly reflects Kalshi's shallow book rather than genuine information, making Polymarket's 15% the more defensible reference price for a desk tracking this claim.
