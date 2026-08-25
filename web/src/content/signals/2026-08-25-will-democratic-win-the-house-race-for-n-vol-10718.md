---
signal_id: "CMSIG20260825VS04"
signal_slug: "will-democratic-win-the-house-race-for-n-vol-10718"
headline: "Dem NE-2 House win: 90% on $10.7K spike"
semantic_title: "Democrats heavily backed to take NE-2 at 90%"
telemetry: "90% · $11K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-25T08:37:37+00:00"
event_id: "CM-EVT-FRN7LK1C00"
event_slug: "housene2-26"
event_question: "NE-02 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSENE2-26-D"
  question_raw: "Will Democratic win the House race for NE-2?"
  current_price: 0.9
  volume_24h_usd: 10718.7
  volume_cumulative_usd: 14821.51
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices Democrats to win Nebraska's 2nd congressional district House race at 90%, a strong implied lock."
  - "24h volume of $10.7K is 72% of all-time, the vast majority of lifetime liquidity traded in a single session."
  - "NE-2 is an electoral-vote-splitting district that has drawn national attention; a 72% all-time concentration signals a positioning or information event."
  - "No resolution date specified; outcome ties to the next general election cycle."
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
      kalshi_vol_24h_usd: 10718.7
sources:
  - label: "ClearMarket market record: NE-02 House winner?"
    url: "https://clearmarket.fyi/events/housene2-26"
    retrieved_at: "2026-08-25T08:37:37+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 72% all-time volume share in one day on a 90% contract in NE-2 suggests desks are locking in a directional read on a nationally watched district, likely driven by candidate news, redistricting update, or internal polling.
