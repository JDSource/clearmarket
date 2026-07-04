---
signal_id: "CMSIG20260704DV03"
signal_slug: "applied-intuition-ipo-k11-p18"
headline: "Applied Intuition IPO before 2027: Kalshi 11% vs Polymarket 18%"
semantic_title: "Applied Intuition IPO decouples across venues on thin flow"
telemetry: "Polymarket 18% vs Kalshi 11%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-07-04T10:06:13+00:00"
event_id: "CM-EVT-858NYLKF97"
event_slug: "kxipo-26"
event_question: "Applied Intuition IPO before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x76d92e422d9a4c1d9ceeea7445fa709df9df03e45b6372623abec7254caee3a9"
  question_raw: "Applied Intuition IPO before 2027?"
  current_price: 0.185
  volume_cumulative_usd: 205297.0835039999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXIPO-26-AINTUITION"
    question_raw: "Who will IPO before 2027?"
    current_price: 0.11
bullets:
  - "Polymarket marks Applied Intuition IPO at 18%, Kalshi at 11%, an 8pp gap on the same claim."
  - "Polymarket is the higher side and holds the overwhelming share of traded volume."
  - "Kalshi's near-empty book means its 11% print carries little price-discovery weight."
  - "Resolution requires a completed Applied Intuition public listing before Jan 1, 2027."
atomic_claims:
  - type: "cross_venue_spread"
    provenance: "CM cross-venue link (question_id CMX-52E2DEB126); prices direct from venue APIs"
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
      kalshi_vol_24h_usd: 0.0
      poly_vol_24h_usd: 0.0
sources:
  - label: "ClearMarket cross-venue record: Applied Intuition IPO before 2027?"
    url: "https://clearmarket.fyi/compare/applied-intuition-ipo-y-2026"
    retrieved_at: "2026-07-04T10:06:13+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With Kalshi volume negligible, the divergence is largely a function of illiquidity rather than genuine belief disagreement, Polymarket's 18% is the only operationally credible price for a desk.
