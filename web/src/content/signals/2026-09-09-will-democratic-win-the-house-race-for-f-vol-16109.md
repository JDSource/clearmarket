---
signal_id: "CMSIG20260909VS06"
signal_slug: "will-democratic-win-the-house-race-for-f-vol-16109"
headline: "FL-14 Democrat: 65% on $16K volume pickup"
semantic_title: "Buyers back Democrats at 65% in FL-14 contest"
telemetry: "65% · $16K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-09T12:40:54+00:00"
event_id: "CM-EVT-H89NH9QH14"
event_slug: "kxhouserace-fl14-26"
event_question: "Will a winner be determined in the FL-14 House race by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-FL14-26-D"
  question_raw: "Will Democratic win the House race for FL-14?"
  current_price: 0.65
  volume_24h_usd: 16109.7
  volume_cumulative_usd: 35814.06
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "Kalshi prices a Democratic win in FL-14 at 65%, a meaningful but not overwhelming favorite read."
  - "45% of all-time volume arrived in 24h, a moderate but notable concentration of lifecycle activity."
  - "FL-14 at 65% Democratic is a competitive signal in a state Republicans have dominated at the federal level."
  - "Resolves on 2026 midterm Election Night certified results for Florida's 14th Congressional District."
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
      kalshi_vol_24h_usd: 16109.7
sources:
  - label: "ClearMarket market record: Will a winner be determined in the FL-14 House race by "
    url: "https://clearmarket.fyi/events/kxhouserace-fl14-26"
    retrieved_at: "2026-09-09T12:40:54+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 65% Democratic price in Florida is a genuine outlier worth flagging to a desk, the volume surge likely reflects new district-level data or candidate news that is not yet fully reflected in public polling.
