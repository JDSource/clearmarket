---
signal_id: "CMSIG20260629VS00"
signal_slug: "aleksandar-vu-i-out-as-serbian-presiden-vol-418142"
headline: "Vučić out by June 30: 96% on $418K surge"
semantic_title: "Traders stack near-certainty on Vučić exit by June 30"
telemetry: "96% · $418K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-29T12:29:31+00:00"
event_id: "CM-EVT-01R21H5GP2"
event_slug: "aleksandar-vui-out-as-serbian-president-by"
event_question: "Will Aleksandar Vučić cease to be Serbian President by end of 2025?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xf47e8cc490e9fd5f0ac8bd36aa4bc3b1abf12025dd145baac6cd95ee58e2d286"
  question_raw: "Aleksandar Vučić out as Serbian President by June 30, 2026?"
  current_price: 0.963
  volume_24h_usd: 418142.7832129997
  volume_cumulative_usd: 554697.6059900004
  arbitration_model: "uma_oracle"
  resolves_at: "2026-06-30T00:00:00Z"
bullets:
  - "96% implies Polymarket crowd treats Vučić departure as all but confirmed within 24 hours."
  - "$418K traded in 24h, 75% of the contract's entire all-time volume, signals last-minute conviction rush."
  - "Resolution deadline is tomorrow; volume spike reflects positioning ahead of imminent settlement."
  - "Contract resolves June 30; today's flow is effectively final-settlement arbitrage pressure."
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
      poly_vol_24h_usd: 418142.7832129997
sources:
  - label: "ClearMarket market record: Will Aleksandar Vučić cease to be Serbian President by "
    url: "https://clearmarket.fyi/events/aleksandar-vui-out-as-serbian-president-by"
    retrieved_at: "2026-06-29T12:29:31+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should read this as near-terminal contract compression, the volume is settlement-driven, not new information, but the 75% all-time share in one session flags that late capital is still absorbing residual short risk.
