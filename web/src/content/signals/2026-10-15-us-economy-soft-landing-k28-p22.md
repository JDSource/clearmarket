---
signal_id: "CMSIG20261015DV00"
signal_slug: "us-economy-soft-landing-k28-p22"
headline: "U.S. economy 'good/great' by end-2026: Kalshi 29% vs Polymarket 22%"
semantic_title: "Economy-state claim carries a premium on the low-volume desk"
telemetry: "Polymarket 22% vs Kalshi 29%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-15T07:49:06+00:00"
event_id: "CM-EVT-ZRG5DFDMZ8"
event_slug: "kxeconpath-26"
event_question: "State of the economy at the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x50e3ee8f93a464d04ea2cea6efff45c902f43642aedbf43f7afdc899e10f71d8"
  question_raw: "Will the US economy be in a soft landing at the end of 2026?"
  current_price: 0.22
  volume_cumulative_usd: 49359.988159
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXECONPATH-26-SOFT"
    question_raw: "State of the economy at the end of 2026?"
    current_price: 0.288
bullets:
  - "Kalshi prices the positive-economy outcome at 29%, Polymarket at 22%, a 7pp gap."
  - "Kalshi is higher on thin volume; Polymarket holds the lower price with roughly six times the liquidity."
  - "Kalshi's vaguer resolution criteria may be drawing optimistic pricing; Polymarket's deeper pool likely reflects broader sentiment."
  - "Resolution hinges on the specific grading rubric each platform applies to 'state of the economy', definitions may differ materially."
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
      kalshi_vol_24h_usd: 228.88
      poly_vol_24h_usd: 266.711819
sources:
  - label: "ClearMarket cross-venue record: State of the economy at the end of 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-soft-landing-y-2026"
    retrieved_at: "2026-10-15T07:49:06+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 7pp spread likely reflects definitional ambiguity in the claim's resolution criteria rather than a pure arbitrage opportunity, and the lopsided liquidity makes closing the gap costly in practice.
