---
signal_id: "CMSIG2026070301"
signal_slug: "june-fed-funds-upper-bound-seen-3-50-3-75-kalshi-2026-07-03"
headline: "June Fed funds upper bound seen 3.50-3.75%: Kalshi"
semantic_title: "Fed funds rate consensus anchors at 3.50-3.75 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-03T15:32:48.000Z"
event_id: "CM-EVT-PHWX2H6DM5"
event_slug: "kxfed-26jul"
event_question: "Fed funds upper bound (next meeting)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26JUL-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Jul 29, 2026 meeting?"
  current_price: 0.1
  volume_24h_usd: 114.22
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-07-29T18:05:00Z"
bullets:
  - "Kalshi pins the Fed funds upper bound in the 3.50-3.75% range: 98% above 3.50% but only 10% above 3.75%."
  - "June payrolls of 57,000, roughly half consensus, are consistent with the market holding the rate steady below 3.75%."
  - "A separate Kalshi ladder (CM-EVT-6BS28TS762) shows 78% above 3.50% but only 20% above 3.75%, confirming cross-venue alignment on a pause."
  - "Resolves via the Federal Reserve's official post-meeting rate announcement; any emergency inter-meeting action would also trigger settlement."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The U.S. economy added only 57,000 jobs in June, well below forecasts, casting doubt on any near-term Fed rate hike."
    publisher: "Estefano Gomez"
    published_at: "2026-07-03T15:32:48.000Z"
    source_url: "https://cryptobriefing.com/us-adds-57000-jobs-in-june-fed-rate-hike-in-doubt/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Estefano Gomez"
        source_url: "https://cryptobriefing.com/us-adds-57000-jobs-in-june-fed-rate-hike-in-doubt/"
        retrieved_at: "2026-07-06T12:00:14+00:00"
  - type: "pm_response"
    notes: "Three Kalshi ladders independently converge on 3.50-3.75% as the implied upper bound, with near-zero probability of a hike to 4.00% or above."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Estefano Gomez: US adds 57,000 jobs in June, Fed rate hike in doubt"
    url: "https://cryptobriefing.com/us-adds-57000-jobs-in-june-fed-rate-hike-in-doubt/"
    published_at: "2026-07-03T15:32:48.000Z"
    retrieved_at: "2026-07-06T12:00:14+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
