---
signal_id: "CMSIG20260822VS05"
signal_slug: "will-xrp-trimmed-mean-be-above-1-60-by-vol-21809"
headline: "XRP above $1.60 by Aug 31: 99% on $22K"
semantic_title: "XRP above $1.60 by Aug 31 is a near-certain bet"
telemetry: "99% · $22K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-22T08:24:03+00:00"
event_id: "CM-EVT-SL8FQN9Q73"
event_slug: "kxxrpmaxmon-xrp-26aug31"
event_question: "XRP trimmed mean price, August 31, 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXXRPMAXMON-XRP-26AUG31-160"
  question_raw: "Will XRP trimmed mean be above $1.60 by 11:59 PM ET on Aug 31, 2026?"
  current_price: 0.99
  volume_24h_usd: 21809.9
  volume_cumulative_usd: 37220.48
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-09-08T03:59:59Z"
bullets:
  - "Kalshi prices 99%, market treats this threshold as already cleared with nine days left."
  - "24h volume $22K is 59% of all-time, large for a contract priced at virtual certainty."
  - "Late-contract volume at 99% likely reflects traders collecting remaining premium or closing hedges."
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
      kalshi_vol_24h_usd: 21809.9
sources:
  - label: "ClearMarket market record: XRP trimmed mean price, August 31, 2026"
    url: "https://clearmarket.fyi/events/kxxrpmaxmon-xrp-26aug31"
    retrieved_at: "2026-08-22T08:24:03+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

High volume on a near-certain contract signals position-closing or premium harvesting activity, desks should note XRP is firmly above $1.60 and look to the $1.70 contract for live price discovery.
