---
signal_id: "CMSIG20260827VS02"
signal_slug: "will-chris-pappas-be-the-democratic-nomi-vol-24863"
headline: "Pappas NH Senate Dem nominee: 94% on $25K"
semantic_title: "Traders back Pappas as the NH Senate Democratic pick"
telemetry: "94% · $25K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-27T18:47:16+00:00"
event_id: "CM-EVT-9VM5MYBG78"
event_slug: "kxsenatenhd-26"
event_question: "Will the New Hampshire Democratic Senate nominee be determined by 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXSENATENHD-26-CPAP"
  question_raw: "Will Chris Pappas be the Democratic nominee for the Senate in New Hampshire?"
  current_price: 0.936
  volume_24h_usd: 24863.58
  volume_cumulative_usd: 51269.73
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-11-03T15:00:00Z"
bullets:
  - "Kalshi prices 94%, strong consensus Pappas locks up the Democratic Senate nomination in New Hampshire."
  - "24h volume of $25K is 48% of all-time, indicating a meaningful fresh-attention moment."
  - "Spike likely reflects a filing deadline, endorsement, or candidate news narrowing the field."
  - "Nominee determination is the resolution trigger; general-election pricing would follow separately."
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
      kalshi_vol_24h_usd: 24863.58
sources:
  - label: "ClearMarket market record: Will the New Hampshire Democratic Senate nominee be det"
    url: "https://clearmarket.fyi/events/kxsenatenhd-26"
    retrieved_at: "2026-08-27T18:47:16+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 48% all-time share in one day suggests a discrete news catalyst, a desk monitoring NH Senate exposure should check for recent filing or withdrawal developments.
