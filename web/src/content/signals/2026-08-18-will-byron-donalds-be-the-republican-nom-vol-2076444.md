---
signal_id: "CMSIG20260818VS00"
signal_slug: "will-byron-donalds-be-the-republican-nom-vol-2076444"
headline: "Donalds FL governor: 99% on $2.1M surge"
semantic_title: "Donalds FL GOP nod priced as settled at 99%"
telemetry: "99% · $2.1M 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-18T08:31:22+00:00"
event_id: "CM-EVT-8WBM80ZB13"
event_slug: "kxgovflnomr-26"
event_question: "Will Ron DeSantis be the Florida Republican Governor nominee by 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXGOVFLNOMR-26-BD"
  question_raw: "Will Byron Donalds be the Republican nominee for Governor in Florida?"
  current_price: 0.987
  volume_24h_usd: 2076444.3
  volume_cumulative_usd: 7418396.78
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-11-03T15:00:00Z"
bullets:
  - "Kalshi prices Donalds at 99%, market treats the Republican nomination as a near-certainty."
  - "28% of all-time volume hit in 24h ($2.1M), signaling a decisive positioning event."
  - "Surge likely tied to primary results or filing deadlines collapsing remaining uncertainty."
  - "Resolves on official GOP nominee certification for Florida governor race."
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
      kalshi_vol_24h_usd: 2076444.3
sources:
  - label: "ClearMarket market record: Will Ron DeSantis be the Florida Republican Governor no"
    url: "https://clearmarket.fyi/events/kxgovflnomr-26"
    retrieved_at: "2026-08-18T08:31:22+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A $2.1M single-session flush at 99% indicates the market is closing out residual short positions, desks should treat the nomination as resolved for downstream general-election pricing.
