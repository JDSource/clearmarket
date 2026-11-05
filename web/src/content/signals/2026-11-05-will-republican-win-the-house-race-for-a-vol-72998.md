---
signal_id: "CMSIG20261105VS06"
signal_slug: "will-republican-win-the-house-race-for-a-vol-72998"
headline: "AK-AL House GOP: 96% on $73K Election Day volume"
semantic_title: "Republicans lock up Alaska At-Large House seat at 96%"
telemetry: "96% · $73K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-05T16:03:26+00:00"
event_id: "CM-EVT-97GCZBGWV8"
event_slug: "houseakal-26"
event_question: "Will the Alaska House winner be determined by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSEAKAL-26-R"
  question_raw: "Will Republican win the House race for AK-AL?"
  current_price: 0.955
  volume_24h_usd: 72998.94
  volume_cumulative_usd: 184103.04
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Market prices Republican AK at-large House win at 96%, near-certain retention."
  - "$73K in 24h is 40% of all-time; substantial Election Day share for a low-odds outcome."
  - "Alaska's at-large seat is a GOP hold in House majority arithmetic; volume is confirmatory."
  - "Kalshi contract resolves on certified Alaska at-large House winner."
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
      kalshi_vol_24h_usd: 72998.94
sources:
  - label: "ClearMarket market record: Will the Alaska House winner be determined by January 4"
    url: "https://clearmarket.fyi/events/houseakal-26"
    retrieved_at: "2026-11-05T16:03:26+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Elevated Election Day share-of-all-time on a 96% contract indicates traders are closing out positions as Alaska returns roll in, treating this seat as a banked GOP column in House count models.
