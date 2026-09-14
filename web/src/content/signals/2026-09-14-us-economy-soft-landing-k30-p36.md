---
signal_id: "CMSIG20260914DV02"
signal_slug: "us-economy-soft-landing-k30-p36"
headline: "Strong economy end of 2026: Kalshi 30% vs Polymarket 36%"
semantic_title: "U.S. economy end-of-2026 outlook diverges across venues"
telemetry: "Polymarket 36% vs Kalshi 30%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-09-14T14:42:13+00:00"
event_id: "CM-EVT-ZRG5DFDMZ8"
event_slug: "kxeconpath-26"
event_question: "State of the economy at the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x50e3ee8f93a464d04ea2cea6efff45c902f43642aedbf43f7afdc899e10f71d8"
  question_raw: "Will the US economy be in a soft landing at the end of 2026?"
  current_price: 0.36
  volume_cumulative_usd: 39061.582217999996
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXECONPATH-26-SOFT"
    question_raw: "State of the economy at the end of 2026?"
    current_price: 0.3
bullets:
  - "Kalshi prices a strong economy outcome at 30%, Polymarket at 36%, a 6pp gap"
  - "Polymarket sits higher and holds roughly 5x more cumulative volume"
  - "Resolution-definition ambiguity is high here; the two venues may be resolving against different benchmarks or outcome buckets, driving structural mispricing"
  - "Resolves based on agreed economic indicators or designated resolver judgment at end of 2026"
atomic_claims:
  - type: "cross_venue_spread"
    provenance: "CM cross-venue link (question_id CMX-534611296D); prices direct from venue APIs"
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
      kalshi_vol_24h_usd: 32.15
      poly_vol_24h_usd: 56.022223
sources:
  - label: "ClearMarket cross-venue record: State of the economy at the end of 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-soft-landing-y-2026"
    retrieved_at: "2026-09-14T14:42:13+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 6pp gap combined with differing volume levels likely signals a resolution-criteria mismatch between platforms rather than genuine crowd disagreement, a desk should audit each contract's resolution rules before treating this as a tradeable arbitrage.
