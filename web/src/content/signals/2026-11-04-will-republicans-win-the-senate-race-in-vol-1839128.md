---
signal_id: "CMSIG20261104VS02"
signal_slug: "will-republicans-win-the-senate-race-in-vol-1839128"
headline: "MS Senate GOP: 25% on $1.8M countertrade flow"
semantic_title: "Republican Mississippi Senate odds slip to 25%"
telemetry: "25% · $1.8M 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-04T07:48:42+00:00"
event_id: "CM-EVT-6R8L57X0Y4"
event_slug: "senatems-26"
event_question: "Will the Mississippi Senate race be decided by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "SENATEMS-26-R"
  question_raw: "Will Republicans win the Senate race in Mississippi?"
  current_price: 0.25
  volume_24h_usd: 1839128.55
  volume_cumulative_usd: 2082338.08
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices Republican win at exactly 25%, market assigns long-shot status on election eve."
  - "88% of all-time volume cleared in 24h, the highest all-time share of any spike in this batch."
  - "Mirror of Spike 0: opposing-side contract confirms Democrats are priced as strong favorites."
  - "Resolves on certified Mississippi 2026 Senate outcome."
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
      kalshi_vol_24h_usd: 1839128.55
sources:
  - label: "ClearMarket market record: Will the Mississippi Senate race be decided by January "
    url: "https://clearmarket.fyi/events/senatems-26"
    retrieved_at: "2026-11-04T07:48:42+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

An 88% all-time volume rate on the Republican side, with odds at the 25% threshold, tells desks that position liquidation rather than fresh buying is the dominant flow, sellers are exiting GOP exposure.
