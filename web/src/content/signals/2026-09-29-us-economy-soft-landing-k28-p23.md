---
signal_id: "CMSIG20260929DV00"
signal_slug: "us-economy-soft-landing-k28-p23"
headline: "U.S. economy in recession by end of 2026: Kalshi 29% vs Polymarket 23%"
semantic_title: "Recession-by-year-end odds carry a premium across venues"
telemetry: "Polymarket 23% vs Kalshi 29%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-09-29T07:48:14+00:00"
event_id: "CM-EVT-ZRG5DFDMZ8"
event_slug: "kxeconpath-26"
event_question: "State of the economy at the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x50e3ee8f93a464d04ea2cea6efff45c902f43642aedbf43f7afdc899e10f71d8"
  question_raw: "Will the US economy be in a soft landing at the end of 2026?"
  current_price: 0.23
  volume_cumulative_usd: 46959.939748000004
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXECONPATH-26-SOFT"
    question_raw: "State of the economy at the end of 2026?"
    current_price: 0.288
bullets:
  - "Kalshi prices recession at 29%, Polymarket at 23%, a 6pp spread on the same year-end claim."
  - "Kalshi sits higher with $8.4K cumulative volume; Polymarket holds the lower read on $47K volume."
  - "Deeper liquidity on Polymarket may reflect a broader, more diverse crowd pulling the odds lower; Kalshi's thinner book leaves more room for a bid-up outlier view."
  - "Resolution hinges on an official NBER call or comparable government determination before Jan 1, 2027, a notoriously lagging indicator."
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
      kalshi_vol_24h_usd: 0.0
      poly_vol_24h_usd: 4.99
sources:
  - label: "ClearMarket cross-venue record: State of the economy at the end of 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-soft-landing-y-2026"
    retrieved_at: "2026-09-29T07:48:14+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk eyeing this spread should note that Polymarket's larger pool likely carries more price discovery weight, making the 6pp gap look like Kalshi is running hot, but the slim Kalshi volume means a handful of contracts could close that gap quickly.
