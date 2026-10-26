---
signal_id: "CMSIG20261026VS04"
signal_slug: "will-anthropic-s-public-ticker-be-ant-vol-24568"
headline: "Anthropic ticker $ANT: 98% on $25K volume surge"
semantic_title: "Anthropic ticker $ANT near-certain at 98% on strong flow"
telemetry: "98% · $25K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-26T14:48:56+00:00"
event_id: "CM-EVT-11K3FN6LM8"
event_slug: "what-will-anthropics-public-ticker-be"
event_question: "What will Anthropic's public ticker symbol be?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xa1b504ea42655312c0e3b5b0d1ee97d7a3d0f414adc8b2c59fc94459ff051de1"
  question_raw: "Will Anthropic's public ticker be $ANT?"
  current_price: 0.982
  volume_24h_usd: 24568.967753
  volume_cumulative_usd: 60202.419888
  arbitration_model: "uma_oracle"
  resolves_at: "2027-12-31T23:30:00Z"
bullets:
  - "At 98%, traders have near-fully priced $ANT as Anthropic's IPO ticker symbol."
  - "41% of all-time volume cleared in 24 hours, reinforcing conviction at a high price."
  - "A fresh filing or insider confirmation likely catalyzed the volume burst near full certainty."
  - "Resolves when Anthropic's public ticker is officially confirmed or assigned."
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
      poly_vol_24h_usd: 24568.967753
sources:
  - label: "ClearMarket market record: What will Anthropic's public ticker symbol be?"
    url: "https://clearmarket.fyi/events/what-will-anthropics-public-ticker-be"
    retrieved_at: "2026-10-26T14:48:56+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Near-certain pricing drawing 41% of lifetime volume in one session suggests a credible ticker confirmation signal has surfaced, desks monitoring the Anthropic IPO pipeline should take note.
