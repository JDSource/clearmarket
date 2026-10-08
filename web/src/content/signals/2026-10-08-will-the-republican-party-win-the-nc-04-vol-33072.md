---
signal_id: "CMSIG20261008VS01"
signal_slug: "will-the-republican-party-win-the-nc-04-vol-33072"
headline: "NC-04 GOP win: 5% on $33K volume surge"
semantic_title: "NC-04 Republican odds hold near the floor on fresh volume"
telemetry: "5% · $33K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-08T07:49:04+00:00"
event_id: "CM-EVT-NWW6JR41T9"
event_slug: "nc-04-house-election-winner"
event_question: "NC-04 House Election Winner"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xe29af21f8c8b4646f0d9b771193ab99a2a75a3ae8b360c138f8fad1acdd12cf2"
  question_raw: "Will the Republican Party win the NC-04 House seat?"
  current_price: 0.047
  volume_24h_usd: 33072.620834
  volume_cumulative_usd: 67446.06262499999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices a Republican win at 5%, reflecting NC-04 as a strong Democratic district with minimal GOP path."
  - "49% of all-time volume, $33K, traded in 24 hours, marking a notable attention spike."
  - "Fresh activity at depressed odds suggests the market is stress-testing the Democratic lean rather than pricing a shift."
  - "Resolves on NC-04 House race result; 5% leaves a small but nonzero tail risk priced."
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
      poly_vol_24h_usd: 33072.620834
sources:
  - label: "ClearMarket market record: NC-04 House Election Winner"
    url: "https://clearmarket.fyi/events/nc-04-house-election-winner"
    retrieved_at: "2026-10-08T07:49:04+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 49% all-time volume share at 5% odds tells desks that NC-04 is being actively confirmed as safe Democratic territory in seat-count models, with no evidence of an emerging competitive race.
