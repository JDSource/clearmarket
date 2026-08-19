---
signal_id: "CMSIG20260819DV02"
signal_slug: "us-economy-soft-landing-k59-p65"
headline: "Economy strong at end of 2026: Kalshi 59% vs Polymarket 65%"
semantic_title: "Economy-state odds hold apart across the major prediction desks"
telemetry: "Polymarket 65% vs Kalshi 59%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-08-19T08:32:47+00:00"
event_id: "CM-EVT-ZRG5DFDMZ8"
event_slug: "kxeconpath-26"
event_question: "State of the economy at the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x50e3ee8f93a464d04ea2cea6efff45c902f43642aedbf43f7afdc899e10f71d8"
  question_raw: "Will the US economy be in a soft landing at the end of 2026?"
  current_price: 0.65
  volume_cumulative_usd: 32839.38277800001
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXECONPATH-26-SOFT"
    question_raw: "State of the economy at the end of 2026?"
    current_price: 0.59
bullets:
  - "Polymarket prices a strong economy at end-2026 at 65%, Kalshi at 59%, a 6pp gap."
  - "Polymarket is higher and carries roughly 2.6x more cumulative volume than Kalshi."
  - "Differing resolution criteria between venues is the most plausible driver; how 'strong' is defined matters enormously here."
  - "Resolves based on each platform's stated economic benchmark at Dec 31, 2026."
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
      kalshi_vol_24h_usd: 0.0
      poly_vol_24h_usd: 46.242701
sources:
  - label: "ClearMarket cross-venue record: State of the economy at the end of 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-soft-landing-y-2026"
    retrieved_at: "2026-08-19T08:32:47+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 6pp spread likely reflects definitional ambiguity around 'strong economy' rather than a pure information edge, a desk should reconcile each venue's resolution rules before treating this as a clean arbitrage.
