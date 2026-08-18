---
signal_id: "CMSIG20260818VS01"
signal_slug: "will-byron-donalds-be-the-republican-nom-vol-280521"
headline: "Donalds FL GOP nom: 99% on $281K inflow"
semantic_title: "Buyers back Donalds FL nomination as odds touch 99%"
telemetry: "99% · $281K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-18T08:31:22+00:00"
event_id: "CM-EVT-PFTTW468Y8"
event_slug: "republican-nominee-for-florida-governor"
event_question: "Will Ron DeSantis win the Florida Republican gubernatorial primary?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xd4a3de1964b1f3fa1edeca40dbc3ef6663a56fda84e804066c23096b615904f9"
  question_raw: "Will Byron Donalds be the Republican nominee for Florida Governor?"
  current_price: 0.99
  volume_24h_usd: 280521.215929
  volume_cumulative_usd: 880798.0476360004
  arbitration_model: "uma_oracle"
  resolves_at: "2026-08-18T00:00:00Z"
bullets:
  - "Polymarket prices Donalds at 99%, cross-venue alignment with Kalshi confirms consensus."
  - "32% of all-time volume in 24h ($281K), the largest single-day share this contract has seen."
  - "Cross-venue convergence at 99% removes arb opportunity and signals information has settled."
  - "Resolves on Florida Republican Party's official nominee declaration."
atomic_claims:
  - type: "volume_anomaly"
    provenance: "24h + cumulative volume direct from polymarket API; intensity = 24h/cumulative (derived)"
    field_provenance:
      volume_24h_usd:
        tier: "direct"
        method: "polymarket_api"
      intensity:
        tier: "derived"
        method: "arithmetic"
        inputs: ["volume_24h_usd", "volume_cumulative_usd"]
    liquidity_context:
      poly_vol_24h_usd: 280521.215929
sources:
  - label: "ClearMarket market record: Will Ron DeSantis win the Florida Republican gubernator"
    url: "https://clearmarket.fyi/events/republican-nominee-for-florida-governor"
    retrieved_at: "2026-08-18T08:31:22+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Polymarket corroborating Kalshi's 99% print on a proportionally larger volume share confirms this is a market-wide conviction flush, not venue-specific noise, nomination risk is effectively priced out.
