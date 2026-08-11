---
signal_id: "CMSIG2026081002"
signal_slug: "june-fed-funds-upper-bound-seen-3-50-3-75-kalshi-2026-08-10"
headline: "June Fed funds upper bound seen 3.50-3.75%: Kalshi"
semantic_title: "Fed funds upper bound holds near 3.50-3.75% range"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-10T08:48:22.680Z"
event_id: "CM-EVT-4ZQLQPNH91"
event_slug: "kxfed-26sep"
event_question: "Federal funds rate upper bound"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26SEP-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Sep 16, 2026 meeting?"
  current_price: 0.44
  volume_24h_usd: 4835.36
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-09-23T18:05:00Z"
bullets:
  - "Kalshi ladder pins the federal funds upper bound in the 3.50-3.75% range: 98% above 3.50%, only 44% above 3.75%."
  - "Record S&P highs and weak July payrolls align with the distribution: the market is not pricing aggressive additional tightening."
  - "The sharp drop from 98% at 3.50% to 44% at 3.75% marks a clear resistance level the market assigns low probability to breaching."
  - "Polymarket's 60% on any 2026 hike (CM-EVT-87QV1G78C4) is consistent: one move possible but the terminal level likely stays at or below 3.75%."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "S&P 500 hit a record high after weak jobs data cooled rate-hike fears, with investors reassessing the Fed's policy path."
    publisher: "CommBank"
    published_at: "2026-08-10T08:48:22.680Z"
    source_url: "https://www.commbank.com.au/articles/newsroom/2026/08/wall-st-record-high-as-weak-jobs-data-eases-rate-fears.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "CommBank"
        source_url: "https://www.commbank.com.au/articles/newsroom/2026/08/wall-st-record-high-as-weak-jobs-data-eases-rate-fears.html"
        retrieved_at: "2026-08-11T08:49:29+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder; resolution source unspecified but tracks FOMC policy decisions; distribution implies a single additional hike is the outer bound of consensus."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "CommBank: S&P 500 hits record high as weak jobs data eases rate fears"
    url: "https://www.commbank.com.au/articles/newsroom/2026/08/wall-st-record-high-as-weak-jobs-data-eases-rate-fears.html"
    published_at: "2026-08-10T08:48:22.680Z"
    retrieved_at: "2026-08-11T08:49:29+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
