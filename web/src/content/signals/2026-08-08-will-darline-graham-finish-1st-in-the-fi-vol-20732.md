---
signal_id: "CMSIG20260808VS07"
signal_slug: "will-darline-graham-finish-1st-in-the-fi-vol-20732"
headline: "Graham SC Rep 1st round: 63% on $21K surge"
semantic_title: "Fresh volume returns to Darline Graham leading South Carolina's first round"
telemetry: "63% · $21K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-08T08:36:03+00:00"
event_id: "CM-EVT-34WPGXDWQ8"
event_slug: "kxprimaryplace-scrsens26-1"
event_question: "Will the candidate receiving the most votes win first place in the first round of the South Carolina Republican Senate special primary?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPRIMARYPLACE-SCRSENS26-1-DGRA"
  question_raw: "Will Darline Graham finish 1st in the first round of the 2026 South Carolina Republican Senate special primary?"
  current_price: 0.63
  volume_24h_usd: 20732.82
  volume_cumulative_usd: 37305.68
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-08-11T14:00:00Z"
bullets:
  - "Kalshi prices Graham finishing first in the South Carolina Republican primary first round at 63%."
  - "24h volume of $21K is 56% of all-time, the majority of lifetime liquidity just traded in one day."
  - "A surge of this proportion against lifetime volume typically signals a near-term catalyst, likely polling or a filing deadline."
  - "Resolves on certified first-round results from the 2026 South Carolina Republican primary."
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
      kalshi_vol_24h_usd: 20732.82
sources:
  - label: "ClearMarket market record: Will the candidate receiving the most votes win first p"
    url: "https://clearmarket.fyi/events/kxprimaryplace-scrsens26-1"
    retrieved_at: "2026-08-08T08:36:03+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

More than half of all-time volume printing in one session at 63% tells a political desk that new information, likely a poll or endorsement, has sharpened conviction on Graham's first-round lead.
