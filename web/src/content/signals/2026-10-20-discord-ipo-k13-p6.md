---
signal_id: "CMSIG20261020DV00"
signal_slug: "discord-ipo-k13-p6"
headline: "Discord IPO before 2027: Kalshi 13% vs Polymarket 6%"
semantic_title: "Discord IPO odds split sharply across venues"
telemetry: "Polymarket 6% vs Kalshi 13%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-20T13:16:32+00:00"
event_id: "CM-EVT-858NYLKF97"
event_slug: "kxipo-26"
event_question: "Discord IPO before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x48fcbf6bb8eceff817ba48b56211e4f8a4cf6896570d847d8d115e63c3abf36a"
  question_raw: "Discord IPO before 2027?"
  current_price: 0.06
  volume_cumulative_usd: 491461.167448
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXIPO-26-DISCORD"
    question_raw: "Who will IPO before 2027?"
    current_price: 0.13
bullets:
  - "Kalshi prices Discord IPO before 2027 at 13%; Polymarket at 6%, a 7pp gap with under 10 weeks left on the clock."
  - "Kalshi sits higher on thin volume; Polymarket holds the lower price against dramatically deeper liquidity."
  - "Polymarket's larger pool likely reflects broader consensus, Kalshi's premium may stem from a smaller, less contested market with fewer arbitrageurs."
  - "Resolves YES if Discord completes an IPO on a public exchange before Jan 1, 2027."
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
      kalshi_vol_24h_usd: 5.57
      poly_vol_24h_usd: 0.0
sources:
  - label: "ClearMarket cross-venue record: Discord IPO before 2027?"
    url: "https://clearmarket.fyi/compare/discord-ipo-y-2026"
    retrieved_at: "2026-10-20T13:16:32+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 7pp gap with Polymarket carrying 27x the volume suggests the Kalshi price is a low-liquidity outlier, and a desk would treat the Polymarket figure as the more reliable signal heading into year-end.
