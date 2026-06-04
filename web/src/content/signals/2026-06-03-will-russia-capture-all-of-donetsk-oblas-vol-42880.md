---
signal_id: "CMSIG20260603VS08"
signal_slug: "will-russia-capture-all-of-donetsk-oblas-vol-42880"
headline: "Russia captures all Donetsk by Dec 31: 5% on $43K"
semantic_title: "Traders write off Russia capturing all Donetsk by Dec 31"
telemetry: "5% · $43K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-03T01:46:55+00:00"
event_id: "CM-EVT-00P074X336"
event_slug: "will-russia-capture-all-of-donetsk-oblast-by"
event_question: "Will Russia capture all of Donetsk Oblast by June 30, 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xec4366aa6a191c8dc392e2b3bc874d5ce9a22637a60f33e72e869ce39c89ef4e"
  question_raw: "Will Russia capture all of Donetsk Oblast by December 31, 2026?"
  current_price: 0.046
  volume_24h_usd: 42880.027108
  volume_cumulative_usd: 48710.641048000005
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket at 5%, market assigns low but non-trivial probability of full Donetsk capture this year."
  - "$43K in 24h is 88% of all-time volume; contract newly active with concentrated single-session flow."
  - "Ceasefire or negotiation developments likely prompted contract creation and immediate positioning."
  - "Resolves December 31; full oblast capture requires substantial battlefield acceleration."
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
      poly_vol_24h_usd: 42880.027108
sources:
  - label: "ClearMarket market record: Will Russia capture all of Donetsk Oblast by June 30, 2"
    url: "https://clearmarket.fyi/events/will-russia-capture-all-of-donetsk-oblast-by"
    retrieved_at: "2026-06-03T01:46:55+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

88% of lifetime volume arriving in one session on a low-probability contract suggests a new catalyst, geopolitical and European energy desks should investigate what recent Ukraine-Russia development prompted this market's creation.
