---
signal_id: "CMSIG20260801DV02"
signal_slug: "us-economy-stagflation-k12-p6"
headline: "US economy in recession end-2026: Kalshi 12% vs Polymarket 6%"
semantic_title: "Recession outcome for end-2026 builds a premium on one venue"
telemetry: "Polymarket 6% vs Kalshi 12%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-08-01T09:56:15+00:00"
event_id: "CM-EVT-ZRG5DFDMZ8"
event_slug: "kxeconpath-26"
event_question: "State of the economy at the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x9b1804352d6246bc8b609bc05a3021134269c133bda15e76e05f844539b59774"
  question_raw: "Will the US economy be in stagflation at the end of 2026?"
  current_price: 0.06
  volume_cumulative_usd: 8975.382111000003
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXECONPATH-26-STAG"
    question_raw: "State of the economy at the end of 2026?"
    current_price: 0.121
bullets:
  - "Kalshi prices a recession outcome at 12%, Polymarket at 6%, a 6pp gap"
  - "Kalshi higher on ~$3K volume; Polymarket carries ~$9K, roughly 3x deeper"
  - "Definitional differences in 'recession' resolution criteria likely drive the spread as much as market depth"
  - "Resolution turns on the specific economic indicator or official body named in each venue's contract rules"
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
      kalshi_vol_24h_usd: 83.73
      poly_vol_24h_usd: 1501.814837
sources:
  - label: "ClearMarket cross-venue record: State of the economy at the end of 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-stagflation-y-2026"
    retrieved_at: "2026-08-01T09:56:15+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 6pp gap on a low-probability outcome is disproportionately large and likely reflects divergent resolution language between the two contracts, making direct arbitrage risky until criteria are reconciled.
