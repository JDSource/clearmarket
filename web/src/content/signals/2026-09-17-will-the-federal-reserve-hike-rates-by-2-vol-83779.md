---
signal_id: "CMSIG20260917VS03"
signal_slug: "will-the-federal-reserve-hike-rates-by-2-vol-83779"
headline: "Fed Oct. 25bps hike: 45% on $84K surge"
semantic_title: "A 25bps October hike stays a live risk trade at 45%"
telemetry: "45% · $84K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-17T13:05:20+00:00"
event_id: "CM-EVT-FPF77GZ320"
event_slug: "kxfeddecision-26oct"
event_question: "Will the Federal Reserve make a decision in October 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFEDDECISION-26OCT-H25"
  question_raw: "Will the Federal Reserve Hike rates by 25bps at their October 2026 meeting?"
  current_price: 0.45
  volume_24h_usd: 83779.96
  volume_cumulative_usd: 141852.78
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-10-28T18:05:00Z"
bullets:
  - "Market prices a 45% chance the Fed hikes 25bps in October, nearly matching the hold contract."
  - "$84K traded in 24h, 59% of all-time, showing concentrated fresh interest in the hike scenario."
  - "Paired with the hold contract at 55%, the two together reflect genuine rate-path uncertainty."
  - "Resolves on the October 2026 FOMC announcement."
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
      kalshi_vol_24h_usd: 83779.96
sources:
  - label: "ClearMarket market record: Will the Federal Reserve make a decision in October 202"
    url: "https://clearmarket.fyi/events/kxfeddecision-26oct"
    retrieved_at: "2026-09-17T13:05:20+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With hold at 55% and hike at 45%, traders are treating October as genuinely binary, desks should monitor for catalysts that collapse either tail before the meeting.
