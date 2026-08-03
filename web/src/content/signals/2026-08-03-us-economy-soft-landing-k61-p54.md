---
signal_id: "CMSIG20260803DV01"
signal_slug: "us-economy-soft-landing-k61-p54"
headline: "Economy strong end-2026: Kalshi 62% vs Polymarket 54%"
semantic_title: "Economy-state outlook builds a premium on one major desk"
telemetry: "Polymarket 54% vs Kalshi 62%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-08-03T11:19:40+00:00"
event_id: "CM-EVT-ZRG5DFDMZ8"
event_slug: "kxeconpath-26"
event_question: "State of the economy at the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x50e3ee8f93a464d04ea2cea6efff45c902f43642aedbf43f7afdc899e10f71d8"
  question_raw: "Will the US economy be in a soft landing at the end of 2026?"
  current_price: 0.54
  volume_cumulative_usd: 30419.807992999995
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXECONPATH-26-SOFT"
    question_raw: "State of the economy at the end of 2026?"
    current_price: 0.617
bullets:
  - "Kalshi prices a strong economy at end-2026 at 62%, Polymarket at 54%, an 8pp gap."
  - "Kalshi is higher at $11,475 volume; Polymarket is lower at $30,420 volume."
  - "Subjective resolution language may drive divergence, venues may interpret 'strong economy' differently in their rule sets."
  - "Resolution likely tied to GDP, unemployment, or editorial economic benchmarks at year-end 2026."
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
      kalshi_vol_24h_usd: 4.86
      poly_vol_24h_usd: 366.86666499999995
sources:
  - label: "ClearMarket cross-venue record: State of the economy at the end of 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-soft-landing-y-2026"
    retrieved_at: "2026-08-03T11:19:40+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

An 8pp spread on a qualitatively worded claim signals that ambiguous resolution criteria are distorting prices differently across venues, making mid-market averaging unreliable for a desk.
