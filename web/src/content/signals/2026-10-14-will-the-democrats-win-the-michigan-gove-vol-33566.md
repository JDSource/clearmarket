---
signal_id: "CMSIG20261014VS07"
signal_slug: "will-the-democrats-win-the-michigan-gove-vol-33566"
headline: "Dem Michigan governor win: 95% on $33K volume return"
semantic_title: "Michigan governor race leans heavily Democratic as volume returns"
telemetry: "95% · $34K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-14T13:17:59+00:00"
event_id: "CM-EVT-GTDLXYMZQ7"
event_slug: "michigan-governor-winner-2026"
event_question: "Will the Michigan Governor election be won by the Democratic candidate?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x76cface9f6df604ff32447bce58656b7a72b6659324d089c73a13a99f06c8aae"
  question_raw: "Will the Democrats win the Michigan governor race in 2026?"
  current_price: 0.95
  volume_24h_usd: 33566.77137000001
  volume_cumulative_usd: 120158.76706
  arbitration_model: "uma_oracle"
bullets:
  - "Polymarket prices 95%, market is pricing near-certain Democratic victory in the Michigan governor race."
  - "$33K in 24h is 28% of all-time volume on a $120K contract, consistent with ongoing positioning."
  - "Michigan's open governor seat draws continued attention as a flagship 2026 Democratic hold target."
  - "Resolves on 2026 Michigan gubernatorial election result."
atomic_claims:
  - type: "volume_anomaly"
    provenance: "24h + cumulative volume direct from polymarket API; intensity = 24h/cumulative (derived)"
    field_provenance:
      volume_24h_usd:
        tier: "direct"
        method: "polymarket_api"
      intensity:
        tier: "derived"
        method: "arithmetic"
        inputs: ["volume_24h_usd", "volume_cumulative_usd"]
    liquidity_context:
      poly_vol_24h_usd: 33566.77137000001
sources:
  - label: "ClearMarket market record: Will the Michigan Governor election be won by the Democ"
    url: "https://clearmarket.fyi/events/michigan-governor-winner-2026"
    retrieved_at: "2026-10-14T13:17:59+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Recurring volume on a 95% contract signals desks are maintaining active exposure rather than walking away, any Republican candidate development that moves the price below 90% would be a significant signal.
