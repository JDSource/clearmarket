---
signal_id: "CMSIG2026070802"
signal_slug: "june-fed-funds-upper-bound-at-3-50-kalshi-99-2026-07-08"
headline: "June Fed funds upper bound at 3.50%: Kalshi 99%"
semantic_title: "June Fed hold consensus anchors near 3.50 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "lagging"
published_at: "2026-07-08T17:25:12.000Z"
event_id: "CM-EVT-PHWX2H6DM5"
event_slug: "kxfed-26jul"
event_question: "Fed funds upper bound, June 2026 meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26JUL-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Jul 29, 2026 meeting?"
  current_price: 0.18
  volume_24h_usd: 17161.5
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-08-05T18:05:00Z"
bullets:
  - "Kalshi ladder prices 99% above 3.50% for the June 2026 meeting, with a sharp cliff to just 18% above 3.75%, pinning the implied outcome at exactly 3.50%."
  - "Minutes confirming a hold at the June meeting are fully consistent with this near-certain 3.50% read; the market is not pricing a hike that inflation hawks might have demanded."
  - "The cliff from 99% at 3.50% to 18% at 3.75% shows the market decisively rejected a June hike despite growing inflation concerns in the room."
  - "Resolves via the Federal Reserve's official June 2026 rate announcement; outcome appears effectively settled given the 99% pricing."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Fed minutes from the June meeting show policymakers' inflation concerns grew, with divisions over whether tariff-driven price pressures are transitory or persistent."
    publisher: "jgiesler"
    published_at: "2026-07-08T17:25:12.000Z"
    source_url: "https://srnnews.com/fed-policymakers-inflation-concerns-mounted-at-june-meeting-minutes-show/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "jgiesler"
        source_url: "https://srnnews.com/fed-policymakers-inflation-concerns-mounted-at-june-meeting-minutes-show/"
        retrieved_at: "2026-07-09T10:56:21+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder contract; near-certain resolution at 3.50% upper bound with the June meeting having already occurred."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "jgiesler: Fed policymakers' inflation concerns grew at June meeting, minutes sho"
    url: "https://srnnews.com/fed-policymakers-inflation-concerns-mounted-at-june-meeting-minutes-show/"
    published_at: "2026-07-08T17:25:12.000Z"
    retrieved_at: "2026-07-09T10:56:21+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
