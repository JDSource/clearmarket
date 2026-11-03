---
signal_id: "CMSIG20261103VS07"
signal_slug: "will-the-democrats-win-the-minnesota-sen-vol-185153"
headline: "Minnesota Dem Senate: 92% on $185K volume"
semantic_title: "Minnesota Democrats hold the Senate seat with strong odds at 92%"
telemetry: "92% · $185K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-03T07:49:22+00:00"
event_id: "CM-EVT-3Z75P7P992"
event_slug: "minnesota-senate-election-winner"
event_question: "Will the Minnesota Senate election result in a winner by the scheduled election date?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x44b642636473fb07f0c2319a1d25729a36134969076ffdbb8979cbfdda612b14"
  question_raw: "Will the Democrats win the Minnesota Senate race in 2026?"
  current_price: 0.92
  volume_24h_usd: 185153.512306
  volume_cumulative_usd: 653339.8804
  arbitration_model: "uma_oracle"
bullets:
  - "Polymarket prices Democrats retaining the Minnesota Senate seat at 92%, near-certainty territory."
  - "28% of all-time volume in one session as Election Night closes out open positions on called races."
  - "At 92%, the market treats this as effectively settled; residual volume reflects final position unwinds."
  - "Resolves on certified 2026 Minnesota Senate results."
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
      poly_vol_24h_usd: 185153.512306
sources:
  - label: "ClearMarket market record: Will the Minnesota Senate election result in a winner b"
    url: "https://clearmarket.fyi/events/minnesota-senate-election-winner"
    retrieved_at: "2026-11-03T07:49:22+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Fresh capital flowing into a 92% contract on Election Day signals this race is being marked as resolved by the market, with volume representing position closeouts rather than active directional bets.
