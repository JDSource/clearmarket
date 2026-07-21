---
signal_id: "CMSIG20260721VS02"
signal_slug: "will-john-james-be-the-republican-nomine-vol-102043"
headline: "James MI GOP gov nominee: 84% on $102K"
semantic_title: "John James Michigan GOP nominee status draws conviction bids"
telemetry: "84% · $102K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-21T10:22:52+00:00"
event_id: "CM-EVT-88B3W00208"
event_slug: "kxgovminomr-26"
event_question: "Who will be the Michigan Republican Governor nominee by 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXGOVMINOMR-26-JJ"
  question_raw: "Will John James be the Republican nominee for Governor in Michigan?"
  current_price: 0.84
  volume_24h_usd: 102043.78
  volume_cumulative_usd: 272044.13
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-11-03T15:00:00Z"
bullets:
  - "84% reflects strong market confidence that John James secures the Republican gubernatorial nomination in Michigan."
  - "Kalshi records $102K in 24h, 38% of all-time volume, a notable single-session concentration."
  - "Fresh flow at an elevated price suggests a primary catalyst, filing deadline, poll, or endorsement, is sharpening resolution odds."
  - "Resolves on official Republican nomination outcome in Michigan."
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
      kalshi_vol_24h_usd: 102043.78
sources:
  - label: "ClearMarket market record: Who will be the Michigan Republican Governor nominee by"
    url: "https://clearmarket.fyi/events/kxgovminomr-26"
    retrieved_at: "2026-07-21T10:22:52+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should flag this as primary-resolution positioning: capital is arriving to lock in a near-consensus nominee call, likely ahead of a near-term procedural or political confirmation event in Michigan.
