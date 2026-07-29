---
signal_id: "CMSIG20260729VS00"
signal_slug: "will-turkey-join-the-abraham-accords-bef-vol-158101"
headline: "Turkey Abraham Accords: 6% on $158K surge"
semantic_title: "Turkey joining Abraham Accords by 2027 stays a long shot"
telemetry: "6% · $158K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-29T10:36:04+00:00"
event_id: "CM-EVT-RDHKNVDMQ6"
event_slug: "which-country-will-join-abraham-accords-before-2027"
event_question: "Which country will join the Abraham Accords before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x6cc27a4a35f130c5481805387f567dcb79fec7284ddc4354db257f1bad86e183"
  question_raw: "Will Turkey join the Abraham Accords before 2027?"
  current_price: 0.065
  volume_24h_usd: 158101.20934600002
  volume_cumulative_usd: 463175.7374060004
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices Turkey-Abraham Accords by 2027 at just 6%, market treats it as a tail event."
  - "24h volume of $158K equals 34% of all-time handle, a sharp single-day concentration."
  - "Fresh attention likely tied to renewed Gulf-Turkey diplomatic signaling or back-channel reports."
  - "Contract resolves end-2026; current odds leave little room for a surprise breakthrough."
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
      poly_vol_24h_usd: 158101.20934600002
sources:
  - label: "ClearMarket market record: Which country will join the Abraham Accords before 2027"
    url: "https://clearmarket.fyi/events/which-country-will-join-abraham-accords-before-2027"
    retrieved_at: "2026-07-29T10:36:04+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The volume surge flags that desks are reassessing Turkey-Israel normalization as a live geopolitical tail risk worth pricing, even if consensus remains deeply skeptical.
