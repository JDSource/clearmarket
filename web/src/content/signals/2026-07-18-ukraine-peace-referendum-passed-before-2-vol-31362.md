---
signal_id: "CMSIG20260718VS02"
signal_slug: "ukraine-peace-referendum-passed-before-2-vol-31362"
headline: "Ukraine peace referendum: 7% on $31K volume spike"
semantic_title: "Heavy flows discount a Ukraine peace referendum before 2027"
telemetry: "7% · $31K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-18T09:20:34+00:00"
event_id: "CM-EVT-5SVWYW2FT8"
event_slug: "ukraine-peace-referendum-passed-by-december-31-2026"
event_question: "Will a Ukraine peace referendum be passed before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xaea40d8fdffd33ead8f696f6b9dc0eb33d5c3ed0d31b57751e255bc7466a5c1d"
  question_raw: "Ukraine peace referendum passed before 2027?"
  current_price: 0.07
  volume_24h_usd: 31362.11765
  volume_cumulative_usd: 61439.54094100003
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Price at 7%, Polymarket traders heavily discount any formal Ukraine peace referendum passing before 2027."
  - "24h volume of $31K equals 51% of all-time contract flow, reflecting abrupt re-engagement with the question."
  - "Surge likely trails a peace-talk development, ceasefire framing, or territorial proposal surfacing in diplomatic channels."
  - "Hard end-2026 resolution window leaves minimal runway; 7% reflects structural, not zero, tail-risk for a rushed plebiscite."
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
      poly_vol_24h_usd: 31362.11765
sources:
  - label: "ClearMarket market record: Will a Ukraine peace referendum be passed before 2027?"
    url: "https://clearmarket.fyi/events/ukraine-peace-referendum-passed-by-december-31-2026"
    retrieved_at: "2026-07-18T09:20:34+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A single-session volume burst consuming half the contract's history at just 7% tells a desk that new diplomatic noise is pulling fresh capital in to fade the outcome, monitor Track-1.5 ceasefire and referendum proposal headlines as near-term catalysts.
