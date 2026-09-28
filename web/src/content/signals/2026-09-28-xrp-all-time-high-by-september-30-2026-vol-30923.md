---
signal_id: "CMSIG20260928VS00"
signal_slug: "xrp-all-time-high-by-september-30-2026-vol-30923"
headline: "XRP ATH by Sept 30: 1% with 46% of volume in 24h"
semantic_title: "XRP all-time high by Sept 30 stays a near-certain no"
telemetry: "1% · $31K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-28T07:48:17+00:00"
event_id: "CM-EVT-JRZD8SKXP9"
event_slug: "xrp-all-time-high-by"
event_question: "Will XRP reach a new all-time high by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x86d0232cd2d07900e00a49c1606863ad760618fa36861add2777839bd05b06af"
  question_raw: "XRP all time high by September 30, 2026?"
  current_price: 0.009
  volume_24h_usd: 30923.24
  volume_cumulative_usd: 67391.67306900001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-10-01T05:00:00Z"
bullets:
  - "Polymarket prices a new XRP all-time high by September 30 at just 1%, effectively ruling it out with two days left."
  - "24h volume of $30,923 represents 46% of all-time contract volume, a concentrated late-window flush of activity."
  - "Surge likely reflects traders closing or taking final positions as the 48-hour expiry window forces resolution."
  - "Contract resolves September 30; near-zero price signals the market sees no credible path to a new ATH before close."
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
      poly_vol_24h_usd: 30923.24
sources:
  - label: "ClearMarket market record: Will XRP reach a new all-time high by 2026?"
    url: "https://clearmarket.fyi/events/xrp-all-time-high-by"
    retrieved_at: "2026-09-28T07:48:17+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The volume spike into a 1% contract two days from expiry signals position cleanup and expiry-driven liquidity, not a shift in conviction, desks should read this as terminal settlement flow, not a directional signal on XRP.
