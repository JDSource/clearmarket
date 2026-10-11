---
signal_id: "CMSIG2026100801"
signal_slug: "fed-funds-upper-bound-above-4-kalshi-88-2026-10-08"
headline: "Fed funds upper bound above 4%: Kalshi 88%"
semantic_title: "Fed funds above 4 percent prices in as next hike looms"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-08T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds upper bound post-next meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.19
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder puts 88% odds on the upper bound exceeding 4%, with only 19% above 4.25%, pinning consensus at the 4.0-4.25% range."
  - "The September hike to 3.75-4% was unanimous, and Fed Governor Christopher Waller's call for more hikes is consistent with the ladder's heavy lean above 4%."
  - "Trading volume on this Kalshi contract rose 9,013% day over day, a strong signal the market is actively re-pricing the next hike in real time."
  - "A companion Kalshi ladder (CM-EVT-6BS28TS762) puts only 17% above 4.0% for an earlier meeting, implying the market sees the crossover happening at the subsequent meeting, not immediately."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Fed policymakers raised the target range to 3.75-4% in September and most expect another hike in 2026, though officials split on rationale."
    publisher: "Elias Al Helou"
    published_at: "2026-10-08T00:00:00.000Z"
    source_url: "https://economymiddleeast.com/news/fed-policymakers-split-over-25-bps-hike-rationale-as-most-expect-another-increase-in-2026/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Elias Al Helou"
        source_url: "https://economymiddleeast.com/news/fed-policymakers-split-over-25-bps-hike-rationale-as-most-expect-another-increase-in-2026/"
        retrieved_at: "2026-10-11T07:48:02+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves against actual Fed policy action; the 91x volume surge confirms fresh positioning around the hike path."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Elias Al Helou: Fed policymakers split over 25 bps hike rationale as most expect anoth"
    url: "https://economymiddleeast.com/news/fed-policymakers-split-over-25-bps-hike-rationale-as-most-expect-another-increase-in-2026/"
    published_at: "2026-10-08T00:00:00.000Z"
    retrieved_at: "2026-10-11T07:48:02+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
