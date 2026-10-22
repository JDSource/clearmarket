---
signal_id: "CMSIG20261022DV00"
signal_slug: "discord-ipo-k12-p6"
headline: "Discord IPO before 2027: Kalshi 12% vs Polymarket 7%"
semantic_title: "Discord IPO odds run higher on one venue than the other"
telemetry: "Polymarket 7% vs Kalshi 12%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-22T13:26:05+00:00"
event_id: "CM-EVT-858NYLKF97"
event_slug: "kxipo-26"
event_question: "Discord IPO before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x48fcbf6bb8eceff817ba48b56211e4f8a4cf6896570d847d8d115e63c3abf36a"
  question_raw: "Discord IPO before 2027?"
  current_price: 0.066
  volume_cumulative_usd: 491593.302618
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXIPO-26-DISCORD"
    question_raw: "Who will IPO before 2027?"
    current_price: 0.12
bullets:
  - "Kalshi prices the Discord IPO before 2027 at 12%, while Polymarket sits at 7%, a 5pp gap."
  - "Kalshi is the higher-priced venue; Polymarket carries far deeper liquidity at $491K cumulative volume vs $16K on Kalshi."
  - "Thin Kalshi volume may reflect a small pool of optimistic participants not yet arbitraged down; Polymarket's larger crowd puts long odds against a 2026 listing."
  - "Resolution requires a completed Discord IPO on a major exchange before January 1, 2027, roughly 10 weeks remain."
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
      kalshi_vol_24h_usd: 17.04
      poly_vol_24h_usd: 131.07697
sources:
  - label: "ClearMarket cross-venue record: Discord IPO before 2027?"
    url: "https://clearmarket.fyi/compare/discord-ipo-y-2026"
    retrieved_at: "2026-10-22T13:26:05+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 5pp spread, combined with Polymarket's 30x liquidity advantage, suggests the Kalshi price is more likely a thin-book artifact than informed conviction, a desk leaning on the higher-volume venue would treat 7% as the more reliable anchor.
