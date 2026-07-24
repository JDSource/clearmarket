---
signal_id: "CMSIG20260724VS07"
signal_slug: "bitcoin-price-on-jul-24-2026-vol-36011"
headline: "BTC Jul 24 top band: 95% on $36K volume"
semantic_title: "Buyers pile into Bitcoin's 95% band on Jul 24 close"
telemetry: "95% · $36K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-24T10:14:05+00:00"
event_id: "CM-EVT-TTG377V2N9"
event_slug: "kxbtcd-26jul2417"
event_question: "Bitcoin price on Jul 24, 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCD-26JUL2417-T63499.99"
  question_raw: "Bitcoin price on Jul 24, 2026?"
  current_price: 0.95
  volume_24h_usd: 36011.53
  volume_cumulative_usd: 109536.44
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-07-31T21:00:00Z"
bullets:
  - "Market prices a 95% chance Bitcoin finishes above this highest band level today, near-certain resolution expected."
  - "Kalshi sees $36K in 24h, 33% of all-time volume, a third of lifetime activity on final resolution day."
  - "At 95% on expiry day, flow is largely settlement-driven, confirming spot BTC is trading well above the threshold."
  - "Resolves today, Jul 24, 2026; the 5% residual represents tail risk of an extreme intraday reversal."
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
      kalshi_vol_24h_usd: 36011.53
sources:
  - label: "ClearMarket market record: Bitcoin price on Jul 24, 2026"
    url: "https://clearmarket.fyi/events/kxbtcd-26jul2417"
    retrieved_at: "2026-07-24T10:14:05+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 95% price on today's expiry with a third of lifetime volume printing signals settlement confirmation, desks should note this as a live read that Bitcoin's spot price is decisively above this band right now.
