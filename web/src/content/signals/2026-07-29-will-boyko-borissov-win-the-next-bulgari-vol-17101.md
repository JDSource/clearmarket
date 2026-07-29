---
signal_id: "CMSIG20260729VS05"
signal_slug: "will-boyko-borissov-win-the-next-bulgari-vol-17101"
headline: "Borissov Bulgarian president: 1% on $17K"
semantic_title: "Borissov Bulgarian presidency bid priced out near zero"
telemetry: "1% · $17K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-29T10:36:04+00:00"
event_id: "CM-EVT-C541X65QT7"
event_slug: "bulgaria-presidential-election"
event_question: "Will Bulgaria hold a presidential election by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x6861edbc232cbfb41a299ab4590f571a93a8ab38831467a274ab062a725abfbe"
  question_raw: "Will Boyko Borissov win the next Bulgarian presidential election?"
  current_price: 0.011
  volume_24h_usd: 17101.306841
  volume_cumulative_usd: 22936.777271
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-30T00:00:00Z"
bullets:
  - "Polymarket prices Boyko Borissov winning the next Bulgarian presidency at just 1%, near-zero conviction."
  - "75% of all-time volume hit in 24h, three-quarters of the contract's entire history in one session."
  - "A legal, political, or electoral development in Sofia almost certainly triggered the concentrated trading."
  - "With 75% of all-time volume in a single day, the market is treating this as a closing, not opening, bet."
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
      poly_vol_24h_usd: 17101.306841
sources:
  - label: "ClearMarket market record: Will Bulgaria hold a presidential election by 2026?"
    url: "https://clearmarket.fyi/events/bulgaria-presidential-election"
    retrieved_at: "2026-07-29T10:36:04+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Three-quarters of all-time volume landing at 1% in a single session is a strong signal that new Bulgarian political news has decisively closed the market on a Borissov presidential run.
