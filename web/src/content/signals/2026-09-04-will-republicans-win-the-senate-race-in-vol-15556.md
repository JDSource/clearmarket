---
signal_id: "CMSIG20260904VS05"
signal_slug: "will-republicans-win-the-senate-race-in-vol-15556"
headline: "Republican NC Senate: 9% on $15K Kalshi surge"
semantic_title: "Republican NC Senate odds slip to 9% on fresh volume"
telemetry: "9% · $16K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-04T12:29:08+00:00"
event_id: "CM-EVT-KX1QWP5LQ1"
event_slug: "senatenc-26"
event_question: "North Carolina Senate winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "SENATENC-26-R"
  question_raw: "Will Republicans win the Senate race in North Carolina?"
  current_price: 0.09
  volume_24h_usd: 15556.43
  volume_cumulative_usd: 57368.16
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi marks Republican odds at just 9%, the market prices a Democratic hold in North Carolina as near-certain."
  - "$15K in 24h is 27% of all-time volume, a meaningful inflow relative to a contract previously trading lightly."
  - "A Republican at 9% in a state once considered a tossup reflects a major shift in the Senate landscape; fresh volume may track new polling."
  - "Contract resolves on the certified winner of the North Carolina U.S. Senate general election."
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
      kalshi_vol_24h_usd: 15556.43
sources:
  - label: "ClearMarket market record: North Carolina Senate winner?"
    url: "https://clearmarket.fyi/events/senatenc-26"
    retrieved_at: "2026-09-04T12:29:08+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Renewed volume arriving at 9% on a seat Republicans once targeted tells a desk North Carolina has effectively exited the competitive Senate map, relevant for any model weighting GOP paths to a Senate majority.
