---
signal_id: "CMSIG20260629VS03"
signal_slug: "will-russia-capture-myropillia-by-july-3-vol-20368"
headline: "Russia captures Myropillia by July 31: 6% on $20K"
semantic_title: "Skeptical flows defend against Russian Myropillia capture"
telemetry: "6% · $20K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-29T12:29:31+00:00"
event_id: "CM-EVT-RRPQBLKMY2"
event_slug: "will-russia-capture-myropillia-by-may-31"
event_question: "Will Russia capture Myropillia in 2026? (multi-deadline series)"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xb6fa372cc4cf72394f69c64c0ac23f8bc724bd8ec00c0c7303d2a04f50b52e0a"
  question_raw: "Will Russia capture Myropillia by July 31?"
  current_price: 0.06
  volume_24h_usd: 20368.0
  volume_cumulative_usd: 33998.936828
  arbitration_model: "uma_oracle"
  resolves_at: "2026-07-31T00:00:00Z"
bullets:
  - "6% price indicates Polymarket participants assign very low probability to Russian capture of Myropillia by month-end."
  - "$20K in 24h equals 60% of all-time volume, an outsized single-session share for a low-price contract."
  - "Concentrated flow on a 6% contract suggests either targeted informed selling or a speculative long entering at depressed prices."
  - "July 31 resolution window keeps the contract live; any frontline shift would reprice rapidly."
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
      poly_vol_24h_usd: 20368.0
sources:
  - label: "ClearMarket market record: Will Russia capture Myropillia in 2026? (multi-deadline"
    url: "https://clearmarket.fyi/events/will-russia-capture-myropillia-by-may-31"
    retrieved_at: "2026-06-29T12:29:31+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A geopolitical risk desk should flag that 60% of lifetime volume printing in one day on a 6% contract is structurally anomalous, it may reflect a participant with frontline intelligence taking a contrarian long or existing holders aggressively selling down residual exposure.
