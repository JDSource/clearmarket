---
signal_id: "CMSIG20261031VS00"
signal_slug: "will-republicans-win-the-senate-race-in-vol-808890"
headline: "Nebraska Senate GOP: 75% on $809K Kalshi spike"
semantic_title: "Nebraska Senate GOP odds hold firm through a volume surge"
telemetry: "75% · $809K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-31T14:16:49+00:00"
event_id: "CM-EVT-37PJ66HMC4"
event_slug: "senatene-26"
event_question: "Nebraska Senate winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "SENATENE-26-R"
  question_raw: "Will Republicans win the Senate race in Nebraska?"
  current_price: 0.75
  volume_24h_usd: 808890.8
  volume_cumulative_usd: 2398619.26
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices Nebraska GOP Senate win at 75%, a strong favorite read."
  - "$809K traded in 24h, 34% of all-time contract volume in a single session."
  - "Heavy one-day flow on a Senate race one week out signals election-eve positioning."
  - "Resolves on Nebraska 2026 Senate result; independent candidacy is the key risk factor."
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
      kalshi_vol_24h_usd: 808890.8
sources:
  - label: "ClearMarket market record: Nebraska Senate winner?"
    url: "https://clearmarket.fyi/events/senatene-26"
    retrieved_at: "2026-10-31T14:16:49+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should note that one-third of all-time volume arriving in 24 hours on a 75% GOP line suggests traders are actively defending, or testing, that probability ahead of a near-term resolution.
