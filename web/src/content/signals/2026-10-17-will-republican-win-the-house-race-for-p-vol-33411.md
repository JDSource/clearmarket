---
signal_id: "CMSIG20261017VS00"
signal_slug: "will-republican-win-the-house-race-for-p-vol-33411"
headline: "PA-1 Republican: 65% on $33K volume surge"
semantic_title: "Traders back Republican hold in PA-1 at 65%"
telemetry: "65% · $33K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-17T11:58:01+00:00"
event_id: "CM-EVT-GWDTD01SV1"
event_slug: "housepa1-26"
event_question: "PA-01 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSEPA1-26-R"
  question_raw: "Will Republican win the House race for PA-1?"
  current_price: 0.65
  volume_24h_usd: 33411.81
  volume_cumulative_usd: 54121.93
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices Republican win at 65%, a clear but not commanding lead with real downside priced in."
  - "24h volume of $33K is 62% of all-time, signaling a decisive late-cycle attention spike on this race."
  - "PA-1 is a competitive Pennsylvania seat; surge likely reflects new polling or campaign developments."
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
      kalshi_vol_24h_usd: 33411.81
sources:
  - label: "ClearMarket market record: PA-01 House winner?"
    url: "https://clearmarket.fyi/events/housepa1-26"
    retrieved_at: "2026-10-17T11:58:01+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A dominant share of all-time volume arriving in a single day flags PA-1 as a live battleground desk should treat as a priority watch, not a settled race.
