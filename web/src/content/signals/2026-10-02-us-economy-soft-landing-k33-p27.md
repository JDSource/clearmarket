---
signal_id: "CMSIG20261002DV01"
signal_slug: "us-economy-soft-landing-k33-p27"
headline: "Economy 'good' end of 2026: Kalshi 34% vs Polymarket 27%"
semantic_title: "U.S. economy end-2026 outlook carries a premium across venues"
telemetry: "Polymarket 27% vs Kalshi 34%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-02T07:49:27+00:00"
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
    current_price: 0.339
bullets:
  - "Kalshi prices a positive economy outcome at 34%, Polymarket at 27%, a 7pp gap."
  - "Kalshi is higher; Polymarket holds roughly 5x the cumulative volume at ~$47K vs ~$10K."
  - "Ambiguous resolution criteria, what counts as 'good', may drive divergence as each venue's ruleset or oracle differs."
  - "Resolution likely tied to a defined economic indicator reading or adjudication before Jan 1, 2027."
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
      poly_vol_24h_usd: 0.0
sources:
  - label: "ClearMarket cross-venue record: State of the economy at the end of 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-soft-landing-y-2026"
    retrieved_at: "2026-10-02T07:49:27+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 7pp spread on a subjectively worded claim points to resolution-definition risk as the primary driver; desks should review each venue's specific resolution source before treating this as a clean arbitrage.
