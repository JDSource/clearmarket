---
signal_id: "CMSIG20260912VS00"
signal_slug: "will-the-federal-reserve-hike-rates-by-2-vol-2349087"
headline: "Fed Sept hike: 80% on $2.3M one-day surge"
semantic_title: "Traders pile into a 25bps Fed hike at 80%"
telemetry: "80% · $2.3M 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-12T11:56:57+00:00"
event_id: "CM-EVT-18Z2VTMCX0"
event_slug: "kxfeddecision-26sep"
event_question: "Will the Federal Reserve make a decision in September 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFEDDECISION-26SEP-H25"
  question_raw: "Will the Federal Reserve Hike rates by 25bps at their September 2026 meeting?"
  current_price: 0.8
  volume_24h_usd: 2349087.68
  volume_cumulative_usd: 9100058.7
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-09-16T18:05:00Z"
bullets:
  - "Kalshi prices a 25bps September hike at 80%, market treats it as near-certain."
  - "$2.35M traded in 24h, equal to 26% of all-time contract volume, signals broad conviction."
  - "Heavy flow just before the September FOMC meeting suggests positioning is locking in ahead of the decision."
  - "Contract resolves on the Fed's September 2026 rate announcement."
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
      kalshi_vol_24h_usd: 2349087.68
sources:
  - label: "ClearMarket market record: Will the Federal Reserve make a decision in September 2"
    url: "https://clearmarket.fyi/events/kxfeddecision-26sep"
    retrieved_at: "2026-09-12T11:56:57+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should treat this as a strong consensus signal that rate-sensitive books need to be positioned for a 25bps hike before the FOMC statement drops.
