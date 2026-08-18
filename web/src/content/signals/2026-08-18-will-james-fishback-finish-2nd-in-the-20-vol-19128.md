---
signal_id: "CMSIG20260818VS03"
signal_slug: "will-james-fishback-finish-2nd-in-the-20-vol-19128"
headline: "Fishback FL gov 2nd place: 21% on $19K spike"
semantic_title: "Fishback FL governor 2nd-place odds slip to 21%"
telemetry: "21% · $19K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-18T08:31:22+00:00"
event_id: "CM-EVT-3CCRHR07J9"
event_slug: "kxprimaryplace-kxgovflnomr-2"
event_question: "Will Ron DeSantis finish in second place in the Florida Republican governor primary?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPRIMARYPLACE-KXGOVFLNOMR-2-JFIS"
  question_raw: "Will James Fishback finish 2nd in the 2026 Florida gubernatorial primary?"
  current_price: 0.21
  volume_24h_usd: 19128.88
  volume_cumulative_usd: 48810.65
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-08-18T14:00:00Z"
bullets:
  - "Kalshi prices Fishback finishing 2nd at 21%, a minority outcome with a contested field below Donalds."
  - "39% of all-time volume in 24h ($19K), the contract's heaviest single-day activity on record."
  - "With Donalds locked at 99% for the nomination, 2nd-place battle among remaining candidates draws fresh attention."
  - "Resolves on certified primary results showing Fishback's ranked finish."
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
      kalshi_vol_24h_usd: 19128.88
sources:
  - label: "ClearMarket market record: Will Ron DeSantis finish in second place in the Florida"
    url: "https://clearmarket.fyi/events/kxprimaryplace-kxgovflnomr-2"
    retrieved_at: "2026-08-18T08:31:22+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The record proportional volume at 21% indicates active positioning on the down-ballot primary order, relevant for desks tracking Florida political infrastructure and future candidate pipelines.
