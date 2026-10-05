---
signal_id: "CMSIG20261005VS04"
signal_slug: "will-the-democratic-party-win-the-mn-02-vol-12706"
headline: "MN-02 Dem win: 91% on $13K, 45% of all-time vol"
semantic_title: "Democratic MN-02 hold commands near-certain odds on fresh volume"
telemetry: "91% · $13K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-05T07:48:02+00:00"
event_id: "CM-EVT-Y9F1K0F3B5"
event_slug: "mn-02-house-election-winner"
event_question: "Will the Minnesota 2nd Congressional District House Election result in a Republican winner in 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x7319fceb8b5a315eae707028bd654463e48acec082565ef1abd3cc18b424ff6f"
  question_raw: "Will the Democratic Party win the MN-02 House seat?"
  current_price: 0.911
  volume_24h_usd: 12706.84
  volume_cumulative_usd: 28098.716503
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-04T00:00:00Z"
bullets:
  - "Polymarket prices a Democratic win in MN-02 at 91%, near-certain status, leaving only slim Republican upset tail."
  - "45% of all-time volume cleared in 24 hours, the contract's largest single session."
  - "Minnesota's 2nd district leans Democratic in post-redistricting maps; fresh volume may reflect candidate or fundraising news."
  - "Resolves on November 2026 general election certified result for MN-02."
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
      poly_vol_24h_usd: 12706.84
sources:
  - label: "ClearMarket market record: Will the Minnesota 2nd Congressional District House Ele"
    url: "https://clearmarket.fyi/events/mn-02-house-election-winner"
    retrieved_at: "2026-10-05T07:48:02+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

High volume at 91% on a House district race signals that market participants are using this contract to hedge or express conviction on House majority math at the district level, the seat is near-priced-in as a Democratic hold.
