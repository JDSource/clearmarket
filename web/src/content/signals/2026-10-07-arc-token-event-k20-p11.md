---
signal_id: "CMSIG20261007DV00"
signal_slug: "arc-token-event-k20-p11"
headline: "Arc token launch before 2027: Kalshi 20% vs Polymarket 11%"
semantic_title: "Arc token launch odds split sharply across venues"
telemetry: "Polymarket 11% vs Kalshi 20%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-07T07:49:04+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.11
  volume_cumulative_usd: 176254.82999499995
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.2
bullets:
  - "Kalshi prices Arc token launch at 20%, Polymarket at 11%, a 9pp gap with under three months to resolution."
  - "Kalshi is the higher venue; liquidity runs thin at $3,949 cumulative vs Polymarket's $176,255."
  - "Thin Kalshi volume likely explains the premium, shallow book, fewer participants anchoring the price toward the better-informed crowd on the larger venue."
  - "Resolves YES if Arc publicly launches a token before Jan 1, 2027; any soft launch or testnet status may complicate adjudication."
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
      kalshi_vol_24h_usd: 17.97
      poly_vol_24h_usd: 0.0
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-10-07T07:49:04+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 9pp gap strongly favors the Polymarket price as the credible signal given volume depth roughly 45x greater, making Kalshi's 20% look like a thin-book artifact worth fading toward 11%.
