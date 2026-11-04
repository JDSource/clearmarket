---
signal_id: "CMSIG20261104VS05"
signal_slug: "will-the-democrats-win-the-maine-senate-vol-1565635"
headline: "ME Senate Dem: 100% on $1.6M Polymarket surge"
semantic_title: "Betting picks up on Democrats holding the Maine Senate seat"
telemetry: "100% · $1.6M 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-04T07:48:42+00:00"
event_id: "CM-EVT-7YMVN17NP0"
event_slug: "maine-senate-election-winner"
event_question: "Will the winner of the Maine Senate election be determined by the settlement date?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x66bbf6d55e0296278858b3147689f3df9259374f158f9f028b608baa322a639c"
  question_raw: "Will the Democrats win the Maine Senate race in 2026?"
  current_price: 0.999
  volume_24h_usd: 1565635.6468580002
  volume_cumulative_usd: 3495618.114
  arbitration_model: "uma_oracle"
bullets:
  - "Polymarket prices Democratic Maine Senate win at 100%, market sees no path for a GOP pickup."
  - "45% of all-time volume cleared in 24h, a substantial late concentration of activity."
  - "Maine was watched for independent/crossover risk; ceiling price confirms that scenario has collapsed."
  - "Resolves on certified Maine 2026 Senate result."
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
      poly_vol_24h_usd: 1565635.6468580002
sources:
  - label: "ClearMarket market record: Will the winner of the Maine Senate election be determi"
    url: "https://clearmarket.fyi/events/maine-senate-election-winner"
    retrieved_at: "2026-11-04T07:48:42+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Volume at 45% of lifetime with a ceiling price tells desks Maine is off the competitive board; the flow likely represents final settlement trades and position closures.
