---
signal_id: "CMSIG20260708VS02"
signal_slug: "fed-rate-hike-by-september-2026-meeting-vol-59969"
headline: "Fed hike by Sep 2026: 35% on $60K Polymarket vol"
semantic_title: "Fed hike by September sits at 35% on fresh flows"
telemetry: "35% · $60K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-08T10:14:29+00:00"
event_id: "CM-EVT-VZKJ3PV470"
event_slug: "fed-rate-hike-by"
event_question: "Will the Federal Reserve raise its benchmark interest rate by the settlement date?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x73d8a8208d23a74937d114a713d6a56cd4161a1068056c52ac74c8419c99da7c"
  question_raw: "Fed Rate Hike by September 2026 Meeting?"
  current_price: 0.35
  volume_24h_usd: 59969.537583
  volume_cumulative_usd: 210901.20875400005
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-09T00:00:00Z"
bullets:
  - "35% price implies the market is genuinely split on whether the Fed resumes tightening by September."
  - "24h volume $60K is 28% of all-time, suggesting renewed macro attention rather than a spike rumor."
  - "Fresh CPI, labor, or Fed communication likely reignited debate over the September meeting path."
  - "Resolves at the September 2026 FOMC decision."
atomic_claims:
  - type: "volume_anomaly"
    provenance: "24h + cumulative volume direct from polymarket API; intensity = 24h/cumulative (derived)"
    field_provenance:
      volume_24h_usd:
        tier: "direct"
        method: "polymarket_api"
      intensity:
        tier: "derived"
        method: "arithmetic"
        inputs: ["volume_24h_usd", "volume_cumulative_usd"]
    liquidity_context:
      poly_vol_24h_usd: 59969.537583
sources:
  - label: "ClearMarket market record: Will the Federal Reserve raise its benchmark interest r"
    url: "https://clearmarket.fyi/events/fed-rate-hike-by"
    retrieved_at: "2026-07-08T10:14:29+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A rates desk should note that 35% is high enough to hedge against a hike scenario, the volume surge implies macro participants are actively repricing the September meeting following recent data or Fed commentary.
