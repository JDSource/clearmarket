---
signal_id: "CMSIG20261022VS02"
signal_slug: "will-the-republican-party-win-the-govern-vol-148765"
headline: "Georgia GOP governor: 41% on $149K inflow"
semantic_title: "Georgia governorship fight stays close below 50%"
telemetry: "41% · $149K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-22T13:25:36+00:00"
event_id: "CM-EVT-RHX55RJPT1"
event_slug: "govpartyga-26"
event_question: "Georgia Governor winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "GOVPARTYGA-26-R"
  question_raw: "Will the Republican party win the governorship in Georgia"
  current_price: 0.41
  volume_24h_usd: 148765.76
  volume_cumulative_usd: 510495.29
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-14T15:00:00Z"
bullets:
  - "Kalshi prices Republican win at 41%, placing Democrats as modest favorites in a competitive race."
  - "$149K in 24h, 29% of all-time volume, makes this the single largest dollar spike in the batch."
  - "Near-coin-flip pricing with a surge of fresh capital points to a catalyst: polling shift, candidate news, or fundraising data."
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
      kalshi_vol_24h_usd: 148765.76
sources:
  - label: "ClearMarket market record: Georgia Governor winner?"
    url: "https://clearmarket.fyi/events/govpartyga-26"
    retrieved_at: "2026-10-22T13:25:36+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The largest raw dollar flow of the batch on a near-toss-up contract signals active directional repositioning, likely after fresh state-level polling or a campaign development that moved consensus.
