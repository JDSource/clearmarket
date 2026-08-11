---
signal_id: "CMSIG20260811VS07"
signal_slug: "will-average-gas-prices-be-above-3-vol-17714"
headline: "Gas prices above $3.80: 98% on $18K surge"
semantic_title: "Average gas prices staying above $3.80 priced at 98%"
telemetry: "98% · $18K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-11T08:50:18+00:00"
event_id: "CM-EVT-0WLSN5GTP4"
event_slug: "kxaaagasm-26aug31"
event_question: "AAA average gas price, August 31, 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXAAAGASM-26AUG31-3.80"
  question_raw: "Will average **gas prices** be above $3.80?"
  current_price: 0.98
  volume_24h_usd: 17714.38
  volume_cumulative_usd: 30975.31
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-09-30T14:00:00Z"
bullets:
  - "Market prices average U.S. gas prices remaining above $3.80 at 98%, near-certain."
  - "$18K in 24h, 57% of all-time volume, signals a decisive surge in conviction on this contract."
  - "Activity likely follows weekly EIA price data or refinery/crude news keeping prices elevated."
  - "Resolves YES if the average U.S. gas price benchmark is recorded above $3.80 at resolution."
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
      kalshi_vol_24h_usd: 17714.38
sources:
  - label: "ClearMarket market record: AAA average gas price, August 31, 2026"
    url: "https://clearmarket.fyi/events/kxaaagasm-26aug31"
    retrieved_at: "2026-08-11T08:50:18+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

More than half of all-time volume printing at 98% in a single session indicates the market is closing residual short exposure, desks with consumer discretionary or inflation exposure should note the market treating sub-$3.80 gas as essentially ruled out.
