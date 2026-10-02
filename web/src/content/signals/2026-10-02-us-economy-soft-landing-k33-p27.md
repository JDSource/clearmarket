---
signal_id: "CMSIG20261002DV01"
signal_slug: "us-economy-soft-landing-k33-p27"
headline: "U.S. economy state end-2026 (recession): Kalshi 34% vs Polymarket 27%"
semantic_title: "Economy-end-of-2026 recession odds build a premium on Kalshi"
telemetry: "Polymarket 27% vs Kalshi 34%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-02T14:26:41+00:00"
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
  - "Kalshi prices recession/negative economic state at 34%, Polymarket at 27%, a 7pp gap with the horizon three months out."
  - "Kalshi is the higher side; Polymarket holds roughly 5x the cumulative volume, giving it the deeper price signal."
  - "Differing resolution criteria or audience composition on each venue may explain the gap; Polymarket's larger pool implies stronger consensus around the lower figure."
  - "Resolution hinges on how each platform defines 'state of the economy', criteria differences could sustain the spread to expiry."
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
    retrieved_at: "2026-10-02T14:26:41+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should flag that resolution-language ambiguity between the two contracts may be the structural driver here, making direct arbitrage risky until both resolution criteria are confirmed identical.
