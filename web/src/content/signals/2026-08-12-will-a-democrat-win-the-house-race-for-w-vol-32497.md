---
signal_id: "CMSIG20260812VS07"
signal_slug: "will-a-democrat-win-the-house-race-for-w-vol-32497"
headline: "Democrat wins WI-3: 63% on $32K surge"
semantic_title: "Buyers back Democrats to flip WI-3 in a thin market"
telemetry: "63% · $32K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-12T09:08:32+00:00"
event_id: "CM-EVT-6C7CNWJ6R7"
event_slug: "housewi3-26"
event_question: "WI-03 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSEWI3-26-D"
  question_raw: "Will a Democrat win the House race for WI-3?"
  current_price: 0.63
  volume_24h_usd: 32497.97
  volume_cumulative_usd: 36717.86
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices a Democratic WI-3 House win at 63%, a modest lean in a district that leans competitive."
  - "$32K in 24h is 89% of all-time volume, the vast majority of this contract's lifetime trading just printed."
  - "WI-3 gained attention alongside the Crowley Wisconsin primary sweep; coat-tail positioning likely."
  - "Resolves on the certified winner of the 2026 WI-3 House general election."
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
      kalshi_vol_24h_usd: 32497.97
sources:
  - label: "ClearMarket market record: WI-03 House winner?"
    url: "https://clearmarket.fyi/events/housewi3-26"
    retrieved_at: "2026-08-12T09:08:32+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With 89% of all-time volume clearing in one session on a thin contract, this is an initializing market rather than a deep one, desks should treat the 63% price as indicative but not yet robust until more liquidity develops.
