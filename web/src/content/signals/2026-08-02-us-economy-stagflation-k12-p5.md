---
signal_id: "CMSIG20260802DV02"
signal_slug: "us-economy-stagflation-k12-p5"
headline: "U.S. economy in recession end-2026: Kalshi 12% vs Polymarket 6%"
semantic_title: "Recession call for end of 2026 trades far apart on the major desks"
telemetry: "Polymarket 6% vs Kalshi 12%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-08-02T09:54:06+00:00"
event_id: "CM-EVT-ZRG5DFDMZ8"
event_slug: "kxeconpath-26"
event_question: "State of the economy at the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x9b1804352d6246bc8b609bc05a3021134269c133bda15e76e05f844539b59774"
  question_raw: "Will the US economy be in stagflation at the end of 2026?"
  current_price: 0.057
  volume_cumulative_usd: 9642.057142000001
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXECONPATH-26-STAG"
    question_raw: "State of the economy at the end of 2026?"
    current_price: 0.12
bullets:
  - "Kalshi prices a recessionary outcome at 12%, Polymarket at 6%, a 6pp gap"
  - "Kalshi is double Polymarket's odds; Polymarket holds three times Kalshi's cumulative volume"
  - "Resolution ambiguity, defining 'state of the economy', may explain why the smaller venue prices in more uncertainty"
  - "Resolves based on an agreed economic indicator or official designation at year-end 2026"
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
      kalshi_vol_24h_usd: 72.64
      poly_vol_24h_usd: 666.675031
sources:
  - label: "ClearMarket cross-venue record: State of the economy at the end of 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-stagflation-y-2026"
    retrieved_at: "2026-08-02T09:54:06+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Definitional fuzziness in the claim's resolution criteria likely drives the spread more than genuine forecast disagreement, so a desk should wait for clearer resolution rules before leaning on either price.
