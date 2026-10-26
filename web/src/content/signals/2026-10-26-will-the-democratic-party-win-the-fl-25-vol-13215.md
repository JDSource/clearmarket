---
signal_id: "CMSIG20261026VS06"
signal_slug: "will-the-democratic-party-win-the-fl-25-vol-13215"
headline: "Dems FL-25: 79% on $13K, 45% of all-time vol"
semantic_title: "Democrats favored at 79% to take FL-25 as volume surges"
telemetry: "79% · $13K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-26T14:48:56+00:00"
event_id: "CM-EVT-HQP7KZ8L31"
event_slug: "fl-25-house-election-winner"
event_question: "Will the Republican candidate win the FL-25 House election in 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x9da6028526359f1b342620308e871f8479844fb06d7c699dc478a165e39c594d"
  question_raw: "Will the Democratic Party win the FL-25 House seat?"
  current_price: 0.79
  volume_24h_usd: 13215.300598
  volume_cumulative_usd: 29640.173230999993
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "At 79%, the market prices Democrats as clear but not locked-in favorites in FL-25."
  - "45% of all-time volume cleared in one session alongside the Republican FL-25 contract."
  - "Paired with the GOP contract spike, both sides are seeing simultaneous re-pricing activity."
  - "Resolves on the 2026 FL-25 House general election result."
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
      poly_vol_24h_usd: 13215.300598
sources:
  - label: "ClearMarket market record: Will the Republican candidate win the FL-25 House elect"
    url: "https://clearmarket.fyi/events/fl-25-house-election-winner"
    retrieved_at: "2026-10-26T14:48:56+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The simultaneous FL-25 Democratic and Republican contract spikes point to a single catalyst, a poll, candidate announcement, or filing, repricing both sides of the same race at once.
