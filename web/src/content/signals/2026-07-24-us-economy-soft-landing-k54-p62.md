---
signal_id: "CMSIG20260724DV02"
signal_slug: "us-economy-soft-landing-k54-p62"
headline: "Economy 'good' at end of 2026: Kalshi 54% vs Polymarket 62%"
semantic_title: "Economy-state claim trades far apart on the major desks"
telemetry: "Polymarket 62% vs Kalshi 54%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-07-24T10:14:49+00:00"
event_id: "CM-EVT-ZRG5DFDMZ8"
event_slug: "kxeconpath-26"
event_question: "State of the economy at the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x50e3ee8f93a464d04ea2cea6efff45c902f43642aedbf43f7afdc899e10f71d8"
  question_raw: "Will the US economy be in a soft landing at the end of 2026?"
  current_price: 0.62
  volume_cumulative_usd: 25034.996867000005
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXECONPATH-26-SOFT"
    question_raw: "State of the economy at the end of 2026?"
    current_price: 0.542
bullets:
  - "Kalshi prices a positive economy outcome at 54%, Polymarket at 62%, an 8pp gap"
  - "Polymarket is the higher venue; $25,035 vs Kalshi's $8,436 in cumulative volume"
  - "Resolution ambiguity is the key risk: 'state of the economy' lacks a crisp binary trigger, and each venue may be resolving against a different benchmark"
  - "Divergence likely widens further if the resolution criteria remain loosely defined heading into year-end"
atomic_claims:
  - type: "cross_venue_spread"
    provenance: "CM cross-venue link (question_id CMX-534611296D); prices direct from venue APIs"
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
      kalshi_vol_24h_usd: 1898.35
      poly_vol_24h_usd: 4021.776424
sources:
  - label: "ClearMarket cross-venue record: State of the economy at the end of 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-soft-landing-y-2026"
    retrieved_at: "2026-07-24T10:14:49+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 8pp gap here is as much a resolution-definition problem as a pricing problem, a desk should scrutinize each venue's stated resolution rules before taking a view, as definitional differences may prevent clean arbitrage.
