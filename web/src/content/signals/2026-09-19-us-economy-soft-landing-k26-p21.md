---
signal_id: "CMSIG20260919DV02"
signal_slug: "us-economy-soft-landing-k26-p21"
headline: "Economy in recession end-2026: Kalshi 27% vs Polymarket 21%"
semantic_title: "U.S. economy outlook for end-2026 diverges on the major desks"
telemetry: "Polymarket 21% vs Kalshi 27%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-09-19T12:16:09+00:00"
event_id: "CM-EVT-ZRG5DFDMZ8"
event_slug: "kxeconpath-26"
event_question: "State of the economy at the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x50e3ee8f93a464d04ea2cea6efff45c902f43642aedbf43f7afdc899e10f71d8"
  question_raw: "Will the US economy be in a soft landing at the end of 2026?"
  current_price: 0.21
  volume_cumulative_usd: 40595.52730700001
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXECONPATH-26-SOFT"
    question_raw: "State of the economy at the end of 2026?"
    current_price: 0.268
bullets:
  - "6pp gap: Kalshi prices the negative economy outcome at 27%, Polymarket at 21% for end-2026."
  - "Kalshi is higher; Polymarket holds roughly 5.6x more cumulative volume, giving its reading more weight."
  - "Ambiguity in resolution criteria, how 'state of the economy' is defined, may drive audience-specific interpretation differences between the two venues."
  - "Resolution likely tied to official GDP, NBER, or designated index readings at or before Dec 31, 2026."
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
    retrieved_at: "2026-09-19T12:16:09+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 6pp spread on a loosely defined claim suggests resolution-criteria ambiguity is doing most of the work; a desk should flag that contract language differences, not pure information, may be driving the gap.
