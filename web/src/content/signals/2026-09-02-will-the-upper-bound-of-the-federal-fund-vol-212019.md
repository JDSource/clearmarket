---
signal_id: "CMSIG20260902VS00"
signal_slug: "will-the-upper-bound-of-the-federal-fund-vol-212019"
headline: "Fed funds above 3.50%: 98% on $212K surge"
semantic_title: "Traders back rates staying above 3.50% after the Fed"
telemetry: "98% · $212K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-02T12:29:56+00:00"
event_id: "CM-EVT-4ZQLQPNH91"
event_slug: "kxfed-26sep"
event_question: "Federal funds rate upper bound, September 2026 meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26SEP-T3.50"
  question_raw: "Will the upper bound of the federal funds rate be above 3.50% following the Fed's Sep 16, 2026 meeting?"
  current_price: 0.98
  volume_24h_usd: 212019.82
  volume_cumulative_usd: 244744.27
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-09-23T18:05:00Z"
bullets:
  - "Kalshi prices a 98% chance the fed funds upper bound holds above 3.50% post-meeting, leaving almost no room for a cut."
  - "24h volume of $212K is 87% of the contract's entire all-time handle, a near-record single-day flush."
  - "With a Fed decision imminent, traders are locking in the no-cut view at extreme conviction levels."
  - "Contract resolves on the rate announced at the next FOMC meeting."
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
      kalshi_vol_24h_usd: 212019.82
sources:
  - label: "ClearMarket market record: Federal funds rate upper bound, September 2026 meeting"
    url: "https://clearmarket.fyi/events/kxfed-26sep"
    retrieved_at: "2026-09-02T12:29:56+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The near-record volume surge at 98% signals desks are treating a hold above 3.50% as a near-certainty and positioning accordingly ahead of the FOMC announcement.
