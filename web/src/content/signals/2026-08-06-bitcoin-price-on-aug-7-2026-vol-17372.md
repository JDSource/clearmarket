---
signal_id: "CMSIG20260806VS06"
signal_slug: "bitcoin-price-on-aug-7-2026-vol-17372"
headline: "Bitcoin Aug 7 price band: 34% on $17K"
semantic_title: "Bitcoin Aug 7 range bet draws heavy trading at 34% odds"
telemetry: "34% · $17K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-06T10:36:04+00:00"
event_id: "CM-EVT-PFHRR5PCZ2"
event_slug: "kxbtcd-26aug0717"
event_question: "Bitcoin price, August 7, 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCD-26AUG0717-T64999.99"
  question_raw: "Bitcoin price on Aug 7, 2026?"
  current_price: 0.34
  volume_24h_usd: 17372.25
  volume_cumulative_usd: 35846.93
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-08-14T21:00:00Z"
bullets:
  - "34% price means the targeted BTC range for Aug 7 is seen as a minority-probability outcome."
  - "48% of all-time volume in one session flags sharp positioning ahead of tomorrow's settlement."
  - "Overnight BTC moves or macro sentiment shifts are likely driving last-minute range speculation."
  - "Resolves Aug 7, imminent expiry concentrates risk and amplifies volume in the final hours."
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
      kalshi_vol_24h_usd: 17372.25
sources:
  - label: "ClearMarket market record: Bitcoin price, August 7, 2026"
    url: "https://clearmarket.fyi/events/kxbtcd-26aug0717"
    retrieved_at: "2026-08-06T10:36:04+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Near-expiry concentration of volume at a 34% strike tells a desk that the market is pricing meaningful BTC range uncertainty, monitor spot price into the Aug 7 open for settlement risk.
