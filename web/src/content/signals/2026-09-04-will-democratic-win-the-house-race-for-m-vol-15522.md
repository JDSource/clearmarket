---
signal_id: "CMSIG20260904VS02"
signal_slug: "will-democratic-win-the-house-race-for-m-vol-15522"
headline: "Democrat MO-05 House: 84% on $15K surge"
semantic_title: "Heavy trading backs Democrat in MO-05 at 84%"
telemetry: "84% · $16K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-04T12:29:08+00:00"
event_id: "CM-EVT-9K8QCZYSH5"
event_slug: "kxhousemo5-26"
event_question: "Will the winner of the Missouri 5th Congressional District House race be determined by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSEMO5-26-D"
  question_raw: "Will Democratic win the House race for MO-05?"
  current_price: 0.84
  volume_24h_usd: 15522.6
  volume_cumulative_usd: 22144.73
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices the Democratic candidate at 84%, odds consistent with a safely leaning but not locked district."
  - "$15K in 24h accounts for 70% of all-time volume, an unusually dense single-session print."
  - "MO-05 drawing fresh capital at this stage suggests a catalyst, candidate news or a competitive challenge emerging."
  - "Contract resolves on the certified winner of the MO-05 U.S. House general election."
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
      kalshi_vol_24h_usd: 15522.6
sources:
  - label: "ClearMarket market record: Will the winner of the Missouri 5th Congressional Distr"
    url: "https://clearmarket.fyi/events/kxhousemo5-26"
    retrieved_at: "2026-09-04T12:29:08+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Seventy percent of lifetime volume in one day on a nominally safe Democratic seat warrants attention, a desk should check for a credible Republican challenger or redistricting development that is pulling in hedging flow.
