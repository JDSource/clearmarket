---
signal_id: "CMSIG20260710VS07"
signal_slug: "will-greg-stanton-be-the-democratic-nomi-vol-12437"
headline: "Stanton AZ-04 Dem nominee: 94% on $12K Kalshi flow"
semantic_title: "Greg Stanton stacks as dominant AZ-04 Democratic nominee"
telemetry: "94% · $12K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-10T10:50:20+00:00"
event_id: "CM-EVT-QF3YQZRMN1"
event_slug: "kxazprimary-04d26"
event_question: "Will the Democratic nominee for Arizona's 4th congressional district be determined by the 2026 election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXAZPRIMARY-04D26-GSTA"
  question_raw: "Will Greg Stanton be the Democratic nominee for AZ-04?"
  current_price: 0.94
  volume_24h_usd: 12437.32
  volume_cumulative_usd: 42384.84
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-11-03T15:00:00Z"
bullets:
  - "Contract at 94%, Kalshi capital strongly backs Stanton as the Democratic standard-bearer in AZ-04."
  - "24h volume $12.4K is 29% of all-time; fresh session activity suggests a filing or endorsement catalyst."
  - "Primary field consolidation or a rival's withdrawal would explain renewed high-conviction accumulation."
  - "Resolves at primary conclusion; 6% residual covers late-entry or surprise challenger scenarios."
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
      kalshi_vol_24h_usd: 12437.32
sources:
  - label: "ClearMarket market record: Will the Democratic nominee for Arizona's 4th congressi"
    url: "https://clearmarket.fyi/events/kxazprimary-04d26"
    retrieved_at: "2026-07-10T10:50:20+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

High-conviction volume at 94% on a House primary contract signals that political-risk desks are treating Stanton's nomination as effectively settled, likely following a concrete primary field development.
