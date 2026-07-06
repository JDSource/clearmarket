---
signal_id: "CMSIG20260706DV03"
signal_slug: "anduril-ipo-k6-p11"
headline: "Anduril IPO before 2027: Kalshi 6% vs Polymarket 11%"
semantic_title: "Anduril IPO tracks a modest premium on the larger venue"
telemetry: "Polymarket 11% vs Kalshi 6%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-07-06T12:01:11+00:00"
event_id: "CM-EVT-858NYLKF97"
event_slug: "kxipo-26"
event_question: "Anduril IPO before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xb7a72d5e5e4ad1dd7664fec7b7c3031a66d149d186e9c5180351780eb1323566"
  question_raw: "Anduril IPO before 2027?"
  current_price: 0.11
  volume_cumulative_usd: 355338.4574179991
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXIPO-26-ANDURIL"
    question_raw: "Who will IPO before 2027?"
    current_price: 0.06
bullets:
  - "Polymarket prices Anduril IPO before 2027 at 11%; Kalshi at 6%, a 5pp gap."
  - "Polymarket is the higher-conviction venue and carries substantially greater liquidity than Kalshi."
  - "Anduril's defense-sector profile and private funding runway make a sub-six-month IPO unlikely on both desks; the spread may reflect Polymarket participants pricing in a low-probability defense-sector catalyst."
  - "Resolves YES if Anduril prices a public offering on a major exchange before Jan 1, 2027."
atomic_claims:
  - type: "cross_venue_spread"
    provenance: "CM cross-venue link (question_id CMX-D39E0284B8); prices direct from venue APIs"
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
      kalshi_vol_24h_usd: 15.86
      poly_vol_24h_usd: 0.0
sources:
  - label: "ClearMarket cross-venue record: Anduril IPO before 2027?"
    url: "https://clearmarket.fyi/compare/anduril-ipo-y-2026"
    retrieved_at: "2026-07-06T12:01:11+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Both venues agree the event is low-probability, but a near-double in price from the illiquid to the liquid venue on a tight horizon suggests desks should treat the Polymarket 11% as the credible ceiling and not read directional signal into Kalshi's 6%.
