---
signal_id: "CMSIG20260814DV01"
signal_slug: "globalfoundries-us-government-stake-k74-p85"
headline: "US gov stake in GlobalFoundries: Kalshi 74% vs Polymarket 85%"
semantic_title: "GlobalFoundries federal stake trades far apart on major desks"
telemetry: "Kalshi 74% vs Polymarket 85%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-08-14T09:05:25+00:00"
event_id: "CM-EVT-TDJHRGQTY1"
event_slug: "kxusacompanystake-27jan01"
event_question: "Will any part of the United States federal government take a stake of above 0% in GlobalFoundries?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXUSACOMPANYSTAKE-27JAN01-GFS"
  question_raw: "Will any part of the United States federal government take a stake of above 0% in GlobalFoundries?"
  current_price: 0.74
  volume_cumulative_usd: 20537.02
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-01T15:00:00Z"
related_markets:
  - platform: "polymarket"
    platform_market_id: "0x29de69eea09afcb0cde8301eca3e6fcabf826dcb8a8dafacc0d20f3404a735ff"
    question_raw: "Will the US federal government take a stake in GlobalFoundries Inc.?"
    current_price: 0.851
bullets:
  - "Polymarket prices US government stake at 85%, Kalshi at 74%, an 11pp gap"
  - "Polymarket is higher at 85% on lighter volume; Kalshi sits lower at 74% on a moderately larger book"
  - "Polymarket may be pricing in a broader definition of 'stake'; resolution mechanic ambiguity could drive the spread"
  - "Resolves YES if any federal entity acquires any ownership share above 0% in GlobalFoundries"
atomic_claims:
  - type: "cross_venue_spread"
    provenance: "CM cross-venue link (question_id CMX-64E6FFD2DB); prices direct from venue APIs"
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
      kalshi_vol_24h_usd: 140.6
      poly_vol_24h_usd: 6.89655
sources:
  - label: "ClearMarket cross-venue record: Will any part of the United States federal government take a"
    url: "https://clearmarket.fyi/compare/globalfoundries-us-government-stake-y-2026"
    retrieved_at: "2026-08-14T09:05:25+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

An 11pp gap with Polymarket running hotter on thinner liquidity points to a definitional mismatch on what counts as a federal stake, a desk should stress-test the resolution criteria before leaning on either price.
