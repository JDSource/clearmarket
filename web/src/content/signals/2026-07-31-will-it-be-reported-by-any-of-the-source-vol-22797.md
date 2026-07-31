---
signal_id: "CMSIG20260731VS02"
signal_slug: "will-it-be-reported-by-any-of-the-source-vol-22797"
headline: "Senate Judiciary Comm report: 33% on $22K"
semantic_title: "Heavy trading tests Senate Judiciary Committee odds at a discount"
telemetry: "33% · $23K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-31T10:35:22+00:00"
event_id: "CM-EVT-5ZY4R2CPG9"
event_slug: "kxblanchejudiciary-27"
event_question: "Will Todd Blanche's Attorney General nomination advance from committee?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBLANCHEJUDICIARY-27-26SEP01"
  question_raw: "Will it be reported by any of the Source Agencies that the Senate Judiciary Committee reports Todd Blanche's nomination to be U.S. Attorney General to the full Senate before Sep 1, 2026?"
  current_price: 0.33
  volume_24h_usd: 22797.71
  volume_cumulative_usd: 28625.13
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-09-08T14:00:00Z"
bullets:
  - "At 33%, Kalshi prices the Senate Judiciary Committee action as more likely not to occur."
  - "$22K in 24h is 80% of all-time volume, near the entire contract lifetime in one session."
  - "An 80% all-time share implies a sharp new catalyst or deadline forcing a binary decision."
  - "Resolution tied to reporting by designated source agencies."
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
      kalshi_vol_24h_usd: 22797.71
sources:
  - label: "ClearMarket market record: Will Todd Blanche's Attorney General nomination advance"
    url: "https://clearmarket.fyi/events/kxblanchejudiciary-27"
    retrieved_at: "2026-07-31T10:35:22+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With 80% of lifetime volume clearing in a single day, a desk should treat this as a breaking-news trigger, someone is taking a strong directional stance ahead of an expected committee development.
