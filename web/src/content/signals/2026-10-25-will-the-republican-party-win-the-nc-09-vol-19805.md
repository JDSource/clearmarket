---
signal_id: "CMSIG20261025VS05"
signal_slug: "will-the-republican-party-win-the-nc-09-vol-19805"
headline: "GOP wins NC-09: 63% on $20K volume"
semantic_title: "GOP odds hold at 63% in NC-09 on renewed trading"
telemetry: "63% · $20K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-25T12:57:02+00:00"
event_id: "CM-EVT-0PM0Y1S600"
event_slug: "nc-09-house-election-winner"
event_question: "Will the winner of the NC-09 House election be determined by November 3, 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x31727e0e298757e552661f62733cc401c6066b80a7d2607d2ac56b729eb15a00"
  question_raw: "Will the Republican Party win the NC-09 House seat?"
  current_price: 0.63
  volume_24h_usd: 19805.912649999995
  volume_cumulative_usd: 49899.60765199999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "63% prices Republicans as moderate favorites in NC-09, same race where Democrats show 36% on a parallel contract."
  - "Polymarket's $20K 24h volume is 40% of all-time, running alongside the larger Democratic-side NC-09 spike."
  - "Dual-contract volume surge on the same race points to two-sided repositioning, not a one-directional bet."
  - "Resolves on 2026 midterm NC-09 House race certification; prices on both contracts should sum near 100%."
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
      poly_vol_24h_usd: 19805.912649999995
sources:
  - label: "ClearMarket market record: Will the winner of the NC-09 House election be determin"
    url: "https://clearmarket.fyi/events/nc-09-house-election-winner"
    retrieved_at: "2026-10-25T12:57:02+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Simultaneous spikes on both the Republican and Democratic NC-09 contracts suggest active two-sided trading, desks should treat this as a liquidity event in a contested district, not a directional signal.
