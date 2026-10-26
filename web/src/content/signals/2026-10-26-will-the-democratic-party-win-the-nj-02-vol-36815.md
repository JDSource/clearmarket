---
signal_id: "CMSIG20261026VS03"
signal_slug: "will-the-democratic-party-win-the-nj-02-vol-36815"
headline: "Dem NJ-02 House seat: 21% on $36K surge"
semantic_title: "Buyers back Democrats in NJ-02 despite steep 21% odds"
telemetry: "21% · $37K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-26T07:48:41+00:00"
event_id: "CM-EVT-T2ZK5ZDTH1"
event_slug: "nj-02-house-election-winner"
event_question: "Will the New Jersey 2nd Congressional District House election winner be determined by November 3, 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xda6443c47be5c76cfe19a36b6de027558fbf669c825b7aa20c0642b753127b58"
  question_raw: "Will the Democratic Party win the NJ-02 House seat?"
  current_price: 0.21
  volume_24h_usd: 36815.958312999996
  volume_cumulative_usd: 65370.206109000006
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Democrats sit at 21% in NJ-02, market treats this as a lean-Republican hold."
  - "56% of all-time volume hit in 24 hours, the highest all-time share in this batch."
  - "NJ-02 fresh attention at long-shot odds may signal a candidate development or district-level data shift."
  - "Resolves on the NJ-02 general election outcome."
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
      poly_vol_24h_usd: 36815.958312999996
sources:
  - label: "ClearMarket market record: Will the New Jersey 2nd Congressional District House el"
    url: "https://clearmarket.fyi/events/nj-02-house-election-winner"
    retrieved_at: "2026-10-26T07:48:41+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Absorbing more than half of all-time volume in a single session at 21% points to an asymmetric information event in NJ-02, a desk should check candidate filings, fundraising disclosures, or local news for a catalyst.
