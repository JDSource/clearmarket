---
signal_id: "CMSIG20260820VS05"
signal_slug: "u-s-agrees-to-a-new-trade-deal-with-ca-vol-13493"
headline: "U.S.-Canada trade deal by 2027: 22% on $13K surge"
semantic_title: "Odds on a U.S.-Canada trade deal before 2027 stay low"
telemetry: "22% · $13K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-20T08:33:38+00:00"
event_id: "CM-EVT-RNYN7VH246"
event_slug: "which-countries-will-trump-make-new-trade-deals-with-before-2027-921"
event_question: "Will Trump make new trade deals with specific countries before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x81e8f9fd1c08c597b716ea800a97c6d04d60c985a2c388bc6d77a0f85e643df8"
  question_raw: "U.S. agrees to a new trade deal with \"Canada\" before 2027?"
  current_price: 0.22
  volume_24h_usd: 13493.108742
  volume_cumulative_usd: 17535.046599
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices 22%, market remains skeptical a formal deal closes before January 2027."
  - "24h volume $13K is 77% of all-time, nearly the entire contract's history traded in a single session."
  - "77% all-time share in one day flags a breaking diplomatic development or headline driving fresh attention."
  - "Resolves on deal announcement before January 1, 2027; roughly four months of window remain."
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
      poly_vol_24h_usd: 13493.108742
sources:
  - label: "ClearMarket market record: Will Trump make new trade deals with specific countries"
    url: "https://clearmarket.fyi/events/which-countries-will-trump-make-new-trade-deals-with-before-2027-921"
    retrieved_at: "2026-08-20T08:33:38+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

When 77% of a contract's lifetime volume lands in one day, a specific news catalyst is almost certainly driving it, desks covering Canadian trade exposure should treat this as an early-warning signal.
