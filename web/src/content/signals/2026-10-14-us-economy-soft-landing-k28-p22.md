---
signal_id: "CMSIG20261014DV00"
signal_slug: "us-economy-soft-landing-k28-p22"
headline: "U.S. economy in recession by end-2026: Kalshi 29% vs Polymarket 22%"
semantic_title: "Economy-recession call builds a premium on the smaller desk"
telemetry: "Polymarket 22% vs Kalshi 29%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-14T13:18:28+00:00"
event_id: "CM-EVT-ZRG5DFDMZ8"
event_slug: "kxeconpath-26"
event_question: "State of the economy at the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x50e3ee8f93a464d04ea2cea6efff45c902f43642aedbf43f7afdc899e10f71d8"
  question_raw: "Will the US economy be in a soft landing at the end of 2026?"
  current_price: 0.22
  volume_cumulative_usd: 49099.276340000004
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXECONPATH-26-SOFT"
    question_raw: "State of the economy at the end of 2026?"
    current_price: 0.287
bullets:
  - "Kalshi prices recession at 29%, Polymarket at 22%, a 7pp spread on the same end-2026 claim."
  - "Kalshi sits higher with roughly $8.6K cumulative volume; Polymarket's 22% is backed by nearly $49K, far deeper liquidity."
  - "Thin volume on Kalshi may leave its price less anchored; Polymarket's deeper pool is more likely to reflect consensus."
  - "Resolution ties to an official determination (e.g., NBER declaration or GDP prints) covering the full 2026 calendar year."
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
      kalshi_vol_24h_usd: 152.4
      poly_vol_24h_usd: 794.746328
sources:
  - label: "ClearMarket cross-venue record: State of the economy at the end of 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-soft-landing-y-2026"
    retrieved_at: "2026-10-14T13:18:28+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 7pp gap, with the higher price sitting on the thinner book, suggests Kalshi's recession odds are likely overstated relative to the deeper Polymarket market, a desk could lean on Polymarket as the more reliable signal until Kalshi volume catches up.
