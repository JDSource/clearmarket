---
signal_id: "CMSIG20261024DV00"
signal_slug: "us-economy-soft-landing-k17-p9"
headline: "U.S. economy in recession by end-2026: Kalshi 17% vs Polymarket 9%"
semantic_title: "Economy-in-recession call trades far apart across venues"
telemetry: "Polymarket 9% vs Kalshi 17%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-24T12:27:18+00:00"
event_id: "CM-EVT-ZRG5DFDMZ8"
event_slug: "kxeconpath-26"
event_question: "State of the economy at the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x50e3ee8f93a464d04ea2cea6efff45c902f43642aedbf43f7afdc899e10f71d8"
  question_raw: "Will the US economy be in a soft landing at the end of 2026?"
  current_price: 0.09
  volume_cumulative_usd: 52112.032628
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXECONPATH-26-SOFT"
    question_raw: "State of the economy at the end of 2026?"
    current_price: 0.174
bullets:
  - "Kalshi prices recession by end-2026 at 17%, Polymarket at 9%, an 8pp gap."
  - "Kalshi sits higher on thin volume; Polymarket holds the lower read with roughly 8x more cumulative activity."
  - "Polymarket's deeper pool likely reflects broader crowd input; Kalshi's premium may stem from a smaller, more pessimistic participant base or differing resolution criteria."
  - "Resolution hinges on an official or widely accepted recession determination before Jan 1, 2027, definitional ambiguity may itself explain part of the spread."
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
      kalshi_vol_24h_usd: 3.48
      poly_vol_24h_usd: 1096.64
sources:
  - label: "ClearMarket cross-venue record: State of the economy at the end of 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-soft-landing-y-2026"
    retrieved_at: "2026-10-24T12:27:18+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 8pp gap on a thin-vs-deep liquidity split suggests Polymarket's 9% is the more crowd-vetted read, but desks should check whether the two contracts resolve against the same recession definition before treating this as clean arbitrage.
