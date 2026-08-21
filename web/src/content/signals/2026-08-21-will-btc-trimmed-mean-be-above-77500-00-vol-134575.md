---
signal_id: "CMSIG20260821VS01"
signal_slug: "will-btc-trimmed-mean-be-above-77500-00-vol-134575"
headline: "BTC above $77.5K by Aug 31: 82% on $135K"
semantic_title: "BTC above $77.5K by Aug 31 draws heavy backing at 82%"
telemetry: "82% · $135K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-21T08:35:56+00:00"
event_id: "CM-EVT-91N8R2ZK22"
event_slug: "kxbtcmaxmon-btc-26aug31"
event_question: "BTC trimmed mean price, August 31, 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCMAXMON-BTC-26AUG31-7750000"
  question_raw: "Will BTC trimmed mean be above $77500.00 by 11:59 PM ET on Aug 31, 2026?"
  current_price: 0.82
  volume_24h_usd: 134575.37
  volume_cumulative_usd: 206706.02
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-09-08T03:59:59Z"
bullets:
  - "At 82%, Kalshi traders assign strong probability Bitcoin holds above $77.5K through month-end."
  - "24h volume of $135K represents 65% of all-time, the bulk of this contract's liquidity landed today."
  - "With 10 days to expiry and Bitcoin currently well above the strike, fresh volume may reflect confirmation-buying or late hedging."
  - "Resolves 11:59 PM ET Aug 31 on trimmed-mean price; a sharp BTC drawdown is the primary scenario threatening this outcome."
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
      kalshi_vol_24h_usd: 134575.37
sources:
  - label: "ClearMarket market record: BTC trimmed mean price, August 31, 2026"
    url: "https://clearmarket.fyi/events/kxbtcmaxmon-btc-26aug31"
    retrieved_at: "2026-08-21T08:35:56+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Concentrated volume at 65% of all-time on a high-conviction outcome suggests desks are locking in exposure ahead of month-end, treating the $77.5K floor as near-certain barring a macro shock.
