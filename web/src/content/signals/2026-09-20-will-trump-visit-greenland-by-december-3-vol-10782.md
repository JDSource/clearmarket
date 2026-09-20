---
signal_id: "CMSIG20260920VS05"
signal_slug: "will-trump-visit-greenland-by-december-3-vol-10782"
headline: "Trump Greenland visit: 16% on $11K inflow"
semantic_title: "A Trump visit to Greenland by Dec 31 stays unlikely at 16%"
telemetry: "16% · $11K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-20T07:47:56+00:00"
event_id: "CM-EVT-3TR9YVM622"
event_slug: "will-trump-visit-greenland-by-march-31"
event_question: "Will Trump visit Greenland by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x840fe2606472a13ee62e3009a360af8be2576cd1d9dbcda8749e89eed5d02a98"
  question_raw: "Will Trump visit Greenland by December 31?"
  current_price: 0.16
  volume_24h_usd: 10782.137966
  volume_cumulative_usd: 38804.952173000005
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "16% odds sharply discount a physical Trump visit to Greenland even as a deal nears 96%."
  - "$11K in 24h is 28% of all-time volume, elevated relative to contract size."
  - "The visit/deal spread (16% vs. 96%) tells the market a deal can close without a presidential trip."
  - "Resolves Dec 31; a confirmed travel schedule would be a major repricing catalyst."
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
      poly_vol_24h_usd: 10782.137966
sources:
  - label: "ClearMarket market record: Will Trump visit Greenland by 2026?"
    url: "https://clearmarket.fyi/events/will-trump-visit-greenland-by-march-31"
    retrieved_at: "2026-09-20T07:47:56+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 80-point gap between the deal contract at 96% and the visit contract at 16% is the actionable signal, a desk should monitor whether a confirmed Trump itinerary collapses that spread rapidly.
