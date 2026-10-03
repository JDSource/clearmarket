---
signal_id: "CMSIG20261003VS06"
signal_slug: "will-democratic-win-the-house-race-for-w-vol-15845"
headline: "WA-3 House Dem: 89% on $16K Kalshi surge"
semantic_title: "Fresh volume backs Democrats in WA-3 House race at 89%"
telemetry: "89% · $16K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-03T13:00:25+00:00"
event_id: "CM-EVT-H6TY7G52C4"
event_slug: "housewa3-26"
event_question: "Will the winner of the Washington 3rd congressional district House race be determined by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSEWA3-26-D"
  question_raw: "Will Democratic win the House race for WA-3?"
  current_price: 0.89
  volume_24h_usd: 15845.89
  volume_cumulative_usd: 38814.41
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices a Democratic win in WA-3 at 89%, strong favorite territory in a competitive Pacific Northwest district."
  - "41% of all-time volume cleared in 24 hours, a concentrated burst on a district-level House contract."
  - "WA-3 has been a closely watched swing seat; 89% implies the race has largely resolved in traders' view."
  - "Resolves on the 2026 WA-3 House general election result."
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
      kalshi_vol_24h_usd: 15845.89
sources:
  - label: "ClearMarket market record: Will the winner of the Washington 3rd congressional dis"
    url: "https://clearmarket.fyi/events/housewa3-26"
    retrieved_at: "2026-10-03T13:00:25+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

An 89% price on 41% all-time volume in WA-3 suggests the market has materially re-priced Democratic strength in this district, desks tracking House majority scenarios should update their WA-3 assumption accordingly.
