---
signal_id: "CMSIG20260810VS04"
signal_slug: "will-darline-graham-finish-1st-in-the-fi-vol-29355"
headline: "Graham SC Rep first round: 58% on $29K surge"
semantic_title: "Graham leads South Carolina GOP round one at 58%"
telemetry: "58% · $29K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-10T09:15:14+00:00"
event_id: "CM-EVT-34WPGXDWQ8"
event_slug: "kxprimaryplace-scrsens26-1"
event_question: "Will the candidate receiving the most votes win first place in the first round of the South Carolina Republican Senate special primary?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPRIMARYPLACE-SCRSENS26-1-DGRA"
  question_raw: "Will Darline Graham finish 1st in the first round of the 2026 South Carolina Republican Senate special primary?"
  current_price: 0.58
  volume_24h_usd: 29355.12
  volume_cumulative_usd: 93404.72
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-08-11T14:00:00Z"
bullets:
  - "Kalshi prices Darline Graham as the first-round leader in the 2026 South Carolina Republican race at 58%, a modest-conviction lead."
  - "24h volume of $29K is 31% of all-time handle, reflecting a meaningful single-day engagement for a down-ballot primary."
  - "Fresh volume ahead of a primary vote suggests local polling, endorsements, or candidate news is driving traders to take a position."
  - "Resolves on the certified first-round result of the 2026 South Carolina Republican contest."
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
      kalshi_vol_24h_usd: 29355.12
sources:
  - label: "ClearMarket market record: Will the candidate receiving the most votes win first p"
    url: "https://clearmarket.fyi/events/kxprimaryplace-scrsens26-1"
    retrieved_at: "2026-08-10T09:15:14+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

58% pricing with a fresh 31% all-time volume day tells a desk this race has moved from ignored to actively contested, watch for a polling release or major endorsement as the likely catalyst.
