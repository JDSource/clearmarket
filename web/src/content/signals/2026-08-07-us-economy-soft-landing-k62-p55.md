---
signal_id: "CMSIG20260807DV01"
signal_slug: "us-economy-soft-landing-k62-p55"
headline: "Economy strong end-2026: Kalshi 62% vs Polymarket 55%"
semantic_title: "Economy-strong-at-year-end odds carry a premium on one major desk"
telemetry: "Polymarket 55% vs Kalshi 62%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-08-07T08:55:00+00:00"
event_id: "CM-EVT-ZRG5DFDMZ8"
event_slug: "kxeconpath-26"
event_question: "State of the economy at the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x50e3ee8f93a464d04ea2cea6efff45c902f43642aedbf43f7afdc899e10f71d8"
  question_raw: "Will the US economy be in a soft landing at the end of 2026?"
  current_price: 0.55
  volume_cumulative_usd: 30506.797993000004
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXECONPATH-26-SOFT"
    question_raw: "State of the economy at the end of 2026?"
    current_price: 0.624
bullets:
  - "Kalshi prices a strong economy at end-2026 at 62%, Polymarket at 55%, a 7pp gap"
  - "Kalshi is the higher venue; Polymarket carries roughly $30.5K in volume vs Kalshi's $11.7K"
  - "Differing resolution criteria, Kalshi may use a specific index threshold while Polymarket's wording could differ, likely explains the spread"
  - "Both venues resolve before Jan 1, 2027, but the exact economic indicator used may not be identical"
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
      kalshi_vol_24h_usd: 71.05
      poly_vol_24h_usd: 50.21
sources:
  - label: "ClearMarket cross-venue record: State of the economy at the end of 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-soft-landing-y-2026"
    retrieved_at: "2026-08-07T08:55:00+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 7pp premium on Kalshi relative to a deeper Polymarket book suggests desks check resolution language carefully before treating this as a clean arbitrage, criteria mismatch is the most probable driver.
