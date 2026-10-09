---
signal_id: "CMSIG20261009VS02"
signal_slug: "will-republican-win-the-house-race-for-w-vol-23071"
headline: "Republican WI-1 House: 65% on $23K volume spike"
semantic_title: "Republican WI-1 House seat trades at 65% in volume surge"
telemetry: "65% · $23K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-09T07:49:05+00:00"
event_id: "CM-EVT-CM1BLLFVK3"
event_slug: "housewi1-26"
event_question: "Will the WI-01 House race winner be determined by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSEWI1-26-R"
  question_raw: "Will Republican win the House race for WI-1?"
  current_price: 0.65
  volume_24h_usd: 23071.07
  volume_cumulative_usd: 31697.17
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices the Republican at 65%, a clear but not decisive favorite heading into the WI-1 race."
  - "$23K in 24h represents 73% of all-time contract volume, marking today as the market's single most active session."
  - "Elevated attention on a House district race suggests internal polling, candidate news, or early-vote data is driving fresh positioning."
  - "Resolves on the certified winner of the Wisconsin 1st Congressional District race."
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
      kalshi_vol_24h_usd: 23071.07
sources:
  - label: "ClearMarket market record: Will the WI-01 House race winner be determined by Janua"
    url: "https://clearmarket.fyi/events/housewi1-26"
    retrieved_at: "2026-10-09T07:49:05+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 73%-of-all-time daily volume surge on a down-ballot House race is unusual enough that a desk should flag it as potential signal of district-level information entering the market.
