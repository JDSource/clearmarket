---
signal_id: "CMSIG20261012DV01"
signal_slug: "discord-ipo-k14-p8"
headline: "Discord IPO before 2027: Kalshi 14% vs Polymarket 8%"
semantic_title: "Discord IPO timeline splits sharply across the major prediction desks"
telemetry: "Polymarket 8% vs Kalshi 14%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-12T17:18:52+00:00"
event_id: "CM-EVT-858NYLKF97"
event_slug: "kxipo-26"
event_question: "Discord IPO before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x48fcbf6bb8eceff817ba48b56211e4f8a4cf6896570d847d8d115e63c3abf36a"
  question_raw: "Discord IPO before 2027?"
  current_price: 0.084
  volume_cumulative_usd: 490654.13732600014
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXIPO-26-DISCORD"
    question_raw: "Who will IPO before 2027?"
    current_price: 0.14
bullets:
  - "Kalshi prices Discord IPO by end-2026 at 14%; Polymarket prices it at 8%, a 6pp spread."
  - "Kalshi reads higher on $18,980 cumulative volume; Polymarket's 8% is backed by $490,654, roughly 26× deeper."
  - "Polymarket's heavily traded 8% is the stronger signal; Kalshi's thin book likely overstates the probability due to low price discovery."
  - "Resolution requires a completed IPO or equivalent public listing event before January 1, 2027."
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
      kalshi_vol_24h_usd: 1.94
      poly_vol_24h_usd: 106.799048
sources:
  - label: "ClearMarket cross-venue record: Discord IPO before 2027?"
    url: "https://clearmarket.fyi/compare/discord-ipo-y-2026"
    retrieved_at: "2026-10-12T17:18:52+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With Polymarket running 26× the liquidity at a notably lower price, a desk should lean on the 8% handle and treat any Kalshi exposure above 10% as an illiquidity-driven mispricing worth fading toward the deeper venue.
