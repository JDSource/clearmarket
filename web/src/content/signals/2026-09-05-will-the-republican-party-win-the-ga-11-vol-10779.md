---
signal_id: "CMSIG20260905VS03"
signal_slug: "will-the-republican-party-win-the-ga-11-vol-10779"
headline: "GOP wins GA-11 House seat: 95% on $10K volume surge"
semantic_title: "Republican lock on GA-11 holds through a volume surge at 95%"
telemetry: "95% · $11K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-05T11:35:07+00:00"
event_id: "CM-EVT-Q69VMQDDC9"
event_slug: "ga-11-house-election-winner"
event_question: "Will the GA-11 House election be won by a Republican candidate in 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x707dd8bd283b72a13ec9cf79b18b6238744a9250a8e5e18d9cab9dbbe55db8b2"
  question_raw: "Will the Republican Party win the GA-11 House seat?"
  current_price: 0.95
  volume_24h_usd: 10779.97262
  volume_cumulative_usd: 30468.538513999996
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices a Republican win in Georgia's 11th district at 95%, near-certain, with minimal residual risk priced in."
  - "24h volume of $10.8K is 35% of all-time flow, a significant single-session share for a safe-seat contract."
  - "GA-11 is a heavily Republican district; unusual volume at this late stage may reflect either late arbitrage or an attempt to test whether any opposing scenario is being priced."
  - "Resolves on the certified winner of the GA-11 general election."
atomic_claims:
  - type: "volume_anomaly"
    provenance: "24h + cumulative volume direct from polymarket API; intensity = 24h/cumulative (derived)"
    field_provenance:
      volume_24h_usd:
        tier: "direct"
        method: "polymarket_api"
      intensity:
        tier: "derived"
        method: "arithmetic"
        inputs: ["volume_24h_usd", "volume_cumulative_usd"]
    liquidity_context:
      poly_vol_24h_usd: 10779.97262
sources:
  - label: "ClearMarket market record: Will the GA-11 House election be won by a Republican ca"
    url: "https://clearmarket.fyi/events/ga-11-house-election-winner"
    retrieved_at: "2026-09-05T11:35:07+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Heavy volume on a 95%-priced safe-seat contract is an arbitrage signal, desks probing for mispricing or closing out opposing positions rather than expressing new directional conviction.
