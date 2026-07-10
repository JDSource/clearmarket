---
signal_id: "CMSIG20260710VS04"
signal_slug: "will-the-upper-bound-of-the-federal-fund-vol-21470"
headline: "Fed funds above 3.00%: 99% on $21K Kalshi flow"
semantic_title: "Rates capital stacks the 3.00% floor as unthreatened into next FOMC"
telemetry: "99% · $21K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-10T10:50:20+00:00"
event_id: "CM-EVT-PHWX2H6DM5"
event_slug: "kxfed-26jul"
event_question: "Federal funds rate upper bound, July 2026 meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26JUL-T3.00"
  question_raw: "Will the upper bound of the federal funds rate be above 3.00% following the Fed's Jul 29, 2026 meeting?"
  current_price: 0.99
  volume_24h_usd: 21470.13
  volume_cumulative_usd: 64599.89
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-08-05T18:05:00Z"
bullets:
  - "Contract at 99%, market treats any cut below 3.00% as essentially impossible near-term."
  - "24h volume $21.5K is 33% of all-time, a meaningful single-day share for a deep-in-the-money contract."
  - "Flows complement the 3.25% and 3.50% contracts; desks are layering across the rates floor curve."
  - "Resolves at next Fed meeting; 1% residual is pure black-swan optionality."
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
      kalshi_vol_24h_usd: 21470.13
sources:
  - label: "ClearMarket market record: Federal funds rate upper bound, July 2026 meeting"
    url: "https://clearmarket.fyi/events/kxfed-26jul"
    retrieved_at: "2026-07-10T10:50:20+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Coordinated volume across the 3.00%, 3.25%, and 3.50% Kalshi rate contracts on the same session signals systematic desk positioning to lock in the rates-on-hold narrative ahead of the next FOMC.
