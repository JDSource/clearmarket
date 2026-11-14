---
signal_id: "CMSIG20261114VS01"
signal_slug: "will-the-federal-reserve-hike-rates-by-vol-126684"
headline: "Fed Dec hike >25bps: 10% on $127K volume"
semantic_title: "Fed December hike above 25bps stays a long shot at 10%"
telemetry: "10% · $127K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-14T07:48:40+00:00"
event_id: "CM-EVT-FKPVVZFMR8"
event_slug: "kxfeddecision-26dec"
event_question: "Will the Federal Reserve make a decision in December 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFEDDECISION-26DEC-H26"
  question_raw: "Will the Federal Reserve Hike rates by >25bps at their December 2026 meeting?"
  current_price: 0.1
  volume_24h_usd: 126684.3
  volume_cumulative_usd: 464979.55
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-12-09T19:05:00Z"
bullets:
  - "Kalshi prices a December 2026 Fed hike above 25bps at just 10%, market firmly expects a hold or smaller move."
  - "24h volume of $127K is 27% of all-time, a meaningful one-day inflow against an established contract."
  - "Renewed trading likely tied to incoming inflation data or Fed speaker commentary this week."
  - "Resolves at the December 2026 FOMC decision, any hawkish pivot would reprice sharply."
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
      kalshi_vol_24h_usd: 126684.3
sources:
  - label: "ClearMarket market record: Will the Federal Reserve make a decision in December 20"
    url: "https://clearmarket.fyi/events/kxfeddecision-26dec"
    retrieved_at: "2026-11-14T07:48:40+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Fresh capital loading the 'No' side at 90% conviction on an aggressive Fed hike is a clean rates-desk signal that aggressive tightening remains largely off the table, though the volume spike warrants monitoring for a reversing catalyst.
