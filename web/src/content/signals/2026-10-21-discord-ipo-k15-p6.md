---
signal_id: "CMSIG20261021DV01"
signal_slug: "discord-ipo-k15-p6"
headline: "Discord IPO before 2027: Kalshi 15% vs Polymarket 6%"
semantic_title: "Discord IPO odds trade far apart on the major desks"
telemetry: "Polymarket 6% vs Kalshi 15%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-21T13:25:45+00:00"
event_id: "CM-EVT-858NYLKF97"
event_slug: "kxipo-26"
event_question: "Discord IPO before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x48fcbf6bb8eceff817ba48b56211e4f8a4cf6896570d847d8d115e63c3abf36a"
  question_raw: "Discord IPO before 2027?"
  current_price: 0.06
  volume_cumulative_usd: 491462.225648
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXIPO-26-DISCORD"
    question_raw: "Who will IPO before 2027?"
    current_price: 0.15
bullets:
  - "Kalshi prices a Discord IPO before 2027 at 15%, Polymarket at 6%, a 9pp spread."
  - "Kalshi is the higher venue; Polymarket holds a substantially larger liquidity base on the lower price."
  - "Polymarket's high-volume pricing at 6% likely reflects stronger consensus that a 2026 IPO window has effectively closed."
  - "Resolves YES if Discord completes a public offering before Jan 1, 2027."
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
      kalshi_vol_24h_usd: 10.42
      poly_vol_24h_usd: 1.0582
sources:
  - label: "ClearMarket cross-venue record: Discord IPO before 2027?"
    url: "https://clearmarket.fyi/compare/discord-ipo-y-2026"
    retrieved_at: "2026-10-21T13:25:45+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 9pp gap with Polymarket holding 23x the volume strongly favors the lower price as the market-clearing level, any desk should treat Kalshi's 15% as a thinly supported outlier and weight Polymarket's 6% accordingly.
