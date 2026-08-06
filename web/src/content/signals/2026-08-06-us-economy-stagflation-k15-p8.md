---
signal_id: "CMSIG20260806DV04"
signal_slug: "us-economy-stagflation-k15-p8"
headline: "U.S. strong-growth economy end-2026: Kalshi 15% vs Polymarket 8%"
semantic_title: "Strong-growth economy odds stay wide across venues"
telemetry: "Polymarket 8% vs Kalshi 15%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-08-06T10:36:44+00:00"
event_id: "CM-EVT-ZRG5DFDMZ8"
event_slug: "kxeconpath-26"
event_question: "State of the economy at the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x9b1804352d6246bc8b609bc05a3021134269c133bda15e76e05f844539b59774"
  question_raw: "Will the US economy be in stagflation at the end of 2026?"
  current_price: 0.085
  volume_cumulative_usd: 10052.124928000001
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXECONPATH-26-STAG"
    question_raw: "State of the economy at the end of 2026?"
    current_price: 0.15
bullets:
  - "Kalshi prices a strong-growth economy outcome at 15%; Polymarket at 8%, a 6pp gap on a low-probability outcome."
  - "Kalshi holds the higher price on $4K volume; Polymarket is lower with $10K behind it."
  - "On a sub-20% claim, a 6pp spread is proportionally large and likely reflects differing audience priors or resolution-criteria ambiguity rather than genuine information."
  - "Resolution depends on the specific macro threshold each venue defines for 'strong growth' at year-end 2026."
atomic_claims:
  - type: "cross_venue_spread"
    provenance: "CM cross-venue link (question_id CMX-DF50C877D3); prices direct from venue APIs"
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
      poly_vol_24h_usd: 0.0
sources:
  - label: "ClearMarket cross-venue record: State of the economy at the end of 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-stagflation-y-2026"
    retrieved_at: "2026-08-06T10:36:44+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 6pp spread at these low probability levels is proportionally significant and signals that resolution language differences, not informed disagreement, are the primary driver; desks should clarify contract specs before taking a position.
