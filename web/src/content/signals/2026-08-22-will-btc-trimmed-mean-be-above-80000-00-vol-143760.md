---
signal_id: "CMSIG20260822VS00"
signal_slug: "will-btc-trimmed-mean-be-above-80000-00-vol-143760"
headline: "BTC $80K by Aug 31: 64% on $144K surge"
semantic_title: "BTC above $80K by Aug 31 stays the favored side"
telemetry: "64% · $144K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-22T08:24:03+00:00"
event_id: "CM-EVT-91N8R2ZK22"
event_slug: "kxbtcmaxmon-btc-26aug31"
event_question: "BTC trimmed mean price, August 31, 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCMAXMON-BTC-26AUG31-8000000"
  question_raw: "Will BTC trimmed mean be above $80000.00 by 11:59 PM ET on Aug 31, 2026?"
  current_price: 0.64
  volume_24h_usd: 143760.62
  volume_cumulative_usd: 287494.89
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-09-08T03:59:59Z"
bullets:
  - "Kalshi prices 64%, market leans BTC holds above $80K through month-end."
  - "24h volume $144K is 50% of all-time, marking a decisive mid-contract liquidity event."
  - "Nine days to expiry; August 31 deadline compresses time, lifting urgency to take positions."
  - "Resolves 11:59 PM ET Aug 31 on trimmed-mean BTC price."
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
      kalshi_vol_24h_usd: 143760.62
sources:
  - label: "ClearMarket market record: BTC trimmed mean price, August 31, 2026"
    url: "https://clearmarket.fyi/events/kxbtcmaxmon-btc-26aug31"
    retrieved_at: "2026-08-22T08:24:03+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Half the contract's lifetime volume printing in one session with nine days left signals desks are actively hedging or expressing directional BTC conviction into month-end.
