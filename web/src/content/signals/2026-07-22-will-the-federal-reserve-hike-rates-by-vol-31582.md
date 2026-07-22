---
signal_id: "CMSIG20260722VS01"
signal_slug: "will-the-federal-reserve-hike-rates-by-vol-31582"
headline: "Fed July hike >25bps: 1% on $32K volume spike"
semantic_title: "Odds stay near zero on a Fed hike above 25bps in July"
telemetry: "1% · $32K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-22T10:22:39+00:00"
event_id: "CM-EVT-BHTHYWRLH7"
event_slug: "kxfeddecision-26jul"
event_question: "Will the Federal Reserve make a decision in July 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFEDDECISION-26JUL-H26"
  question_raw: "Will the Federal Reserve Hike rates by >25bps at their July 2026 meeting?"
  current_price: 0.01
  volume_24h_usd: 31582.52
  volume_cumulative_usd: 56437.78
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-07-29T18:05:00Z"
bullets:
  - "Kalshi prices a July rate hike above 25bps at just 1%, market dismisses the scenario outright."
  - "24h volume of $32K is 56% of all-time, the largest single-day activity on this contract."
  - "Volume surge likely driven by pre-meeting positioning as the July FOMC decision approaches."
  - "Resolves on the Federal Reserve's announced rate decision at the July 2026 FOMC meeting."
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
      kalshi_vol_24h_usd: 31582.52
sources:
  - label: "ClearMarket market record: Will the Federal Reserve make a decision in July 2026?"
    url: "https://clearmarket.fyi/events/kxfeddecision-26jul"
    retrieved_at: "2026-07-22T10:22:39+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Heavy one-session flow into a 1% contract reads as participants paying cheap insurance or closing out residual long positions ahead of the meeting, the consensus is firmly no-hike.
