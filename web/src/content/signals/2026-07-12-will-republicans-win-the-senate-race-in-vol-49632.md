---
signal_id: "CMSIG20260712VS04"
signal_slug: "will-republicans-win-the-senate-race-in-vol-49632"
headline: "GOP SC Senate win: 81% on $50K fresh inflow"
semantic_title: "Republicans defend South Carolina Senate seat at heavy odds"
telemetry: "81% · $50K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-12T09:48:30+00:00"
event_id: "CM-EVT-YB0M8XXMW8"
event_slug: "senatesc-26"
event_question: "Who will win the South Carolina Senate election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "SENATESC-26-R"
  question_raw: "Will Republicans win the Senate race in South Carolina?"
  current_price: 0.81
  volume_24h_usd: 49632.05
  volume_cumulative_usd: 104636.37
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices Republican South Carolina Senate victory at 81%, solid but not locked favorite."
  - "$50K in 24h is 47% of a $105K all-time pool, marking the contract's most active trading session."
  - "Fresh attention may reflect candidate filing clarity, early polling, or national Democratic resource allocation news."
  - "Resolves on 2026 South Carolina Senate election night; price leaves meaningful uncertainty for the opposition."
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
      kalshi_vol_24h_usd: 49632.05
sources:
  - label: "ClearMarket market record: Who will win the South Carolina Senate election?"
    url: "https://clearmarket.fyi/events/senatesc-26"
    retrieved_at: "2026-07-12T09:48:30+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Rising volume at 81% with nearly half of all-time flow in one day suggests a tactical hedge desk is either topping up Republican exposure or shorting against complacent pricing.
