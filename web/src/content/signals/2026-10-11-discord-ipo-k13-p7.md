---
signal_id: "CMSIG20261011DV00"
signal_slug: "discord-ipo-k13-p7"
headline: "Discord IPO before 2027: Kalshi 13% vs Polymarket 8%"
semantic_title: "Discord IPO odds carry a premium across venues"
telemetry: "Polymarket 8% vs Kalshi 13%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-11T07:49:16+00:00"
event_id: "CM-EVT-858NYLKF97"
event_slug: "kxipo-26"
event_question: "Discord IPO before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x48fcbf6bb8eceff817ba48b56211e4f8a4cf6896570d847d8d115e63c3abf36a"
  question_raw: "Discord IPO before 2027?"
  current_price: 0.078
  volume_cumulative_usd: 490547.338278
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXIPO-26-DISCORD"
    question_raw: "Who will IPO before 2027?"
    current_price: 0.13
bullets:
  - "Kalshi prices Discord IPO before 2027 at 13%; Polymarket at 8%, a 5pp gap with under 3 months to resolution."
  - "Kalshi is the higher-priced venue; Polymarket carries substantially deeper liquidity on this contract."
  - "Thin volume on Kalshi may allow the elevated price to persist; Polymarket's larger pool likely reflects a more stress-tested consensus."
  - "Resolves YES if Discord completes an IPO before Jan 1, 2027; no partial credit for filing or S-1 submission."
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
      kalshi_vol_24h_usd: 97.03
      poly_vol_24h_usd: 1571.962432
sources:
  - label: "ClearMarket cross-venue record: Discord IPO before 2027?"
    url: "https://clearmarket.fyi/compare/discord-ipo-y-2026"
    retrieved_at: "2026-10-11T07:49:16+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 5pp spread with resolution weeks away flags a pricing inefficiency likely driven by Kalshi's shallow liquidity rather than any genuine information asymmetry, making the Polymarket level the more defensible reference for a desk assessing true odds.
