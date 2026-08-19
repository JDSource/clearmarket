---
signal_id: "CMSIG20260819VS06"
signal_slug: "who-will-win-alaska-s-top-four-primary-f-vol-38412"
headline: "AK governor top-four, alt candidate: 91% on $38K"
semantic_title: "Second Alaska governor primary outcome holds at 91%"
telemetry: "91% · $38K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-19T08:32:13+00:00"
event_id: "CM-EVT-D03FJ4YFW7"
event_slug: "kxgovakprimary-26"
event_question: "Who will advance from the Alaska Governor primary?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXGOVAKPRIMARY-26-DBRO"
  question_raw: "Who will win Alaska's top-four primary for Governor?"
  current_price: 0.907
  volume_24h_usd: 38412.46
  volume_cumulative_usd: 54024.04
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-08-31T14:00:00Z"
bullets:
  - "A separate Alaska top-four governor primary outcome contract prices at 91%, strong but not certain."
  - "$38K in 24h is 71% of all-time volume for this contract, the highest single-day share of any spike here."
  - "The 9% discount alongside near-total volume concentration suggests a contested or close individual slot."
  - "Resolves on Alaska's certified top-four primary list, likely a specific candidate's advancement."
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
      kalshi_vol_24h_usd: 38412.46
sources:
  - label: "ClearMarket market record: Who will advance from the Alaska Governor primary?"
    url: "https://clearmarket.fyi/events/kxgovakprimary-26"
    retrieved_at: "2026-08-19T08:32:13+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

71% of all-time volume in one day at 91% tells a desk this specific Alaska slot is near-certain but carries live residual risk, worth monitoring for a late count shift.
