---
signal_id: "CMSIG20260820VS04"
signal_slug: "will-btc-trimmed-mean-be-above-75000-00-vol-31277"
headline: "BTC $75K by Aug 31: 20% on $31K surge"
semantic_title: "BTC at $75K by Aug 31 stays a long shot at 20%"
telemetry: "20% · $31K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-20T08:33:38+00:00"
event_id: "CM-EVT-91N8R2ZK22"
event_slug: "kxbtcmaxmon-btc-26aug31"
event_question: "BTC trimmed mean price, August 31, 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCMAXMON-BTC-26AUG31-7500000"
  question_raw: "Will BTC trimmed mean be above $75000.00 by 11:59 PM ET on Aug 31, 2026?"
  current_price: 0.2
  volume_24h_usd: 31277.44
  volume_cumulative_usd: 81573.53
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-09-08T03:59:59Z"
bullets:
  - "Kalshi prices 20%, market assigns low but non-trivial odds to BTC clearing $75K in 11 days."
  - "24h volume $31K is 38% of all-time, a meaningful spike for a contract priced deep out of the money."
  - "Volume at 20% odds suggests speculative interest or a hedge against a sharp upside breakout scenario."
  - "Resolves 11:59 PM ET Aug 31, 2026; sits at the top rung of the Kalshi August BTC ladder."
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
      kalshi_vol_24h_usd: 31277.44
sources:
  - label: "ClearMarket market record: BTC trimmed mean price, August 31, 2026"
    url: "https://clearmarket.fyi/events/kxbtcmaxmon-btc-26aug31"
    retrieved_at: "2026-08-20T08:33:38+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Fresh money entering a 20%-odds contract with over a third of its lifetime volume signals desks are buying cheap tail exposure on a BTC breakout, worth monitoring alongside the $70K and $72.5K rungs.
