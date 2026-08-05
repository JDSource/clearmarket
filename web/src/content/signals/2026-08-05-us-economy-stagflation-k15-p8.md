---
signal_id: "CMSIG20260805DV02"
signal_slug: "us-economy-stagflation-k15-p8"
headline: "US economy in recession end-2026: Kalshi 15% vs Polymarket 8%"
semantic_title: "Recession call for end-2026 splits sharply across venues"
telemetry: "Polymarket 8% vs Kalshi 15%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-08-05T10:32:12+00:00"
event_id: "CM-EVT-ZRG5DFDMZ8"
event_slug: "kxeconpath-26"
event_question: "State of the economy at the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x9b1804352d6246bc8b609bc05a3021134269c133bda15e76e05f844539b59774"
  question_raw: "Will the US economy be in stagflation at the end of 2026?"
  current_price: 0.085
  volume_cumulative_usd: 10052.124928000001
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXECONPATH-26-STAG"
    question_raw: "State of the economy at the end of 2026?"
    current_price: 0.15
bullets:
  - "Kalshi prices recession at 15% vs Polymarket at 8%, a 6pp spread on the same outcome"
  - "Kalshi is higher on $4K volume; Polymarket is lower with $10K cumulative"
  - "Both books are thin, but Polymarket's lower price aligns with broader consensus that recession remains a tail risk through year-end"
  - "Resolution depends on the specific definition of 'recession' each platform uses, a key ambiguity risk"
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
      kalshi_vol_24h_usd: 5.89
      poly_vol_24h_usd: 36.0
sources:
  - label: "ClearMarket cross-venue record: State of the economy at the end of 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-stagflation-y-2026"
    retrieved_at: "2026-08-05T10:32:12+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With both venues lightly traded, this spread is more noise than signal, but the definitional gap in what each platform counts as 'recession' is the real risk a desk should price in before leaning either direction.
