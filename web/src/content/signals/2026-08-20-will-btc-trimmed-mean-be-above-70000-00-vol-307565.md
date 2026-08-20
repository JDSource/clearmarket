---
signal_id: "CMSIG20260820VS00"
signal_slug: "will-btc-trimmed-mean-be-above-70000-00-vol-307565"
headline: "BTC $70K by Aug 31: 90% on $308K surge"
semantic_title: "BTC above $70K by Aug 31 stays a heavy favorite"
telemetry: "90% · $308K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-20T08:33:38+00:00"
event_id: "CM-EVT-91N8R2ZK22"
event_slug: "kxbtcmaxmon-btc-26aug31"
event_question: "BTC trimmed mean price, August 31, 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCMAXMON-BTC-26AUG31-7000000"
  question_raw: "Will BTC trimmed mean be above $70000.00 by 11:59 PM ET on Aug 31, 2026?"
  current_price: 0.9
  volume_24h_usd: 307565.84
  volume_cumulative_usd: 599695.3
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-09-08T03:59:59Z"
bullets:
  - "Kalshi prices 90% odds, market treats $70K floor as near-certain through month-end."
  - "24h volume $308K equals 51% of all-time handle, signaling a decisive fresh-money rush."
  - "Surge implies traders are locking in the near-term floor thesis ahead of August close."
  - "Resolves 11:59 PM ET Aug 31, 2026, 11 days of runway remain."
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
      kalshi_vol_24h_usd: 307565.84
sources:
  - label: "ClearMarket market record: BTC trimmed mean price, August 31, 2026"
    url: "https://clearmarket.fyi/events/kxbtcmaxmon-btc-26aug31"
    retrieved_at: "2026-08-20T08:33:38+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Half the contract's lifetime volume printing in a single day at 90% odds suggests a desk is either hedging a short or aggressively confirming a BTC floor position ahead of month-end.
