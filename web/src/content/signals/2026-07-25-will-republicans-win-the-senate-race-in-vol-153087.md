---
signal_id: "CMSIG20260725VS00"
signal_slug: "will-republicans-win-the-senate-race-in-vol-153087"
headline: "Iowa Senate GOP: 60% on $153K inflow"
semantic_title: "Iowa Senate GOP odds hold at 60% through a volume surge"
telemetry: "60% · $153K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-25T09:43:16+00:00"
event_id: "CM-EVT-R8V0583H75"
event_slug: "senateia-26"
event_question: "Iowa Senate winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "SENATEIA-26-R"
  question_raw: "Will Republicans win the Senate race in Iowa?"
  current_price: 0.6
  volume_24h_usd: 153087.2
  volume_cumulative_usd: 317039.71
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices Republicans at 60%, a clear but not commanding lead in the Iowa Senate race."
  - "$153K traded in 24h, nearly half (48%) of all-time volume, signaling a sharp burst of fresh attention."
  - "Surge likely tied to a candidate announcement, polling drop, or fundraising news drawing traders to reprice."
  - "Contract resolves on Iowa Senate election outcome; 60% implies Democrats remain live at 40%."
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
      kalshi_vol_24h_usd: 153087.2
sources:
  - label: "ClearMarket market record: Iowa Senate winner?"
    url: "https://clearmarket.fyi/events/senateia-26"
    retrieved_at: "2026-07-25T09:43:16+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Nearly half of all-time volume arriving in one session flags an imminent catalyst, polling, a candidate move, or national party spending, that a desk should track before the next price shift.
