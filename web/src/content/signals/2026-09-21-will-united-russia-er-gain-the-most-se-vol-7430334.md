---
signal_id: "CMSIG20260921VS00"
signal_slug: "will-united-russia-er-gain-the-most-se-vol-7430334"
headline: "United Russia Duma lead: 100% on $7.4M surge"
semantic_title: "United Russia holds the Duma at near-certainty"
telemetry: "100% · $7.4M 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-21T07:48:00+00:00"
event_id: "CM-EVT-XS1TS19GP7"
event_slug: "which-party-will-gain-most-seats-in-russian-parliamentary-election"
event_question: "Which party will gain the most seats in the Russian Parliamentary Election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x502a94e5c525766d5ee7f16c6568131ba1b2cbadb69c703af05a6ef00336ed64"
  question_raw: "Will United Russia (ER) gain the most seats in the next Russian parliamentary election?"
  current_price: 0.996
  volume_24h_usd: 7430334.077882989
  volume_cumulative_usd: 23758117.797354992
  arbitration_model: "uma_oracle"
  resolves_at: "2026-09-30T00:00:00Z"
bullets:
  - "Polymarket prices United Russia at 100% to win the most seats, outcome treated as resolved."
  - "24h volume of $7.4M represents 31% of all-time volume, a major single-session commitment."
  - "Surge likely tied to election cycle confirmation or official results entering the market window."
  - "Contract resolves on next Russian parliamentary election seat totals."
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
      poly_vol_24h_usd: 7430334.077882989
sources:
  - label: "ClearMarket market record: Which party will gain the most seats in the Russian Par"
    url: "https://clearmarket.fyi/events/which-party-will-gain-most-seats-in-russian-parliamentary-election"
    retrieved_at: "2026-09-21T07:48:00+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should read this as the market fully closing out any residual uncertainty on Duma composition, the volume flush signals position settlement, not price discovery.
