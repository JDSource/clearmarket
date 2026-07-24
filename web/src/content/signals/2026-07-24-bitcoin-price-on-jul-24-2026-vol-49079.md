---
signal_id: "CMSIG20260724VS06"
signal_slug: "bitcoin-price-on-jul-24-2026-vol-49079"
headline: "BTC Jul 24 high band: 90% on $49K volume"
semantic_title: "Fresh volume backs Bitcoin above its 90% band today"
telemetry: "90% · $49K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-24T10:14:05+00:00"
event_id: "CM-EVT-TTG377V2N9"
event_slug: "kxbtcd-26jul2417"
event_question: "Bitcoin price on Jul 24, 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCD-26JUL2417-T63999.99"
  question_raw: "Bitcoin price on Jul 24, 2026?"
  current_price: 0.9
  volume_24h_usd: 49079.08
  volume_cumulative_usd: 188386.39
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-07-31T21:00:00Z"
bullets:
  - "Market prices a 90% probability Bitcoin clears this upper threshold by today's close, strong directional consensus."
  - "Kalshi logs $49K in 24h, 26% of all-time volume, a notable but not dominant share, suggesting steady rather than panic flow."
  - "High confidence on expiry day reflects current spot prices already well above the band line, locking in near-certain resolution."
  - "Resolves today, Jul 24, 2026 against Bitcoin's closing price."
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
      kalshi_vol_24h_usd: 49079.08
sources:
  - label: "ClearMarket market record: Bitcoin price on Jul 24, 2026"
    url: "https://clearmarket.fyi/events/kxbtcd-26jul2417"
    retrieved_at: "2026-07-24T10:14:05+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 90% price with meaningful expiry-day volume indicates Bitcoin is comfortably above this band threshold in spot markets, desks can use this as a soft real-time price floor signal.
