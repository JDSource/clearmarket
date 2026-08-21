---
signal_id: "CMSIG2026081901"
signal_slug: "next-fed-funds-upper-bound-seen-3-75-4-kalshi-55-16-2026-08-19"
headline: "Next Fed funds upper bound seen 3.75-4%: Kalshi 55%/16%"
semantic_title: "Markets put short odds on Fed funds above 4 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-19T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds rate upper bound (next meeting)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.16
  volume_24h_usd: 0.16
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder prices the next Fed funds upper bound in the 3.75-4.00% range, with 55% above 3.75% but only 16% above 4.00%."
  - "July minutes confirmed hawkish lean with 3 dissenters, but the Kalshi distribution is consistent with a hold-leaning market still pricing hike risk as a tail event."
  - "The 3.50% strike sits at 84%, meaning markets see a move above current levels as the clear base case, just not a full hike to 4.00%-plus."
  - "A companion Kalshi ladder (CM-EVT-4ZQLQPNH91) pins an earlier meeting's upper bound tightly at 3.50-3.75%, with only 28% above 3.75%, showing the term structure flattens quickly."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "July FOMC minutes showed officials saw potential for higher rates if inflation stays elevated, with three dissenters favoring an immediate 25-basis-point hike."
    publisher: "Jeff Cox"
    published_at: "2026-08-19T00:00:00.000Z"
    source_url: "https://www.cnbc.com/2026/08/19/fed-minutes-july-2026-officials-saw-need-for-rate-hike-if-inflation-doesnt-cool.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Jeff Cox"
        source_url: "https://www.cnbc.com/2026/08/19/fed-minutes-july-2026-officials-saw-need-for-rate-hike-if-inflation-doesnt-cool.html"
        retrieved_at: "2026-08-21T08:35:01+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves against the actual FOMC decision; the 16% at 4.00% is the key hike probability the minutes hawkishness has not yet pushed higher."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Jeff Cox: Fed minutes July 2026: Officials saw need for rate hike if inflation d"
    url: "https://www.cnbc.com/2026/08/19/fed-minutes-july-2026-officials-saw-need-for-rate-hike-if-inflation-doesnt-cool.html"
    published_at: "2026-08-19T00:00:00.000Z"
    retrieved_at: "2026-08-21T08:35:01+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
