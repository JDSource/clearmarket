---
signal_id: "CMSIG20260822VS06"
signal_slug: "will-xrp-trimmed-mean-be-above-1-70-by-vol-12349"
headline: "XRP above $1.70 by Aug 31: 84% on $12K"
semantic_title: "Buyers back XRP clearing $1.70 by Aug 31 at heavy odds"
telemetry: "84% · $12K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-22T08:24:03+00:00"
event_id: "CM-EVT-SL8FQN9Q73"
event_slug: "kxxrpmaxmon-xrp-26aug31"
event_question: "XRP trimmed mean price, August 31, 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXXRPMAXMON-XRP-26AUG31-170"
  question_raw: "Will XRP trimmed mean be above $1.70 by 11:59 PM ET on Aug 31, 2026?"
  current_price: 0.84
  volume_24h_usd: 12349.51
  volume_cumulative_usd: 16800.42
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-09-08T03:59:59Z"
bullets:
  - "Kalshi prices 84%, strong conviction XRP stays above $1.70 through month-end."
  - "24h volume $12K is 74% of all-time, the dominant session in this contract's history."
  - "With $1.60 at 99%, the $1.70 contract is the active price-discovery layer for XRP near-term."
  - "Resolves 11:59 PM ET Aug 31 on trimmed-mean XRP price."
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
      kalshi_vol_24h_usd: 12349.51
sources:
  - label: "ClearMarket market record: XRP trimmed mean price, August 31, 2026"
    url: "https://clearmarket.fyi/events/kxxrpmaxmon-xrp-26aug31"
    retrieved_at: "2026-08-22T08:24:03+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The bulk of XRP contract lifetime volume arriving at 84% with nine days to go positions this as the key live risk level, a move below $1.70 would reprice this contract rapidly.
