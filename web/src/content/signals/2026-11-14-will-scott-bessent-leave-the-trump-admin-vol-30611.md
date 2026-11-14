---
signal_id: "CMSIG20261114VS05"
signal_slug: "will-scott-bessent-leave-the-trump-admin-vol-30611"
headline: "Bessent exit before 2027: 9% on $31K volume"
semantic_title: "Bessent leaving before 2027 stays a long shot at 9%"
telemetry: "9% · $31K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-14T07:48:40+00:00"
event_id: "CM-EVT-KZSP2MGN63"
event_slug: "who-will-leave-trump-administration-before-2027"
event_question: "Will anyone leave the Trump Administration before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xe51901c28b674d46cca978bb16790dbb42e291c31ce2acc8faa7bb16960c8eda"
  question_raw: "Will Scott Bessent leave the Trump administration before 2027?"
  current_price: 0.091
  volume_24h_usd: 30611.424554999998
  volume_cumulative_usd: 120211.72464699995
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices Treasury Secretary Bessent departing before 2027 at just 9%, market strongly backs his staying."
  - "24h volume of $31K is 25% of all-time, a fresh quarter of total contract activity arriving today."
  - "Surge mirrors the Lutnick contract, suggesting broad Cabinet-stability repricing is underway across multiple positions."
  - "Resolves January 1, 2027, any reported White House tension would move this price quickly."
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
      poly_vol_24h_usd: 30611.424554999998
sources:
  - label: "ClearMarket market record: Will anyone leave the Trump Administration before 2027?"
    url: "https://clearmarket.fyi/events/who-will-leave-trump-administration-before-2027"
    retrieved_at: "2026-11-14T07:48:40+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Low exit probability paired with a notable single-day volume share indicates desks are running paired Cabinet-risk screens today, likely in response to a common political headline affecting the administration broadly.
