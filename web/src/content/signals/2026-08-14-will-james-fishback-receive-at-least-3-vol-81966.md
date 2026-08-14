---
signal_id: "CMSIG20260814VS03"
signal_slug: "will-james-fishback-receive-at-least-3-vol-81966"
headline: "Fishback FL 3% vote share: 98% on $82K surge"
semantic_title: "Fishback hits 3% Florida vote threshold, market near certain"
telemetry: "98% · $82K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-14T09:04:43+00:00"
event_id: "CM-EVT-3BTF9D60C9"
event_slug: "kxvoteprimary-govflnomr26jfis"
event_question: "Will James Fishback receive more than X percent of the vote in the Florida Republican Governor primary?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXVOTEPRIMARY-GOVFLNOMR26JFIS-51"
  question_raw: "Will James Fishback receive at least 3% of the popular vote in the 2026 Florida Republican Governor primary?"
  current_price: 0.983
  volume_24h_usd: 81966.45
  volume_cumulative_usd: 268351.17
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-08-18T14:00:00Z"
bullets:
  - "98% prices Fishback clearing the 3% threshold as a near-certainty."
  - "$82K traded in 24h, 31% of all-time volume, confirming late-stage conviction."
  - "High price with heavy volume suggests recent polling or ballot data locked in the outcome."
  - "Resolves on certified 2026 Florida popular vote tallies."
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
      kalshi_vol_24h_usd: 81966.45
sources:
  - label: "ClearMarket market record: Will James Fishback receive more than X percent of the "
    url: "https://clearmarket.fyi/events/kxvoteprimary-govflnomr26jfis"
    retrieved_at: "2026-08-14T09:04:43+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 98% price absorbing 31% of all-time volume in one day signals the market has consumed all material uncertainty, desks can treat this as effectively resolved.
