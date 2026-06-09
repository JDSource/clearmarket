---
signal_id: "CMSIG20260603DV01"
signal_slug: "anthropic-ipo-k76-p70"
headline: "Anthropic IPO before 2027: Kalshi 76% vs Polymarket 70%"
semantic_title: "Anthropic IPO before 2027 pricing splits across venues"
telemetry: "Polymarket 70% vs Kalshi 76%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-06-03T01:49:11+00:00"
event_id: "CM-EVT-858NYLKF97"
event_slug: "kxipo-26"
event_question: "Anthropic IPO before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x6522024c060166830e53a48b0db1cab9296601a8539ab005124db5e4bf50a303"
  question_raw: "Anthropic IPO before 2027?"
  current_price: 0.7
  volume_cumulative_usd: 249824.4751379992
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXIPO-26-ANTHROPIC"
    question_raw: "Who will IPO before 2027?"
    current_price: 0.76
bullets:
  - "Kalshi prices 76%, Polymarket 70%, a 6pp gap on the same end-2026 horizon."
  - "Kalshi is higher; volume $123,518 vs Polymarket's $249,824, Polymarket roughly 2x more liquid."
  - "With volumes closer in magnitude, divergence may reflect differing resolution standards or retail vs. informed crowd composition."
  - "Resolves YES on completion of a public equity offering; private funding rounds or direct listings may introduce adjudication ambiguity across venues."
atomic_claims:
  - type: "cross_venue_spread"
    provenance: "CM cross-venue link (question_id CMX-4D70594555); prices direct from venue APIs"
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
      kalshi_vol_24h_usd: 481.54
      poly_vol_24h_usd: 1286.915279
sources:
  - label: "ClearMarket cross-venue record: Anthropic IPO before 2027?"
    url: "https://clearmarket.fyi/compare/anthropic-ipo-y-2026"
    retrieved_at: "2026-06-03T01:49:11+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Both venues price high probability, but Kalshi's 6pp premium on roughly half the liquidity warrants scrutiny of whether resolution criteria are aligned before taking a cross-venue position.
