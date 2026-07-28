---
signal_id: "CMSIG20260728VS02"
signal_slug: "will-russia-capture-all-of-huliaipole-by-vol-73921"
headline: "Russia Huliaipole by Sep 30: 84% on $74K"
semantic_title: "Traders back Russia taking all of Huliaipole by September 30"
telemetry: "84% · $74K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-28T10:31:13+00:00"
event_id: "CM-EVT-TVK27N2C00"
event_slug: "will-russia-capture-all-of-huliaipole-by-february-28"
event_question: "Will Russia capture all of Huliaipole in 2026? (multi-deadline series)"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xb49a2d10b3a7638874ce52f167c82f484acbaa7e5ae1a36d74805e5842b26257"
  question_raw: "Will Russia capture all of Huliaipole by September 30?"
  current_price: 0.84
  volume_24h_usd: 73921.32841999999
  volume_cumulative_usd: 133076.76838200015
  arbitration_model: "uma_oracle"
  resolves_at: "2026-09-30T00:00:00Z"
bullets:
  - "Polymarket prices full Russian capture of Huliaipole by Sep 30 at 84%, a high-conviction directional read."
  - "$74K in 24h is 56% of all-time volume, the largest single-day share in this contract's history."
  - "Fresh capital flowing into an 84% price suggests recent battlefield reporting or geolocated footage catalyzed the move."
  - "Resolves September 30; remaining 16% reflects either timeline risk or contested verification standards."
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
      poly_vol_24h_usd: 73921.32841999999
sources:
  - label: "ClearMarket market record: Will Russia capture all of Huliaipole in 2026? (multi-d"
    url: "https://clearmarket.fyi/events/will-russia-capture-all-of-huliaipole-by-february-28"
    retrieved_at: "2026-07-28T10:31:13+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A majority of all-time volume printing in one session at an already-elevated price signals that a desk-relevant battlefield update is circulating, cross-reference OSINT sources and ISW daily assessments immediately.
