---
signal_id: "CMSIG20261007DV00"
signal_slug: "discord-ipo-k14-p4"
headline: "Discord IPO before 2027: Kalshi 14% vs Polymarket 5%"
semantic_title: "Discord IPO odds split sharply across venues"
telemetry: "Polymarket 5% vs Kalshi 14%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-07T15:03:14+00:00"
event_id: "CM-EVT-858NYLKF97"
event_slug: "kxipo-26"
event_question: "Discord IPO before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x48fcbf6bb8eceff817ba48b56211e4f8a4cf6896570d847d8d115e63c3abf36a"
  question_raw: "Discord IPO before 2027?"
  current_price: 0.048
  volume_cumulative_usd: 487506.1268199999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXIPO-26-DISCORD"
    question_raw: "Who will IPO before 2027?"
    current_price: 0.14
bullets:
  - "Kalshi prices the claim at 14%, Polymarket at 5%, a 9pp gap with under three months to resolution."
  - "Kalshi sits higher with roughly $19K in cumulative volume; Polymarket carries the deeper book at ~$488K."
  - "Polymarket's larger, more liquid market likely reflects stronger consensus; Kalshi's thin book may overstate IPO odds."
  - "Resolution requires a public Discord listing before Jan 1, 2027, a hard, verifiable date trigger."
atomic_claims:
  - type: "cross_venue_spread"
    provenance: "CM cross-venue link (question_id CMX-26DA00133D); prices direct from venue APIs"
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
      kalshi_vol_24h_usd: 126.52
      poly_vol_24h_usd: 201.13
sources:
  - label: "ClearMarket cross-venue record: Discord IPO before 2027?"
    url: "https://clearmarket.fyi/compare/discord-ipo-y-2026"
    retrieved_at: "2026-10-07T15:03:14+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 9pp spread with Polymarket holding 26x the volume suggests the deeper venue is the more reliable price signal, and a desk looking to arb should treat Kalshi's 14% as the stale or illiquid leg.
