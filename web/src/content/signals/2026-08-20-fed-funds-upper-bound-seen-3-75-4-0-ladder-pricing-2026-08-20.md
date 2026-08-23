---
signal_id: "CMSIG2026082001"
signal_slug: "fed-funds-upper-bound-seen-3-75-4-0-ladder-pricing-2026-08-20"
headline: "Fed funds upper bound seen 3.75-4.0%: ladder pricing"
semantic_title: "Fed rate hike by year-end stays a minority bet"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-20T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds upper bound, post-2026 meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.17
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Ladder pricing puts the Fed funds upper bound in the 3.75-4.0% range: 55% above 3.75% but only 17% above 4.0%."
  - "Fed minutes flagged three governors favoring a hike, but the distribution shows markets treating a full hike beyond 4.0% as a tail event."
  - "The Polymarket contract on a Fed rate hike in 2026 sits at 55%, meaning the broader market is nearly split on whether any hike materializes."
  - "A companion ladder (CM-EVT-4ZQLQPNH91) implies a lower bound near 3.5-3.75%, suggesting a near-term meeting may hold while a later one moves; the spread reveals timeline uncertainty."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Fed minutes showed three officials favored a 25-basis-point hike, sparking a debate about whether the hiking cycle has resumed."
    publisher: "ANI"
    published_at: "2026-08-20T00:00:00.000Z"
    source_url: "https://www.thehindubusinessline.com/news/world/us-fed-minutes-signal-rate-hike-debate-as-inflation-risks-persist-3-officials-favoured-25-bps-increase/article71368240.ece"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "ANI"
        source_url: "https://www.thehindubusinessline.com/news/world/us-fed-minutes-signal-rate-hike-debate-as-inflation-risks-persist-3-officials-favoured-25-bps-increase/article71368240.ece"
        retrieved_at: "2026-08-23T08:24:02+00:00"
  - type: "pm_response"
    notes: "Ladder data via resolution source FRED; the 3.75% strike at 55% is the median pivot point across the distribution."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "ANI: US Fed Minutes signal rate hike debate as inflation risks persist; 3 o"
    url: "https://www.thehindubusinessline.com/news/world/us-fed-minutes-signal-rate-hike-debate-as-inflation-risks-persist-3-officials-favoured-25-bps-increase/article71368240.ece"
    published_at: "2026-08-20T00:00:00.000Z"
    retrieved_at: "2026-08-23T08:24:02+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
