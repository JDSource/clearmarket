---
signal_id: "CMSIG20260802VS02"
signal_slug: "will-shri-thanedar-be-the-democratic-nom-vol-53321"
headline: "Thanedar MI-13 Dem nominee: 14% on $53K"
semantic_title: "Thanedar MI-13 nomination odds slip to 14% under fresh pressure"
telemetry: "14% · $53K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-02T09:53:38+00:00"
event_id: "CM-EVT-KJP3106M36"
event_slug: "mi-13-democratic-primary-winner"
event_question: "Will the Democratic primary winner be determined for Michigan's 13th congressional district by August 4, 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x399b69600812f9997ee0dcac06c74c9351f230baa53765eacbc443a77bc520b9"
  question_raw: "Will Shri Thanedar be the Democratic Nominee for MI-13?"
  current_price: 0.14
  volume_24h_usd: 53321.649389
  volume_cumulative_usd: 154638.70524700003
  arbitration_model: "uma_oracle"
  resolves_at: "2026-08-04T00:00:00Z"
bullets:
  - "Polymarket prices Shri Thanedar as the MI-13 Democratic nominee at 14%, a clear underdog read against McKinney."
  - "34% of all-time volume hit in 24h, showing sharp acceleration as the primary approaches."
  - "Paired volume with McKinney's contract (Spike 3) confirms active reallocation, capital moving between the two candidates."
  - "MI-13 primary result will resolve both contracts; resolution date proximity is likely driving the urgency."
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
      poly_vol_24h_usd: 53321.649389
sources:
  - label: "ClearMarket market record: Will the Democratic primary winner be determined for Mi"
    url: "https://clearmarket.fyi/events/mi-13-democratic-primary-winner"
    retrieved_at: "2026-08-02T09:53:38+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The simultaneous spike in both MI-13 contracts points to active position rebalancing ahead of the primary, with the market pricing McKinney as a heavy favorite at 86%.
