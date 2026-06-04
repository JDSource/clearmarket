---
signal_id: "CMSIG20260603VS02"
signal_slug: "us-x-iran-permanent-peace-deal-by-june-7-vol-642130"
headline: "US-Iran permanent peace by June 7: 29% on $642K"
semantic_title: "Traders target US-Iran peace by June 7 as a long shot"
telemetry: "29% · $642K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-03T01:46:55+00:00"
event_id: "CM-EVT-TQTJ2MLTV8"
event_slug: "us-x-iran-permanent-peace-deal-by"
event_question: "US x Iran permanent peace deal by May 31, 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x366f89649caea042c96ee741b185461ec7faa408a2664ec44469a0061924b537"
  question_raw: "US x Iran permanent peace deal by June 7, 2026?"
  current_price: 0.29
  volume_24h_usd: 642130.112547
  volume_cumulative_usd: 1669165.8192469946
  arbitration_model: "uma_oracle"
  resolves_at: "2026-06-07T00:00:00Z"
bullets:
  - "Polymarket at 29%, meaningful but minority probability of formal US-Iran deal within 4 days."
  - "$642K in 24h is 38% of all-time volume; fresh capital entering ahead of hard deadline."
  - "Diplomatic signals or back-channel reports likely driving attention into a tight 4-day window."
  - "Resolves June 7; failure to close by then collapses contract to zero."
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
      poly_vol_24h_usd: 642130.112547
sources:
  - label: "ClearMarket market record: US x Iran permanent peace deal by May 31, 2026?"
    url: "https://clearmarket.fyi/events/us-x-iran-permanent-peace-deal-by"
    retrieved_at: "2026-06-03T01:46:55+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Nearly 30% on a 4-day resolution window with a large volume surge signals live negotiation risk, macro and energy desks should treat this as a real near-term geopolitical optionality event.
