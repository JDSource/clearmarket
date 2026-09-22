---
signal_id: "CMSIG20260922DV02"
signal_slug: "us-economy-soft-landing-k25-p19"
headline: "US economy strong end of 2026: Kalshi 25% vs Polymarket 19%"
semantic_title: "Economy-state outlook trades apart on the major desks"
telemetry: "Polymarket 19% vs Kalshi 25%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-09-22T07:49:09+00:00"
event_id: "CM-EVT-ZRG5DFDMZ8"
event_slug: "kxeconpath-26"
event_question: "State of the economy at the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x50e3ee8f93a464d04ea2cea6efff45c902f43642aedbf43f7afdc899e10f71d8"
  question_raw: "Will the US economy be in a soft landing at the end of 2026?"
  current_price: 0.19
  volume_cumulative_usd: 43456.89845
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXECONPATH-26-SOFT"
    question_raw: "State of the economy at the end of 2026?"
    current_price: 0.25
bullets:
  - "Kalshi prices the strong-economy outcome at 25%, Polymarket at 19%, a 6pp spread."
  - "Kalshi is the higher venue; Polymarket carries roughly 6x more cumulative volume."
  - "Ambiguous resolution criteria ('state of economy') may be read differently across platforms, partly explaining the divergence."
  - "Claim resolves on an assessed economic condition by end of 2026, subjective framing raises basis risk."
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
      kalshi_vol_24h_usd: 283.3
      poly_vol_24h_usd: 2382.9151680000004
sources:
  - label: "ClearMarket cross-venue record: State of the economy at the end of 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-soft-landing-y-2026"
    retrieved_at: "2026-09-22T07:49:09+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 6pp gap on a qualitatively defined claim suggests that resolution-criteria ambiguity is amplifying the spread as much as genuine probability disagreement, a desk should scrutinize the exact resolver and methodology before treating either price as a clean signal.
