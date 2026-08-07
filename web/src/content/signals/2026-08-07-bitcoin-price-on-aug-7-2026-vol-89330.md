---
signal_id: "CMSIG20260807VS04"
signal_slug: "bitcoin-price-on-aug-7-2026-vol-89330"
headline: "BTC Aug 7 upper range: 80% on $89K surge"
semantic_title: "Bitcoin Aug 7 upper range holds at 80% through heavy trading"
telemetry: "80% · $89K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-07T08:54:29+00:00"
event_id: "CM-EVT-PFHRR5PCZ2"
event_slug: "kxbtcd-26aug0717"
event_question: "Bitcoin price, August 7, 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCD-26AUG0717-T63999.99"
  question_raw: "Bitcoin price on Aug 7, 2026?"
  current_price: 0.8
  volume_24h_usd: 89330.94
  volume_cumulative_usd: 256275.27
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-08-14T21:00:00Z"
bullets:
  - "80% odds favor Bitcoin closing in the upper price bracket on today's settlement."
  - "$89K in 24h is 35% of all-time volume for this contract, a meaningful single-day concentration."
  - "Same-day resolution amplifies urgency, traders locking in directional views into the close."
  - "Resolves on Bitcoin's official price at end of August 7, 2026."
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
      kalshi_vol_24h_usd: 89330.94
sources:
  - label: "ClearMarket market record: Bitcoin price, August 7, 2026"
    url: "https://clearmarket.fyi/events/kxbtcd-26aug0717"
    retrieved_at: "2026-08-07T08:54:29+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

High volume at 80% on a same-day Bitcoin price contract tells a crypto desk that positioning is heavily skewed to the upside bucket with hours remaining before resolution.
