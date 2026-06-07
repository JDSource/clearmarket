---
signal_id: "CMSIG20260603DV02"
signal_slug: "xai-grok-5-release-k16-p11"
headline: "xAI Grok 5 release before Jul 1 2026: Kalshi 16% vs Polymarket 11%"
semantic_title: "Grok 5 by June 30 pricing splits across venues"
telemetry: "Polymarket 11% vs Kalshi 16%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-06-03T01:49:11+00:00"
event_id: "CM-EVT-CW5RM996H4"
event_slug: "kxgrok-grok5"
event_question: "Will xAI release Grok 5 before Jul 1, 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0c61adaf2d0c903081573c305892a84c12701330258d912252eef226faa5c50f"
  question_raw: "Grok 5 released by June 30, 2026?"
  current_price: 0.11
  volume_cumulative_usd: 50726.60849299994
  arbitration_model: "uma_oracle"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXGROK-GROK5-26JUL01"
    question_raw: "Will xAI release Grok 5 before Jul 1, 2026?"
    current_price: 0.16
bullets:
  - "Kalshi prices 16%, Polymarket 11%, a 5pp gap with under four weeks to resolution."
  - "Kalshi is higher; volume only $3,884 vs Polymarket's $50,727, Polymarket ~13x more liquid."
  - "Kalshi's elevated print likely reflects illiquidity rather than informed conviction; Polymarket's 11% is the more traded signal."
  - "Resolves on public xAI announcement or verifiable model release before Jul 1, 2026."
atomic_claims:
  - type: "cross_venue_spread"
    provenance: "CM cross-venue link (cross_venue_id CMX-967EBBB3FC); prices direct from venue APIs"
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
      kalshi_vol_24h_usd: 263.04
      poly_vol_24h_usd: 1754.857141
sources:
  - label: "ClearMarket cross-venue record: Will xAI release Grok 5 before Jul 1, 2026?"
    url: "https://clearmarket.fyi/compare/xai-grok-5-release-m-2026-06"
    retrieved_at: "2026-06-03T01:49:11+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With Kalshi's book extremely thin and the deadline imminent, the 5pp gap is best read as a liquidity artifact, Polymarket's 11% represents the actionable market consensus on a Grok 5 June release.
