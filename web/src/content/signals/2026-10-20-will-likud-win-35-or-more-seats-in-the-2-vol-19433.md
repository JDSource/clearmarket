---
signal_id: "CMSIG20261020VS04"
signal_slug: "will-likud-win-35-or-more-seats-in-the-2-vol-19433"
headline: "Likud 35+ seats 2026 election: 0% on $19K surge"
semantic_title: "Likud at 35-plus seats trades to zero through fresh volume"
telemetry: "0% · $19K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-20T13:16:06+00:00"
event_id: "CM-EVT-49Z7YZY008"
event_slug: "israel-election-likud-of-seats"
event_question: "Will Likud win at least 30 seats in the next Israeli election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x78b3aec55f914a149fc110ffd4dcfb008ff94e2df4a451b396f7c14a572d6aa7"
  question_raw: "Will Likud win 35 or more seats in the 2026 Israeli legislative election?"
  current_price: 0.004
  volume_24h_usd: 19433.557932
  volume_cumulative_usd: 67951.24386399999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-10-27T00:00:00Z"
bullets:
  - "Market has fully closed the door on Likud winning 35 or more seats, price sits at 0%, a near-certain 'No'."
  - "24h volume of $19K is 29% of all-time handle, confirming active interest in locking in the outcome."
  - "Latest polling or coalition dynamics have apparently made a Likud supermajority-adjacent result mathematically implausible to traders."
  - "Resolves at the 2026 Israeli legislative election result; a zero price means the market is done debating this bracket."
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
      poly_vol_24h_usd: 19433.557932
sources:
  - label: "ClearMarket market record: Will Likud win at least 30 seats in the next Israeli el"
    url: "https://clearmarket.fyi/events/israel-election-likud-of-seats"
    retrieved_at: "2026-10-20T13:16:06+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A zero-priced contract still drawing fresh volume signals traders actively closing or arbitraging residual positions, useful as a baseline for adjacent Likud seat-count brackets which remain live.
