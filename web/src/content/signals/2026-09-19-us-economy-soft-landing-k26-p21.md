---
signal_id: "CMSIG20260919DV03"
signal_slug: "us-economy-soft-landing-k26-p21"
headline: "U.S. economy in recession end-2026: Kalshi 27% vs Polymarket 21%"
semantic_title: "Economy-in-recession call for end-2026 diverges across venues"
telemetry: "Polymarket 21% vs Kalshi 27%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-09-19T07:48:36+00:00"
event_id: "CM-EVT-ZRG5DFDMZ8"
event_slug: "kxeconpath-26"
event_question: "State of the economy at the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x50e3ee8f93a464d04ea2cea6efff45c902f43642aedbf43f7afdc899e10f71d8"
  question_raw: "Will the US economy be in a soft landing at the end of 2026?"
  current_price: 0.21
  volume_cumulative_usd: 40595.527307000004
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXECONPATH-26-SOFT"
    question_raw: "State of the economy at the end of 2026?"
    current_price: 0.268
bullets:
  - "Kalshi prices a recessionary economy at end-2026 at 27%, Polymarket at 21%, a 6pp gap."
  - "Kalshi is the higher venue; Polymarket holds roughly 6x more cumulative volume at $41K vs $7K."
  - "Resolution criteria may differ between venues on what constitutes a 'recession' state, which could independently explain part of the spread."
  - "Resolves based on prevailing economic conditions assessed at end of calendar year 2026."
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
      kalshi_vol_24h_usd: 149.39
      poly_vol_24h_usd: 100.416668
sources:
  - label: "ClearMarket cross-venue record: State of the economy at the end of 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-soft-landing-y-2026"
    retrieved_at: "2026-09-19T07:48:36+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Unlike pure binary IPO claims, ambiguous resolution language on an 'economy state' question can legitimately widen spreads, desks should examine each venue's resolution rules before treating the 6pp as pure arbitrage.
