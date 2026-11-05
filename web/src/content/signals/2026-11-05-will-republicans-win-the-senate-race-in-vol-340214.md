---
signal_id: "CMSIG20261105VS01"
signal_slug: "will-republicans-win-the-senate-race-in-vol-340214"
headline: "AK Senate GOP: 6% on $340K Election Day flow"
semantic_title: "Republicans trail Alaska Senate race at 6%"
telemetry: "6% · $340K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-05T16:03:26+00:00"
event_id: "CM-EVT-KQWMXB6NX7"
event_slug: "senateak-26"
event_question: "Will a new senator be elected to represent Alaska in the U.S. Senate?"
primary_market:
  platform: "kalshi"
  platform_market_id: "SENATEAK-26-R"
  question_raw: "Will Republicans win the Senate race in Alaska?"
  current_price: 0.06
  volume_24h_usd: 340214.57
  volume_cumulative_usd: 788701.77
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Market prices Republican Alaska Senate win at just 6%, deep underdog territory."
  - "$340K in 24h is 43% of all-time volume; proportionally outsized given the low odds."
  - "Election Day results today are the immediate catalyst; contract resolves on certified winner."
  - "Paired with Spike 0, opposing side of the same Kalshi race contract."
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
      kalshi_vol_24h_usd: 340214.57
sources:
  - label: "ClearMarket market record: Will a new senator be elected to represent Alaska in th"
    url: "https://clearmarket.fyi/events/senateak-26"
    retrieved_at: "2026-11-05T16:03:26+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

High share-of-all-time volume on a 6% contract suggests late hedging or last-minute contrary bets as Alaska returns develop, worth monitoring for any surprise shifts.
