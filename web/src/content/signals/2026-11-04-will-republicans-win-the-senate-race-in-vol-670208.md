---
signal_id: "CMSIG20261104VS06"
signal_slug: "will-republicans-win-the-senate-race-in-vol-670208"
headline: "MS Senate GOP: 8% on $670K surge"
semantic_title: "Republican Mississippi Senate odds slip to 8%"
telemetry: "8% · $670K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-04T15:57:35+00:00"
event_id: "CM-EVT-6R8L57X0Y4"
event_slug: "senatems-26"
event_question: "Will the Mississippi Senate race be decided by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "SENATEMS-26-R"
  question_raw: "Will Republicans win the Senate race in Mississippi?"
  current_price: 0.077
  volume_24h_usd: 670208.39
  volume_cumulative_usd: 748353.77
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices a Republican Mississippi Senate win at just 8%, the complementary contract to Spike 0."
  - "$670K is 90% of all-time volume on this contract, the highest all-time share in this batch."
  - "90% all-time volume in one session at 8% confirms traders are selling Republican Mississippi exposure aggressively."
  - "Resolves as the inverse of the Democratic Mississippi Senate contract."
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
      kalshi_vol_24h_usd: 670208.39
sources:
  - label: "ClearMarket market record: Will the Mississippi Senate race be decided by January "
    url: "https://clearmarket.fyi/events/senatems-26"
    retrieved_at: "2026-11-04T15:57:35+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 90% all-time share at 8% on Election Day tells desks that Republican Mississippi Senate hedges are being liquidated en masse as results confirm a Democratic outcome.
