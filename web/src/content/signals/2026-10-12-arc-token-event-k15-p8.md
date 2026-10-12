---
signal_id: "CMSIG20261012DV01"
signal_slug: "arc-token-event-k15-p8"
headline: "Arc token launch before Jan 1 2027: Kalshi 15% vs Polymarket 8%"
semantic_title: "Arc token launch pricing decouples on the major prediction desks"
telemetry: "Polymarket 8% vs Kalshi 15%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-12T07:50:58+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.08
  volume_cumulative_usd: 177568.67280900004
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.15
bullets:
  - "Kalshi prices an Arc token launch at 15%, Polymarket at 8%, a 7pp spread on identical terms."
  - "Kalshi is the higher venue; Polymarket holds roughly 56x greater cumulative volume, anchoring the low."
  - "Low overall liquidity on Kalshi makes its 15% susceptible to noise from a handful of contracts; Polymarket depth suggests stronger price discovery."
  - "Resolution hinges on any confirmed Arc token announcement or launch before Jan 1, 2027."
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
      kalshi_vol_24h_usd: 39.47
      poly_vol_24h_usd: 481.922814
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-10-12T07:50:58+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With Polymarket running 56x the volume at nearly half the probability, a desk eyeing this spread should treat Kalshi's 15% as illiquidity-inflated until corroborating on-chain or news signals emerge.
