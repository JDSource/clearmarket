---
signal_id: "CMSIG2026091802"
signal_slug: "fed-funds-upper-bound-by-year-end-kalshi-sees-4-00-4-25-2026-09-18"
headline: "Fed funds upper bound by year-end: Kalshi sees 4.00-4.25%"
semantic_title: "Fed funds upper bound seen landing near 4 to 4.25 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-18T00:00:00.000Z"
event_id: "CM-EVT-6BS28TS762"
event_slug: "kxfed-26oct"
event_question: "Fed funds upper bound, year-end 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26OCT-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Oct 28, 2026 meeting?"
  current_price: 0.02
  volume_24h_usd: 44.58
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-11-04T18:05:00Z"
bullets:
  - "The Kalshi ladder prices the upper bound in the 4.00%-4.25% range: 98% above 3.75%, but only 2% above 4.25%, pinning the consensus at one more 25bp hike."
  - "The September hike to 3.75%-4% and the Fed's own dot-plot projecting 4.00%-4.25% are fully consistent with this narrow distribution."
  - "The sharp drop from 98% above 3.75% to just 2% above 4.25% signals the market views a second consecutive hike as very unlikely, capping the tightening cycle near consensus."
  - "Resolves via the Federal Reserve's official policy rate announcement; any upside surprise above 4.25% is priced as a near-zero tail event."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Multiple outlets report the Fed hiked to 3.75%-4% in September 2026 and projected the policy rate reaching 4.00%-4.25% by year-end, with CNN noting potential midterm political fallout."
    publisher: "Zachary B. Wolf"
    published_at: "2026-09-18T00:00:00.000Z"
    source_url: "https://www.cnn.com/2026/09/18/politics/fed-rate-increase-trump-midterms"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Zachary B. Wolf"
        source_url: "https://www.cnn.com/2026/09/18/politics/fed-rate-increase-trump-midterms"
        retrieved_at: "2026-09-19T07:47:13+00:00"
  - type: "pm_response"
    notes: "The Kalshi ladder distribution is tightly bunched around the 4.00%-4.25% range, leaving almost no probability mass above that level."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Zachary B. Wolf: How the Fed’s rate decisions could hurt GOP chances in the midterms |"
    url: "https://www.cnn.com/2026/09/18/politics/fed-rate-increase-trump-midterms"
    published_at: "2026-09-18T00:00:00.000Z"
    retrieved_at: "2026-09-19T07:47:13+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
