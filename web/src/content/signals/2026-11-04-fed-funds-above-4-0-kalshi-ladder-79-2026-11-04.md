---
signal_id: "CMSIG2026110401"
signal_slug: "fed-funds-above-4-0-kalshi-ladder-79-2026-11-04"
headline: "Fed funds above 4.0%: Kalshi ladder 79%"
semantic_title: "Fed funds above 4 percent stays heavily favored"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-04T13:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds upper bound (next meeting)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.03
  volume_24h_usd: 196.3
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder puts 79% on the Fed funds upper bound clearing 4.0%, implying a market-consensus target in the 4.0-4.25% range."
  - "News calls December hike near-certain at 80% futures odds; Kalshi distribution is consistent, with 99% pricing at or above 3.75% already."
  - "Sharp cliff above 4.25%, Kalshi at only 3%, signals the market sees one more hike as the base case, not a prolonged cycle."
  - "Resolution via the Federal Reserve's official rate announcement at the next FOMC meeting; any hot October payroll print arriving Friday could shift the 4.25% tail rapidly."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Markets price a near-certain December Fed hike with futures showing 80% odds, and a hot October jobs report could force additional tightening into 2027."
    publisher: "marketwatch.com"
    published_at: "2026-11-04T13:00:00.000Z"
    source_url: "https://www.marketwatch.com/story/think-the-fed-will-be-done-after-two-more-rate-hikes-how-fridays-jobs-report-may-trigger-a-major-market-repricing-6aca874c"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "marketwatch.com"
        source_url: "https://www.marketwatch.com/story/think-the-fed-will-be-done-after-two-more-rate-hikes-how-fridays-jobs-report-may-trigger-a-major-market-repricing-6aca874c"
        retrieved_at: "2026-11-04T15:56:48+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder carries live strike probabilities from 2.75% to 5.25%; the distribution clusters tightly at 4.0-4.25%, with thin tail above."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "marketwatch.com: Think the Fed will be done after two more rate hikes? How Friday’s job"
    url: "https://www.marketwatch.com/story/think-the-fed-will-be-done-after-two-more-rate-hikes-how-fridays-jobs-report-may-trigger-a-major-market-repricing-6aca874c"
    published_at: "2026-11-04T13:00:00.000Z"
    retrieved_at: "2026-11-04T15:56:48+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
