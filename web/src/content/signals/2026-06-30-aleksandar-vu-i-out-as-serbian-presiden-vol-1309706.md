---
signal_id: "CMSIG20260630VS00"
signal_slug: "aleksandar-vu-i-out-as-serbian-presiden-vol-1309706"
headline: "Vučić out by June 30: 100% as $1.3M floods in"
semantic_title: "Traders price Vučić exit as settled fact by June 30"
telemetry: "100% · $1.3M 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-30T10:55:12+00:00"
event_id: "CM-EVT-01R21H5GP2"
event_slug: "aleksandar-vui-out-as-serbian-president-by"
event_question: "Will Aleksandar Vučić cease to be Serbian President by end of 2025?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xf47e8cc490e9fd5f0ac8bd36aa4bc3b1abf12025dd145baac6cd95ee58e2d286"
  question_raw: "Aleksandar Vučić out as Serbian President by June 30, 2026?"
  current_price: 0.999
  volume_24h_usd: 1309706.5450060007
  volume_cumulative_usd: 1784448.6793210001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-06-30T00:00:00Z"
bullets:
  - "Polymarket at 100%, market treats Vučić's departure as a done deal."
  - "24h volume $1.3M is 73% of all-time float, signaling terminal resolution rush."
  - "Today is the contract deadline; flows reflect last-minute settlement certainty."
  - "Resolves June 30; near-unanimous capital confirms outcome already in effect."
atomic_claims:
  - type: "volume_anomaly"
    provenance: "24h + cumulative volume direct from polymarket API; intensity = 24h/cumulative (derived)"
    field_provenance:
      volume_24h_usd:
        tier: "direct"
        method: "polymarket_api"
      intensity:
        tier: "derived"
        method: "arithmetic"
        inputs: ["volume_24h_usd", "volume_cumulative_usd"]
    liquidity_context:
      poly_vol_24h_usd: 1309706.5450060007
sources:
  - label: "ClearMarket market record: Will Aleksandar Vučić cease to be Serbian President by "
    url: "https://clearmarket.fyi/events/aleksandar-vui-out-as-serbian-president-by"
    retrieved_at: "2026-06-30T10:55:12+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 100% price on resolution day with 73% of all-time volume in 24 hours signals desks are collecting final settlement dollars, not expressing new directional conviction.
