---
signal_id: "CMSIG20260821VS02"
signal_slug: "will-btc-trimmed-mean-be-above-80000-00-vol-100066"
headline: "BTC above $80K by Aug 31: 67% on $100K surge"
semantic_title: "Traders back BTC staying above $80K through August"
telemetry: "67% · $100K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-21T08:35:56+00:00"
event_id: "CM-EVT-91N8R2ZK22"
event_slug: "kxbtcmaxmon-btc-26aug31"
event_question: "BTC trimmed mean price, August 31, 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCMAXMON-BTC-26AUG31-8000000"
  question_raw: "Will BTC trimmed mean be above $80000.00 by 11:59 PM ET on Aug 31, 2026?"
  current_price: 0.67
  volume_24h_usd: 100066.03
  volume_cumulative_usd: 150768.34
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-09-08T03:59:59Z"
bullets:
  - "67% odds on Kalshi place BTC above $80K at month-end as the base case, not a stretch."
  - "24h volume of $100K equals 66% of all-time, signaling this contract is newly active with concentrated fresh interest."
  - "The $80K level sits roughly in the middle of current BTC trading range, making this the market's clearest directional read."
  - "Resolves trimmed-mean Aug 31; pairs naturally with the $77.5K and $82.5K strikes bracketing trader positioning."
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
      kalshi_vol_24h_usd: 100066.03
sources:
  - label: "ClearMarket market record: BTC trimmed mean price, August 31, 2026"
    url: "https://clearmarket.fyi/events/kxbtcmaxmon-btc-26aug31"
    retrieved_at: "2026-08-21T08:35:56+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With two-thirds of all-time volume hitting today, the $80K strike is the fulcrum contract for BTC month-end positioning, desks should treat 67% here as the consensus anchor for August close.
