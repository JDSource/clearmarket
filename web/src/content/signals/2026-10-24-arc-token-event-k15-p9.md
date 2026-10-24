---
signal_id: "CMSIG20261024DV01"
signal_slug: "arc-token-event-k15-p9"
headline: "Arc token launch before Jan 1, 2027: Kalshi 15% vs Polymarket 9%"
semantic_title: "Arc token launch odds carry a premium on Kalshi heading into year-end"
telemetry: "Polymarket 9% vs Kalshi 15%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-24T12:27:18+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.09
  volume_cumulative_usd: 184557.302986
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.15
bullets:
  - "Kalshi prices an Arc token launch before 2027 at 15%, Polymarket at 9%, a 6pp spread."
  - "Kalshi is higher on $3.3K cumulative volume; Polymarket's 9% is supported by roughly 56x more trading activity."
  - "Polymarket's substantially deeper market makes its 9% the more stress-tested price; Kalshi's premium likely reflects thin-market noise rather than an informed edge."
  - "Resolution requires a confirmed, publicly announced Arc token launch on or before Dec 31, 2026."
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
      kalshi_vol_24h_usd: 20.05
      poly_vol_24h_usd: 0.0
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-10-24T12:27:18+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With Polymarket carrying nearly all the liquidity, the 6pp gap looks like a thin-market artifact on Kalshi rather than genuine information asymmetry, desks should weight Polymarket's 9% as the reference price.
