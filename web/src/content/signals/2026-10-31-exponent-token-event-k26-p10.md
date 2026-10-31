---
signal_id: "CMSIG20261031DV00"
signal_slug: "exponent-token-event-k26-p10"
headline: "Exponent token before 2027: Kalshi 26% vs Polymarket 10%"
semantic_title: "Exponent token launch odds split sharply across venues"
telemetry: "Polymarket 10% vs Kalshi 26%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-31T14:17:31+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Exponent launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x411d2f1251d86d9a4f30186c660745c597d18a19737fd8f7b4ee1483ece9ffde"
  question_raw: "Will Exponent launch a token by December 31, 2026?"
  current_price: 0.1
  volume_cumulative_usd: 359334.40975200007
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-EXPO"
    question_raw: "Will Exponent launch a token before Jan 1, 2027?"
    current_price: 0.26
bullets:
  - "Kalshi prices the launch at 26%, Polymarket at 10%, a 16pp gap with two months left on the clock."
  - "Kalshi sits higher on thin volume; Polymarket holds the lower read on dramatically deeper liquidity."
  - "Polymarket's crowd is likely more informed on crypto project timelines; the smaller Kalshi pool may reflect noise rather than signal."
  - "Resolution: contract settles YES if Exponent publicly launches a token before Jan 1, 2027."
atomic_claims:
  - type: "cross_venue_spread"
    provenance: "CM cross-venue link (question_id CMX-B8681B67DA); prices direct from venue APIs"
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
      kalshi_vol_24h_usd: 16.99
      poly_vol_24h_usd: 0.0
sources:
  - label: "ClearMarket cross-venue record: Will Exponent launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/exponent-token-event-y-2026"
    retrieved_at: "2026-10-31T14:17:31+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With Polymarket carrying over 99% of combined volume and pricing this at 10%, a desk should treat the Kalshi 26% as a thin-market outlier and weight Polymarket's figure as the more reliable probability anchor.
