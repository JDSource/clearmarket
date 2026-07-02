---
signal_id: "CMSIG20260702VS05"
signal_slug: "will-victor-marx-be-the-republican-nomin-vol-145141"
headline: "Marx CO GOP nominee: 96% on $145K Kalshi surge"
semantic_title: "Victor Marx GOP Colorado governor nomination sits near certainty"
telemetry: "96% · $145K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-02T10:35:06+00:00"
event_id: "CM-EVT-3X1XZGV3C4"
event_slug: "kxgovconomr-26"
event_question: "Will Abe Suthers be elected Colorado Republican Governor nominee by 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXGOVCONOMR-26-VMAR"
  question_raw: "Will Victor Marx be the Republican nominee for Governor in Colorado?"
  current_price: 0.965
  volume_24h_usd: 145141.93
  volume_cumulative_usd: 441812.16
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-11-03T15:00:00Z"
bullets:
  - "96% price reflects near-unanimous market conviction that Marx locks up the Republican Colorado governor nomination."
  - "$145K in 24h, 33% of all-time Kalshi volume, indicates fresh informed capital entering, not just noise."
  - "Surge likely follows a primary filing deadline, candidate dropout, or delegate count update confirming Marx's lead."
  - "Resolution tied to the Republican primary outcome; thin residual 4% covers spoiler or procedural risk."
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
      kalshi_vol_24h_usd: 145141.93
sources:
  - label: "ClearMarket market record: Will Abe Suthers be elected Colorado Republican Governo"
    url: "https://clearmarket.fyi/events/kxgovconomr-26"
    retrieved_at: "2026-07-02T10:35:06+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Fresh capital at 96% suggests a recent primary development has materially reduced uncertainty, desks tracking Colorado 2026 gubernatorial dynamics should treat this as a near-resolved contract and shift focus to the general election market.
