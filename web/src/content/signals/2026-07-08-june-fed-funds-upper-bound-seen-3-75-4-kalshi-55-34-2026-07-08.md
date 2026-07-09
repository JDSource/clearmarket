---
signal_id: "CMSIG2026070801"
signal_slug: "june-fed-funds-upper-bound-seen-3-75-4-kalshi-55-34-2026-07-08"
headline: "June Fed funds upper bound seen 3.75-4%: Kalshi 55%/34%"
semantic_title: "Fed funds upper bound wavers between 3.75 and 4 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-08T18:44:48.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Fed funds upper bound (later 2026 meeting)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.34
  volume_24h_usd: 44.33
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder prices the implied upper bound in the 3.75-4.0% range: 55% above 3.75%, but only 34% above 4.0%."
  - "Fed minutes showing deep internal division are consistent with a market that cannot commit above 4.0%, leaving the modal outcome near 3.75-4.0%."
  - "A separate nearer-term Kalshi ladder (CM-EVT-PHWX2H6DM5) prices 99% above 3.50% for an earlier meeting, suggesting markets see near-term stability with divergence only at longer horizons."
  - "Resolves via Federal Reserve official rate announcement; any interim hawkish surprise at a future FOMC could shift the distribution sharply above 4.0%."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Fed minutes reveal officials are deeply divided over whether US inflation will stay elevated or cool, reflecting genuine uncertainty about the path of monetary policy."
    publisher: "ABC News"
    published_at: "2026-07-08T18:44:48.000Z"
    source_url: "https://abcnews.com/US/wireStory/fed-minutes-officials-deeply-divided-future-path-us-134593000"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "ABC News"
        source_url: "https://abcnews.com/US/wireStory/fed-minutes-officials-deeply-divided-future-path-us-134593000"
        retrieved_at: "2026-07-09T10:56:21+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder contract; the 3.75-4.0% range captures the modal pricing, with steep drop-off above 4.0% reflecting the divided Fed signal."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "ABC News: Fed minutes: Officials deeply divided over future path of US inflation"
    url: "https://abcnews.com/US/wireStory/fed-minutes-officials-deeply-divided-future-path-us-134593000"
    published_at: "2026-07-08T18:44:48.000Z"
    retrieved_at: "2026-07-09T10:56:21+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
