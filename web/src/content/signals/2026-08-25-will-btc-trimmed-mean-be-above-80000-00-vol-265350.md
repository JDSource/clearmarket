---
signal_id: "CMSIG20260825VS00"
signal_slug: "will-btc-trimmed-mean-be-above-80000-00-vol-265350"
headline: "BTC $80K floor: 99% on $265K surge"
semantic_title: "BTC above $80K by Aug 31 draws near-certain odds"
telemetry: "99% · $265K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-25T08:37:37+00:00"
event_id: "CM-EVT-91N8R2ZK22"
event_slug: "kxbtcmaxmon-btc-26aug31"
event_question: "BTC trimmed mean price, August 31, 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCMAXMON-BTC-26AUG31-8000000"
  question_raw: "Will BTC trimmed mean be above $80000.00 by 11:59 PM ET on Aug 31, 2026?"
  current_price: 0.99
  volume_24h_usd: 265350.99
  volume_cumulative_usd: 805258.61
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-09-08T03:59:59Z"
bullets:
  - "Kalshi prices near-certainty (99%) that BTC trimmed mean stays above $80K through Aug 31."
  - "24h volume of $265K equals 33% of all-time, a heavy single-day commitment in a shallow book."
  - "With six days to expiry, fresh capital is pressing into a bet that has almost no room left to move."
  - "Resolves 11:59 PM ET Aug 31, 2026; near-zero implied miss risk leaves almost all value in theta decay."
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
      kalshi_vol_24h_usd: 265350.99
sources:
  - label: "ClearMarket market record: BTC trimmed mean price, August 31, 2026"
    url: "https://clearmarket.fyi/events/kxbtcmaxmon-btc-26aug31"
    retrieved_at: "2026-08-25T08:37:37+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The surge into a 99% contract signals desks are harvesting residual premium on a near-certain near-term outcome, worth watching for any late shock that could reprice the tail.
