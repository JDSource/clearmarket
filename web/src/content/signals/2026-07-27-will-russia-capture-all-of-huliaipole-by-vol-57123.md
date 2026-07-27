---
signal_id: "CMSIG20260727VS01"
signal_slug: "will-russia-capture-all-of-huliaipole-by-vol-57123"
headline: "Russia takes Huliaipole: 94% on $57K volume"
semantic_title: "Traders pile into Russia taking Huliaipole by September 30"
telemetry: "94% · $57K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-27T11:16:33+00:00"
event_id: "CM-EVT-TVK27N2C00"
event_slug: "will-russia-capture-all-of-huliaipole-by-february-28"
event_question: "Will Russia capture all of Huliaipole in 2026? (multi-deadline series)"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xb49a2d10b3a7638874ce52f167c82f484acbaa7e5ae1a36d74805e5842b26257"
  question_raw: "Will Russia capture all of Huliaipole by September 30?"
  current_price: 0.94
  volume_24h_usd: 57123.78722200007
  volume_cumulative_usd: 80879.38424600006
  arbitration_model: "uma_oracle"
  resolves_at: "2026-09-30T00:00:00Z"
bullets:
  - "Polymarket prices full Russian capture of Huliaipole by Sep 30 at 94%, near-certain."
  - "24h volume $57K is 71% of the contract's all-time total, compressing nearly all trading into one session."
  - "High-conviction price likely reflects confirmed battlefield advances reported in the eastern Ukraine theater."
  - "Resolves September 30, 2026; minimal tail risk priced in at 6%."
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
      poly_vol_24h_usd: 57123.78722200007
sources:
  - label: "ClearMarket market record: Will Russia capture all of Huliaipole in 2026? (multi-d"
    url: "https://clearmarket.fyi/events/will-russia-capture-all-of-huliaipole-by-february-28"
    retrieved_at: "2026-07-27T11:16:33+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 94% price combined with a one-day all-time volume surge signals the market has found a near-final consensus, desks can treat this as a near-settled geopolitical data point rather than a live trade.
