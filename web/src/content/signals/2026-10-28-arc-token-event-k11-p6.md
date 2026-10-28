---
signal_id: "CMSIG20261028DV01"
signal_slug: "arc-token-event-k11-p6"
headline: "Arc token before 2027: Kalshi 11% vs Polymarket 6%"
semantic_title: "Arc token launch pricing diverges across the major desks"
telemetry: "Polymarket 6% vs Kalshi 11%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-28T07:50:33+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.06
  volume_cumulative_usd: 186020.44298599998
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.11
bullets:
  - "Kalshi prices Arc token launch at 11%, Polymarket at 6%, a 5pp spread with resolution in roughly 65 days."
  - "Kalshi sits higher; Polymarket holds the dominant liquidity position by a wide margin."
  - "At these low absolute levels, a 5pp gap is proportionally large but both venues agree the event is unlikely; Polymarket's volume-weighted price carries more weight."
  - "Resolves YES only upon a confirmed Arc token launch before Jan 1, 2027."
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
      kalshi_vol_24h_usd: 68.22
      poly_vol_24h_usd: 183.63
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-10-28T07:50:33+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Both venues assign long odds to Arc launching a token this year, and the 5pp divergence at such low probability levels likely reflects Kalshi's sparse order book rather than a tradeable signal.
