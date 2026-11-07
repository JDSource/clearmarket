---
signal_id: "CMSIG20261107VS04"
signal_slug: "will-scott-bessent-leave-the-trump-admin-vol-53176"
headline: "Bessent leaves Treasury: 9% on $53K volume"
semantic_title: "Bessent keeping Treasury post; odds of exit stay at 9%"
telemetry: "9% · $53K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-07T14:39:51+00:00"
event_id: "CM-EVT-KZSP2MGN63"
event_slug: "who-will-leave-trump-administration-before-2027"
event_question: "Will anyone leave the Trump Administration before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xe51901c28b674d46cca978bb16790dbb42e291c31ce2acc8faa7bb16960c8eda"
  question_raw: "Will Scott Bessent leave the Trump administration before 2027?"
  current_price: 0.091
  volume_24h_usd: 53176.268415999984
  volume_cumulative_usd: 76532.41716999999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices Bessent departing the Trump administration before 2027 at just 9%, market rates him as likely to stay."
  - "$53K in 24h is 69% of all-time contract volume, a large share suggesting this question is newly active."
  - "Fresh attention may reflect spillover from the Miller departure spike (Spike 0), prompting traders to reprice other cabinet exit risks."
  - "Contract resolves end-2026."
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
      poly_vol_24h_usd: 53176.268415999984
sources:
  - label: "ClearMarket market record: Will anyone leave the Trump Administration before 2027?"
    url: "https://clearmarket.fyi/events/who-will-leave-trump-administration-before-2027"
    retrieved_at: "2026-11-07T14:39:51+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The high all-time volume share on a low-probability contract signals a desk that traders are actively monitoring cabinet stability broadly, Bessent is repriced as low-risk but the question is live.
