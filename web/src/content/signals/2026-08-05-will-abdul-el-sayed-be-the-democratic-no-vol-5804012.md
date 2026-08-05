---
signal_id: "CMSIG20260805VS00"
signal_slug: "will-abdul-el-sayed-be-the-democratic-no-vol-5804012"
headline: "El-Sayed MI Senate nominee: 99% on $5.8M surge"
semantic_title: "Traders pile into El-Sayed as MI Senate Dem nominee"
telemetry: "99% · $5.8M 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-05T10:31:36+00:00"
event_id: "CM-EVT-ZMWFMPNXD9"
event_slug: "kxsenatemid-26"
event_question: "Will the Michigan Democratic Senate nominee be determined by the 2026 election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXSENATEMID-26-AELS"
  question_raw: "Will Abdul El-Sayed be the Democratic nominee for the Senate in Michigan?"
  current_price: 0.989
  volume_24h_usd: 5804012.91
  volume_cumulative_usd: 9626052.32
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-11-03T15:00:00Z"
bullets:
  - "Kalshi prices El-Sayed at 99%, market treats nomination as effectively decided."
  - "24h volume of $5.8M is 60% of all-time; single-day flow dominates contract history."
  - "Primary day or imminent vote count likely driving final settlement positioning."
  - "Resolves on certification of 2026 Michigan Democratic Senate primary result."
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
      kalshi_vol_24h_usd: 5804012.91
sources:
  - label: "ClearMarket market record: Will the Michigan Democratic Senate nominee be determin"
    url: "https://clearmarket.fyi/events/kxsenatemid-26"
    retrieved_at: "2026-08-05T10:31:36+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Near-unanimous odds backed by majority of all-time volume in one session signals the market is in terminal settlement mode, the primary outcome is no longer in dispute.
