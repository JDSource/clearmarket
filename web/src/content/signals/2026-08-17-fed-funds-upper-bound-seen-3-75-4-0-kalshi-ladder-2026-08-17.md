---
signal_id: "CMSIG2026081704"
signal_slug: "fed-funds-upper-bound-seen-3-75-4-0-kalshi-ladder-2026-08-17"
headline: "Fed funds upper bound seen 3.75-4.0%: Kalshi ladder"
semantic_title: "Fed funds upper bound seen in the 3.75 to 4 percent range"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-17T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds upper bound after next meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.21
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder prices the federal funds upper bound at 55% above 3.75% but only 21% above 4.00%, implying consensus in the 3.75%-4.00% range."
  - "Wall Street's retreat from a September hike is broadly consistent with this distribution, the market is not pricing aggressive tightening."
  - "A separate Kalshi ladder for a later horizon puts 99% above 3.50% but only 28% above 3.75%, showing the term structure leans toward stable rates."
  - "Reuters poll consensus of no hike through year-end aligns with the ladder's implied ceiling near 4.00% with little weight above."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Wall Street is souring on a September rate hike move, with four reasons cited for diminished tightening expectations."
    publisher: "William Edwards"
    published_at: "2026-08-17T00:00:00.000Z"
    source_url: "https://www.businessinsider.com/why-wall-street-is-abandoning-higher-interest-rates-federal-reserve-2026-8"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "William Edwards"
        source_url: "https://www.businessinsider.com/why-wall-street-is-abandoning-higher-interest-rates-federal-reserve-2026-8"
        retrieved_at: "2026-08-20T08:32:51+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves by Federal Reserve policy announcement; the two ladders across different horizons show a consistent hold-biased term structure."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "William Edwards: Rate Hike Forecast: 4 Reasons Why Wall Street Is Souring on a Sept. Mo"
    url: "https://www.businessinsider.com/why-wall-street-is-abandoning-higher-interest-rates-federal-reserve-2026-8"
    published_at: "2026-08-17T00:00:00.000Z"
    retrieved_at: "2026-08-20T08:32:51+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
