---
signal_id: "CMSIG20260728DV02"
signal_slug: "us-economy-recession-k8-p13"
headline: "US recession in 2026: Kalshi 8% vs Polymarket 13%"
semantic_title: "Recession-in-2026 odds diverge, Polymarket builds the higher price"
telemetry: "Polymarket 13% vs Kalshi 8%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-07-28T10:31:37+00:00"
event_id: "CM-EVT-L7017DJDX1"
event_slug: "kxrecssnber-26"
event_question: "Will there be a recession in 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xfdc73f10edf0266756686f35b5712cffa828b0940fc015e0426c76c934c2105d"
  question_raw: "US recession by end of 2026?"
  current_price: 0.13
  volume_cumulative_usd: 1685124.0479729977
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXRECSSNBER-26"
    question_raw: "Will there be a recession in 2026?"
    current_price: 0.08
bullets:
  - "Kalshi prices a 2026 recession at 8%, Polymarket at 13%, a 5pp gap"
  - "Polymarket is higher and carries vastly deeper liquidity; Kalshi's book is comparatively thin"
  - "Polymarket's larger, more active base may be incorporating macro data more efficiently, making its 13% the stronger signal"
  - "Resolution typically tied to NBER official recession declaration within the 2026 calendar year"
atomic_claims:
  - type: "cross_venue_spread"
    provenance: "CM cross-venue link (question_id CMX-2FB03D51D4); prices direct from venue APIs"
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
      kalshi_vol_24h_usd: 694.58
      poly_vol_24h_usd: 291.309089
sources:
  - label: "ClearMarket cross-venue record: Will there be a recession in 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-recession-y-2026"
    retrieved_at: "2026-07-28T10:31:37+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Unlike the other two divergences, here the deeper venue prices the event higher, a 5pp gap that desks should treat as a genuine directional disagreement worth monitoring as macro data arrives through year-end.
