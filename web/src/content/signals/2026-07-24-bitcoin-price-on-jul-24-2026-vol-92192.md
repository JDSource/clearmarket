---
signal_id: "CMSIG20260724VS02"
signal_slug: "bitcoin-price-on-jul-24-2026-vol-92192"
headline: "BTC Jul 24 upper band: 76% on $92K volume"
semantic_title: "Traders back Bitcoin above its Jul 24 band at 76%"
telemetry: "76% · $92K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-24T10:14:05+00:00"
event_id: "CM-EVT-TTG377V2N9"
event_slug: "kxbtcd-26jul2417"
event_question: "Bitcoin price on Jul 24, 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCD-26JUL2417-T64499.99"
  question_raw: "Bitcoin price on Jul 24, 2026?"
  current_price: 0.76
  volume_24h_usd: 92192.04
  volume_cumulative_usd: 258940.82
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-07-31T21:00:00Z"
bullets:
  - "Market prices a 76% probability Bitcoin clears the upper price threshold today, a meaningful lean above the line."
  - "Kalshi records $92K in 24h, 36% of all-time volume for this contract, concentrated on expiry day."
  - "Same-day resolution means this is live directional flow, not a forward bet; price reflects where traders see the close."
  - "Resolves today, Jul 24, 2026 against Bitcoin's final spot price."
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
      kalshi_vol_24h_usd: 92192.04
sources:
  - label: "ClearMarket market record: Bitcoin price on Jul 24, 2026"
    url: "https://clearmarket.fyi/events/kxbtcd-26jul2417"
    retrieved_at: "2026-07-24T10:14:05+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Strong conviction at 76% with heavy expiry-day volume suggests the desk consensus is leaning bullish on Bitcoin's intraday close, worth watching for spot confirmation.
