---
signal_id: "CMSIG20260710VS06"
signal_slug: "will-the-upper-bound-of-the-federal-fund-vol-15197"
headline: "Fed funds above 3.50%: 98% on $15K Kalshi surge"
semantic_title: "Conviction above 3.50% priced deep in the money as flows accelerate"
telemetry: "98% · $15K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-10T10:50:20+00:00"
event_id: "CM-EVT-PHWX2H6DM5"
event_slug: "kxfed-26jul"
event_question: "Federal funds rate upper bound, July 2026 meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26JUL-T3.50"
  question_raw: "Will the upper bound of the federal funds rate be above 3.50% following the Fed's Jul 29, 2026 meeting?"
  current_price: 0.98
  volume_24h_usd: 15197.98
  volume_cumulative_usd: 59765.49
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-08-05T18:05:00Z"
bullets:
  - "At 98%, capital prices a sub-3.50% Fed funds rate as a remote tail risk at current FOMC trajectory."
  - "24h volume $15.2K is 25% of all-time; third active rate-floor contract seeing simultaneous flow."
  - "Concurrent with 3.00% and 3.25% contracts surging, systematic rates desk activity across the curve."
  - "Resolves at next Fed decision; 2% residual reflects slightly wider tail given the higher threshold."
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
      kalshi_vol_24h_usd: 15197.98
sources:
  - label: "ClearMarket market record: Federal funds rate upper bound, July 2026 meeting"
    url: "https://clearmarket.fyi/events/kxfed-26jul"
    retrieved_at: "2026-07-10T10:50:20+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Three Kalshi Fed funds floor contracts spiking in unison on the same day points to institutional desk hedging or a directional macro trade expressing high confidence in rates remaining restrictive through the next meeting.
