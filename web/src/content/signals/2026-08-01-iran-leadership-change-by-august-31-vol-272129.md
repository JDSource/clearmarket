---
signal_id: "CMSIG20260801VS01"
signal_slug: "iran-leadership-change-by-august-31-vol-272129"
headline: "Iran leadership change by Aug 31: 5% on $272K"
semantic_title: "Iran leadership-change odds hold near zero through a volume rush"
telemetry: "5% · $272K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-01T09:55:41+00:00"
event_id: "CM-EVT-TYRP27H901"
event_slug: "iran-leadership-change-by"
event_question: "Will Iran's leadership change by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x43e12647a58ee0b20d2539d23764b0d561ea7be322acb8823f7bb126e67c115e"
  question_raw: "Iran leadership change by August 31?"
  current_price: 0.046
  volume_24h_usd: 272129.1662449999
  volume_cumulative_usd: 347940.5819829999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-08-31T00:00:00Z"
bullets:
  - "Market holds at 5%, near-certain 'no' on an Iran leadership change before August 31."
  - "24h volume of $272K is 78% of all-time flow; almost the entire contract lifetime traded today."
  - "Spike likely reflects a news catalyst, a threat, health report, or geopolitical flashpoint, that drew attention but did not move the price."
  - "Resolves August 31, 2026; three weeks remain for the contract to run."
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
      poly_vol_24h_usd: 272129.1662449999
sources:
  - label: "ClearMarket market record: Will Iran's leadership change by 2026?"
    url: "https://clearmarket.fyi/events/iran-leadership-change-by"
    retrieved_at: "2026-08-01T09:55:41+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

For a desk, a 78% all-time volume flush into a 5% price means fresh capital tested a regime-change thesis and found no takers, the signal is a confirmed low-probability read even under maximum scrutiny.
