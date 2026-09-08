---
signal_id: "CMSIG20260908DV00"
signal_slug: "discord-ipo-k24-p8"
headline: "Discord IPO before 2027: Kalshi 24% vs Polymarket 9%"
semantic_title: "Discord IPO odds split sharply across venues"
telemetry: "Polymarket 9% vs Kalshi 24%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-09-08T12:35:19+00:00"
event_id: "CM-EVT-858NYLKF97"
event_slug: "kxipo-26"
event_question: "Discord IPO before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x48fcbf6bb8eceff817ba48b56211e4f8a4cf6896570d847d8d115e63c3abf36a"
  question_raw: "Discord IPO before 2027?"
  current_price: 0.086
  volume_cumulative_usd: 476860.83021399984
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXIPO-26-DISCORD"
    question_raw: "Who will IPO before 2027?"
    current_price: 0.24
bullets:
  - "Kalshi prices Discord IPO before 2027 at 24%; Polymarket at 9%, a 15pp gap."
  - "Kalshi sits higher with cumulative volume near $30K; Polymarket carries the deeper book at roughly $477K."
  - "Polymarket's larger liquidity base likely reflects broader consensus; Kalshi's thin volume may amplify an outlier position."
  - "Resolves YES if Discord completes an IPO or direct listing before January 1, 2027."
atomic_claims:
  - type: "cross_venue_spread"
    provenance: "CM cross-venue link (question_id CMX-26DA00133D); prices direct from venue APIs"
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
      kalshi_vol_24h_usd: 27.79
      poly_vol_24h_usd: 472.724509
sources:
  - label: "ClearMarket cross-venue record: Discord IPO before 2027?"
    url: "https://clearmarket.fyi/compare/discord-ipo-y-2026"
    retrieved_at: "2026-09-08T12:35:19+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 15pp spread with heavily asymmetric liquidity suggests Kalshi's elevated print is a thin-book artifact rather than a genuine information signal, a desk leaning on Polymarket's deeper pool as the more credible reference price would treat Kalshi's 24% as a potential short opportunity if cross-venue arbitrage mechanics allow it.
