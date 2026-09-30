---
signal_id: "CMSIG20260930DV00"
signal_slug: "us-economy-soft-landing-k33-p27"
headline: "Economy in recession by end-2026: Kalshi 33% vs Polymarket 27%"
semantic_title: "2026 recession odds carry a premium across venues"
telemetry: "Polymarket 27% vs Kalshi 33%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-09-30T07:48:33+00:00"
event_id: "CM-EVT-ZRG5DFDMZ8"
event_slug: "kxeconpath-26"
event_question: "State of the economy at the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x50e3ee8f93a464d04ea2cea6efff45c902f43642aedbf43f7afdc899e10f71d8"
  question_raw: "Will the US economy be in a soft landing at the end of 2026?"
  current_price: 0.27
  volume_cumulative_usd: 47038.800713000004
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXECONPATH-26-SOFT"
    question_raw: "State of the economy at the end of 2026?"
    current_price: 0.33
bullets:
  - "Kalshi prices recession at 33%, Polymarket at 27%, a 6pp gap with three months to resolution."
  - "Kalshi is higher; Polymarket carries roughly five times the cumulative volume, suggesting deeper liquidity on the lower price."
  - "Thinner Kalshi book may reflect a more pessimistic user base or less arbitrage pressure given the modest pool size."
  - "Resolution likely tied to NBER declaration or a designated official economic indicator reading before Jan 1, 2027."
atomic_claims:
  - type: "cross_venue_spread"
    provenance: "CM cross-venue link (question_id CMX-534611296D); prices direct from venue APIs"
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
      kalshi_vol_24h_usd: 18.03
      poly_vol_24h_usd: 78.860965
sources:
  - label: "ClearMarket cross-venue record: State of the economy at the end of 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-soft-landing-y-2026"
    retrieved_at: "2026-09-30T07:48:33+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 6pp spread, sitting on the side of a heavier-volume lower price at Polymarket, suggests a desk could lean on the Polymarket read as the more liquid signal while flagging Kalshi as prone to drift given its shallow book.
