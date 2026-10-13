---
signal_id: "CMSIG20261013VS01"
signal_slug: "will-democratic-win-the-house-race-for-m-vol-49592"
headline: "MN-05 Democrat: 91% on $50K volume burst"
semantic_title: "Heavy trading tests the MN-05 Democratic hold near 91%"
telemetry: "91% · $50K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-13T15:33:23+00:00"
event_id: "CM-EVT-1F7LPV1P19"
event_slug: "kxhouserace-mn05-26"
event_question: "MN-05 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-MN05-26-D"
  question_raw: "Will Democratic win the House race for MN-05?"
  current_price: 0.912
  volume_24h_usd: 49592.47
  volume_cumulative_usd: 63249.05
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "Kalshi prices Democrats at 91% in MN-05, near-certainty, with slim but priced tail risk."
  - "$49.6K in 24h volume represents 78% of the contract's entire all-time flow, an extraordinary concentration."
  - "Late-cycle volume at extreme odds often reflects hedgers or arbitrageurs rather than genuine outcome uncertainty."
  - "Resolves on the November 2026 House election."
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
      kalshi_vol_24h_usd: 49592.47
sources:
  - label: "ClearMarket market record: MN-05 House winner?"
    url: "https://clearmarket.fyi/events/kxhouserace-mn05-26"
    retrieved_at: "2026-10-13T15:33:23+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With 78% of lifetime volume arriving in a single session at 91%, a desk should treat this as a liquidity/arb event rather than a signal of shifting fundamentals in a safe Democratic seat.
