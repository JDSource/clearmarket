---
signal_id: "CMSIG20261022VS04"
signal_slug: "will-democratic-win-the-house-race-for-n-vol-59786"
headline: "NC-11 Dem House: 83% on $60K Kalshi surge"
semantic_title: "Democrats priced as heavy favorites in NC-11"
telemetry: "83% · $60K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-22T13:25:36+00:00"
event_id: "CM-EVT-0N8GC3M3K5"
event_slug: "kxhousenc11-26"
event_question: "Who will win the North Carolina 11th congressional district House election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSENC11-26-DEM"
  question_raw: "Will Democratic win the House race for NC-11?"
  current_price: 0.83
  volume_24h_usd: 59786.12
  volume_cumulative_usd: 148842.28
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices a Democratic win at 83%, a strong favorite read in a race drawing fresh volume."
  - "$60K in 24h equals 40% of all-time volume, concentrated spike relative to contract history."
  - "NC-11 has been a competitive Appalachian district; an 83% Democratic price implies a significant landscape shift."
  - "Resolves on 2026 general election night."
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
      kalshi_vol_24h_usd: 59786.12
sources:
  - label: "ClearMarket market record: Who will win the North Carolina 11th congressional dist"
    url: "https://clearmarket.fyi/events/kxhousenc11-26"
    retrieved_at: "2026-10-22T13:25:36+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Four-in-ten lifetime dollars trading in a single day on an 83% contract in a historically competitive district signals a meaningful new data point, likely redistricting news, candidate withdrawal, or internal polling, that desks are acting on.
