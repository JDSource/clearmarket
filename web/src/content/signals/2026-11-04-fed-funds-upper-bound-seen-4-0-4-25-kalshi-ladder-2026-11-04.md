---
signal_id: "CMSIG2026110403"
signal_slug: "fed-funds-upper-bound-seen-4-0-4-25-kalshi-ladder-2026-11-04"
headline: "Fed funds upper bound seen 4.0-4.25%: Kalshi ladder"
semantic_title: "Fed funds upper bound near 4.0-4.25%, rate hike path stays short"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-04T13:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds rate upper bound post-current meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.02
  volume_24h_usd: 189.96
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder puts 80% odds on the upper bound being above 4.0%, but only 2% above 4.25%, pinning the consensus range tightly at 4.0%-4.25%."
  - "The MarketWatch scenario of a 'major repricing' toward more hikes finds little support in the Kalshi distribution, which prices near-zero probability above 4.25%."
  - "The cliff from 80% to 2% between the 4.0% and 4.25% strikes shows the market has effectively closed the door on additional hikes beyond the current level."
  - "Resolves via the Fed's post-meeting statement on the federal funds target range; a payrolls beat Friday would be the near-term catalyst to watch against this pricing."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "MarketWatch commentary argues that a hot jobs report Friday could trigger repricing of the number and timing of remaining Fed rate hikes."
    publisher: "Michael Kramer"
    published_at: "2026-11-04T13:00:00.000Z"
    source_url: "https://www.marketwatch.com/story/think-the-fed-will-be-done-after-two-more-rate-hikes-how-fridays-jobs-report-may-trigger-a-major-market-repricing-6aca874c"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Michael Kramer"
        source_url: "https://www.marketwatch.com/story/think-the-fed-will-be-done-after-two-more-rate-hikes-how-fridays-jobs-report-may-trigger-a-major-market-repricing-6aca874c"
        retrieved_at: "2026-11-05T07:48:08+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder firmly prices the upper bound at 4.0%-4.25%, contradicting the hawkish-repricing scenario floated in commentary ahead of the jobs report."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Michael Kramer: Think the Fed will be done after two more rate hikes? How Friday’s job"
    url: "https://www.marketwatch.com/story/think-the-fed-will-be-done-after-two-more-rate-hikes-how-fridays-jobs-report-may-trigger-a-major-market-repricing-6aca874c"
    published_at: "2026-11-04T13:00:00.000Z"
    retrieved_at: "2026-11-05T07:48:08+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
