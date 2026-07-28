---
signal_id: "CMSIG20260728VS06"
signal_slug: "will-the-democratic-party-win-the-govern-vol-17081"
headline: "Colorado Dem governor: 91% on $17K inflow"
semantic_title: "Colorado Dem governorship holds heavy odds on fresh volume"
telemetry: "91% · $17K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-28T10:31:13+00:00"
event_id: "CM-EVT-QVJSDH7K98"
event_slug: "govpartyco-26"
event_question: "Colorado Governor winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "GOVPARTYCO-26-D"
  question_raw: "Will the Democratic party win the governorship in Colorado"
  current_price: 0.91
  volume_24h_usd: 17081.42
  volume_cumulative_usd: 33029.41
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-08T15:00:00Z"
bullets:
  - "Kalshi prices a Democratic Colorado governorship at 91%, a strong lean with limited upside left to price in."
  - "$17K in 24h represents 52% of all-time volume, notable for a contract already pricing near resolution."
  - "Fresh volume at 91% implies either confirmation of the Democratic field or Republican candidate weakness surfacing."
  - "Resolves on election; remaining 9% prices an upset scenario or late-race structural shift."
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
      kalshi_vol_24h_usd: 17081.42
sources:
  - label: "ClearMarket market record: Colorado Governor winner?"
    url: "https://clearmarket.fyi/events/govpartyco-26"
    retrieved_at: "2026-07-28T10:31:13+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Heavy volume on an already high-conviction contract suggests a confirmatory development, a desk should check for GOP candidate dropout, polling, or filing deadline news in Colorado.
