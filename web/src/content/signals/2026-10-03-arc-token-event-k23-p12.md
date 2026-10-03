---
signal_id: "CMSIG20261003DV00"
signal_slug: "arc-token-event-k23-p12"
headline: "Arc token launch before Jan 2027: Kalshi 23% vs Polymarket 12%"
semantic_title: "Arc token launch before 2027 trades far apart across venues"
telemetry: "Polymarket 12% vs Kalshi 23%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-03T07:48:42+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.12
  volume_cumulative_usd: 167029.88333499996
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.23
bullets:
  - "Kalshi prices Arc token launch at 23%, Polymarket at 12%, an 11pp gap"
  - "Kalshi is the higher-probability venue; Polymarket carries far deeper liquidity at $167K cumulative vs Kalshi's $3.9K"
  - "Thin Kalshi volume leaves that market susceptible to noise; Polymarket's larger pool likely reflects broader consensus"
  - "Resolution hinges on a verifiable Arc token launch announcement before Jan 1, 2027"
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
      kalshi_vol_24h_usd: 32.27
      poly_vol_24h_usd: 46.0
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-10-03T07:48:42+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 11pp spread is almost certainly a liquidity artifact, Kalshi's negligible volume makes it an unreliable price signal, and Polymarket's deeper market at 12% is the more credible reference for a desk assessing this outcome.
