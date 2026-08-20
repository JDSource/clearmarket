---
signal_id: "CMSIG20260820VS01"
signal_slug: "will-btc-trimmed-mean-be-above-72500-00-vol-71125"
headline: "BTC $72.5K by Aug 31: 46% on $71K surge"
semantic_title: "Traders split evenly on BTC clearing $72.5K by Aug 31"
telemetry: "46% · $71K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-20T08:33:38+00:00"
event_id: "CM-EVT-91N8R2ZK22"
event_slug: "kxbtcmaxmon-btc-26aug31"
event_question: "BTC trimmed mean price, August 31, 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCMAXMON-BTC-26AUG31-7250000"
  question_raw: "Will BTC trimmed mean be above $72500.00 by 11:59 PM ET on Aug 31, 2026?"
  current_price: 0.46
  volume_24h_usd: 71125.96
  volume_cumulative_usd: 150080.54
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-09-08T03:59:59Z"
bullets:
  - "Kalshi sits at 46%, the market is essentially a coin flip on BTC reaching $72.5K in 11 days."
  - "24h volume $71K is 47% of all-time, showing fresh conviction on both sides of the line."
  - "Near-50% pricing invites arbitrage versus the 90%-priced $70K contract, driving cross-market attention."
  - "Resolves 11:59 PM ET Aug 31, 2026."
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
      kalshi_vol_24h_usd: 71125.96
sources:
  - label: "ClearMarket market record: BTC trimmed mean price, August 31, 2026"
    url: "https://clearmarket.fyi/events/kxbtcmaxmon-btc-26aug31"
    retrieved_at: "2026-08-20T08:33:38+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Near-even odds drawing half the contract's lifetime volume in one session flags active two-sided positioning, desks should watch for spread trades against the $70K and $75K Kalshi ladders.
