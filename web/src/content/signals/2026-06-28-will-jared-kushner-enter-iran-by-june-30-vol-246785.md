---
signal_id: "CMSIG20260628VS03"
signal_slug: "will-jared-kushner-enter-iran-by-june-30-vol-246785"
headline: "Kushner enters Iran: 0% on $247K volume"
semantic_title: "Traders defend the zero on Kushner entering Iran by June 30"
telemetry: "0% · $247K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-28T10:25:52+00:00"
event_id: "CM-EVT-QF15YF74T9"
event_slug: "who-will-enter-iran-by-june-30"
event_question: "Will someone enter Iran by June 30?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x9c9c61a05eb70ddd796283b86db07efd0c07a4d29b48870987f1c8279217f783"
  question_raw: "Will Jared Kushner enter Iran by June 30?"
  current_price: 0.001
  volume_24h_usd: 246785.82966500003
  volume_cumulative_usd: 871875.1720080001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-06-30T00:00:00Z"
bullets:
  - "Polymarket holds Kushner entering Iran at 0% probability before June 30 deadline."
  - "$247K in 24h is 28% of all-time volume, meaningful flow into a contract priced at zero."
  - "Back-channel Iran diplomacy reports may be triggering speculative buying; sellers are absorbing all comers."
  - "Resolves June 30; zero price implies consensus that any Kushner Iran visit remains beyond near-term horizon."
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
      poly_vol_24h_usd: 246785.82966500003
sources:
  - label: "ClearMarket market record: Will someone enter Iran by June 30?"
    url: "https://clearmarket.fyi/events/who-will-enter-iran-by-june-30"
    retrieved_at: "2026-06-28T10:25:52+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Sustained inflow into a zero-priced contract 48 hours from expiry suggests speculative actors chasing a diplomatic surprise scenario, desks should note the volume as a sentiment indicator on U.S., Iran back-channel rumors rather than a credible probability shift.
