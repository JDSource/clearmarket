---
signal_id: "CMSIG20260712VS02"
signal_slug: "will-donald-trump-attend-ufc-329-vol-87060"
headline: "Trump at UFC 329: 1% on $87K calendar flush"
semantic_title: "Traders fade Trump's UFC 329 appearance as near-zero risk"
telemetry: "1% · $87K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-12T09:48:30+00:00"
event_id: "CM-EVT-YFTQM3YVN6"
event_slug: "kxtrumpufc-26jul"
event_question: "Will Donald Trump attend UFC 329?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXTRUMPUFC-26JUL-DJT"
  question_raw: "Will Donald Trump attend UFC 329?"
  current_price: 0.01
  volume_24h_usd: 87060.61
  volume_cumulative_usd: 130658.99
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-07-12T14:00:00Z"
bullets:
  - "Kalshi prices Trump UFC 329 attendance at 1%, market assigns near-certainty he will not attend."
  - "$87K in 24h is 67% of all-time volume, suggesting concentrated resolution-window activity."
  - "Proximity to the event date is driving settlement flows rather than new directional conviction."
  - "Contract resolves on UFC 329 date; volume pattern consistent with late-stage arbitrage compression."
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
      kalshi_vol_24h_usd: 87060.61
sources:
  - label: "ClearMarket market record: Will Donald Trump attend UFC 329?"
    url: "https://clearmarket.fyi/events/kxtrumpufc-26jul"
    retrieved_at: "2026-07-12T09:48:30+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

High share of all-time volume at 1% near event date signals market participants closing positions into resolution rather than expressing a fresh view.
