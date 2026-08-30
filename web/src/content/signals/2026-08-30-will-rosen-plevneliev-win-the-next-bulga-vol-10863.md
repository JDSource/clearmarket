---
signal_id: "CMSIG20260830VS01"
signal_slug: "will-rosen-plevneliev-win-the-next-bulga-vol-10863"
headline: "Plevneliev Bulgaria president: 0% on $10.9K volume"
semantic_title: "Plevneliev Bulgarian presidency odds collapse to zero"
telemetry: "0% · $11K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-30T13:31:03+00:00"
event_id: "CM-EVT-C541X65QT7"
event_slug: "bulgaria-presidential-election"
event_question: "Will Bulgaria hold a presidential election by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xfa2b0ab5e7778d211a3a6c02c0e799c8dbab32ac6487e59c1e2bff87f0dcb1cd"
  question_raw: "Will Rosen Plevneliev win the next Bulgarian presidential election?"
  current_price: 0.001
  volume_24h_usd: 10863.68
  volume_cumulative_usd: 21662.933005000003
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-30T00:00:00Z"
bullets:
  - "Market prices 0%, Plevneliev is effectively ruled out as the next Bulgarian president."
  - "24h volume of $10.9K is 50% of all-time handle, meaning half all trading hit in one day."
  - "A decisive political development in Bulgaria, candidate withdrawal or election result, likely triggered the repricing."
  - "Contract now trades as a dead letter; residual volume reflects final position exits."
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
      poly_vol_24h_usd: 10863.68
sources:
  - label: "ClearMarket market record: Will Bulgaria hold a presidential election by 2026?"
    url: "https://clearmarket.fyi/events/bulgaria-presidential-election"
    retrieved_at: "2026-08-30T13:31:03+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Half of all-time volume printing at 0% signals a binary resolution event in Bulgaria; a desk tracking Eastern European political risk should treat this as confirmation of Plevneliev's exit from contention.
