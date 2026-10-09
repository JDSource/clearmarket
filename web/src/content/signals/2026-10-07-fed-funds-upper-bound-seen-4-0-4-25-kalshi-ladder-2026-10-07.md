---
signal_id: "CMSIG2026100701"
signal_slug: "fed-funds-upper-bound-seen-4-0-4-25-kalshi-ladder-2026-10-07"
headline: "Fed funds upper bound seen 4.0-4.25%: Kalshi ladder"
semantic_title: "Fed funds rate stays priced near 4 to 4.25 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-07T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds upper bound (next meeting)"
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
  - "Kalshi ladder puts the federal funds upper bound in the 4.0-4.25% range: 82% above 4.0% but only 19% above 4.25%."
  - "FOMC minutes flagged another hike as 'likely,' and the Kalshi distribution is broadly consistent, though the 19% read above 4.25% shows the market stops well short of pricing a larger move. Trading volume surged 147x day over day, signaling fresh attention on this contract."
  - "The sharp drop from 82% to 19% between the 4.0% and 4.25% strikes means the market sees the next hike as more probable than not, but caps the upper bound near 4.25%."
  - "The Kalshi contract on a Fed cut greater than 25 basis points this year sits at just 3%, reinforcing the ladder's tightening-not-easing tilt and leaving little probability mass on any dovish pivot."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "FOMC minutes showed most officials viewed another rate hike as likely in 2026, with Fed Governor Christopher Waller speaking on the economic outlook at the Istanbul Economic Forum."
    publisher: "Max Rego"
    published_at: "2026-10-07T00:00:00.000Z"
    source_url: "https://thehill.com/business/6135206-fed-officials-project-future-increases"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Max Rego"
        source_url: "https://thehill.com/business/6135206-fed-officials-project-future-increases"
        retrieved_at: "2026-10-09T14:55:32+00:00"
  - type: "pm_response"
    notes: "Kalshi's ladder on the federal funds upper bound drew 147x normal daily volume as FOMC minutes hit wires, with implied peak near 4.0-4.25%."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Max Rego: Federal Reserve minutes indicate most board members anticipated anothe"
    url: "https://thehill.com/business/6135206-fed-officials-project-future-increases"
    published_at: "2026-10-07T00:00:00.000Z"
    retrieved_at: "2026-10-09T14:55:32+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
