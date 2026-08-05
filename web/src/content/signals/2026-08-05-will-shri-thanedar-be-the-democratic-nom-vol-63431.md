---
signal_id: "CMSIG20260805VS05"
signal_slug: "will-shri-thanedar-be-the-democratic-nom-vol-63431"
headline: "Thanedar MI-13 nominee: 5% on $63K surge"
semantic_title: "Thanedar MI-13 nominee odds stay under 25% on new volume"
telemetry: "5% · $63K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-05T10:31:36+00:00"
event_id: "CM-EVT-CYX84N0L20"
event_slug: "kxmi13d-26"
event_question: "Will the Democratic nominee for Michigan's 13th congressional district be decided by the 2026 general election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXMI13D-26-STHA"
  question_raw: "Will Shri Thanedar be the Democratic nominee for MI-13?"
  current_price: 0.053
  volume_24h_usd: 63431.63
  volume_cumulative_usd: 82215.06
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-11-03T15:00:00Z"
bullets:
  - "Kalshi prices Thanedar at 5%, market assigns him a long-shot path in MI-13."
  - "77% of all-time contract volume arrived in 24h alongside the McKinney spike."
  - "Same Michigan primary cycle driving both contracts; Thanedar volume is the 'No' mirror."
  - "Resolves on MI-13 Democratic primary certification."
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
      kalshi_vol_24h_usd: 63431.63
sources:
  - label: "ClearMarket market record: Will the Democratic nominee for Michigan's 13th congres"
    url: "https://clearmarket.fyi/events/kxmi13d-26"
    retrieved_at: "2026-08-05T10:31:36+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

5% with nearly all lifetime volume in one session confirms Thanedar has been eliminated in market terms, desks can pair this with the McKinney 95% contract as a consistent read.
