---
signal_id: "CMSIG20260824DV02"
signal_slug: "us-economy-soft-landing-k55-p61"
headline: "U.S. economy healthy end of 2026? Kalshi 55% vs Polymarket 61%"
semantic_title: "Economy-state outlook builds a modest lead on one venue"
telemetry: "Polymarket 61% vs Kalshi 55%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-08-24T08:43:09+00:00"
event_id: "CM-EVT-ZRG5DFDMZ8"
event_slug: "kxeconpath-26"
event_question: "State of the economy at the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x50e3ee8f93a464d04ea2cea6efff45c902f43642aedbf43f7afdc899e10f71d8"
  question_raw: "Will the US economy be in a soft landing at the end of 2026?"
  current_price: 0.61
  volume_cumulative_usd: 33156.042778
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXECONPATH-26-SOFT"
    question_raw: "State of the economy at the end of 2026?"
    current_price: 0.551
bullets:
  - "Kalshi prices a healthy economy at end-2026 at 55%, Polymarket at 61%, a 6pp gap."
  - "Polymarket carries the higher price on ~$33K volume; Kalshi sits lower on ~$12K cumulative volume."
  - "The gap may reflect differing resolution criteria between venues, how each platform defines 'healthy' drives meaningful price distance."
  - "Resolves based on each platform's stated economic indicator or adjudication standard at end of 2026."
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
      poly_vol_24h_usd: 117.86
sources:
  - label: "ClearMarket cross-venue record: State of the economy at the end of 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-soft-landing-y-2026"
    retrieved_at: "2026-08-24T08:43:09+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 6pp divergence on a subjective macro claim is likely driven by definitional differences in resolution language across platforms rather than opposing views on the economy, a desk should reconcile each venue's resolution criteria before acting on the spread.
