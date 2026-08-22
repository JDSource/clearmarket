---
signal_id: "CMSIG20260822VS04"
signal_slug: "will-the-republican-party-win-the-tx-30-vol-23344"
headline: "GOP TX-30 House seat: 2% on $23K volume"
semantic_title: "Republicans given almost no shot at TX-30 as volume piles in"
telemetry: "2% · $23K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-22T08:24:03+00:00"
event_id: "CM-EVT-GDNJKGCBY3"
event_slug: "tx-30-house-election-winner"
event_question: "Will the Republican Party win the Texas House District 30 seat in the 2026 general election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x3f01d7c70a805677183768f7d8d7993cb6a84f909b20ea27bf6d1fb7bed08977"
  question_raw: "Will the Republican Party win the TX-30 House seat?"
  current_price: 0.022
  volume_24h_usd: 23344.8
  volume_cumulative_usd: 41486.564129000006
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices Republican win at 2%, near-total dismissal of the outcome."
  - "24h flow of $23K is 56% of all-time, a majority of lifetime liquidity in a single day."
  - "TX-30 is a heavily Democratic Dallas-area district; fresh volume reinforces, not questions, that consensus."
  - "Resolves on certified TX-30 election result."
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
      poly_vol_24h_usd: 23344.8
sources:
  - label: "ClearMarket market record: Will the Republican Party win the Texas House District "
    url: "https://clearmarket.fyi/events/tx-30-house-election-winner"
    retrieved_at: "2026-08-22T08:24:03+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Heavy volume confirming a near-zero price on a congressional seat suggests informed traders are locking in Democratic win exposure, useful as a baseline for downstream Texas political risk models.
