---
signal_id: "CMSIG20261029VS01"
signal_slug: "will-the-federal-reserve-hike-rates-by-2-vol-122424"
headline: "Fed Dec hike 25bps: 79% on $122K volume"
semantic_title: "Traders pile into a December Fed hike at heavy odds"
telemetry: "79% · $122K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-29T07:48:41+00:00"
event_id: "CM-EVT-FKPVVZFMR8"
event_slug: "kxfeddecision-26dec"
event_question: "Will the Federal Reserve make a decision in December 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFEDDECISION-26DEC-H25"
  question_raw: "Will the Federal Reserve Hike rates by 25bps at their December 2026 meeting?"
  current_price: 0.79
  volume_24h_usd: 122424.25
  volume_cumulative_usd: 342360.55
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-12-09T19:05:00Z"
bullets:
  - "Kalshi prices a 25bps Fed hike at the December 2026 meeting at 79%, strong consensus for tightening."
  - "$122K in 24h volume represents 36% of all-time contract turnover, a significant single-session conviction print."
  - "Fresh positioning likely driven by macro data or Fed communication sharpening rate-path expectations."
  - "Resolves on the December 2026 FOMC decision date."
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
      kalshi_vol_24h_usd: 122424.25
sources:
  - label: "ClearMarket market record: Will the Federal Reserve make a decision in December 20"
    url: "https://clearmarket.fyi/events/kxfeddecision-26dec"
    retrieved_at: "2026-10-29T07:48:41+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 79% print with 36% of all-time volume in one session tells the desk the rate market is repricing December tightening as base case, cross-check against front-end rates and Fed funds futures for confirmation.
