---
signal_id: "CMSIG20261031VS04"
signal_slug: "will-the-democratic-party-win-the-govern-vol-485574"
headline: "Nevada Dem governor: 75% on $486K Kalshi surge"
semantic_title: "Nevada governor Democratic odds hold at 75% on fresh volume"
telemetry: "75% · $486K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-31T14:16:49+00:00"
event_id: "CM-EVT-TNC2QWG2J9"
event_slug: "govpartynv-26"
event_question: "Nevada Governor winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "GOVPARTYNV-26-D"
  question_raw: "Will the Democratic party win the governorship in Nevada"
  current_price: 0.75
  volume_24h_usd: 485574.18
  volume_cumulative_usd: 1599331.57
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-02T15:00:00Z"
bullets:
  - "Kalshi prices Democratic Nevada governorship win at 75%, a solid favorite stance."
  - "$486K traded in 24h, equal to 30% of the contract's all-time volume."
  - "Nevada governorship is a top-tier battleground; election-eve attention often precedes late news."
  - "Resolves on Nevada 2026 gubernatorial election outcome."
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
      kalshi_vol_24h_usd: 485574.18
sources:
  - label: "ClearMarket market record: Nevada Governor winner?"
    url: "https://clearmarket.fyi/events/govpartynv-26"
    retrieved_at: "2026-10-31T14:16:49+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 30% all-time volume day on a battleground governorship at 75% tells a desk that traders are reinforcing, not questioning, the Democratic lean heading into the final stretch.
