---
signal_id: "CMSIG20261003VS05"
signal_slug: "will-the-democrats-win-the-michigan-gove-vol-25521"
headline: "Michigan Dem governor: 97% on $26K surge"
semantic_title: "Democrats near-locked for Michigan governor at 97%"
telemetry: "97% · $26K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-03T13:00:25+00:00"
event_id: "CM-EVT-GTDLXYMZQ7"
event_slug: "michigan-governor-winner-2026"
event_question: "Will the Michigan Governor election be won by the Democratic candidate?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x76cface9f6df604ff32447bce58656b7a72b6659324d089c73a13a99f06c8aae"
  question_raw: "Will the Democrats win the Michigan governor race in 2026?"
  current_price: 0.97
  volume_24h_usd: 25521.228701
  volume_cumulative_usd: 76695.82196700001
  arbitration_model: "uma_oracle"
bullets:
  - "Polymarket prices Democrats at 97% for the Michigan governor race, a near-certain outcome at current odds."
  - "33% of all-time volume cleared in 24 hours on a contract already priced as effectively resolved."
  - "At 97%, fresh volume likely reflects arbitrage, position exit, or hedging against a tail scenario rather than competitive speculation."
  - "Resolves on the 2026 Michigan gubernatorial election outcome."
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
      poly_vol_24h_usd: 25521.228701
sources:
  - label: "ClearMarket market record: Will the Michigan Governor election be won by the Democ"
    url: "https://clearmarket.fyi/events/michigan-governor-winner-2026"
    retrieved_at: "2026-10-03T13:00:25+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 97% price drawing a third of all-time volume in one session suggests closing arbitrage or structured unwinding, desks can treat the remaining 3% as a negligible tail risk unless new candidate or legal news emerges.
