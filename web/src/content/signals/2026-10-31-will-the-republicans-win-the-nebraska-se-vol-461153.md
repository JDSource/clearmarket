---
signal_id: "CMSIG20261031VS03"
signal_slug: "will-the-republicans-win-the-nebraska-se-vol-461153"
headline: "Nebraska Senate GOP: 76% on $461K Polymarket surge"
semantic_title: "Traders pile into Nebraska GOP Senate line at 76%"
telemetry: "76% · $461K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-31T14:16:49+00:00"
event_id: "CM-EVT-CY3W5Z2793"
event_slug: "nebraska-senate-election-winner"
event_question: "Nebraska Senate Election Winner  "
primary_market:
  platform: "polymarket"
  platform_market_id: "0x71e9f5312aac62bdc9b87fa8d171fa929eca6243d815298c4c7d61303f7d53dd"
  question_raw: "Will the Republicans win the Nebraska Senate race in 2026?"
  current_price: 0.76
  volume_24h_usd: 461153.02531400014
  volume_cumulative_usd: 1141558.685218
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices Nebraska Republican Senate win at 76%, near-identical to the Kalshi read."
  - "$461K in 24h is 40% of the contract's all-time volume, the highest all-time share in this cluster."
  - "Cross-venue price alignment at 75-76% signals a stable consensus under heavy two-platform flow."
  - "Resolves on Nebraska 2026 Senate race; independent candidate viability is the swing variable."
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
      poly_vol_24h_usd: 461153.02531400014
sources:
  - label: "ClearMarket market record: Nebraska Senate Election Winner  "
    url: "https://clearmarket.fyi/events/nebraska-senate-election-winner"
    retrieved_at: "2026-10-31T14:16:49+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With 40% of all-time volume printing in one day and cross-venue consensus locked at 75-76%, a desk should treat any gap between Kalshi and Polymarket prices as a short-lived arbitrage rather than a genuine disagreement.
