---
signal_id: "CMSIG20261030VS02"
signal_slug: "will-the-democratic-party-win-the-nc-11-vol-72022"
headline: "Dem NC-11: 86% on $72K Polymarket spike"
semantic_title: "Democrats lead NC-11 at 86% through a volume surge"
telemetry: "86% · $72K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-30T14:48:27+00:00"
event_id: "CM-EVT-DFRWVBVQ98"
event_slug: "nc-11-house-election-winner"
event_question: "Who will win the NC-11 House election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x7fd71c48a98bb515664cadb1f62cf1f27b770fe9cc1216571e183b982a48e42a"
  question_raw: "Will the Democratic Party win the NC-11 House seat?"
  current_price: 0.86
  volume_24h_usd: 72022.222157
  volume_cumulative_usd: 111022.32258499999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-04T00:00:00Z"
bullets:
  - "86% prices the Democratic candidate as a solid frontrunner in North Carolina's 11th district."
  - "$72K in 24h equals 65% of all-time contract volume, most of the market's lifetime traded today."
  - "Mirrors Spike 0: both sides of NC-11 are seeing simultaneous high activity, rare for a House race."
  - "Resolution tied to certified NC-11 election result."
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
      poly_vol_24h_usd: 72022.222157
sources:
  - label: "ClearMarket market record: Who will win the NC-11 House election?"
    url: "https://clearmarket.fyi/events/nc-11-house-election-winner"
    retrieved_at: "2026-10-30T14:48:27+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Simultaneous high volume on both the Democratic and Republican NC-11 contracts points to active two-sided positioning, consistent with a contested district drawing late capital.
