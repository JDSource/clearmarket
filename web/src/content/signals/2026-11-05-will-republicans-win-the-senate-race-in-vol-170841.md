---
signal_id: "CMSIG20261105VS03"
signal_slug: "will-republicans-win-the-senate-race-in-vol-170841"
headline: "MS Senate GOP: 97% on $171K Election Day bet"
semantic_title: "Mississippi Senate stays a Republican lock at 97%"
telemetry: "3% · $171K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-05T16:03:26+00:00"
event_id: "CM-EVT-6R8L57X0Y4"
event_slug: "senatems-26"
event_question: "Will the Mississippi Senate race be decided by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "SENATEMS-26-R"
  question_raw: "Will Republicans win the Senate race in Mississippi?"
  current_price: 0.033
  volume_24h_usd: 170841.39
  volume_cumulative_usd: 491913.06
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Market prices Republican Mississippi Senate win at 97%, effectively a certain hold."
  - "$171K in 24h is 35% of all-time; notable flow into a near-foregone conclusion."
  - "Election Day today triggers resolution activity; volume likely reflects contract closeout."
  - "Kalshi contract resolves on certified Mississippi Senate winner."
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
      kalshi_vol_24h_usd: 170841.39
sources:
  - label: "ClearMarket market record: Will the Mississippi Senate race be decided by January "
    url: "https://clearmarket.fyi/events/senatems-26"
    retrieved_at: "2026-11-05T16:03:26+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Fresh volume into a 97%-priced contract on Election Day is predominantly position-closing activity; the desk signal is confirmatory, Mississippi does not move the needle on Senate majority math.
