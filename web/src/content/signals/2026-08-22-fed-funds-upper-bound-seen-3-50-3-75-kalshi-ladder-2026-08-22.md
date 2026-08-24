---
signal_id: "CMSIG2026082201"
signal_slug: "fed-funds-upper-bound-seen-3-50-3-75-kalshi-ladder-2026-08-22"
headline: "Fed funds upper bound seen 3.50-3.75%: Kalshi ladder"
semantic_title: "Fed funds upper bound stays near 3.5 to 3.75 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-22T00:00:00.000Z"
event_id: "CM-EVT-4ZQLQPNH91"
event_slug: "kxfed-26sep"
event_question: "Federal funds upper bound"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26SEP-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Sep 16, 2026 meeting?"
  current_price: 0.35
  volume_24h_usd: 2518.24
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-09-23T18:05:00Z"
bullets:
  - "Kalshi ladder puts the federal funds upper bound in the 3.50-3.75% range: 99% above 3.50% but only 35% above 3.75%."
  - "Fed officials eyeing higher rates is consistent with the ladder distribution, which firmly rules out a return below 3.50%."
  - "The sharp drop from 99% at 3.50% to 35% at 3.75% shows the market treats one more hike as likely but a second as a stretch."
  - "Only 1% odds at 4.0% and above shows the market is not pricing an aggressive multi-hike cycle despite hawkish rhetoric."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Fed officials signaled readiness to raise rates further as grocery and gas prices remain elevated and unemployment claims fell."
    publisher: "wtop.com"
    published_at: "2026-08-22T00:00:00.000Z"
    source_url: "https://wtop.com/news/2026/08/america-in-focus-fed-officials-eye-higher-rates-unemployment-claims-fall/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "wtop.com"
        source_url: "https://wtop.com/news/2026/08/america-in-focus-fed-officials-eye-higher-rates-unemployment-claims-fall/"
        retrieved_at: "2026-08-24T08:42:17+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves on the actual federal funds upper bound; distribution sharpest at the 3.50-3.75% gap."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "wtop.com: America In Focus: Fed officials eye higher rates; unemployment claims"
    url: "https://wtop.com/news/2026/08/america-in-focus-fed-officials-eye-higher-rates-unemployment-claims-fall/"
    published_at: "2026-08-22T00:00:00.000Z"
    retrieved_at: "2026-08-24T08:42:17+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
