---
signal_id: "CMSIG20261018VS02"
signal_slug: "will-the-democratic-party-win-the-nc-11-vol-15002"
headline: "NC-11 Dem win: 80% on $15K volume burst"
semantic_title: "Democrats back NC-11 as buyers return in force"
telemetry: "80% · $15K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-18T12:26:25+00:00"
event_id: "CM-EVT-DFRWVBVQ98"
event_slug: "nc-11-house-election-winner"
event_question: "Who will win the NC-11 House election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x7fd71c48a98bb515664cadb1f62cf1f27b770fe9cc1216571e183b982a48e42a"
  question_raw: "Will the Democratic Party win the NC-11 House seat?"
  current_price: 0.8
  volume_24h_usd: 15002.906302
  volume_cumulative_usd: 26904.630377
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-04T00:00:00Z"
bullets:
  - "Polymarket prices Democratic NC-11 win at 80%, the complementary leg to the 17% Republican contract."
  - "24h volume of $15K equals 56% of all-time handle, matching the Republican contract's share almost exactly, confirming coordinated repricing."
  - "An 80/17 split (with residual slippage) implies the market has substantially resolved its uncertainty; volume here is conviction capital, not discovery."
  - "Resolution tied to Nov 3 NC-11 general election results."
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
      poly_vol_24h_usd: 15002.906302
sources:
  - label: "ClearMarket market record: Who will win the NC-11 House election?"
    url: "https://clearmarket.fyi/events/nc-11-house-election-winner"
    retrieved_at: "2026-10-18T12:26:25+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The near-mirror volume surge across both NC-11 contracts on the same day tells a desk that a single catalyst drove synchronized repositioning, worth identifying the triggering event before assuming the 80% price is stale.
