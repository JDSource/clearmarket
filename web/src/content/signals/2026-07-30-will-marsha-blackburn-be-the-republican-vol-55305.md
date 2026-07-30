---
signal_id: "CMSIG20260730VS05"
signal_slug: "will-marsha-blackburn-be-the-republican-vol-55305"
headline: "Blackburn TN GOP nominee: 93% on $55K"
semantic_title: "Blackburn locks up the Tennessee GOP governor nod"
telemetry: "93% · $55K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-30T10:21:41+00:00"
event_id: "CM-EVT-5MV6W6X5T7"
event_slug: "kxgovtnnomr-2-26"
event_question: "Will Bill Lee be the Tennessee Republican Governor nominee by 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXGOVTNNOMR-2-26-MBLA"
  question_raw: "Will Marsha Blackburn be the Republican nominee for Governor in Tennessee?"
  current_price: 0.929
  volume_24h_usd: 55305.48
  volume_cumulative_usd: 88978.27
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-08-31T14:00:00Z"
bullets:
  - "93% pricing reflects near-certainty in the prediction market that Blackburn wins the Republican gubernatorial nomination."
  - "$55K in 24h is 62% of all-time volume, the contract's heaviest session by share, suggesting a catalyst is in play."
  - "Heavy one-sided flow at a high price points to a recent development, filing deadline, poll, or endorsement, cementing her position."
  - "Resolves on the outcome of the Tennessee Republican gubernatorial primary."
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
      kalshi_vol_24h_usd: 55305.48
sources:
  - label: "ClearMarket market record: Will Bill Lee be the Tennessee Republican Governor nomi"
    url: "https://clearmarket.fyi/events/kxgovtnnomr-2-26"
    retrieved_at: "2026-07-30T10:21:41+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 93% price on record relative volume signals the market has priced in near-certainty of Blackburn's nomination, desks covering U.S. political risk should treat Tennessee's governor race as effectively called for her on the Republican side.
