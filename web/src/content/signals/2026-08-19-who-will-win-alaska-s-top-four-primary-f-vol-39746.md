---
signal_id: "CMSIG20260819VS05"
signal_slug: "who-will-win-alaska-s-top-four-primary-f-vol-39746"
headline: "AK governor top-four winner: 100% on $40K surge"
semantic_title: "Alaska top-four governor primary winner priced as certain"
telemetry: "100% · $40K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-19T08:32:13+00:00"
event_id: "CM-EVT-D03FJ4YFW7"
event_slug: "kxgovakprimary-26"
event_question: "Who will advance from the Alaska Governor primary?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXGOVAKPRIMARY-26-BWIL"
  question_raw: "Who will win Alaska's top-four primary for Governor?"
  current_price: 0.999
  volume_24h_usd: 39746.3
  volume_cumulative_usd: 57544.01
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-08-31T14:00:00Z"
bullets:
  - "One candidate priced at 100% to advance from Alaska's top-four gubernatorial primary on Kalshi."
  - "$40K in 24h is 69% of all-time volume, the single largest session by share for this contract."
  - "Alaska's August primary calendar and today's date suggest results are driving the certainty print."
  - "Resolves on official Alaska Division of Elections certifying the top-four primary results."
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
      kalshi_vol_24h_usd: 39746.3
sources:
  - label: "ClearMarket market record: Who will advance from the Alaska Governor primary?"
    url: "https://clearmarket.fyi/events/kxgovakprimary-26"
    retrieved_at: "2026-08-19T08:32:13+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Nearly 70% of lifetime volume in one day at 100% is a settlement signal, the Alaska primary result is known and this contract is being closed out.
