---
signal_id: "CMSIG20260811VS00"
signal_slug: "will-ned-lamont-be-the-democratic-nomine-vol-53014"
headline: "Lamont CT Dem nominee: 100% on $53K surge"
semantic_title: "Lamont's CT Democratic nomination locked in at 100%"
telemetry: "100% · $53K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-11T08:50:18+00:00"
event_id: "CM-EVT-LJV7747HM9"
event_slug: "kxgovctnomd-26"
event_question: "Will Ned Lamont be the Connecticut Democratic Governor nominee?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXGOVCTNOMD-26-NLAM"
  question_raw: "Will Ned Lamont be the Democratic nominee for Governor in Connecticut?"
  current_price: 0.999
  volume_24h_usd: 53014.02
  volume_cumulative_usd: 71704.64
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-08-31T14:00:00Z"
bullets:
  - "Market prices Lamont as a certainty for the CT Democratic gubernatorial nomination."
  - "$53K traded in 24h, 74% of all-time volume, a near-complete market flush."
  - "Volume likely reflects late positioning ahead of a formal filing or party confirmation deadline."
  - "Resolves YES on Lamont securing the Democratic nomination for Connecticut governor."
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
      kalshi_vol_24h_usd: 53014.02
sources:
  - label: "ClearMarket market record: Will Ned Lamont be the Connecticut Democratic Governor "
    url: "https://clearmarket.fyi/events/kxgovctnomd-26"
    retrieved_at: "2026-08-11T08:50:18+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A near-total drawdown of all-time liquidity at 100% signals the market is closing out residual risk ahead of an imminent official confirmation, desks should treat this as effectively resolved.
