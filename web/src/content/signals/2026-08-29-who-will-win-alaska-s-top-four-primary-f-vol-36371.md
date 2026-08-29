---
signal_id: "CMSIG20260829VS03"
signal_slug: "who-will-win-alaska-s-top-four-primary-f-vol-36371"
headline: "Alaska Gov primary leader: 84% on $36K"
semantic_title: "Buyers back the Alaska governor primary favorite at 84%"
telemetry: "84% · $36K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-29T13:34:58+00:00"
event_id: "CM-EVT-D03FJ4YFW7"
event_slug: "kxgovakprimary-26"
event_question: "Who will advance from the Alaska Governor primary?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXGOVAKPRIMARY-26-TTAY"
  question_raw: "Who will win Alaska's top-four primary for Governor?"
  current_price: 0.84
  volume_24h_usd: 36371.08
  volume_cumulative_usd: 90831.3
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-08-31T14:00:00Z"
bullets:
  - "84% price reflects strong consensus around a single front-runner in Alaska's top-four gubernatorial primary."
  - "Kalshi sees $36K in 24h, equal to 40% of all-time volume, meaningful liquidity for a state-level race."
  - "Fresh volume at 84% suggests the field has narrowed and traders are pricing out remaining challengers."
  - "Resolves on the Alaska primary election result."
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
      kalshi_vol_24h_usd: 36371.08
sources:
  - label: "ClearMarket market record: Who will advance from the Alaska Governor primary?"
    url: "https://clearmarket.fyi/events/kxgovakprimary-26"
    retrieved_at: "2026-08-29T13:34:58+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 40% all-time volume day at an already-high probability indicates the race is approaching resolution consensus, a desk tracking gubernatorial political risk should note the strong directional lean.
