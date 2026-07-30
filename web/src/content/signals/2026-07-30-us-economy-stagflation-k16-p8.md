---
signal_id: "CMSIG20260730DV01"
signal_slug: "us-economy-stagflation-k16-p8"
headline: "US economy in recession end-2026: Kalshi 17% vs Polymarket 8%"
semantic_title: "Recession-economy outcome carries a premium on one major desk"
telemetry: "Polymarket 8% vs Kalshi 17%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-07-30T10:22:05+00:00"
event_id: "CM-EVT-ZRG5DFDMZ8"
event_slug: "kxeconpath-26"
event_question: "State of the economy at the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x9b1804352d6246bc8b609bc05a3021134269c133bda15e76e05f844539b59774"
  question_raw: "Will the US economy be in stagflation at the end of 2026?"
  current_price: 0.083
  volume_cumulative_usd: 7444.587273999999
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXECONPATH-26-STAG"
    question_raw: "State of the economy at the end of 2026?"
    current_price: 0.169
bullets:
  - "Kalshi prices a recession outcome at 17%, Polymarket at 8%, a 9pp gap"
  - "Kalshi is the higher-priced venue ($4,348 cumulative volume) vs Polymarket's $7,445 book"
  - "Differences in how each venue defines 'recession' or buckets economy states may explain the spread"
  - "Resolves against a defined economic-condition snapshot at end of calendar year 2026"
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
      kalshi_vol_24h_usd: 0.04
      poly_vol_24h_usd: 0.0
sources:
  - label: "ClearMarket cross-venue record: State of the economy at the end of 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-stagflation-y-2026"
    retrieved_at: "2026-07-30T10:22:05+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 9pp divergence on a macro claim with modest liquidity on both sides points to definitional ambiguity in resolution criteria, a desk should reconcile each venue's rulebook before assuming pure mispricing.
