---
signal_id: "CMSIG20260806VS05"
signal_slug: "will-marcelo-aro-win-the-2026-minas-gera-vol-14998"
headline: "Aro MG governor 2026: 2% on $15K surge"
semantic_title: "Aro Minas Gerais governor bid stays near zero on near-record volume"
telemetry: "2% · $15K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-06T10:36:04+00:00"
event_id: "CM-EVT-S4L4VK6RC3"
event_slug: "minas-gerais-governor-election-winner"
event_question: "Will the Minas Gerais Governor Election be decided by October 4, 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x03b6ebcc9d8a0f16954a87c001f0dcc43e86426db2e7981635c90e8127277388"
  question_raw: "Will Marcelo Aro win the 2026 Minas Gerais gubernatorial election?"
  current_price: 0.021
  volume_24h_usd: 14998.520471000002
  volume_cumulative_usd: 19846.384122000003
  arbitration_model: "uma_oracle"
  resolves_at: "2026-10-04T06:00:00Z"
bullets:
  - "2% pricing is a near-total dismissal of Aro's chances in the Minas Gerais race."
  - "76% of all-time volume hit in 24h, the contract is seeing its most active session by far."
  - "Surge may reflect a poll release, rival candidate consolidation, or a field-clarifying event in MG."
  - "Resolves on 2026 Brazilian state election; the near-zero price limits further downside."
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
      poly_vol_24h_usd: 14998.520471000002
sources:
  - label: "ClearMarket market record: Will the Minas Gerais Governor Election be decided by O"
    url: "https://clearmarket.fyi/events/minas-gerais-governor-election-winner"
    retrieved_at: "2026-08-06T10:36:04+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A near-record session at 2% odds signals a desk that the volume is informational, someone is either hedging a position or the market just received hard news definitively ruling Aro out.
