---
signal_id: "CMSIG20260810DV01"
signal_slug: "applied-intuition-ipo-k9-p15"
headline: "Applied Intuition IPO before 2027: Kalshi 9% vs Polymarket 16%, 7pp gap"
semantic_title: "Applied Intuition IPO odds trade far apart across venues"
telemetry: "Polymarket 16% vs Kalshi 9%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-08-10T09:15:39+00:00"
event_id: "CM-EVT-858NYLKF97"
event_slug: "kxipo-26"
event_question: "Applied Intuition IPO before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x76d92e422d9a4c1d9ceeea7445fa709df9df03e45b6372623abec7254caee3a9"
  question_raw: "Applied Intuition IPO before 2027?"
  current_price: 0.157
  volume_cumulative_usd: 205870.78790399997
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXIPO-26-AINTUITION"
    question_raw: "Who will IPO before 2027?"
    current_price: 0.09
bullets:
  - "Polymarket prices an Applied Intuition IPO before 2027 at 16% vs Kalshi's 9%, a 7pp divergence."
  - "Polymarket holds the higher price backed by over $205.8K in volume; Kalshi shows just $2.2K, making it a thin, potentially stale market."
  - "Polymarket's much deeper liquidity makes its 16% the more credible signal; Kalshi's low volume suggests the contract may not have attracted informed participants."
  - "Resolution requires a completed Applied Intuition public offering before Jan 1, 2027, a binary, unambiguous trigger."
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
    retrieved_at: "2026-08-10T09:15:39+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With Kalshi's volume nearly 100x smaller, the 7pp gap is most likely a liquidity artifact rather than a genuine information difference, a desk should weight Polymarket's 16% as the more reliable estimate.
