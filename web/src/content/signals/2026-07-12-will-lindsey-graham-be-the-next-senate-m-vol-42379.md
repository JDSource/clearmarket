---
signal_id: "CMSIG20260712VS03"
signal_slug: "will-lindsey-graham-be-the-next-senate-m-vol-42379"
headline: "Graham next Senate Majority Leader: 1% on $42K"
semantic_title: "Graham Senate majority leader bid priced into long-shot territory"
telemetry: "1% · $42K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-12T09:48:30+00:00"
event_id: "CM-EVT-ZZZ60Y4302"
event_slug: "next-senate-majority-leader-485"
event_question: "Who will be the Senate Majority Leader in the next Congress?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0f8ba4259a1b9f7fcbed4cc0297ce177f09802e95ba778462582c1e882a4c40b"
  question_raw: "Will Lindsey Graham be the next Senate Majority Leader?"
  current_price: 0.011
  volume_24h_usd: 42379.029
  volume_cumulative_usd: 55099.296277
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-03T00:00:00Z"
bullets:
  - "Polymarket prices Graham at 1%, market assigns him virtually no path to Senate Majority Leader."
  - "$42K in 24h is 77% of a thin $55K all-time pool, indicating a concentrated, decisive flow event."
  - "Senate leadership race attention may reflect broader Thune succession chatter or caucus positioning news."
  - "Resolves upon next Senate Majority Leader selection; flows confirm consensus against Graham."
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
      poly_vol_24h_usd: 42379.029
sources:
  - label: "ClearMarket market record: Who will be the Senate Majority Leader in the next Cong"
    url: "https://clearmarket.fyi/events/next-senate-majority-leader-485"
    retrieved_at: "2026-07-12T09:48:30+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The near-total all-time volume concentration in a single session at 1% suggests a small number of informed actors settling a contrarian position after a leadership catalyst.
