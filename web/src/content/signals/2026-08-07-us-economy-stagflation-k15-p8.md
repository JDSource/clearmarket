---
signal_id: "CMSIG20260807DV03"
signal_slug: "us-economy-stagflation-k15-p8"
headline: "Economy weak end-2026: Kalshi 15% vs Polymarket 9%"
semantic_title: "Recession-by-year-end odds run higher on one desk than the other"
telemetry: "Polymarket 9% vs Kalshi 15%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-08-07T08:55:00+00:00"
event_id: "CM-EVT-ZRG5DFDMZ8"
event_slug: "kxeconpath-26"
event_question: "State of the economy at the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x9b1804352d6246bc8b609bc05a3021134269c133bda15e76e05f844539b59774"
  question_raw: "Will the US economy be in stagflation at the end of 2026?"
  current_price: 0.086
  volume_cumulative_usd: 10083.752833000002
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXECONPATH-26-STAG"
    question_raw: "State of the economy at the end of 2026?"
    current_price: 0.15
bullets:
  - "Kalshi prices a weak economy at end-2026 at 15%, Polymarket at 9%, a 6pp gap"
  - "Kalshi is the higher venue; Polymarket has ~$10.1K in volume vs Kalshi's ~$4.1K"
  - "Resolution-criteria differences, what each platform counts as 'weak', likely drive the gap more than genuine sentiment divergence"
  - "Both sides are pricing a low-probability outcome; small absolute volume on each venue limits confidence in either print"
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
      kalshi_vol_24h_usd: 0.0
      poly_vol_24h_usd: 31.627905
sources:
  - label: "ClearMarket cross-venue record: State of the economy at the end of 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-stagflation-y-2026"
    retrieved_at: "2026-08-07T08:55:00+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 6pp spread on a low-probability outcome with modest liquidity on both sides warrants a resolution-language review before any position, the gap is more likely definitional than a tradeable dislocation.
