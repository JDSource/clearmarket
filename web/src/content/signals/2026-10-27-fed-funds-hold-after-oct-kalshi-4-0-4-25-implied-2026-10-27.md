---
signal_id: "CMSIG2026102703"
signal_slug: "fed-funds-hold-after-oct-kalshi-4-0-4-25-implied-2026-10-27"
headline: "Fed funds hold after Oct: Kalshi ~4.0-4.25% implied"
semantic_title: "Markets price Fed hold firmly, future hikes remain in view"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-27T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Fed funds upper bound after October 2026 meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.08
  volume_24h_usd: 831.35
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder implies the post-October Fed funds upper bound in the 4.00-4.25% range: 96% above 3.75%, only 8% above 4.25%."
  - "CNBC survey's 93% pause expectation matches the market's pricing of no hike this week, putting both in agreement."
  - "The 76% surveyed expecting a future hike is consistent with the ladder's meaningful probability mass above 4.00%, leaving room for a later move."
  - "Kalshi's separate jumbo-cut contract (CM-EVT-RWRZ1R3SD6) sits at 3%, confirming cuts are not on the table for 2026."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "A CNBC Fed Survey shows 93% of respondents expect a pause this week, with 76% anticipating a hike at a later meeting."
    publisher: "Steve Liesman"
    published_at: "2026-10-27T00:00:00.000Z"
    source_url: "https://www.cnbc.com/2026/10/27/federal-reserve-rate-hike-timing-expectations.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Steve Liesman"
        source_url: "https://www.cnbc.com/2026/10/27/federal-reserve-rate-hike-timing-expectations.html"
        retrieved_at: "2026-10-28T07:49:08+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves based on the Federal Reserve's official post-meeting rate announcement; the implied range is derived from the strike distribution, not a single binary."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Steve Liesman: Federal Reserve rate hikes are coming, but not this week: CNBC survey"
    url: "https://www.cnbc.com/2026/10/27/federal-reserve-rate-hike-timing-expectations.html"
    published_at: "2026-10-27T00:00:00.000Z"
    retrieved_at: "2026-10-28T07:49:08+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
