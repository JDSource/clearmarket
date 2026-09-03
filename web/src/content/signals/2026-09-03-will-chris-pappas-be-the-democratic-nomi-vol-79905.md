---
signal_id: "CMSIG20260903VS00"
signal_slug: "will-chris-pappas-be-the-democratic-nomi-vol-79905"
headline: "Pappas NH Senate Dem: 97% on $79K surge"
semantic_title: "Pappas locks up NH Senate Democratic nod at 97%"
telemetry: "97% · $80K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-03T12:31:50+00:00"
event_id: "CM-EVT-9VM5MYBG78"
event_slug: "kxsenatenhd-26"
event_question: "Will the New Hampshire Democratic Senate nominee be determined by 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXSENATENHD-26-CPAP"
  question_raw: "Will Chris Pappas be the Democratic nominee for the Senate in New Hampshire?"
  current_price: 0.973
  volume_24h_usd: 79905.54
  volume_cumulative_usd: 203485.3
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-11-03T15:00:00Z"
bullets:
  - "Kalshi prices Pappas at 97%, market treats the Democratic nomination as virtually decided."
  - "24h volume of $79K is 39% of all-time flow, a significant single-day capital commitment."
  - "September timing aligns with pre-primary filing deadlines, drawing fresh attention to the race."
  - "Resolves on NH Democratic Senate primary result."
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
      kalshi_vol_24h_usd: 79905.54
sources:
  - label: "ClearMarket market record: Will the New Hampshire Democratic Senate nominee be det"
    url: "https://clearmarket.fyi/events/kxsenatenhd-26"
    retrieved_at: "2026-09-03T12:31:50+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The outsized volume share at near-certainty odds signals traders are closing out residual uncertainty ahead of an imminent primary formality, leaving little hedging room.
