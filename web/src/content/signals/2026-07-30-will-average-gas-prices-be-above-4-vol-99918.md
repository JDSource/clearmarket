---
signal_id: "CMSIG20260730VS06"
signal_slug: "will-average-gas-prices-be-above-4-vol-99918"
headline: "Gas above $4.10: 94% on $100K surge"
semantic_title: "Gas prices staying above $4.10 draws heavy backing"
telemetry: "94% · $100K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-30T10:21:41+00:00"
event_id: "CM-EVT-9BFFMNBK34"
event_slug: "kxaaagasm-26jul31"
event_question: "Average **gas prices**"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXAAAGASM-26JUL31-4.10"
  question_raw: "Will average **gas prices** be above $4.10?"
  current_price: 0.94
  volume_24h_usd: 99918.17
  volume_cumulative_usd: 302755.17
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-08-30T14:00:00Z"
bullets:
  - "94% pricing signals the market is highly confident average gas prices will remain above the $4.10 threshold."
  - "$100K in 24h volume is 33% of all-time, a significant one-day share for an energy consumer price contract."
  - "Fresh attention to a high-conviction contract may reflect new pump-price data, crude moves, or seasonal demand reads."
  - "Resolves on reported average national gas prices against the $4.10 benchmark."
atomic_claims:
  - type: "volume_anomaly"
    provenance: "24h + cumulative volume direct from kalshi API; intensity = 24h/cumulative (derived)"
    field_provenance:
      volume_24h_usd:
        tier: "direct"
        method: "kalshi_api"
      intensity:
        tier: "derived"
        method: "arithmetic"
        inputs: ["volume_24h_usd", "volume_cumulative_usd"]
    liquidity_context:
      kalshi_vol_24h_usd: 99918.17
sources:
  - label: "ClearMarket market record: Average **gas prices**"
    url: "https://clearmarket.fyi/events/kxaaagasm-26jul31"
    retrieved_at: "2026-07-30T10:21:41+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Strong volume into a 94%-priced energy consumer contract tells a desk the market treats elevated gas prices as a durable condition, relevant for inflation expectations, consumer discretionary positioning, and Fed rate-path context.
