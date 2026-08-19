---
signal_id: "CMSIG20260819VS03"
signal_slug: "will-jay-collins-finish-2nd-in-the-2026-vol-86926"
headline: "Collins FL primary 2nd place: 99% on $87K volume"
semantic_title: "Jay Collins second-place Florida finish holds at 99%"
telemetry: "99% · $87K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-19T08:32:13+00:00"
event_id: "CM-EVT-3CCRHR07J9"
event_slug: "kxprimaryplace-kxgovflnomr-2"
event_question: "Will Ron DeSantis finish in second place in the Florida Republican governor primary?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPRIMARYPLACE-KXGOVFLNOMR-2-JCOL"
  question_raw: "Will Jay Collins finish 2nd in the 2026 Florida gubernatorial primary?"
  current_price: 0.99
  volume_24h_usd: 86926.28
  volume_cumulative_usd: 207262.8
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-08-18T14:00:00Z"
bullets:
  - "Market prices Jay Collins finishing runner-up in the 2026 Florida gubernatorial primary at 99%."
  - "$87K in 24h covers 42% of all-time volume, elevated but leaving a sliver of residual uncertainty."
  - "The 1% discount from certainty suggests some open risk on official canvass rounding or certification."
  - "Contract resolves on Florida's certified primary finishing order for the gubernatorial race."
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
      kalshi_vol_24h_usd: 86926.28
sources:
  - label: "ClearMarket market record: Will Ron DeSantis finish in second place in the Florida"
    url: "https://clearmarket.fyi/events/kxprimaryplace-kxgovflnomr-2"
    retrieved_at: "2026-08-19T08:32:13+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Near-certainty pricing with a meaningful all-time share spike tells a desk Collins' second-place result is widely accepted but awaiting official confirmation.
