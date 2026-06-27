---
signal_id: "CMSIG20260627VS00"
signal_slug: "will-jared-kushner-enter-iran-by-june-30-vol-417342"
headline: "Kushner Iran entry: 0% on $417K surge"
semantic_title: "Traders write off Kushner entering Iran by June 30"
telemetry: "0% · $417K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-27T01:36:27+00:00"
event_id: "CM-EVT-QF15YF74T9"
event_slug: "who-will-enter-iran-by-june-30"
event_question: "Will someone enter Iran by June 30?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x9c9c61a05eb70ddd796283b86db07efd0c07a4d29b48870987f1c8279217f783"
  question_raw: "Will Jared Kushner enter Iran by June 30?"
  current_price: 0.001
  volume_24h_usd: 417342.1
  volume_cumulative_usd: 624813.828343
  arbitration_model: "uma_oracle"
  resolves_at: "2026-06-30T00:00:00Z"
bullets:
  - "Market prices zero probability, no credible pathway seen before June 30."
  - "$417K traded in 24h, equal to 67% of the contract's entire all-time volume."
  - "Three days to deadline; late capital flooding in to lock in the 'No' at zero cost."
  - "Resolves June 30, sellers absorbing any residual speculative long interest."
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
      poly_vol_24h_usd: 417342.1
sources:
  - label: "ClearMarket market record: Will someone enter Iran by June 30?"
    url: "https://clearmarket.fyi/events/who-will-enter-iran-by-june-30"
    retrieved_at: "2026-06-27T01:36:27+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should read this as terminal settlement activity: the market is resolved in all but name, and the volume surge reflects traders harvesting near-certain 'No' positions before expiry.
