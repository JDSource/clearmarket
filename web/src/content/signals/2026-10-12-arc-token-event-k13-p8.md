---
signal_id: "CMSIG20261012DV02"
signal_slug: "arc-token-event-k13-p8"
headline: "Arc token launch before Jan 1 2027: Kalshi 13% vs Polymarket 8%"
semantic_title: "Arc token launch odds run wide between the major venues"
telemetry: "Polymarket 8% vs Kalshi 13%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-12T17:18:52+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.08
  volume_cumulative_usd: 177568.67280899998
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.13
bullets:
  - "Kalshi prices an Arc token launch before 2027 at 13%; Polymarket prices it at 8%, a 5pp gap."
  - "Kalshi's 13% rests on just $2,776 in volume; Polymarket's 8% is supported by $177,569, about 64× more liquidity."
  - "The extreme volume asymmetry makes Polymarket's 8% far more credible; Kalshi's price is essentially set by a handful of trades."
  - "Resolution requires a publicly confirmed Arc token launch or generation event before January 1, 2027."
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
      kalshi_vol_24h_usd: 22.38
      poly_vol_24h_usd: 309.922814
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-10-12T17:18:52+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 64× liquidity gap means the 5pp spread almost certainly reflects Kalshi price discovery failure on a thinly traded contract, not genuine informational disagreement, a desk should anchor to Polymarket's 8%.
