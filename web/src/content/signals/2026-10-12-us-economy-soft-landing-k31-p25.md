---
signal_id: "CMSIG20261012DV02"
signal_slug: "us-economy-soft-landing-k31-p25"
headline: "US economy 'good' end of 2026: Kalshi 31% vs Polymarket 25%"
semantic_title: "Economy-state odds hold apart across venues heading into year-end"
telemetry: "Polymarket 25% vs Kalshi 31%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-12T07:50:58+00:00"
event_id: "CM-EVT-ZRG5DFDMZ8"
event_slug: "kxeconpath-26"
event_question: "State of the economy at the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x50e3ee8f93a464d04ea2cea6efff45c902f43642aedbf43f7afdc899e10f71d8"
  question_raw: "Will the US economy be in a soft landing at the end of 2026?"
  current_price: 0.25
  volume_cumulative_usd: 47375.491529
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXECONPATH-26-SOFT"
    question_raw: "State of the economy at the end of 2026?"
    current_price: 0.312
bullets:
  - "Kalshi prices a positive economy outcome at 31%, Polymarket at 25%, a 6pp divergence on the same year-end claim."
  - "Kalshi is the higher venue; Polymarket carries roughly 5x more cumulative volume, lending its 25% figure more weight."
  - "The gap may reflect differing resolution criteria: subjective economic-state definitions can vary by venue ruleset, producing structural price differences."
  - "Resolution depends on the specific economic indicator or index each venue designates as the official end-of-2026 benchmark."
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
      kalshi_vol_24h_usd: 11.29
      poly_vol_24h_usd: 12.07
sources:
  - label: "ClearMarket cross-venue record: State of the economy at the end of 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-soft-landing-y-2026"
    retrieved_at: "2026-10-12T07:50:58+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 6pp spread on a macro sentiment claim with ambiguous resolution language is a classic definition-arbitrage situation, a desk should audit both venue rulebooks before treating this as a tradeable dislocation.
