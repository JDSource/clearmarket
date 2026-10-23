---
signal_id: "CMSIG20261023VS01"
signal_slug: "will-republicans-win-the-senate-race-in-vol-133911"
headline: "Idaho Senate GOP: 96% on $134K volume burst"
semantic_title: "Idaho Senate stays deep red as odds hold near certainty"
telemetry: "96% · $134K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-23T07:49:03+00:00"
event_id: "CM-EVT-TRRJX6C1D5"
event_slug: "senateid-26"
event_question: "Idaho Senate winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "SENATEID-26-R"
  question_raw: "Will Republicans win the Senate race in Idaho?"
  current_price: 0.956
  volume_24h_usd: 133911.08
  volume_cumulative_usd: 384027.85
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "96% price on Kalshi reflects near-certain Republican retention of the Idaho seat."
  - "$133,911 in 24h trading is 35% of all-time volume, notable fresh engagement on a foregone conclusion."
  - "Late-cycle volume on a locked-in race may reflect arbitrage activity or hedging against a broader Senate seat basket."
  - "Resolves on 2026 Idaho Senate election result."
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
      kalshi_vol_24h_usd: 133911.08
sources:
  - label: "ClearMarket market record: Idaho Senate winner?"
    url: "https://clearmarket.fyi/events/senateid-26"
    retrieved_at: "2026-10-23T07:49:03+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Heavy fresh volume on a 96% contract warrants a look at whether traders are using Idaho as a low-cost hedge within a Senate-sweep position rather than expressing a directional view.
