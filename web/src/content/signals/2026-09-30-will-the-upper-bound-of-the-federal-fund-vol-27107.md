---
signal_id: "CMSIG20260930VS05"
signal_slug: "will-the-upper-bound-of-the-federal-fund-vol-27107"
headline: "Fed funds above 4%: 46% on $27K, 44% of all-time"
semantic_title: "Fed funds above 4.00% post-meeting at 46%, fresh volume returns"
telemetry: "46% · $27K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-30T07:48:11+00:00"
event_id: "CM-EVT-6BS28TS762"
event_slug: "kxfed-26oct"
event_question: "Federal funds rate upper bound, October 2026 meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26OCT-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Oct 28, 2026 meeting?"
  current_price: 0.46
  volume_24h_usd: 27107.05
  volume_cumulative_usd: 60925.38
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-11-04T18:05:00Z"
bullets:
  - "Kalshi prices a 46% chance the federal funds upper bound stays above 4.00% after the next Fed meeting, near a coin-flip."
  - "$27K traded in 24h equals 44% of all-time contract volume, a heavily concentrated liquidity event."
  - "Closely correlated with Spike 0; dual-contract activity suggests active hedging across Fed rate path scenarios."
  - "Contract resolves on the announced upper bound of the fed funds rate following the relevant FOMC decision."
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
      kalshi_vol_24h_usd: 27107.05
sources:
  - label: "ClearMarket market record: Federal funds rate upper bound, October 2026 meeting"
    url: "https://clearmarket.fyi/events/kxfed-26oct"
    retrieved_at: "2026-09-30T07:48:11+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Parallel volume surges across two Fed rate contracts on the same day confirm that macro traders are actively taking positions on the October FOMC outcome, making both contracts worth tracking as a paired signal.
