---
signal_id: "CMSIG20260806DV00"
signal_slug: "arc-token-event-k47-p24"
headline: "Arc token launch before 2027: Kalshi 47% vs Polymarket 24%"
semantic_title: "Arc token launch odds split sharply across venues"
telemetry: "Polymarket 24% vs Kalshi 47%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-08-06T10:36:44+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.24
  volume_cumulative_usd: 136614.568997
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.47
bullets:
  - "Kalshi prices Arc token launch at 47%; Polymarket at 24%, a 23pp gap."
  - "Kalshi carries the higher price on thin volume; Polymarket holds the lower price on far deeper liquidity."
  - "Thin Kalshi volume likely reflects low-information positioning; Polymarket's deeper pool may better reflect resolution ambiguity on what counts as a 'launch'."
  - "Resolution hinges on whether a public token issuance or airdrop occurs before Jan 1, 2027, criteria clarity may differ by venue."
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
      kalshi_vol_24h_usd: 1.63
      poly_vol_24h_usd: 6043.159103999999
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-08-06T10:36:44+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 23pp gap against a large liquidity imbalance suggests Kalshi's higher price is noise-driven and Polymarket's 24% is the more credible anchor for a desk assessing this claim.
