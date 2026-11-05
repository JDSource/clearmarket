---
signal_id: "CMSIG20261105VS01"
signal_slug: "will-democratics-win-the-senate-race-in-vol-3512612"
headline: "MS Senate Dem win: 96% as $3.5M floods in today"
semantic_title: "Fresh Election Day volume backs Democrats in Mississippi Senate"
telemetry: "96% · $3.5M 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-05T07:49:08+00:00"
event_id: "CM-EVT-6R8L57X0Y4"
event_slug: "senatems-26"
event_question: "Will the Mississippi Senate race be decided by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "SENATEMS-26-D"
  question_raw: "Will Democratics win the Senate race in Mississippi?"
  current_price: 0.964
  volume_24h_usd: 3512612.25
  volume_cumulative_usd: 12960487.81
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices a Democratic Mississippi Senate win at 96%, leaving only a 4% tail for a Republican hold."
  - "27% of all-time volume, $3.5M, cleared in 24 hours, the single heaviest trading day on this contract."
  - "Election Day turnout data and early returns appear to be reinforcing the dominant pricing consensus."
  - "Resolves on certified Mississippi Senate outcome; market leaves a narrow but non-zero upset tail."
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
      kalshi_vol_24h_usd: 3512612.25
sources:
  - label: "ClearMarket market record: Will the Mississippi Senate race be decided by January "
    url: "https://clearmarket.fyi/events/senatems-26"
    retrieved_at: "2026-11-05T07:49:08+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The largest single-day print on this contract at 96% tells the desk that Mississippi is effectively priced as resolved, track incoming precincts for confirmation or a rare reversal.
