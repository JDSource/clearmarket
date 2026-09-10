---
signal_id: "CMSIG20260910VS02"
signal_slug: "who-will-win-the-2026-providence-ri-may-vol-62290"
headline: "Providence mayor 2026: 98% on $62K surge"
semantic_title: "Providence mayor race locked in at 98% on dominant volume"
telemetry: "98% · $62K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-10T12:40:48+00:00"
event_id: "CM-EVT-2T4GQHNZN2"
event_slug: "kxprovidencemayor-26"
event_question: "Will there be a winner of the Providence mayoral election by November 3, 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPROVIDENCEMAYOR-26-DMOR"
  question_raw: "Who will win the 2026 Providence, RI mayoral election?"
  current_price: 0.98
  volume_24h_usd: 62290.39
  volume_cumulative_usd: 93665.22
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-11-03T15:00:00Z"
bullets:
  - "Kalshi prices the leading candidate at 98%, leaving almost no room for an upset."
  - "$62K in 24h volume represents 67% of all-time contract volume, an extraordinary concentration of late money."
  - "A near-total late-stage pile-in at near-certainty odds suggests a decisive primary result or ballot certification is imminent."
  - "Resolves on the 2026 Providence, RI mayoral election outcome."
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
      kalshi_vol_24h_usd: 62290.39
sources:
  - label: "ClearMarket market record: Will there be a winner of the Providence mayoral electi"
    url: "https://clearmarket.fyi/events/kxprovidencemayor-26"
    retrieved_at: "2026-09-10T12:40:48+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 67% all-time volume share flooding in at 98% is a strong signal that resolution is close and the field has effectively cleared, desks tracking municipal New England politics should treat this as near-closed.
