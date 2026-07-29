---
signal_id: "CMSIG2026072903"
signal_slug: "fed-funds-upper-bound-implied-3-75-4-0-kalshi-ladder-2026-07-29"
headline: "Fed funds upper bound implied 3.75-4.0%: Kalshi ladder"
semantic_title: "Fed funds upper bound seen in the 3.75 to 4.0 percent range"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-29T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Fed funds rate upper bound"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.36
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder prices the Fed funds upper bound in the 3.75-4.0% range: 91% above 3.50%, 71% above 3.75%, but only 36% above 4.0%."
  - "The AP hold-expected story aligns with the ladder's steep cliff between 3.75% and 4.0%, showing markets see 4.0% as a stretch near-term."
  - "A companion ladder (CM-EVT-PHWX2H6DM5) prices 99% above 3.50% but only 23% above 3.75%, suggesting some disagreement across contracts on whether 3.75% is already in or still a risk."
  - "Resolves via Federal Reserve Economic Data; the gap between the two ladders may reflect different settlement horizons rather than conflicting views."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The AP reports the Fed is expected to hold rates unchanged at its July meeting despite policymaker frustration with persistent inflation."
    publisher: "apnews.com"
    published_at: "2026-07-29T00:00:00.000Z"
    source_url: "https://apnews.com/article/federal-reserve-inflation-interest-rates-iran-war-ad10c177cb8d96f9e3ed122e12352a74"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "apnews.com"
        source_url: "https://apnews.com/article/federal-reserve-inflation-interest-rates-iran-war-ad10c177cb8d96f9e3ed122e12352a74"
        retrieved_at: "2026-07-29T10:35:12+00:00"
  - type: "pm_response"
    notes: "Two Kalshi-sourced ladders cover this metric with slightly different implied ranges, likely reflecting different settlement dates."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "apnews.com: Despite frustration over high prices, Federal Reserve is expected to k"
    url: "https://apnews.com/article/federal-reserve-inflation-interest-rates-iran-war-ad10c177cb8d96f9e3ed122e12352a74"
    published_at: "2026-07-29T00:00:00.000Z"
    retrieved_at: "2026-07-29T10:35:12+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
