---
signal_id: "CMSIG2026101302"
signal_slug: "post-meeting-fed-funds-upper-bound-at-4-0-4-25-kalshi-2026-10-13"
headline: "Post-meeting Fed funds upper bound at 4.0-4.25%: Kalshi"
semantic_title: "Fed funds after next meeting stays near 4 to 4.25 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-13T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Fed funds upper bound after next FOMC meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.14
  volume_24h_usd: 4.34
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder prices the post-meeting Fed funds upper bound in the 4.0-4.25% range: 83% above 4.0% but only 14% above 4.25%."
  - "Fed minutes signaling another hike as likely are broadly consistent with the ladder's concentration just above 4.0%; the market is not pricing a larger move."
  - "A companion Kalshi ladder tied to a prior meeting already prices 99% above 3.75%, reflecting the confirmed September hike to 3.75-4.00%."
  - "The Kalshi contract resolves via the Federal Reserve's official post-meeting statement; a unanimous hold would collapse the 14% tail above 4.25%."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Federal Reserve minutes released this week showed most officials viewed another 25-basis-point hike by year-end as likely, with AI infrastructure spending flagged as an additional inflation risk."
    publisher: "WireNorth Staff"
    published_at: "2026-10-13T00:00:00.000Z"
    source_url: "https://wirenorth.com/article/fed-minutes-ai-inflation-2026-10-08"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "WireNorth Staff"
        source_url: "https://wirenorth.com/article/fed-minutes-ai-inflation-2026-10-08"
        retrieved_at: "2026-10-13T07:48:09+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder on the Fed funds upper bound after the next meeting is priced tightly around the 4.0-4.25% range, consistent with the minutes' tightening signal."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "WireNorth Staff: Fed Minutes Point to Another 2026 Rate Hike as AI Spending Adds Inflat"
    url: "https://wirenorth.com/article/fed-minutes-ai-inflation-2026-10-08"
    published_at: "2026-10-13T00:00:00.000Z"
    retrieved_at: "2026-10-13T07:48:09+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
