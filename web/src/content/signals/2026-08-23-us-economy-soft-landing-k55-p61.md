---
signal_id: "CMSIG20260823DV01"
signal_slug: "us-economy-soft-landing-k55-p61"
headline: "US economy rated 'good' end of 2026: Kalshi 55% vs Polymarket 61%"
semantic_title: "Economy-end-of-2026 'good' odds carry a premium on Polymarket"
telemetry: "Polymarket 61% vs Kalshi 55%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-08-23T08:25:08+00:00"
event_id: "CM-EVT-ZRG5DFDMZ8"
event_slug: "kxeconpath-26"
event_question: "State of the economy at the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x50e3ee8f93a464d04ea2cea6efff45c902f43642aedbf43f7afdc899e10f71d8"
  question_raw: "Will the US economy be in a soft landing at the end of 2026?"
  current_price: 0.61
  volume_cumulative_usd: 33038.182777999995
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXECONPATH-26-SOFT"
    question_raw: "State of the economy at the end of 2026?"
    current_price: 0.551
bullets:
  - "Polymarket prices the economy as 'good' by end of 2026 at 61%, Kalshi at 55%, a 6pp spread."
  - "Polymarket sits higher with $33K cumulative volume versus Kalshi's $11K."
  - "Definitional ambiguity in 'state of the economy' likely drives the gap, resolution criteria may differ or be interpreted differently across platforms."
  - "Both markets resolve on an assessable economic benchmark at or before December 31, 2026."
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
      kalshi_vol_24h_usd: 0.61
      poly_vol_24h_usd: 59.14
sources:
  - label: "ClearMarket cross-venue record: State of the economy at the end of 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-soft-landing-y-2026"
    retrieved_at: "2026-08-23T08:25:08+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 6pp spread on a subjective, definition-sensitive claim signals resolution-criteria risk, a desk should scrutinize each venue's exact resolution rules before positioning, as the gap may close or widen purely on adjudication differences.
