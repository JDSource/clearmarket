---
signal_id: "CMSIG20260824VS00"
signal_slug: "will-russia-capture-havrylivka-by-decemb-vol-18465"
headline: "Havrylivka capture: 6% on $18K volume surge"
semantic_title: "Havrylivka capture by Dec 31 stays a long shot at 6%"
telemetry: "6% · $18K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-24T08:42:36+00:00"
event_id: "CM-EVT-RYR4XV6NT4"
event_slug: "will-russia-capture-havrylivka-by-february-28"
event_question: "Will Russia capture Havrylivka in 2026? (monthly series)"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xca63577f886917a299e60c25626641e06f74885b2bb848d67c0915551a05cc5b"
  question_raw: "Will Russia capture Havrylivka by December 31, 2026?"
  current_price: 0.06
  volume_24h_usd: 18465.0
  volume_cumulative_usd: 22307.022348000002
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Market prices Russian capture of Havrylivka by year-end at just 6%, signaling deep skepticism."
  - "24h volume of $18,465 equals 83% of all-time traded value, nearly the entire contract history in one session."
  - "Sudden attention likely tied to fresh frontline reporting or Ukrainian/Russian operational updates near the village."
  - "Resolves December 31, 2026; current odds leave little room for a bullish Russia-advance case."
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
      poly_vol_24h_usd: 18465.0
sources:
  - label: "ClearMarket market record: Will Russia capture Havrylivka in 2026? (monthly series"
    url: "https://clearmarket.fyi/events/will-russia-capture-havrylivka-by-february-28"
    retrieved_at: "2026-08-24T08:42:36+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A near-total repricing of the contract's lifetime liquidity in 24 hours at unchanged low odds signals a sharp catalyst, likely new battlefield dispatches, that desks should cross-reference against Donetsk frontline intelligence before dismissing as noise.
