---
signal_id: "CMSIG2026081401"
signal_slug: "fed-funds-upper-bound-at-3-50-3-75-kalshi-ladder-2026-08-14"
headline: "Fed funds upper bound at 3.50-3.75%: Kalshi ladder"
semantic_title: "Fed funds upper bound seen holding at 3.50-3.75%"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-14T00:00:00.000Z"
event_id: "CM-EVT-4ZQLQPNH91"
event_slug: "kxfed-26sep"
event_question: "Fed funds upper bound, next meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26SEP-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Sep 16, 2026 meeting?"
  current_price: 0.25
  volume_24h_usd: 76.61
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-09-23T18:05:00Z"
bullets:
  - "Kalshi ladder prices the Fed funds upper bound in the 3.50-3.75% range, with 98% above 3.50% but only 25% above 3.75%."
  - "Retail sales dropped 0.6% in July and consumer confidence fell, consistent with a market that prices near-zero chance of a hike."
  - "The sharp cliff from 98% to 25% between 3.50% and 3.75% signals strong consensus the upper bound stays at 3.75% or below."
  - "Companion Kalshi contract on an emergency Fed meeting in 2026 sits at just 5%, ruling out an out-of-cycle move as the catalyst."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Weak retail sales and falling consumer confidence are pushing markets to bet the Fed holds rates steady at its next meeting."
    publisher: "americanbanker.com"
    published_at: "2026-08-14T00:00:00.000Z"
    source_url: "https://www.americanbanker.com/news/markets-eye-fed-hold-after-retail-sales-consumer-confidence-fall"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "americanbanker.com"
        source_url: "https://www.americanbanker.com/news/markets-eye-fed-hold-after-retail-sales-consumer-confidence-fall"
        retrieved_at: "2026-08-17T08:37:49+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves via the Federal Reserve's post-meeting announcement; the 3.50-3.75% implied range reflects the dominant hold scenario."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "americanbanker.com: Markets eye Fed hold after retail sales, consumer confidence fall | Am"
    url: "https://www.americanbanker.com/news/markets-eye-fed-hold-after-retail-sales-consumer-confidence-fall"
    published_at: "2026-08-14T00:00:00.000Z"
    retrieved_at: "2026-08-17T08:37:49+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
