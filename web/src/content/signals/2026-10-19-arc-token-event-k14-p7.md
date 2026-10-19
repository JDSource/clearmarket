---
signal_id: "CMSIG20261019DV01"
signal_slug: "arc-token-event-k14-p7"
headline: "Arc token launch before 2027: Kalshi 14% vs Polymarket 7%"
semantic_title: "Arc token odds build higher on Kalshi than on rival venues"
telemetry: "Polymarket 7% vs Kalshi 14%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-19T07:48:36+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.07
  volume_cumulative_usd: 179969.5493209999
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.14
bullets:
  - "Kalshi prices Arc's token launch at 14%, Polymarket at 7%, a 7pp spread with the horizon closing in weeks."
  - "Kalshi is the higher venue; Polymarket again holds the overwhelming share of liquidity, with volume roughly 59x larger."
  - "Pattern mirrors the Exponent divergence: sparse Kalshi activity inflates the probability print relative to the more liquid Polymarket market."
  - "Resolves YES only upon a confirmed public Arc token launch before Jan 1, 2027."
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
      kalshi_vol_24h_usd: 1.23
      poly_vol_24h_usd: 1215.28
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-10-19T07:48:36+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 7pp gap on a thin Kalshi book suggests price discovery has not occurred on that venue, Polymarket's 7% is the credible anchor, and the spread offers little actionable arbitrage given Kalshi's low liquidity.
