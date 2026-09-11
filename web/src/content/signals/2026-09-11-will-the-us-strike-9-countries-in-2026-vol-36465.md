---
signal_id: "CMSIG20260911VS02"
signal_slug: "will-the-us-strike-9-countries-in-2026-vol-36465"
headline: "US 9-country strikes 2026: 28% on $36K"
semantic_title: "US striking 9 countries in 2026 stays a long shot at 28%"
telemetry: "28% · $36K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-11T12:33:13+00:00"
event_id: "CM-EVT-5855JBL478"
event_slug: "how-many-different-countries-will-the-us-strike-in-2026"
event_question: "Will the US conduct military action against more than one country in 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5759fb62768738cda38232974fa399fd8bfbbe6c04d891a2c4cdb71731f8f692"
  question_raw: "Will the US strike 9 countries in 2026?"
  current_price: 0.282
  volume_24h_usd: 36465.710307
  volume_cumulative_usd: 122504.793027
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket holds the '9-country strike' threshold at 28%, elevated tail-risk pricing, but still odds-against."
  - "30% of all-time volume traded in 24h, pointing to geopolitical news pulling fresh attention to the contract."
  - "On 9/11's anniversary, traders may be repricing broader US military engagement risk across active theaters."
  - "Contract resolves end of calendar year 2026 on verified strike count."
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
      poly_vol_24h_usd: 36465.710307
sources:
  - label: "ClearMarket market record: Will the US conduct military action against more than o"
    url: "https://clearmarket.fyi/events/how-many-different-countries-will-the-us-strike-in-2026"
    retrieved_at: "2026-09-11T12:33:13+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 28% print on a high-count strike threshold with a 9/11 anniversary volume spike is a flag for desks tracking defense and geopolitical risk premiums, watch for any new theater activation that could push the count closer to the threshold.
