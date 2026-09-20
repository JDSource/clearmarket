---
signal_id: "CMSIG20260920DV01"
signal_slug: "us-economy-soft-landing-k26-p20"
headline: "Economy 'good' end of 2026: Kalshi 27% vs Polymarket 20%"
semantic_title: "Economy-state outlook carries a premium on one venue"
telemetry: "Polymarket 20% vs Kalshi 27%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-09-20T07:48:25+00:00"
event_id: "CM-EVT-ZRG5DFDMZ8"
event_slug: "kxeconpath-26"
event_question: "State of the economy at the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x50e3ee8f93a464d04ea2cea6efff45c902f43642aedbf43f7afdc899e10f71d8"
  question_raw: "Will the US economy be in a soft landing at the end of 2026?"
  current_price: 0.2
  volume_cumulative_usd: 41062.95328200002
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXECONPATH-26-SOFT"
    question_raw: "State of the economy at the end of 2026?"
    current_price: 0.268
bullets:
  - "Kalshi prices a positive economy outcome at 27%, Polymarket at 20%, a 7pp gap."
  - "Kalshi sits higher; Polymarket has roughly six times the cumulative volume on this claim."
  - "Divergence likely reflects differing resolution criteria between platforms, subjective 'state' calls are especially sensitive to oracle ambiguity."
  - "Resolution depends on the designated index or adjudicator each venue uses to classify economic conditions at year-end."
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
      kalshi_vol_24h_usd: 88.24
      poly_vol_24h_usd: 467.42597500000005
sources:
  - label: "ClearMarket cross-venue record: State of the economy at the end of 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-soft-landing-y-2026"
    retrieved_at: "2026-09-20T07:48:25+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Ambiguous resolution language on a subjective macro claim is the most probable driver here; desks should scrutinize each venue's oracle before treating this as a clean arb.
