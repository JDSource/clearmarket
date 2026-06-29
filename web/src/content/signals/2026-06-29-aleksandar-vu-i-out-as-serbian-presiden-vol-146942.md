---
signal_id: "CMSIG20260629VS01"
signal_slug: "aleksandar-vu-i-out-as-serbian-presiden-vol-146942"
headline: "Vučić out by Jun 30: 98% on $147K surge"
semantic_title: "Capital stacks heavily behind Vučić exit by June 30"
telemetry: "98% · $147K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-29T01:47:13+00:00"
event_id: "CM-EVT-01R21H5GP2"
event_slug: "aleksandar-vui-out-as-serbian-president-by"
event_question: "Will Aleksandar Vučić cease to be Serbian President by end of 2025?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xf47e8cc490e9fd5f0ac8bd36aa4bc3b1abf12025dd145baac6cd95ee58e2d286"
  question_raw: "Aleksandar Vučić out as Serbian President by June 30, 2026?"
  current_price: 0.983
  volume_24h_usd: 146942.2326369999
  volume_cumulative_usd: 251347.22318400003
  arbitration_model: "uma_oracle"
  resolves_at: "2026-06-30T00:00:00Z"
bullets:
  - "Polymarket prices 98%, near-certainty implies the market has absorbed available contrary evidence."
  - "$147K in 24h represents 58% of all-time volume; conviction capital flooding in at the deadline."
  - "Deadline tomorrow; 98% print with this volume profile suggests informed participants treating resolution as fait accompli."
  - "Resolves June 30, any official confirmation of departure closes at 100%."
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
      poly_vol_24h_usd: 146942.2326369999
sources:
  - label: "ClearMarket market record: Will Aleksandar Vučić cease to be Serbian President by "
    url: "https://clearmarket.fyi/events/aleksandar-vui-out-as-serbian-president-by"
    retrieved_at: "2026-06-29T01:47:13+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The combination of 98% price and 58% lifetime volume in one session reads as deadline-arbitrage by participants with high confidence in a known outcome, warranting desk confirmation of the underlying political event.
