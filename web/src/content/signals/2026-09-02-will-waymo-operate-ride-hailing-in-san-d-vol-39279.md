---
signal_id: "CMSIG20260902VS03"
signal_slug: "will-waymo-operate-ride-hailing-in-san-d-vol-39279"
headline: "Waymo San Diego by Jan 1: 86% on $39K"
semantic_title: "Waymo San Diego odds hold at 86% through a volume test"
telemetry: "86% · $39K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-02T12:29:56+00:00"
event_id: "CM-EVT-GV7S80KSY9"
event_slug: "kxwaymocity-26dec"
event_question: "Where will Waymo operate in 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXWAYMOCITY-26DEC-SAN"
  question_raw: "Will Waymo operate ride-hailing in San Diego, CA before Jan 1, 2027?"
  current_price: 0.86
  volume_24h_usd: 39279.14
  volume_cumulative_usd: 44112.17
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-08T15:00:00Z"
bullets:
  - "Kalshi prices a Waymo San Diego launch before Jan 1, 2027 at 86%, meaningful but not a certainty."
  - "24h volume of $39K is 89% of all-time, the market is pricing in a strong but not locked-in outcome."
  - "San Diego lags Denver and Tampa in odds, implying the regulatory or operational path has more friction."
  - "Resolves YES if commercial Waymo ride-hailing begins in San Diego before January 1, 2027."
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
      kalshi_vol_24h_usd: 39279.14
sources:
  - label: "ClearMarket market record: Where will Waymo operate in 2026?"
    url: "https://clearmarket.fyi/events/kxwaymocity-26dec"
    retrieved_at: "2026-09-02T12:29:56+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 86% print alongside near-total all-time volume suggests the San Diego contract is attracting directional flow that sees a launch as likely but not guaranteed, worth monitoring for permit news.
