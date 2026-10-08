---
signal_id: "CMSIG20261008DV00"
signal_slug: "discord-ipo-k12-p4"
headline: "Discord IPO before 2027: Kalshi 12% vs Polymarket 5%"
semantic_title: "Discord IPO odds split sharply across venues before 2027"
telemetry: "Polymarket 5% vs Kalshi 12%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-08T07:49:35+00:00"
event_id: "CM-EVT-858NYLKF97"
event_slug: "kxipo-26"
event_question: "Discord IPO before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x48fcbf6bb8eceff817ba48b56211e4f8a4cf6896570d847d8d115e63c3abf36a"
  question_raw: "Discord IPO before 2027?"
  current_price: 0.048
  volume_cumulative_usd: 487506.12681999995
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXIPO-26-DISCORD"
    question_raw: "Who will IPO before 2027?"
    current_price: 0.12
bullets:
  - "Kalshi prices the event at 12%, Polymarket at 5%, a 7pp gap on the same claim."
  - "Kalshi sits higher with cumulative volume near $16K; Polymarket holds lower with over $487K traded."
  - "Polymarket's deeper liquidity likely reflects a more informed consensus, Kalshi's thin book may be driving the premium."
  - "Resolution requires a confirmed Discord IPO filing or listing before January 1, 2027, roughly 85 days remain."
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
      kalshi_vol_24h_usd: 100.12
      poly_vol_24h_usd: 0.0
sources:
  - label: "ClearMarket cross-venue record: Discord IPO before 2027?"
    url: "https://clearmarket.fyi/compare/discord-ipo-y-2026"
    retrieved_at: "2026-10-08T07:49:35+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With under three months to resolution and Polymarket's far larger book pricing this near-zero, the 7pp gap looks like a liquidity artifact on Kalshi rather than a genuine information difference, a desk with cross-venue access could lean on the Polymarket side.
