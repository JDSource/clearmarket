---
signal_id: "CMSIG20260902VS02"
signal_slug: "will-waymo-operate-ride-hailing-in-denve-vol-99112"
headline: "Waymo Denver by Jan 1: 99% on $99K surge"
semantic_title: "Waymo Denver launch before Jan 1 draws heavy backing"
telemetry: "99% · $99K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-02T12:29:56+00:00"
event_id: "CM-EVT-GV7S80KSY9"
event_slug: "kxwaymocity-26dec"
event_question: "Where will Waymo operate in 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXWAYMOCITY-26DEC-DEN"
  question_raw: "Will Waymo operate ride-hailing in Denver, CO before Jan 1, 2027?"
  current_price: 0.99
  volume_24h_usd: 99112.07
  volume_cumulative_usd: 112352.48
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-08T15:00:00Z"
bullets:
  - "Kalshi prices Waymo ride-hailing in Denver at 99%, market is treating launch as a done deal."
  - "$99K in 24h is 88% of all-time contract volume, suggesting a specific catalyst drove traders to close out remaining doubt."
  - "A regulatory filing or public launch announcement in Denver likely triggered the volume flush at near-certainty pricing."
  - "Resolves YES if Waymo offers commercial ride-hailing in Denver before January 1, 2027."
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
      kalshi_vol_24h_usd: 99112.07
sources:
  - label: "ClearMarket market record: Where will Waymo operate in 2026?"
    url: "https://clearmarket.fyi/events/kxwaymocity-26dec"
    retrieved_at: "2026-09-02T12:29:56+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Near-total all-time volume printed in a single session at 99% points to a confirmatory news event; desks should check for a Denver launch announcement or permit approval.
