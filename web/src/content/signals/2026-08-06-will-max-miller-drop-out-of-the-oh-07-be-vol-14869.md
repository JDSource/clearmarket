---
signal_id: "CMSIG20260806VS07"
signal_slug: "will-max-miller-drop-out-of-the-oh-07-be-vol-14869"
headline: "Max Miller OH-07 dropout by Aug 11: 29% on $15K"
semantic_title: "Max Miller OH-07 dropout odds reach 29% as volume spikes before deadline"
telemetry: "29% · $15K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-06T10:36:04+00:00"
event_id: "CM-EVT-23BGQQPC61"
event_slug: "kxdropoutprimary-26"
event_question: "Will someone drop out of their election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXDROPOUTPRIMARY-26-MMIL2"
  question_raw: "Will Max Miller drop out of the OH-07 before Aug 11, 2026?"
  current_price: 0.29
  volume_24h_usd: 14869.13
  volume_cumulative_usd: 27490.37
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-08-18T14:00:00Z"
bullets:
  - "29% price implies roughly a 1-in-3 chance Miller exits the OH-07 race before Aug 11."
  - "54% of all-time volume hit in 24h, the contract is at its most active session ever."
  - "Surge points to a credible withdrawal signal, statement, filing news, or candidate-side reporting."
  - "Resolves Aug 11; a 5-day window and rising odds suggest the market is treating this as live."
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
      kalshi_vol_24h_usd: 14869.13
sources:
  - label: "ClearMarket market record: Will someone drop out of their election?"
    url: "https://clearmarket.fyi/events/kxdropoutprimary-26"
    retrieved_at: "2026-08-06T10:36:04+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

More than half of lifetime volume in one session at 29% dropout odds tells a desk this is a real watch item, cross-reference Ohio district filing records and local press for a Miller statement.
