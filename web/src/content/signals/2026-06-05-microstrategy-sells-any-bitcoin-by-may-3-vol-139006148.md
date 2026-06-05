---
signal_id: "CMSIG20260605VS00"
signal_slug: "microstrategy-sells-any-bitcoin-by-may-3-vol-139006148"
headline: "MicroStrategy BTC sale: 0% on $139M surge"
semantic_title: "Traders write off a MicroStrategy Bitcoin sale by May 31"
telemetry: "0% · $139M 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-05T12:03:57+00:00"
event_id: "CM-EVT-QW6P6GZ8N4"
event_slug: "microstrategy-sell-any-bitcoin-in-2025"
event_question: "MicroStrategy sells any Bitcoin? (multi-deadline series, 2025-2027)"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x3733a1b647e7364095736ab0966465d896a84cf3b6bc1695ca1f26c3239b3868"
  question_raw: "MicroStrategy sells any Bitcoin by May 31, 2026?"
  current_price: 0.004
  volume_24h_usd: 139006148.68573284
  volume_cumulative_usd: 230175285.6277966
  arbitration_model: "uma_oracle"
  resolves_at: "2026-07-01T04:00:00Z"
bullets:
  - "Market prices zero probability MicroStrategy liquidated any BTC before May 31 deadline."
  - "Polymarket logged $139M in 24h volume, 60% of the contract's entire all-time handle."
  - "Resolution window has passed; capital rushing in to collect on a settled near-certain 'No'."
  - "Contract likely in final settlement phase; flows reflect arbitrage, not fresh directional conviction."
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
      poly_vol_24h_usd: 139006148.68573284
sources:
  - label: "ClearMarket market record: MicroStrategy sells any Bitcoin? (multi-deadline series"
    url: "https://clearmarket.fyi/events/microstrategy-sell-any-bitcoin-in-2025"
    retrieved_at: "2026-06-05T12:03:57+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The extreme volume at 0% on an expired window signals institutional arbitrage harvesting residual settlement value, not a new macro view on MicroStrategy's treasury policy.
