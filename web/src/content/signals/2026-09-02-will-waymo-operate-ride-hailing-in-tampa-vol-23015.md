---
signal_id: "CMSIG20260902VS05"
signal_slug: "will-waymo-operate-ride-hailing-in-tampa-vol-23015"
headline: "Waymo Tampa by Jan 1: 96% on $23K surge"
semantic_title: "Waymo Tampa launch by Jan 1 holds 96% amid volume spike"
telemetry: "96% · $23K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-02T12:29:56+00:00"
event_id: "CM-EVT-GV7S80KSY9"
event_slug: "kxwaymocity-26dec"
event_question: "Where will Waymo operate in 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXWAYMOCITY-26DEC-TAM"
  question_raw: "Will Waymo operate ride-hailing in Tampa, FL before Jan 1, 2027?"
  current_price: 0.96
  volume_24h_usd: 23015.52
  volume_cumulative_usd: 31929.25
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-08T15:00:00Z"
bullets:
  - "Kalshi prices Waymo ride-hailing in Tampa at 96% before year-end, near-certain but with slightly more residual risk than Denver."
  - "$23K in 24h is 72% of all-time volume, showing concentrated attention across all three Waymo expansion markets simultaneously."
  - "The triple Waymo volume surge across Denver, San Diego, and Tampa points to a company-wide announcement or regulatory update."
  - "Resolves YES if Waymo offers commercial rides in Tampa before January 1, 2027."
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
      kalshi_vol_24h_usd: 23015.52
sources:
  - label: "ClearMarket market record: Where will Waymo operate in 2026?"
    url: "https://clearmarket.fyi/events/kxwaymocity-26dec"
    retrieved_at: "2026-09-02T12:29:56+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The synchronized volume surge across three Waymo city contracts in a single session is a strong signal that a company-level catalyst, expansion announcement, permit batch approval, hit the tape.
