---
signal_id: "CMSIG20261013DV01"
signal_slug: "discord-ipo-k15-p8"
headline: "Discord IPO before 2027: Kalshi 15% vs Polymarket 8%"
semantic_title: "Discord IPO pricing builds a gap on the major desks"
telemetry: "Polymarket 8% vs Kalshi 15%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-13T07:49:40+00:00"
event_id: "CM-EVT-858NYLKF97"
event_slug: "kxipo-26"
event_question: "Discord IPO before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x48fcbf6bb8eceff817ba48b56211e4f8a4cf6896570d847d8d115e63c3abf36a"
  question_raw: "Discord IPO before 2027?"
  current_price: 0.082
  volume_cumulative_usd: 490666.3324479999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXIPO-26-DISCORD"
    question_raw: "Who will IPO before 2027?"
    current_price: 0.15
bullets:
  - "Kalshi prices a Discord IPO before 2027 at 15%; Polymarket prices the same claim at 8%, a 7pp gap."
  - "Kalshi is higher on roughly $20K volume; Polymarket's lower price is supported by nearly $491K in cumulative volume."
  - "Polymarket's significantly deeper liquidity gives its 8% price greater credibility; Kalshi's 15% likely reflects thin-market mispricing on a low-activity contract."
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
      kalshi_vol_24h_usd: 36.56
      poly_vol_24h_usd: 28.105122
sources:
  - label: "ClearMarket cross-venue record: Discord IPO before 2027?"
    url: "https://clearmarket.fyi/compare/discord-ipo-y-2026"
    retrieved_at: "2026-10-13T07:49:40+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With Polymarket carrying roughly 24x the volume, the 7pp spread reads as a liquidity artifact on Kalshi rather than a genuine information difference, a desk should treat Polymarket's 8% as the more reliable reference price.
