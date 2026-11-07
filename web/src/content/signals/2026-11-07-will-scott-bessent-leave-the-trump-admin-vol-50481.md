---
signal_id: "CMSIG20261107VS04"
signal_slug: "will-scott-bessent-leave-the-trump-admin-vol-50481"
headline: "Bessent leaves Treasury: 8% on $50K Polymarket spike"
semantic_title: "Bessent exit odds stay well under 25% despite a fresh volume test"
telemetry: "8% · $50K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-07T07:49:22+00:00"
event_id: "CM-EVT-KZSP2MGN63"
event_slug: "who-will-leave-trump-administration-before-2027"
event_question: "Will anyone leave the Trump Administration before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xe51901c28b674d46cca978bb16790dbb42e291c31ce2acc8faa7bb16960c8eda"
  question_raw: "Will Scott Bessent leave the Trump administration before 2027?"
  current_price: 0.075
  volume_24h_usd: 50481.651961
  volume_cumulative_usd: 72258.34111
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "8% pricing places Bessent's departure firmly in low-probability tail territory."
  - "Polymarket sees $50K in 24h, 70% of all-time, a sharp concentrated burst."
  - "High share of all-time volume on a single session suggests a specific rumour or report prompted position checks."
  - "Resolves end of 2026; market decisively rejects the departure scenario."
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
      poly_vol_24h_usd: 50481.651961
sources:
  - label: "ClearMarket market record: Will anyone leave the Trump Administration before 2027?"
    url: "https://clearmarket.fyi/events/who-will-leave-trump-administration-before-2027"
    retrieved_at: "2026-11-07T07:49:22+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should flag the 70% all-time volume concentration as a signal that targeted speculation about Bessent surfaced and was quickly faded, the 8% price is the market's answer.
