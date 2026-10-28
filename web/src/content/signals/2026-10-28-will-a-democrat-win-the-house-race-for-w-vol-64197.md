---
signal_id: "CMSIG20261028VS03"
signal_slug: "will-a-democrat-win-the-house-race-for-w-vol-64197"
headline: "Democrat WI-3 House: 81% on $64K volume pop"
semantic_title: "Democrat holds 81% odds in WI-3 as buyers back the House race"
telemetry: "81% · $64K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-28T07:50:03+00:00"
event_id: "CM-EVT-6C7CNWJ6R7"
event_slug: "housewi3-26"
event_question: "WI-03 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSEWI3-26-D"
  question_raw: "Will a Democrat win the House race for WI-3?"
  current_price: 0.81
  volume_24h_usd: 64197.49
  volume_cumulative_usd: 162393.15
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "81% pricing puts the Democratic candidate as a strong favorite in Wisconsin's 3rd district."
  - "Kalshi saw $64K in 24h, 40% of all-time volume, a meaningful single-session commitment."
  - "WI-3 is a swing-district bellwether; fresh attention here often precedes polling or candidate news."
  - "Resolves on certified House election result for WI-3."
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
      kalshi_vol_24h_usd: 64197.49
sources:
  - label: "ClearMarket market record: WI-03 House winner?"
    url: "https://clearmarket.fyi/events/housewi3-26"
    retrieved_at: "2026-10-28T07:50:03+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 40% all-time volume surge on an 81% Democratic contract in a competitive district suggests the market is stress-testing a near-consensus call, desks watching House majority math should flag any catalyst that pushed this contract into focus.
