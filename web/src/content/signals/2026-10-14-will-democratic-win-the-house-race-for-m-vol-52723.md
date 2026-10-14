---
signal_id: "CMSIG20261014VS01"
signal_slug: "will-democratic-win-the-house-race-for-m-vol-52723"
headline: "Dem MN-05 House win: 92% on $52K volume spike"
semantic_title: "Democrats heavily favored in MN-05 as fresh volume piles in"
telemetry: "92% · $53K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-14T13:17:59+00:00"
event_id: "CM-EVT-1F7LPV1P19"
event_slug: "kxhouserace-mn05-26"
event_question: "MN-05 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-MN05-26-D"
  question_raw: "Will Democratic win the House race for MN-05?"
  current_price: 0.915
  volume_24h_usd: 52723.54
  volume_cumulative_usd: 104225.2
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "Kalshi prices 92%, market treats a Democratic hold in this Minneapolis seat as near-certain."
  - "$52K in 24h represents 51% of all-time volume, a meaningful mid-cycle liquidity event."
  - "Fresh capital at high odds implies either arbitrage hunting or a specific local development drawing attention."
  - "Resolution on 2026 midterm election night."
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
      kalshi_vol_24h_usd: 52723.54
sources:
  - label: "ClearMarket market record: MN-05 House winner?"
    url: "https://clearmarket.fyi/events/kxhouserace-mn05-26"
    retrieved_at: "2026-10-14T13:17:59+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Heavy volume at 92% in a safe Democratic seat points to yield-seeking capital or a local news catalyst; a desk should monitor for any candidate-level disruption that could crack the price.
