---
signal_id: "CMSIG20261009DV01"
signal_slug: "us-economy-soft-landing-k32-p27"
headline: "Economy in recession end-2026: Kalshi 33% vs Polymarket 27%"
semantic_title: "Economy-in-recession odds stay split across the major desks"
telemetry: "Polymarket 27% vs Kalshi 33%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-09T14:56:34+00:00"
event_id: "CM-EVT-ZRG5DFDMZ8"
event_slug: "kxeconpath-26"
event_question: "State of the economy at the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x50e3ee8f93a464d04ea2cea6efff45c902f43642aedbf43f7afdc899e10f71d8"
  question_raw: "Will the US economy be in a soft landing at the end of 2026?"
  current_price: 0.27
  volume_cumulative_usd: 47227.110419
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXECONPATH-26-SOFT"
    question_raw: "State of the economy at the end of 2026?"
    current_price: 0.328
bullets:
  - "Kalshi prices a recessionary economy at end-2026 at 33%, Polymarket at 27%, a 6pp spread."
  - "Kalshi sits higher with $9.6K cumulative volume; Polymarket lower with $47.2K, meaningful liquidity advantage to Polymarket."
  - "Divergence may reflect differing resolution criteria: the two venues may define 'recession' or 'state of the economy' by different benchmarks, producing structurally different fair values."
  - "Resolution language is the key risk, desks should confirm each contract's exact GDP/NBER trigger before positioning."
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
      kalshi_vol_24h_usd: 0.02
      poly_vol_24h_usd: 9.19
sources:
  - label: "ClearMarket cross-venue record: State of the economy at the end of 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-soft-landing-y-2026"
    retrieved_at: "2026-10-09T14:56:34+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 6pp gap on a subjectively worded economic-state claim is most likely driven by resolution-definition differences between venues rather than genuine belief divergence, making cross-venue arbitrage risky until contract language is confirmed to be equivalent.
