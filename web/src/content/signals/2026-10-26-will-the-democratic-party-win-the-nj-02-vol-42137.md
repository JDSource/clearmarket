---
signal_id: "CMSIG20261026VS02"
signal_slug: "will-the-democratic-party-win-the-nj-02-vol-42137"
headline: "Dems NJ-02: 25% on $42K, majority of all-time vol"
semantic_title: "NJ-02 Democratic House bid holds at 25% in heavy early action"
telemetry: "25% · $42K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-26T14:48:56+00:00"
event_id: "CM-EVT-T2ZK5ZDTH1"
event_slug: "nj-02-house-election-winner"
event_question: "Will the New Jersey 2nd Congressional District House election winner be determined by November 3, 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xda6443c47be5c76cfe19a36b6de027558fbf669c825b7aa20c0642b753127b58"
  question_raw: "Will the Democratic Party win the NJ-02 House seat?"
  current_price: 0.25
  volume_24h_usd: 42137.678313
  volume_cumulative_usd: 70691.926109
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "At 25%, the market prices Republicans as heavy favorites to hold NJ-02."
  - "60% of all-time contract volume cleared in one session, exceptionally concentrated."
  - "NJ-02 is a competitive lean-GOP district; fresh money is stress-testing the Democratic upside."
  - "Resolves on the 2026 NJ-02 House election result."
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
      poly_vol_24h_usd: 42137.678313
sources:
  - label: "ClearMarket market record: Will the New Jersey 2nd Congressional District House el"
    url: "https://clearmarket.fyi/events/nj-02-house-election-winner"
    retrieved_at: "2026-10-26T14:48:56+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Sixty percent of lifetime volume in a single day on a competitive House seat flags that a new poll, candidate development, or redistricting signal has hit the tape.
