---
signal_id: "CMSIG20260711VS02"
signal_slug: "will-donald-trump-attend-ufc-329-vol-77930"
headline: "Trump attends UFC 329: 3% on $78K volume"
semantic_title: "UFC 329 Trump attendance sits deep in tail-risk territory"
telemetry: "3% · $78K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-11T09:24:55+00:00"
event_id: "CM-EVT-YFTQM3YVN6"
event_slug: "kxtrumpufc-26jul"
event_question: "Will Donald Trump attend UFC 329?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXTRUMPUFC-26JUL-DJT"
  question_raw: "Will Donald Trump attend UFC 329?"
  current_price: 0.03
  volume_24h_usd: 77930.64
  volume_cumulative_usd: 130544.5
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-07-12T14:00:00Z"
bullets:
  - "Kalshi prices Trump attendance at 3%, consistent with a low-probability discretionary travel event."
  - "$78K traded in 24h represents 60% of all-time contract volume, significant acceleration of interest."
  - "UFC appearances have been a recurring Trump public engagement venue; fresh scheduling news or event confirmation likely driving attention."
  - "Contract resolves on confirmed attendance at UFC 329; date and venue details are the near-term catalyst."
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
      kalshi_vol_24h_usd: 77930.64
sources:
  - label: "ClearMarket market record: Will Donald Trump attend UFC 329?"
    url: "https://clearmarket.fyi/events/kxtrumpufc-26jul"
    retrieved_at: "2026-07-11T09:24:55+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 60% lifetime-volume single-session spike on a 3% contract suggests a news hook, likely UFC 329 date confirmation or a Trump schedule leak, and warrants a check against White House travel disclosures for event-driven positioning.
