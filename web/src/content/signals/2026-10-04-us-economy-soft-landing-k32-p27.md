---
signal_id: "CMSIG20261004DV01"
signal_slug: "us-economy-soft-landing-k32-p27"
headline: "Economy 'good' at end of 2026: Kalshi 33% vs Polymarket 27%"
semantic_title: "End-2026 economy rated 'good' carries a premium on Kalshi"
telemetry: "Polymarket 27% vs Kalshi 33%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-04T13:40:36+00:00"
event_id: "CM-EVT-ZRG5DFDMZ8"
event_slug: "kxeconpath-26"
event_question: "State of the economy at the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x50e3ee8f93a464d04ea2cea6efff45c902f43642aedbf43f7afdc899e10f71d8"
  question_raw: "Will the US economy be in a soft landing at the end of 2026?"
  current_price: 0.27
  volume_cumulative_usd: 47040.740713
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXECONPATH-26-SOFT"
    question_raw: "State of the economy at the end of 2026?"
    current_price: 0.329
bullets:
  - "Kalshi prices a positive economy rating at 33%, Polymarket at 27%, a 6pp gap."
  - "Kalshi is the higher venue; Polymarket holds roughly five times the cumulative liquidity at $47K vs $9.7K."
  - "Differing resolution criteria or survey sources between venues likely explains part of the gap; the more liquid Polymarket crowd is the cautious read."
  - "Resolves based on an agreed economic-condition benchmark or survey at year-end 2026."
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
      kalshi_vol_24h_usd: 0.95
      poly_vol_24h_usd: 1.94
sources:
  - label: "ClearMarket cross-venue record: State of the economy at the end of 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-soft-landing-y-2026"
    retrieved_at: "2026-10-04T13:40:36+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 6pp gap on a macro sentiment claim, with Polymarket running the heavier book, suggests desks should lean on the Polymarket price as the consensus and treat the Kalshi premium as a basis risk to monitor rather than a clean arbitrage given potential resolution-mechanic differences.
