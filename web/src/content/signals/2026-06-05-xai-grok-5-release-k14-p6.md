---
signal_id: "CMSIG20260605DV00"
signal_slug: "xai-grok-5-release-k14-p6"
headline: "xAI Grok 5 before Jul 1 2026: Kalshi 14% vs Polymarket 6%"
semantic_title: "Grok 5 pre-July release splits sharply across venues"
telemetry: "Polymarket 6% vs Kalshi 14%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-06-05T12:04:05+00:00"
event_id: "CM-EVT-CW5RM996H4"
event_slug: "kxgrok-grok5"
event_question: "Will xAI release Grok 5 before Jul 1, 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0c61adaf2d0c903081573c305892a84c12701330258d912252eef226faa5c50f"
  question_raw: "Grok 5 released by June 30, 2026?"
  current_price: 0.06
  volume_cumulative_usd: 53516.46945899996
  arbitration_model: "uma_oracle"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXGROK-GROK5-26JUL01"
    question_raw: "Will xAI release Grok 5 before Jul 1, 2026?"
    current_price: 0.14
bullets:
  - "Kalshi prices 14%, Polymarket 6%, an 8pp gap on identical near-term release claim."
  - "Kalshi is the higher-conviction desk; Polymarket carries dominant liquidity at roughly 15x cumulative volume."
  - "Thin Kalshi volume suggests idiosyncratic positioning rather than informed consensus; Polymarket's deeper book is likelier to reflect aggregated trader belief."
  - "Resolution hinges on a verifiable xAI product release announcement before Jul 1, 2026, a bright-line mechanic."
atomic_claims:
  - type: "cross_venue_spread"
    provenance: "CM cross-venue link (question_id CMX-967EBBB3FC); prices direct from venue APIs"
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
      poly_vol_24h_usd: 281.15999999999997
sources:
  - label: "ClearMarket cross-venue record: Will xAI release Grok 5 before Jul 1, 2026?"
    url: "https://clearmarket.fyi/compare/xai-grok-5-release-m-2026-06"
    retrieved_at: "2026-06-05T12:04:05+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should weight the Polymarket price as the more liquid and likely more reliable signal, treating Kalshi's elevated print as a thin-book artifact rather than a genuine edge on timing.
