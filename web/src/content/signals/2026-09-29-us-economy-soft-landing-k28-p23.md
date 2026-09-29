---
signal_id: "CMSIG20260929DV01"
signal_slug: "us-economy-soft-landing-k28-p23"
headline: "Economy state end-2026 (recession): Kalshi 29% vs Polymarket 23%"
semantic_title: "End-of-2026 recession odds back higher on the smaller venue"
telemetry: "Polymarket 23% vs Kalshi 29%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-09-29T14:35:30+00:00"
event_id: "CM-EVT-ZRG5DFDMZ8"
event_slug: "kxeconpath-26"
event_question: "State of the economy at the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x50e3ee8f93a464d04ea2cea6efff45c902f43642aedbf43f7afdc899e10f71d8"
  question_raw: "Will the US economy be in a soft landing at the end of 2026?"
  current_price: 0.23
  volume_cumulative_usd: 46974.982906000005
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXECONPATH-26-SOFT"
    question_raw: "State of the economy at the end of 2026?"
    current_price: 0.288
bullets:
  - "Kalshi prices a poor economic outcome at 29%, Polymarket at 23%, a 6pp gap on the same year-end resolution."
  - "Kalshi is higher; Polymarket holds roughly six times the liquidity at $47K vs Kalshi's $8.4K."
  - "Divergence likely reflects different question wording or outcome-bucket definitions across venues rather than a true crowd disagreement."
  - "Resolution hinges on how each platform operationalizes 'state of the economy', wording ambiguity is the primary spread driver here."
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
      kalshi_vol_24h_usd: 1.44
      poly_vol_24h_usd: 20.033158
sources:
  - label: "ClearMarket cross-venue record: State of the economy at the end of 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-soft-landing-y-2026"
    retrieved_at: "2026-09-29T14:35:30+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 6pp split on a macro sentiment claim with mismatched liquidity signals that definitional friction between the two contracts, not new information, is the dominant spread driver, so direct arbitrage carries meaningful resolution risk.
