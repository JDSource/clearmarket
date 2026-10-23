---
signal_id: "CMSIG20261023VS00"
signal_slug: "will-marion-mar-chal-win-the-2027-french-vol-371000"
headline: "Maréchal French presidency: 0% on $371K surge"
semantic_title: "Maréchal 2027 stays a no-go at zero odds"
telemetry: "0% · $371K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-23T07:49:03+00:00"
event_id: "CM-EVT-GD1GGR4710"
event_slug: "next-french-presidential-election"
event_question: "Will a new French president be elected in the next French Presidential Election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xf9f40504425133cce159883ca3eaf376a815ab1ae763086ae8e4a3f5eacea479"
  question_raw: "Will Marion Maréchal win the 2027 French presidential election?"
  current_price: 0.001
  volume_24h_usd: 371000.0
  volume_cumulative_usd: 872673.103
  arbitration_model: "uma_oracle"
  resolves_at: "2027-04-30T00:00:00Z"
bullets:
  - "Price sits at 0%, polymarket traders see no viable path to the Élysée for Maréchal."
  - "24h volume of $371K equals 43% of all-time handle, a massive single-session spike."
  - "Fresh attention likely tied to French right-wing coalition chatter or polling developments in early 2027 race coverage."
  - "Resolves on 2027 French presidential election result."
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
      poly_vol_24h_usd: 371000.0
sources:
  - label: "ClearMarket market record: Will a new French president be elected in the next Fren"
    url: "https://clearmarket.fyi/events/next-french-presidential-election"
    retrieved_at: "2026-10-23T07:49:03+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A market priced at zero drawing 43% of its lifetime volume in one day signals a desk-relevant political event in France, traders are not buying the odds but the activity itself warrants monitoring for sentiment shifts.
