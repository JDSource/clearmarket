---
signal_id: "CMSIG20260707DV01"
signal_slug: "arc-token-event-k63-p51"
headline: "Arc token launch before Jan 1 2027: Kalshi 63% vs Polymarket 51%"
semantic_title: "Arc token launch pricing decouples on the major prediction desks"
telemetry: "Polymarket 51% vs Kalshi 63%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-07-07T10:53:30+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.51
  volume_cumulative_usd: 57561.06587900011
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.63
bullets:
  - "Kalshi at 63%, Polymarket at 51%, a 12pp gap, with Kalshi the higher side."
  - "Kalshi is higher; Polymarket holds far greater liquidity, reflecting a broader participant base."
  - "Kalshi's smaller, potentially crypto-native crowd may assign higher probability to a launch; Polymarket's depth implies more skepticism."
  - "Resolves YES on confirmed Arc token public launch or issuance event before Jan 1, 2027."
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
      kalshi_vol_24h_usd: 0.0
      poly_vol_24h_usd: 338.89
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-07-07T10:53:30+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should treat Polymarket's deeper, lower price as the stronger prior here, Kalshi's illiquid premium looks like an informed-but-thin crowd that hasn't been stress-tested by size.
