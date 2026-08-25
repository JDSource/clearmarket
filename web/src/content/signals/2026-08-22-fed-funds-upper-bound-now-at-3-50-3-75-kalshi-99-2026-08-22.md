---
signal_id: "CMSIG2026082202"
signal_slug: "fed-funds-upper-bound-now-at-3-50-3-75-kalshi-99-2026-08-22"
headline: "Fed funds upper bound now at 3.50-3.75%: Kalshi 99%"
semantic_title: "Current Fed funds rate holds near 3.5 to 3.75 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-22T00:00:00.000Z"
event_id: "CM-EVT-4ZQLQPNH91"
event_slug: "kxfed-26sep"
event_question: "Current Fed funds upper bound"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26SEP-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Sep 16, 2026 meeting?"
  current_price: 0.35
  volume_24h_usd: 765.32
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-09-23T18:05:00Z"
bullets:
  - "Kalshi ladder prices the current Fed funds upper bound firmly in the 3.50-3.75% range: 99% above 3.50%, only 35% above 3.75%."
  - "Officials eyeing higher rates aligns with current pricing, the market acknowledges the hawkish tilt but does not yet price a completed hike."
  - "Falling unemployment claims remove one argument for near-term cuts, keeping the rate pinned at the current range with little downside pressure priced."
  - "Resolves via Federal Reserve official rate announcement; resolution source is the Federal Reserve itself."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Fed officials signaled they are eyeing higher rates as unemployment claims fell, reinforcing the case for holding or hiking at the next meeting."
    publisher: "wtop.com"
    published_at: "2026-08-22T00:00:00.000Z"
    source_url: "https://wtop.com/news/2026/08/america-in-focus-fed-officials-eye-higher-rates-unemployment-claims-fall/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "wtop.com"
        source_url: "https://wtop.com/news/2026/08/america-in-focus-fed-officials-eye-higher-rates-unemployment-claims-fall/"
        retrieved_at: "2026-08-25T08:36:45+00:00"
  - type: "pm_response"
    notes: "Kalshi's current-bound ladder is consistent with the forward-bound ladder (CM-EVT-MR57HVWJT3), which prices the next hike risk at roughly coin-flip odds, together they sketch a credible hike-or-hold term structure."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "wtop.com: America In Focus: Fed officials eye higher rates; unemployment claims"
    url: "https://wtop.com/news/2026/08/america-in-focus-fed-officials-eye-higher-rates-unemployment-claims-fall/"
    published_at: "2026-08-22T00:00:00.000Z"
    retrieved_at: "2026-08-25T08:36:45+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
