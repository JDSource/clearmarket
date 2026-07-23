---
signal_id: "CMSIG20260723VS00"
signal_slug: "will-philip-morris-international-inc-rep-vol-24811"
headline: "PMI Zyn 165M shipments: 98% on $24.8K surge"
semantic_title: "Zyn 165M shipment bar stays a near-certainty"
telemetry: "98% · $25K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-23T10:17:14+00:00"
event_id: "CM-EVT-KP0JV78PC7"
event_slug: "kxpm-26julzynship"
event_question: "Philip Morris Zyn shipments, Q2 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPM-26JULZYNSHIP-165000000"
  question_raw: "Will Philip Morris International Inc report Above 165 million zyn us shipment volume in Q2 2026?"
  current_price: 0.98
  volume_24h_usd: 24811.95
  volume_cumulative_usd: 31738.59
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-08-20T10:00:00Z"
bullets:
  - "Kalshi prices 98% on PMI clearing 165M U.S. Zyn shipments, market sees this as a formality."
  - "24h volume of $24.8K is 78% of all-time, meaning almost the entire contract history traded today."
  - "PMI earnings cycle likely imminent, drawing capital to lock in the near-certain side at minimal edge."
  - "Resolves on PMI's official reported U.S. Zyn shipment figure for the relevant period."
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
      kalshi_vol_24h_usd: 24811.95
sources:
  - label: "ClearMarket market record: Philip Morris Zyn shipments, Q2 2026"
    url: "https://clearmarket.fyi/events/kxpm-26julzynship"
    retrieved_at: "2026-07-23T10:17:14+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The volume concentration, 78% of lifetime flow in one session, signals that an earnings print or shipment disclosure is imminent and the desk consensus is this threshold is not in doubt.
