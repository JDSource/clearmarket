---
signal_id: "CMSIG20260811VS05"
signal_slug: "will-peggy-flanagan-be-the-democratic-no-vol-42761"
headline: "Flanagan MN Dem Senate: 75% on $43K surge"
semantic_title: "Buyers back Flanagan for MN Democratic Senate nomination at 75%"
telemetry: "75% · $43K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-11T08:50:18+00:00"
event_id: "CM-EVT-NNCYHQS2C4"
event_slug: "minnesota-democratic-senate-primary-winner"
event_question: "Will the Minnesota Democratic Senate Primary be won by August 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x125d64e41a8b3225d81e84ec1fbeb58b1d8091fa9d54a9f500e01a00586baf9a"
  question_raw: "Will Peggy Flanagan be the Democratic nominee for Senate in Minnesota?"
  current_price: 0.75
  volume_24h_usd: 42761.145604
  volume_cumulative_usd: 165385.21713199993
  arbitration_model: "uma_oracle"
  resolves_at: "2026-08-11T00:00:00Z"
bullets:
  - "Flanagan priced at 75% to win the Minnesota Democratic Senate nomination on Polymarket."
  - "$43K in 24h, 26% of all-time, marks a notable step-up in trading activity on this race."
  - "Attention likely driven by MN Senate field developments or Flanagan campaign news firming her position."
  - "Resolves YES if Flanagan is named the Democratic Senate nominee for Minnesota in 2026."
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
      poly_vol_24h_usd: 42761.145604
sources:
  - label: "ClearMarket market record: Will the Minnesota Democratic Senate Primary be won by "
    url: "https://clearmarket.fyi/events/minnesota-democratic-senate-primary-winner"
    retrieved_at: "2026-08-11T08:50:18+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Fresh volume at the 75% threshold on Flanagan's Senate nomination signals growing conviction in her path, desks covering the MN Senate race should treat this as a market read that the Democratic field is narrowing around her.
