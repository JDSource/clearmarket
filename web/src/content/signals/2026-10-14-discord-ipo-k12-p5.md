---
signal_id: "CMSIG20261014DV01"
signal_slug: "discord-ipo-k12-p5"
headline: "Discord IPO before 2027: Kalshi 12% vs Polymarket 6%"
semantic_title: "Discord IPO before 2027 trades far apart on the major prediction desks"
telemetry: "Polymarket 6% vs Kalshi 12%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-14T07:49:05+00:00"
event_id: "CM-EVT-858NYLKF97"
event_slug: "kxipo-26"
event_question: "Discord IPO before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x48fcbf6bb8eceff817ba48b56211e4f8a4cf6896570d847d8d115e63c3abf36a"
  question_raw: "Discord IPO before 2027?"
  current_price: 0.057
  volume_cumulative_usd: 490801.0024479999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXIPO-26-DISCORD"
    question_raw: "Who will IPO before 2027?"
    current_price: 0.12
bullets:
  - "Kalshi prices a Discord IPO at 12%, Polymarket at 6%, a 6pp spread on an already low-probability claim."
  - "Kalshi is higher; Polymarket holds roughly 30 times the cumulative volume, making it the more liquid reference."
  - "Kalshi's thinner book is more susceptible to drift; Polymarket's 6% likely reflects a well-informed crowd with little new IPO-window catalyst."
  - "Resolution requires a completed Discord IPO listing on a public exchange before January 1, 2027."
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
      kalshi_vol_24h_usd: 7.39
      poly_vol_24h_usd: 134.67
sources:
  - label: "ClearMarket cross-venue record: Discord IPO before 2027?"
    url: "https://clearmarket.fyi/compare/discord-ipo-y-2026"
    retrieved_at: "2026-10-14T07:49:05+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With Polymarket running 30x the volume at half the probability, a desk should treat the 6% Polymarket print as the anchor and view Kalshi's 12% as a thin-book artifact rather than genuine signal.
