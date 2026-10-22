---
signal_id: "CMSIG20261022VS07"
signal_slug: "will-republican-win-the-house-race-for-f-vol-24842"
headline: "FL-14 GOP House: 37% on $25K Kalshi spike"
semantic_title: "FL-14 Republican odds sit below 50% at 37%"
telemetry: "37% · $25K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-22T13:25:36+00:00"
event_id: "CM-EVT-H89NH9QH14"
event_slug: "kxhouserace-fl14-26"
event_question: "Will a winner be determined in the FL-14 House race by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-FL14-26-R"
  question_raw: "Will Republican win the House race for FL-14?"
  current_price: 0.37
  volume_24h_usd: 24842.27
  volume_cumulative_usd: 61792.49
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "Kalshi prices a Republican win in FL-14 at 37%, putting the GOP as an underdog in a Florida House seat."
  - "$25K in 24h equals 40% of all-time volume, a sharp concentration for a smaller-dollar market."
  - "A sub-50% Republican price in Florida signals a notable candidate or redistricting development worth monitoring."
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
      kalshi_vol_24h_usd: 24842.27
sources:
  - label: "ClearMarket market record: Will a winner be determined in the FL-14 House race by "
    url: "https://clearmarket.fyi/events/kxhouserace-fl14-26"
    retrieved_at: "2026-10-22T13:25:36+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Forty percent of lifetime volume in a single session on a market where Republicans trail in a Florida district flags a specific local catalyst, candidate, legal, or map news, that desks are pricing in before wider coverage catches up.
