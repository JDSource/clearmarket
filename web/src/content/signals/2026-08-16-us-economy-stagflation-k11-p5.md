---
signal_id: "CMSIG20260816DV03"
signal_slug: "us-economy-stagflation-k11-p5"
headline: "State of economy end-2026 (recession): Kalshi 11% vs Polymarket 6%"
semantic_title: "Recession-state odds build a spread on the major prediction desks"
telemetry: "Polymarket 6% vs Kalshi 11%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-08-16T08:24:18+00:00"
event_id: "CM-EVT-ZRG5DFDMZ8"
event_slug: "kxeconpath-26"
event_question: "State of the economy at the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x9b1804352d6246bc8b609bc05a3021134269c133bda15e76e05f844539b59774"
  question_raw: "Will the US economy be in stagflation at the end of 2026?"
  current_price: 0.055
  volume_cumulative_usd: 10358.603387000001
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXECONPATH-26-STAG"
    question_raw: "State of the economy at the end of 2026?"
    current_price: 0.11
bullets:
  - "Kalshi prices 11%, Polymarket 6%, a 6pp gap on the recession outcome of the same claim"
  - "Kalshi is the higher venue; liquidity is modest on both sides ($3,011 vs $10,359)"
  - "Kalshi's higher recession probability may reflect a different interpretation of the resolution criteria or audience composition"
  - "Resolves YES if a defined recession condition is met by end of 2026 per the claim's source methodology"
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
      kalshi_vol_24h_usd: 4.72
      poly_vol_24h_usd: 49.94
sources:
  - label: "ClearMarket cross-venue record: State of the economy at the end of 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-stagflation-y-2026"
    retrieved_at: "2026-08-16T08:24:18+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Nearly double the recession probability on Kalshi versus Polymarket, with both books relatively thin, means a desk should treat this spread as ambiguity risk around resolution language rather than a clean arbitrage signal.
