---
signal_id: "CMSIG20260925DV00"
signal_slug: "abstract-token-event-k43-p21"
headline: "Abstract token before 2027: Kalshi 43% vs Polymarket 21%"
semantic_title: "Abstract token launch trades far apart across venues"
telemetry: "Polymarket 21% vs Kalshi 43%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-09-25T07:48:58+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Abstract launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xd008c45c5320e7453b4e7725bda285cd822a3a61adef14759f2aadf0778c64b6"
  question_raw: "Will Abstract launch a token by December 31, 2026"
  current_price: 0.21
  volume_cumulative_usd: 377315.86204800004
  arbitration_model: "uma_oracle"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ABST"
    question_raw: "Will Abstract launch a token before Jan 1, 2027?"
    current_price: 0.43
bullets:
  - "Kalshi prices 43% vs Polymarket 21%, a 22pp gap on the same claim"
  - "Kalshi sits higher with thin volume; Polymarket carries the deeper book by far"
  - "Polymarket's larger crowd likely reflects broader awareness of Abstract's actual roadmap signals"
  - "Resolves YES if Abstract publicly launches a token before Jan 1, 2027"
atomic_claims:
  - type: "cross_venue_spread"
    provenance: "CM cross-venue link (question_id CMX-3E5461019B); prices direct from venue APIs"
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
      kalshi_vol_24h_usd: 6.58
      poly_vol_24h_usd: 0.0
sources:
  - label: "ClearMarket cross-venue record: Will Abstract launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/abstract-token-event-y-2026"
    retrieved_at: "2026-09-25T07:48:58+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 22pp spread with the thinner venue priced more than twice as high suggests Kalshi's market is underdeveloped on this claim, a desk should treat Polymarket's 21% as the more price-discovered reference.
