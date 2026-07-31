---
signal_id: "CMSIG20260731VS03"
signal_slug: "will-google-release-gemini-3-5-pro-befor-vol-21922"
headline: "Gemini 3.5 Pro by Aug 31: 87% on $21K"
semantic_title: "Odds hold strong on Gemini 3.5 Pro shipping before Aug 31"
telemetry: "87% · $22K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-31T10:35:22+00:00"
event_id: "CM-EVT-HCS172JGG4"
event_slug: "kxgemini-gemi35p"
event_question: "Will Google release Gemini 3.5 Pro?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXGEMINI-GEMI35P-26AUG31"
  question_raw: "Will Google release Gemini 3.5 Pro before Aug 31, 2026?"
  current_price: 0.87
  volume_24h_usd: 21922.93
  volume_cumulative_usd: 27642.18
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-09-07T14:00:00Z"
bullets:
  - "At 87%, Kalshi treats a Gemini 3.5 Pro release before Aug 31, 2026 as near-certain."
  - "$21K in 24h covers 79% of all-time volume, contract essentially repriced in one session."
  - "High conviction may reflect a Google announcement or credible product roadmap leak."
  - "Resolves on confirmed public release of Gemini 3.5 Pro by August 31, 2026."
atomic_claims:
  - type: "volume_anomaly"
    provenance: "24h + cumulative volume direct from kalshi API; intensity = 24h/cumulative (derived)"
    field_provenance:
      volume_24h_usd:
        tier: "direct"
        method: "kalshi_api"
      intensity:
        tier: "derived"
        method: "arithmetic"
        inputs: ["volume_24h_usd", "volume_cumulative_usd"]
    liquidity_context:
      kalshi_vol_24h_usd: 21922.93
sources:
  - label: "ClearMarket market record: Will Google release Gemini 3.5 Pro?"
    url: "https://clearmarket.fyi/events/kxgemini-gemi35p"
    retrieved_at: "2026-07-31T10:35:22+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

An 87% price absorbing nearly all lifetime volume signals the market has received strong confirmation signal, a desk tracking AI product cycles should treat this as a near-done event.
