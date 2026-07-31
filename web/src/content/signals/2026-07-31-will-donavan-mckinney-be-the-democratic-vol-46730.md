---
signal_id: "CMSIG20260731VS04"
signal_slug: "will-donavan-mckinney-be-the-democratic-vol-46730"
headline: "McKinney MI-13 Dem nominee: 83% on $46K"
semantic_title: "Buyers back McKinney as MI-13 Democratic nominee front-runner"
telemetry: "83% · $47K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-31T10:35:22+00:00"
event_id: "CM-EVT-CYX84N0L20"
event_slug: "kxmi13d-26"
event_question: "Will the Democratic nominee for Michigan's 13th congressional district be decided by the 2026 general election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXMI13D-26-DMCK"
  question_raw: "Will Donavan McKinney be the Democratic nominee for MI-13?"
  current_price: 0.83
  volume_24h_usd: 46730.39
  volume_cumulative_usd: 138836.51
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-11-03T15:00:00Z"
bullets:
  - "At 83%, Kalshi prices McKinney as the strong favorite for the MI-13 Democratic nomination."
  - "$46K in 24h is 34% of all-time volume, a meaningful single-day capital deployment."
  - "Volume surge alongside high price suggests reinforcing news, polling, or endorsement activity."
  - "Resolves on official certification of the MI-13 Democratic nominee."
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
      kalshi_vol_24h_usd: 46730.39
sources:
  - label: "ClearMarket market record: Will the Democratic nominee for Michigan's 13th congres"
    url: "https://clearmarket.fyi/events/kxmi13d-26"
    retrieved_at: "2026-07-31T10:35:22+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Sustained high pricing with fresh capital inflow tells a desk the McKinney nomination is near-settled; the 83%/17% split between McKinney and Thanedar (see Spike 6) is a coherent paired signal worth monitoring.
