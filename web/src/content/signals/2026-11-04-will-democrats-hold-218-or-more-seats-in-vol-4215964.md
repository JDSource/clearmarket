---
signal_id: "CMSIG20261104VS01"
signal_slug: "will-democrats-hold-218-or-more-seats-in-vol-4215964"
headline: "House Dem majority: 100% on $4.2M midterm surge"
semantic_title: "Heavy trading backs Democrats locking up a House majority"
telemetry: "100% · $4.2M 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-04T07:48:42+00:00"
event_id: "CM-EVT-QK0HJYVMX2"
event_slug: "kxbluewavecombo-27feb"
event_question: "Will there be a blue wave in 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBLUEWAVECOMBO-27FEB"
  question_raw: "Will Democrats hold 218 or more seats in the House after the 2026 midterms AND hold 49 or more seats in the Senate after the 2026 midterms?"
  current_price: 0.999
  volume_24h_usd: 4215964.42
  volume_cumulative_usd: 9231662.78
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-02-01T15:00:00Z"
bullets:
  - "Kalshi contract prices Democratic House majority at 100%, market treats outcome as resolved."
  - "46% of all-time volume printed in 24h, reflecting late capital confirming the call."
  - "Price at ceiling suggests live results or early vote reporting has collapsed remaining uncertainty."
  - "Resolves on certified seat count post-2026 midterms."
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
      kalshi_vol_24h_usd: 4215964.42
sources:
  - label: "ClearMarket market record: Will there be a blue wave in 2026?"
    url: "https://clearmarket.fyi/events/kxbluewavecombo-27feb"
    retrieved_at: "2026-11-04T07:48:42+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 100% price with nearly half of lifetime volume in one session signals the market is functioning as a settlement mechanism, not a price-discovery one, desks should treat this as effectively closed.
