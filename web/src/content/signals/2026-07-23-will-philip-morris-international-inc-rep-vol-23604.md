---
signal_id: "CMSIG20260723VS01"
signal_slug: "will-philip-morris-international-inc-rep-vol-23604"
headline: "PMI Zyn 160M shipments: 98% on $23.6K surge"
semantic_title: "Zyn 160M shipment line draws heavy late trading"
telemetry: "98% · $24K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-23T10:17:14+00:00"
event_id: "CM-EVT-KP0JV78PC7"
event_slug: "kxpm-26julzynship"
event_question: "Philip Morris Zyn shipments, Q2 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPM-26JULZYNSHIP-160000000"
  question_raw: "Will Philip Morris International Inc report Above 160 million zyn us shipment volume in Q2 2026?"
  current_price: 0.98
  volume_24h_usd: 23604.09
  volume_cumulative_usd: 29048.27
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-08-20T10:00:00Z"
bullets:
  - "Kalshi marks this contract at 98%, the lower 160M bar is priced as even more certain than the 165M line."
  - "24h volume of $23.6K equals 81% of all-time flow, the highest lifetime-share of the two Zyn contracts."
  - "Parallel surge alongside the 165M contract points to a coordinated earnings-driven positioning sweep."
  - "Resolves against PMI's disclosed U.S. Zyn shipment volume for the period in question."
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
      kalshi_vol_24h_usd: 23604.09
sources:
  - label: "ClearMarket market record: Philip Morris Zyn shipments, Q2 2026"
    url: "https://clearmarket.fyi/events/kxpm-26julzynship"
    retrieved_at: "2026-07-23T10:17:14+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Twin Zyn contracts spiking together, each consuming roughly 80% of lifetime volume in a single session, is a strong signal that a PMI disclosure event is hours away and traders are stacking certainty at both thresholds.
