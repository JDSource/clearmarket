---
signal_id: "CMSIG20260702DV03"
signal_slug: "anduril-ipo-k6-p11"
headline: "Anduril IPO before 2027: Kalshi 6% vs Polymarket 11%"
semantic_title: "Anduril IPO pricing tracks a premium on the major desks"
telemetry: "Polymarket 11% vs Kalshi 6%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-07-02T10:35:37+00:00"
event_id: "CM-EVT-858NYLKF97"
event_slug: "kxipo-26"
event_question: "Anduril IPO before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xb7a72d5e5e4ad1dd7664fec7b7c3031a66d149d186e9c5180351780eb1323566"
  question_raw: "Anduril IPO before 2027?"
  current_price: 0.11
  volume_cumulative_usd: 355273.0028739991
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXIPO-26-ANDURIL"
    question_raw: "Who will IPO before 2027?"
    current_price: 0.06
bullets:
  - "Polymarket prices Anduril IPO before 2027 at 11%, Kalshi at 6%, a 5pp gap."
  - "Polymarket is the high side and holds roughly 25x Kalshi's cumulative volume."
  - "The smaller absolute gap may reflect genuine uncertainty; Polymarket's larger book still makes it the more credible price discovery venue."
  - "Resolution: an Anduril IPO pricing or listing event before Jan 1 2027 settles YES."
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
      kalshi_vol_24h_usd: 16.68
      poly_vol_24h_usd: 32.955933
sources:
  - label: "ClearMarket cross-venue record: Anduril IPO before 2027?"
    url: "https://clearmarket.fyi/compare/anduril-ipo-y-2026"
    retrieved_at: "2026-07-02T10:35:37+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 5pp gap with the deeper venue consistently on the high side suggests Kalshi's audience is modestly more skeptical of a near-term Anduril listing, but the spread is narrow enough that a desk need not assign strong directional weight to either side.
