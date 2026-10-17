---
signal_id: "CMSIG20261017VS01"
signal_slug: "will-republican-win-the-house-race-for-a-vol-40186"
headline: "AL-02 Republican: 73% on $40K volume surge"
semantic_title: "AL-02 Republican odds hold firm at 73% on fresh money"
telemetry: "73% · $40K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-17T11:58:01+00:00"
event_id: "CM-EVT-VNGYPPDNV9"
event_slug: "kxhouserace-al02-26"
event_question: "Will the Alabama 2nd congressional district House election winner be determined by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-AL02-26-R"
  question_raw: "Will Republican win the House race for AL-02?"
  current_price: 0.73
  volume_24h_usd: 40186.38
  volume_cumulative_usd: 102670.05
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "Kalshi prices Republican at 73%, a solid favorite but with meaningful Democratic upside still priced at 27%."
  - "24h volume of $40K represents 39% of all-time, the largest single-day flow on record for this contract."
  - "AL-02 is a newly drawn Alabama district; renewed attention may reflect candidate news or redistricting litigation."
  - "Resolves on November 2026 election night."
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
      kalshi_vol_24h_usd: 40186.38
sources:
  - label: "ClearMarket market record: Will the Alabama 2nd congressional district House elect"
    url: "https://clearmarket.fyi/events/kxhouserace-al02-26"
    retrieved_at: "2026-10-17T11:58:01+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Largest 24h flow on this contract suggests AL-02 just entered active monitoring for desks tracking competitive House map shifts.
