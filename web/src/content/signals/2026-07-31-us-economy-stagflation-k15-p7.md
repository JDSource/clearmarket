---
signal_id: "CMSIG20260731DV01"
signal_slug: "us-economy-stagflation-k15-p7"
headline: "Economy 'strong' at end of 2026: Kalshi 16% vs Polymarket 7%"
semantic_title: "Strong-economy verdict for 2026 carries a premium on one venue"
telemetry: "Polymarket 7% vs Kalshi 16%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-07-31T10:35:59+00:00"
event_id: "CM-EVT-ZRG5DFDMZ8"
event_slug: "kxeconpath-26"
event_question: "State of the economy at the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x9b1804352d6246bc8b609bc05a3021134269c133bda15e76e05f844539b59774"
  question_raw: "Will the US economy be in stagflation at the end of 2026?"
  current_price: 0.073
  volume_cumulative_usd: 7473.567274000001
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXECONPATH-26-STAG"
    question_raw: "State of the economy at the end of 2026?"
    current_price: 0.159
bullets:
  - "Kalshi prices a strong-economy outcome at 16%, Polymarket at 7%, a 9pp gap"
  - "Kalshi is the higher-side venue; both markets carry relatively thin liquidity, limiting confidence in either print"
  - "Divergence likely reflects differing resolution criteria or subjective language in how each venue defines 'strong' economy"
  - "Resolution mechanics, who judges the economic state and by what benchmark, are the key variable to audit before trading"
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
      kalshi_vol_24h_usd: 0.84
      poly_vol_24h_usd: 28.98
sources:
  - label: "ClearMarket cross-venue record: State of the economy at the end of 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-stagflation-y-2026"
    retrieved_at: "2026-07-31T10:35:59+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Ambiguous resolution language around 'state of the economy' is the most probable driver of this gap; a desk should review each venue's rules before assuming a clean arbitrage.
