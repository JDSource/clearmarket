---
signal_id: "CMSIG20260710VS02"
signal_slug: "will-the-upper-bound-of-the-federal-fund-vol-63641"
headline: "Fed funds above 3.25%: 99% on $64K volume surge"
semantic_title: "Rates market stacks conviction above 3.25% through next FOMC"
telemetry: "99% · $64K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-10T10:50:20+00:00"
event_id: "CM-EVT-PHWX2H6DM5"
event_slug: "kxfed-26jul"
event_question: "Federal funds rate upper bound, July 2026 meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26JUL-T3.25"
  question_raw: "Will the upper bound of the federal funds rate be above 3.25% following the Fed's Jul 29, 2026 meeting?"
  current_price: 0.99
  volume_24h_usd: 63641.16
  volume_cumulative_usd: 92494.83
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-08-05T18:05:00Z"
bullets:
  - "Kalshi contract at 99%, near-certainty the upper bound holds above 3.25% after the next Fed decision."
  - "24h volume $63.6K is 69% of all-time, a dominant single-session print for this contract."
  - "Fresh rate-cut expectations remain muted; no FOMC catalyst imminent that would break the 3.25% floor."
  - "Resolves on the next Fed meeting outcome; residual 1% reflects only extreme tail-event optionality."
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
      kalshi_vol_24h_usd: 63641.16
sources:
  - label: "ClearMarket market record: Federal funds rate upper bound, July 2026 meeting"
    url: "https://clearmarket.fyi/events/kxfed-26jul"
    retrieved_at: "2026-07-10T10:50:20+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 69% all-time volume concentration at 99% tells rates desks that sophisticated capital is piling into the no-cut side, consistent with a hawkish or on-hold Fed path being treated as near-certain.
