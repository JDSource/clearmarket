---
signal_id: "CMSIG20261104VS04"
signal_slug: "will-the-democrats-win-the-michigan-sena-vol-3026718"
headline: "MI Senate Dem: 100% on $3M Polymarket inflow"
semantic_title: "Fresh volume returns to Democrats winning Michigan Senate"
telemetry: "100% · $3M 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-04T07:48:42+00:00"
event_id: "CM-EVT-P8B8CLLCB5"
event_slug: "michigan-senate-election-winner"
event_question: "Will a Michigan Senate election winner be determined by the next election cycle?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xbfeb6d4cf3eab6071e204219b0647c8224d63a12778df467311b5f2a4b3a5bd4"
  question_raw: "Will the Democrats win the Michigan Senate race in 2026?"
  current_price: 0.999
  volume_24h_usd: 3026718.9755600006
  volume_cumulative_usd: 7831231.852460999
  arbitration_model: "uma_oracle"
bullets:
  - "Polymarket prices Democratic Michigan Senate win at 100%, no residual Republican probability remains."
  - "39% of all-time volume hit in 24h, reflecting broad late-cycle confirmation trading."
  - "Michigan was a marquee battleground; ceiling price signals live returns or early vote data resolved the race."
  - "Resolves on certified Michigan 2026 Senate outcome."
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
      poly_vol_24h_usd: 3026718.9755600006
sources:
  - label: "ClearMarket market record: Will a Michigan Senate election winner be determined by"
    url: "https://clearmarket.fyi/events/michigan-senate-election-winner"
    retrieved_at: "2026-11-04T07:48:42+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A ceiling price with 39% of lifetime volume in one day indicates Polymarket's Michigan contract has effectively settled; desks should use this as a benchmark for other competitive Senate call timing.
