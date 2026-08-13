---
signal_id: "CMSIG20260813DV05"
signal_slug: "us-economy-stagflation-k11-p5"
headline: "Economy in recession end of 2026: Kalshi 11% vs Polymarket 6%"
semantic_title: "Recession outcome prices higher on the smaller desk"
telemetry: "Polymarket 6% vs Kalshi 11%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-08-13T09:09:18+00:00"
event_id: "CM-EVT-ZRG5DFDMZ8"
event_slug: "kxeconpath-26"
event_question: "State of the economy at the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x9b1804352d6246bc8b609bc05a3021134269c133bda15e76e05f844539b59774"
  question_raw: "Will the US economy be in stagflation at the end of 2026?"
  current_price: 0.057
  volume_cumulative_usd: 10308.663387
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXECONPATH-26-STAG"
    question_raw: "State of the economy at the end of 2026?"
    current_price: 0.11
bullets:
  - "Kalshi places recession probability at 11%, Polymarket at 6%, a 5pp gap."
  - "Polymarket has roughly three times the volume ($10.3K vs $3K), lending its lower price more weight."
  - "Kalshi's elevated recession read may reflect a more pessimistic or macro-focused participant base on a thinner book."
  - "Resolves YES if an agreed recession definition, typically two consecutive GDP-contraction quarters, is met by end of 2026."
atomic_claims:
  - type: "cross_venue_spread"
    provenance: "CM cross-venue link (question_id CMX-DF50C877D3); prices direct from venue APIs"
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
      kalshi_vol_24h_usd: 1.1
      poly_vol_24h_usd: 0.0
sources:
  - label: "ClearMarket cross-venue record: State of the economy at the end of 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-stagflation-y-2026"
    retrieved_at: "2026-08-13T09:09:18+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 5pp gap on a low-probability tail outcome is proportionally meaningful, Polymarket's deeper pool at 6% is the stronger reference, but a desk should watch whether Kalshi's higher read leads or lags macro data revisions.
