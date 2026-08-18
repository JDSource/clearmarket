---
signal_id: "CMSIG20260818VS06"
signal_slug: "will-catalina-lauf-be-the-republican-nom-vol-15122"
headline: "Lauf FL-19 GOP nom: 90% on $15K volume rise"
semantic_title: "Lauf FL-19 GOP nomination priced in at 90%"
telemetry: "90% · $15K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-18T08:31:22+00:00"
event_id: "CM-EVT-WPXJQDV350"
event_slug: "fl-19-republican-primary-winner"
event_question: "Will Ron DeSantis win the FL-19 Republican Primary?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xf43d99c0b796e0e5226dffa31c71c9fab943e3f79c0182c144eea93dc6b77ae2"
  question_raw: "Will Catalina Lauf be the Republican nominee for FL-19?"
  current_price: 0.9
  volume_24h_usd: 15122.697801
  volume_cumulative_usd: 58041.97335000001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-08-18T00:00:00Z"
bullets:
  - "Polymarket prices Lauf at 90%, strong favorite but 10% residual uncertainty remains unresolved."
  - "26% of all-time volume in 24h ($15K), contract's most active day, consistent with Florida primary day flow."
  - "Part of the broad Florida primary resolution wave across multiple congressional and statewide contracts."
  - "Resolves on certified Republican nominee for Florida's 19th congressional district."
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
      poly_vol_24h_usd: 15122.697801
sources:
  - label: "ClearMarket market record: Will Ron DeSantis win the FL-19 Republican Primary?"
    url: "https://clearmarket.fyi/events/fl-19-republican-primary-winner"
    retrieved_at: "2026-08-18T08:31:22+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 90% print with a record daily volume share indicates Lauf's nomination is near-consensus but not yet certified, desks should monitor the remaining 10% as a live risk until official canvassing results post.
