---
signal_id: "CMSIG20260924VS00"
signal_slug: "will-the-federal-reserve-hike-rates-by-2-vol-163290"
headline: "Fed Oct hike: 63% as $163K floods Kalshi"
semantic_title: "Heavy trading backs a Fed October hike at 63%"
telemetry: "63% · $163K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-24T13:08:49+00:00"
event_id: "CM-EVT-FPF77GZ320"
event_slug: "kxfeddecision-26oct"
event_question: "Will the Federal Reserve make a decision in October 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFEDDECISION-26OCT-H25"
  question_raw: "Will the Federal Reserve Hike rates by 25bps at their October 2026 meeting?"
  current_price: 0.63
  volume_24h_usd: 163290.1
  volume_cumulative_usd: 528008.85
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-10-28T18:05:00Z"
bullets:
  - "63% odds imply markets lean toward a 25bps October hike as the base case."
  - "Kalshi sees $163K in 24h, 31% of all-time volume in a single session."
  - "Fresh positioning ahead of Fed communications suggests traders are repricing rate-path risk now."
  - "Resolves on the FOMC October 2026 decision date."
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
      kalshi_vol_24h_usd: 163290.1
sources:
  - label: "ClearMarket market record: Will the Federal Reserve make a decision in October 202"
    url: "https://clearmarket.fyi/events/kxfeddecision-26oct"
    retrieved_at: "2026-09-24T13:08:49+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A single-session surge covering nearly a third of all-time volume signals that rate desks are actively hedging or expressing October meeting conviction ahead of key Fed guidance.
