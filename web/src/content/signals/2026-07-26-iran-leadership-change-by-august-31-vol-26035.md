---
signal_id: "CMSIG20260726VS02"
signal_slug: "iran-leadership-change-by-august-31-vol-26035"
headline: "Iran leadership change: 8% on $26K surge"
semantic_title: "Iran leadership-change odds stay low through August"
telemetry: "8% · $26K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-26T09:56:30+00:00"
event_id: "CM-EVT-TYRP27H901"
event_slug: "iran-leadership-change-by"
event_question: "Will Iran's leadership change by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x43e12647a58ee0b20d2539d23764b0d561ea7be322acb8823f7bb126e67c115e"
  question_raw: "Iran leadership change by August 31?"
  current_price: 0.08
  volume_24h_usd: 26035.178882
  volume_cumulative_usd: 47140.168178999986
  arbitration_model: "uma_oracle"
  resolves_at: "2026-08-31T00:00:00Z"
bullets:
  - "Polymarket prices an Iran leadership change by Aug 31 at 8%, traders broadly discount the scenario."
  - "55% of all-time volume cleared in 24h, implying a sharp geopolitical catalyst drove renewed attention."
  - "Escalating Iran-related headlines, sanctions, nuclear talks, or internal unrest, are the likely trigger."
  - "Hard deadline of Aug 31 keeps the contract a near-term binary; resolution is weeks away."
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
      poly_vol_24h_usd: 26035.178882
sources:
  - label: "ClearMarket market record: Will Iran's leadership change by 2026?"
    url: "https://clearmarket.fyi/events/iran-leadership-change-by"
    retrieved_at: "2026-07-26T09:56:30+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 55% all-time volume concentration in one day on a geopolitical tail-risk contract signals desks are actively hedging or expressing a view on Iran instability, the 8% price says the base case remains regime continuity.
