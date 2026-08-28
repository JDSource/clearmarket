---
signal_id: "CMSIG20260828VS02"
signal_slug: "will-chris-pappas-be-the-democratic-nomi-vol-25810"
headline: "Pappas NH Dem Senate: 94% on $26K volume"
semantic_title: "Pappas locks up NH Senate Democratic nod at 94% on Kalshi"
telemetry: "94% · $26K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-28T19:52:39+00:00"
event_id: "CM-EVT-9VM5MYBG78"
event_slug: "kxsenatenhd-26"
event_question: "Will the New Hampshire Democratic Senate nominee be determined by 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXSENATENHD-26-CPAP"
  question_raw: "Will Chris Pappas be the Democratic nominee for the Senate in New Hampshire?"
  current_price: 0.941
  volume_24h_usd: 25810.77
  volume_cumulative_usd: 79781.8
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-11-03T15:00:00Z"
bullets:
  - "94% on Kalshi prices Pappas as the near-certain Democratic Senate nominee in New Hampshire."
  - "Today's $26K is 32% of all-time handle, a meaningful single-day share in a race approaching resolution."
  - "Cross-venue alignment with Polymarket at 93% (spike 5) reinforces the read, two books, same signal."
  - "Resolves when New Hampshire certifies Democratic primary results."
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
      kalshi_vol_24h_usd: 25810.77
sources:
  - label: "ClearMarket market record: Will the New Hampshire Democratic Senate nominee be det"
    url: "https://clearmarket.fyi/events/kxsenatenhd-26"
    retrieved_at: "2026-08-28T19:52:39+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Consistent high-90s pricing across two venues with renewed volume flow tells a desk that Pappas's nomination is effectively settled, attention now belongs on the general-election matchup.
