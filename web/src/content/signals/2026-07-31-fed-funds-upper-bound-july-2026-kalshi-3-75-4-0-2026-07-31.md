---
signal_id: "CMSIG2026073101"
signal_slug: "fed-funds-upper-bound-july-2026-kalshi-3-75-4-0-2026-07-31"
headline: "Fed funds upper bound July 2026: Kalshi 3.75-4.0%"
semantic_title: "Fed funds upper bound seen holding near 3.75 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-31T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "July 2026 Fed funds upper bound"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.36
  volume_24h_usd: 428.19
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder pins the July 2026 fed funds upper bound in the 3.75-4.0% range, pricing 72% above 3.75% but only 36% above 4.0%."
  - "The Fed held at 3.50-3.75% with a 9-3 vote, and the ladder's modal range matches the actual decision, consistent with the outcome reported."
  - "Three dissents for a hike created bond market tension, but Kalshi puts only 6% above 4.25%, meaning markets are not pricing a near-term catch-up hike."
  - "Companion Polymarket contract CM-EVT-4G3H125S53 prices 60% on a Fed rate decision between June and September, suggesting the hold path is expected to continue near term."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Fed Chair Kevin Warsh faces pressure as bond markets signal concern about inflation even as the Fed held rates steady with three dissents at the July FOMC meeting."
    publisher: "jgiesler"
    published_at: "2026-07-31T00:00:00.000Z"
    source_url: "https://srnnews.com/fed-chief-warsh-faces-hard-choice-on-inflation-after-bond-markets-red-flag/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "jgiesler"
        source_url: "https://srnnews.com/fed-chief-warsh-faces-hard-choice-on-inflation-after-bond-markets-red-flag/"
        retrieved_at: "2026-08-01T09:54:52+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves via Federal Reserve official announcement; the modal range of 3.75-4.0% aligns with the held target but the upper tail is limited."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "jgiesler: Fed chief Warsh faces hard choice on inflation after bond market's 're"
    url: "https://srnnews.com/fed-chief-warsh-faces-hard-choice-on-inflation-after-bond-markets-red-flag/"
    published_at: "2026-07-31T00:00:00.000Z"
    retrieved_at: "2026-08-01T09:54:52+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
