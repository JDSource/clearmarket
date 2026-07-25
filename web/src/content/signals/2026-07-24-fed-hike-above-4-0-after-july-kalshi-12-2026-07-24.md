---
signal_id: "CMSIG2026072403"
signal_slug: "fed-hike-above-4-0-after-july-kalshi-12-2026-07-24"
headline: "Fed hike above 4.0% after July: Kalshi 12%"
semantic_title: "Rate hike odds stay short of one-in-two despite historic jobs data"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-24T00:00:00.000Z"
event_id: "CM-EVT-4ZQLQPNH91"
event_slug: "kxfed-26sep"
event_question: "July 2026 Fed funds upper bound"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26SEP-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Sep 16, 2026 meeting?"
  current_price: 0.12
  volume_24h_usd: 4.32
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-09-23T18:05:00Z"
bullets:
  - "Kalshi ladder prices only 12% probability the Fed funds upper bound exceeds 4.0% after the July meeting."
  - "Headlines claim hike odds are past one-in-three, but the Kalshi distribution puts a hike above 4.0% at just 12%, materially below that framing."
  - "Volume on this Kalshi ladder rose 396x day-over-day, confirming the jobs print is drawing heavy fresh attention even as outright hike pricing remains a minority view."
  - "The 3.75% strike at 65% suggests markets see the most likely outcome as a hold at current levels, not a hike."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Jobless claims hitting a 57-year low pushed headlines declaring Fed rate-hike odds past one-in-three, framing historically strong labor data as an inflation risk."
    publisher: "Scott McCain  
 
 
 Published: Jul 24 2026, 7:40 AM EDT"
    published_at: "2026-07-24T00:00:00.000Z"
    source_url: "https://www.techtimes.com/articles/321475/20260724/jobless-claims-fall-57-year-low-pushing-fed-rate-hike-odds-past-one-three.htm"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Scott McCain  
 
 
 Published: Jul 24 2026, 7:40 AM EDT"
        source_url: "https://www.techtimes.com/articles/321475/20260724/jobless-claims-fall-57-year-low-pushing-fed-rate-hike-odds-past-one-three.htm"
        retrieved_at: "2026-07-25T09:42:27+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder, with a massive volume spike, shows the market is fading the one-in-three hike narrative: above-4.0% probability sits at just 12%."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Scott McCain  
 
 
 Published: Jul 24 2026, 7:40 AM EDT: Jobless Claims Fall to 57-Year Low, Pushing Fed Rate-Hike Odds Past On"
    url: "https://www.techtimes.com/articles/321475/20260724/jobless-claims-fall-57-year-low-pushing-fed-rate-hike-odds-past-one-three.htm"
    published_at: "2026-07-24T00:00:00.000Z"
    retrieved_at: "2026-07-25T09:42:27+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
