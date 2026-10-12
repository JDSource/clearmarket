---
signal_id: "CMSIG20261012DV00"
signal_slug: "discord-ipo-k16-p8"
headline: "Discord IPO before 2027: Kalshi 16% vs Polymarket 8%"
semantic_title: "Discord IPO odds split sharply across venues before 2027"
telemetry: "Polymarket 8% vs Kalshi 16%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-12T07:50:58+00:00"
event_id: "CM-EVT-858NYLKF97"
event_slug: "kxipo-26"
event_question: "Discord IPO before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x48fcbf6bb8eceff817ba48b56211e4f8a4cf6896570d847d8d115e63c3abf36a"
  question_raw: "Discord IPO before 2027?"
  current_price: 0.084
  volume_cumulative_usd: 490638.22732599993
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXIPO-26-DISCORD"
    question_raw: "Who will IPO before 2027?"
    current_price: 0.16
bullets:
  - "Kalshi prices Discord IPO at 16%, Polymarket at 8%, an 8pp gap on the same claim."
  - "Kalshi is the higher venue; Polymarket carries roughly 23x more cumulative volume, suggesting deeper consensus on the low side."
  - "Thin Kalshi liquidity may amplify idiosyncratic positioning; Polymarket's larger pool likely reflects a broader informed base."
  - "Resolution requires a confirmed Discord IPO filing or listing before Jan 1, 2027, roughly 80 days remain."
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
      kalshi_vol_24h_usd: 2.38
      poly_vol_24h_usd: 90.88904799999999
sources:
  - label: "ClearMarket cross-venue record: Discord IPO before 2027?"
    url: "https://clearmarket.fyi/compare/discord-ipo-y-2026"
    retrieved_at: "2026-10-12T07:50:58+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The wide spread against a heavily liquid Polymarket low implies Kalshi's 16% may reflect a small-sample skew rather than genuine informational edge, making the long side on Kalshi the riskier leg for any desk considering a cross-venue arb.
