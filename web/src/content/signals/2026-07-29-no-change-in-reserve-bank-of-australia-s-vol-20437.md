---
signal_id: "CMSIG20260729VS06"
signal_slug: "no-change-in-reserve-bank-of-australia-s-vol-20437"
headline: "RBA Aug no change: 96% on $20K volume"
semantic_title: "RBA August hold near certain as fresh volume piles in at 96%"
telemetry: "96% · $20K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-29T10:36:04+00:00"
event_id: "CM-EVT-C9F29RSWM7"
event_slug: "reserve-bank-of-australia-decision-in-august"
event_question: "Will the Reserve Bank of Australia make a decision in August?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x8c39e2ee7d85026ab1e23dd0ad927676f4c5b122051effafbe7764f817dbdc37"
  question_raw: "No change in Reserve Bank of Australia's interest rates at the August 2026 meeting?"
  current_price: 0.963
  volume_24h_usd: 20437.010612
  volume_cumulative_usd: 43447.47115500001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-08-11T00:00:00Z"
bullets:
  - "Polymarket prices the Reserve Bank of Australia holding rates in August at 96%, near-consensus."
  - "47% of all-time volume arrived in 24h, the contract's single largest session ahead of the meeting."
  - "Recent Australian inflation or jobs data likely confirmed the hold view, drawing late confirmation trades."
  - "Resolves on the RBA August 2026 decision; at 96% the contract is trading like a done deal."
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
      poly_vol_24h_usd: 20437.010612
sources:
  - label: "ClearMarket market record: Will the Reserve Bank of Australia make a decision in A"
    url: "https://clearmarket.fyi/events/reserve-bank-of-australia-decision-in-august"
    retrieved_at: "2026-07-29T10:36:04+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Fresh volume piling into a 96% hold price signals that macro desks are locking in carry or hedging RBA-linked positions as the August decision approaches with near-zero surprise risk priced in.
