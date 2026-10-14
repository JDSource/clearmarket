---
signal_id: "CMSIG20261014VS00"
signal_slug: "scotus-accepts-sports-event-contract-cas-vol-62913"
headline: "SCOTUS sports contract case: 36% on $62K surge"
semantic_title: "SCOTUS sports contract case stays a long shot by Dec 31"
telemetry: "36% · $63K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-14T13:17:59+00:00"
event_id: "CM-EVT-FLWXD81WN4"
event_slug: "scotus-accepts-sports-event-contract-case-by-july-31-2026"
event_question: "Will SCOTUS accept a sports event contract case by the settlement date?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x68e2344a2ce725ca99f3b93df06f27a71f3a893a38e8a6a78f8d85bd2698eb20"
  question_raw: "SCOTUS accepts sports event contract case by December 31, 2026?"
  current_price: 0.36
  volume_24h_usd: 62913.772558
  volume_cumulative_usd: 87409.15990599997
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices 36% odds, market leans against acceptance before year-end."
  - "$62K traded in 24h, 72% of all-time volume, signaling sharp new attention."
  - "Late-term SCOTUS docket speculation ahead of potential December cert announcements."
  - "Resolves December 31, 2026; docket activity between now and then is the key trigger."
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
      poly_vol_24h_usd: 62913.772558
sources:
  - label: "ClearMarket market record: Will SCOTUS accept a sports event contract case by the "
    url: "https://clearmarket.fyi/events/scotus-accepts-sports-event-contract-case-by-july-31-2026"
    retrieved_at: "2026-10-14T13:17:59+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A burst covering nearly three-quarters of all-time volume on a sub-50% contract suggests desks are hedging a low-probability but high-consequence docket event before year-end.
