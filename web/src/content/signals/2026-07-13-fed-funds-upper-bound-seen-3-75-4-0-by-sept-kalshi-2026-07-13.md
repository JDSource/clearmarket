---
signal_id: "CMSIG2026071301"
signal_slug: "fed-funds-upper-bound-seen-3-75-4-0-by-sept-kalshi-2026-07-13"
headline: "Fed funds upper bound seen 3.75-4.0% by Sept: Kalshi"
semantic_title: "Near-term hike consensus hardens on Waller urgency signal"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-13T00:00:00.000Z"
event_id: "CM-EVT-4ZQLQPNH91"
event_slug: "kxfed-26sep"
event_question: "September 2026 Fed funds upper bound"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26SEP-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Sep 16, 2026 meeting?"
  current_price: 0.08
  volume_24h_usd: 202.72
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-09-23T18:05:00Z"
bullets:
  - "Kalshi pins the September 2026 Fed funds upper bound in the 3.75-4.0% range, pricing 60% above 3.75% but only 8% above 4.0%."
  - "Fed Governor Christopher Waller's near-term hike call is broadly consistent with a market-implied range just above current levels, not pricing a dramatic overshoot."
  - "A companion near-term ladder (CM-EVT-PHWX2H6DM5) prices only 36% above 3.75%, showing the market sees meaningful but not certain follow-through on Waller's urgency."
  - "Resolves via Federal Reserve official rate announcement; any July or September hike that clears 4.0% would sharply reprice the tail, currently at just 8%."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Fed Governor Christopher Waller said the Fed should hike rates 'in the near term' if CPI and PPI data this week come in hot, signaling urgency ahead of the July meeting."
    publisher: "wolfstreet.com"
    published_at: "2026-07-13T00:00:00.000Z"
    source_url: "https://wolfstreet.com/2026/07/13/fed-should-hike-in-the-near-term-if-cpi-ppi-this-week-are-hot-feds-waller-so-at-the-july-meeting-treasury-yields-jump/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "wolfstreet.com"
        source_url: "https://wolfstreet.com/2026/07/13/fed-should-hike-in-the-near-term-if-cpi-ppi-this-week-are-hot-feds-waller-so-at-the-july-meeting-treasury-yields-jump/"
        retrieved_at: "2026-07-14T09:54:27+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder shows the market absorbing Waller's hawkish signal into a 3.75-4.0% modal range, not pricing an aggressive multi-hike cycle."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "wolfstreet.com: Fed Should Hike “in the Near Term” if CPI & PPI this Week Are “Hot”: F"
    url: "https://wolfstreet.com/2026/07/13/fed-should-hike-in-the-near-term-if-cpi-ppi-this-week-are-hot-feds-waller-so-at-the-july-meeting-treasury-yields-jump/"
    published_at: "2026-07-13T00:00:00.000Z"
    retrieved_at: "2026-07-14T09:54:27+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
