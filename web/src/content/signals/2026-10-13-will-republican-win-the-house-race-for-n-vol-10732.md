---
signal_id: "CMSIG20261013VS06"
signal_slug: "will-republican-win-the-house-race-for-n-vol-10732"
headline: "NV-02 Republican: 71% on $11K Kalshi activity"
semantic_title: "NV-02 Republican odds hold at 71% through a volume pick-up"
telemetry: "71% · $11K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-13T07:49:07+00:00"
event_id: "CM-EVT-MKTKFVXDZ7"
event_slug: "kxhouserace-nv02-26"
event_question: "NV-02 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-NV02-26-R"
  question_raw: "Will Republican win the House race for NV-02?"
  current_price: 0.71
  volume_24h_usd: 10732.57
  volume_cumulative_usd: 28212.04
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "Kalshi prices Republican win in NV-02 at 71%, the widest margin of genuine uncertainty in today's House spike set."
  - "38% of all-time handle moved in 24 hours, the lowest all-time share among today's House spikes but still notable."
  - "A 29% Democratic residual makes NV-02 the most competitively priced district in this batch, Nevada seats historically tighten late."
  - "Resolves on the NV-02 general election result."
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
      kalshi_vol_24h_usd: 10732.57
sources:
  - label: "ClearMarket market record: NV-02 House winner?"
    url: "https://clearmarket.fyi/events/kxhouserace-nv02-26"
    retrieved_at: "2026-10-13T07:49:07+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

NV-02 stands out as the live swing-seat risk in today's House flow, a 71/29 split with fresh volume tells a desk this district warrants active monitoring as Nevada returns come in.
