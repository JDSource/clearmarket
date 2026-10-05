---
signal_id: "CMSIG20261005VS05"
signal_slug: "will-the-democrats-win-the-arizona-gover-vol-14586"
headline: "AZ Dem governor: 92% on $15K, 26% of all-time vol"
semantic_title: "Arizona governor race favors Democrats heavily through a volume surge"
telemetry: "92% · $15K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-05T07:48:02+00:00"
event_id: "CM-EVT-T8VRLGR9D8"
event_slug: "arizona-governor-winner-2026"
event_question: "Will the Arizona Governor election be won by the Republican candidate?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xaf874c80349379303164629c3962b1456f667ca1d44edf95e0474dd13483a4b3"
  question_raw: "Will the Democrats win the Arizona governor race in 2026?"
  current_price: 0.92
  volume_24h_usd: 14586.838639000001
  volume_cumulative_usd: 57106.259288000016
  arbitration_model: "uma_oracle"
bullets:
  - "Polymarket prices a Democratic Arizona governor win at 92%, market treats this as close to resolved over a year out."
  - "26% of all-time volume traded in one session, consistent with a catalyst-driven attention spike."
  - "Arizona governor race in 2026 draws focus as a key Sun Belt executive contest; Republican field and candidate clarity may be driving the re-pricing."
  - "Resolves on certified 2026 Arizona gubernatorial election result."
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
      poly_vol_24h_usd: 14586.838639000001
sources:
  - label: "ClearMarket market record: Will the Arizona Governor election be won by the Republ"
    url: "https://clearmarket.fyi/events/arizona-governor-winner-2026"
    retrieved_at: "2026-10-05T07:48:02+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

92% pricing on Arizona governor with a fresh volume pop is a strong market signal that no credible Republican challenger has emerged in the eyes of active traders, a desk tracking 2026 Sun Belt political risk should note this as a near-consensus Democratic hold.
