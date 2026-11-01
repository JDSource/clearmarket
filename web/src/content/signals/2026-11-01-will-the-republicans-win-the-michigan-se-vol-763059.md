---
signal_id: "CMSIG20261101VS00"
signal_slug: "will-the-republicans-win-the-michigan-se-vol-763059"
headline: "Michigan Senate GOP: 20% on $763K surge"
semantic_title: "Heavy trading tests GOP's long-shot Michigan Senate bid"
telemetry: "20% · $763K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-01T07:49:22+00:00"
event_id: "CM-EVT-P8B8CLLCB5"
event_slug: "michigan-senate-election-winner"
event_question: "Will a Michigan Senate election winner be determined by the next election cycle?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x3fd189cac9280dfc49a07115581e8d4c9e0b7e1c1e8580a44e9ff3d74e39cf2d"
  question_raw: "Will the Republicans win the Michigan Senate race in 2026?"
  current_price: 0.2
  volume_24h_usd: 763059.179458
  volume_cumulative_usd: 2566079.6549519994
  arbitration_model: "uma_oracle"
bullets:
  - "At 20%, Polymarket assigns Democrats a commanding four-in-five shot at holding Michigan."
  - "30% of all-time volume hit in 24h, $763K, flagging a sharp jump in attention."
  - "Michigan Senate draws fresh scrutiny a year out as GOP recruitment and map strategy sharpen."
  - "Resolves on the November 2026 election result."
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
      poly_vol_24h_usd: 763059.179458
sources:
  - label: "ClearMarket market record: Will a Michigan Senate election winner be determined by"
    url: "https://clearmarket.fyi/events/michigan-senate-election-winner"
    retrieved_at: "2026-11-01T07:49:22+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A sudden 30% all-time volume burst on a 20% GOP contract suggests desks are stress-testing downside scenarios for Republican Senate expansion math.
