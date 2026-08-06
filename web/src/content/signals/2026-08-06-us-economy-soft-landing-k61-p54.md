---
signal_id: "CMSIG20260806DV02"
signal_slug: "us-economy-soft-landing-k61-p54"
headline: "U.S. economy in recession end-2026: Kalshi 61% vs Polymarket 54%"
semantic_title: "Economy-in-recession odds build a premium on one venue"
telemetry: "Polymarket 54% vs Kalshi 61%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-08-06T10:36:44+00:00"
event_id: "CM-EVT-ZRG5DFDMZ8"
event_slug: "kxeconpath-26"
event_question: "State of the economy at the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x50e3ee8f93a464d04ea2cea6efff45c902f43642aedbf43f7afdc899e10f71d8"
  question_raw: "Will the US economy be in a soft landing at the end of 2026?"
  current_price: 0.54
  volume_cumulative_usd: 30456.587993
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXECONPATH-26-SOFT"
    question_raw: "State of the economy at the end of 2026?"
    current_price: 0.61
bullets:
  - "Kalshi prices a recession outcome at 61%; Polymarket at 54%, a 7pp gap."
  - "Kalshi holds the higher price on $11K volume; Polymarket is lower with $30K in volume."
  - "Differing resolution criteria, Kalshi and Polymarket may use different official recession definitions, likely drives part of the spread."
  - "Resolution typically tied to NBER declaration or GDP prints, though each venue's rules may specify different triggers."
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
      kalshi_vol_24h_usd: 6.1
      poly_vol_24h_usd: 27.79
sources:
  - label: "ClearMarket cross-venue record: State of the economy at the end of 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-soft-landing-y-2026"
    retrieved_at: "2026-08-06T10:36:44+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 7pp gap on a macro claim with moderate liquidity on both sides suggests venues are reading different resolution standards; desks should audit each contract's definition before acting.
