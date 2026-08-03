---
signal_id: "CMSIG20260803VS01"
signal_slug: "will-snap-inc-report-above-484-million-vol-11891"
headline: "Snap Q2 DAU >484M: 90% on near-total volume reset"
semantic_title: "Snap Q2 DAU above 484M stays a strong 90% favorite"
telemetry: "90% · $12K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-03T11:19:10+00:00"
event_id: "CM-EVT-7KQYTRS9D8"
event_slug: "kxsnap-26augdau"
event_question: "Snap global daily active users, Q2 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXSNAP-26AUGDAU-484000000"
  question_raw: "Will Snap Inc. report Above 484 million global daily active users in Q2 2026?"
  current_price: 0.9
  volume_24h_usd: 11891.27
  volume_cumulative_usd: 14945.36
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-09-03T20:00:00Z"
bullets:
  - "At 90%, the market treats Snap clearing 484M daily active users in Q2 as near-certain."
  - "$11.9K in 24h represents 80% of all-time contract volume, nearly the entire lifetime traded in one session."
  - "Snap's Q2 earnings report is imminent; this volume spike likely reflects last-chance positioning before resolution."
  - "Resolves on Snap's official Q2 earnings disclosure of global DAU."
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
      kalshi_vol_24h_usd: 11891.27
sources:
  - label: "ClearMarket market record: Snap global daily active users, Q2 2026"
    url: "https://clearmarket.fyi/events/kxsnap-26augdau"
    retrieved_at: "2026-08-03T11:19:10+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With 80% of lifetime volume printing in a single day at 90% odds, this contract is effectively in final settlement mode, desks should treat it as resolved pending the earnings print.
