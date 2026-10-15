---
signal_id: "CMSIG20261015VS01"
signal_slug: "will-the-democratic-party-win-the-govern-vol-151439"
headline: "Georgia governor Dem win: 48% on $151K Kalshi spike"
semantic_title: "Georgia governor race pulls back to even as volume builds"
telemetry: "48% · $151K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-15T13:03:58+00:00"
event_id: "CM-EVT-RHX55RJPT1"
event_slug: "govpartyga-26"
event_question: "Georgia Governor winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "GOVPARTYGA-26-D"
  question_raw: "Will the Democratic party win the governorship in Georgia"
  current_price: 0.48
  volume_24h_usd: 151439.94
  volume_cumulative_usd: 456265.85
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-14T15:00:00Z"
bullets:
  - "Democrats priced at 48%, essentially a toss-up, with neither party holding a clear edge."
  - "$151.4K in 24h volume is 33% of all-time, marking the contract's busiest single session."
  - "Fresh attention at near-parity odds suggests a recent poll, candidate event, or fundraising disclosure shifted trader focus."
  - "Resolves on 2026 Georgia gubernatorial election result."
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
      kalshi_vol_24h_usd: 151439.94
sources:
  - label: "ClearMarket market record: Georgia Governor winner?"
    url: "https://clearmarket.fyi/events/govpartyga-26"
    retrieved_at: "2026-10-15T13:03:58+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A coin-flip price drawing its largest daily volume signals the Georgia governor race has entered the competitive battleground tier, desks tracking Senate and House maps should update Georgia's down-ballot covariance.
