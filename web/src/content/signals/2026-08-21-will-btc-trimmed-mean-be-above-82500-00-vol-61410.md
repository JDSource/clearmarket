---
signal_id: "CMSIG20260821VS03"
signal_slug: "will-btc-trimmed-mean-be-above-82500-00-vol-61410"
headline: "BTC above $82.5K by Aug 31: 47% on $61K"
semantic_title: "BTC above $82.5K by Aug 31 sits at a coin-flip, 47%"
telemetry: "47% · $61K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-21T08:35:56+00:00"
event_id: "CM-EVT-91N8R2ZK22"
event_slug: "kxbtcmaxmon-btc-26aug31"
event_question: "BTC trimmed mean price, August 31, 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCMAXMON-BTC-26AUG31-8250000"
  question_raw: "Will BTC trimmed mean be above $82500.00 by 11:59 PM ET on Aug 31, 2026?"
  current_price: 0.47
  volume_24h_usd: 61410.52
  volume_cumulative_usd: 115627.47
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-09-08T03:59:59Z"
bullets:
  - "At 47%, the $82.5K strike is priced as essentially a coin-flip, the most uncertain of the August BTC ladder."
  - "24h volume of $61K is 53% of all-time, confirming meaningful fresh commitment despite the binary uncertainty."
  - "This strike marks the upper-bound stress test; combined with 67% at $80K, the curve implies limited upside conviction above $82K."
  - "Resolves trimmed-mean 11:59 PM ET Aug 31; any BTC rally in the next 10 days would sharply re-price this contract."
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
      kalshi_vol_24h_usd: 61410.52
sources:
  - label: "ClearMarket market record: BTC trimmed mean price, August 31, 2026"
    url: "https://clearmarket.fyi/events/kxbtcmaxmon-btc-26aug31"
    retrieved_at: "2026-08-21T08:35:56+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The near-50% print on the $82.5K strike is the most actionable signal in the BTC ladder, desks hedging or expressing upside views can find maximum two-sided liquidity here before month-end.
