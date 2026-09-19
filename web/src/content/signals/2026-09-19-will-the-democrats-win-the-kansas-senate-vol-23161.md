---
signal_id: "CMSIG20260919VS03"
signal_slug: "will-the-democrats-win-the-kansas-senate-vol-23161"
headline: "Democrats win KS Senate: 27% on $23K surge"
semantic_title: "Democrats face long odds in Kansas Senate race despite fresh bets"
telemetry: "27% · $23K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-19T07:47:59+00:00"
event_id: "CM-EVT-V8Y5SZ7SK0"
event_slug: "kansas-senate-election-winner"
event_question: "Kansas Senate Election Winner"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x460d3942d385cdeda20519c0c5ad804ae48dc18efc9a82e1f1be87a29e69adb3"
  question_raw: "Will the Democrats win the Kansas Senate race in 2026?"
  current_price: 0.27
  volume_24h_usd: 23161.454714
  volume_cumulative_usd: 45677.334355000006
  arbitration_model: "uma_oracle"
bullets:
  - "Polymarket prices Democrats at 27%, a clear underdog position in a reliably Republican state."
  - "51% of all-time volume arriving in one session is striking for a race at this price, signaling a specific catalyst."
  - "Surge may reflect a Republican candidate controversy, an unusual filing, or speculative positioning on a wave scenario."
  - "Resolves on November 2026 general election; 27% implies roughly 3-in-10 chance, not trivial for Kansas."
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
      poly_vol_24h_usd: 23161.454714
sources:
  - label: "ClearMarket market record: Kansas Senate Election Winner"
    url: "https://clearmarket.fyi/events/kansas-senate-election-winner"
    retrieved_at: "2026-09-19T07:47:59+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Half the contract's lifetime volume landing at a 27% price in a deep-red state is a flag for desks that something specific, a candidate scandal, primary upset, or national environment shift, is driving speculative interest.
