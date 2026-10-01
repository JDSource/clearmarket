---
signal_id: "CMSIG2026092901"
signal_slug: "fed-funds-upper-bound-post-nov-kalshi-sees-4-0-4-25-2026-09-29"
headline: "Fed funds upper bound post-Nov: Kalshi sees 4.0-4.25%"
semantic_title: "Fed funds upper bound stays near 4 percent after November"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-29T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Fed funds upper bound, post-November 2026 meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.29
  volume_24h_usd: 795.78
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder pins the post-November Fed funds upper bound in the 4.00-4.25% range, with 89% above 4.00% but only 29% above 4.25%."
  - "New York Fed President John Williams said there is no urgency for another hike, consistent with the market's pricing of a pause near current levels."
  - "A companion Kalshi ladder (CM-EVT-6BS28TS762) shows the market-implied upper bound closer to 3.75-4.00%, with only 44% above 4.00%, suggesting term-structure uncertainty across horizons."
  - "Resolution follows the official FOMC post-meeting statement; any inter-meeting guidance shift would reprice the 4.25% tail sharply."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "New York Fed President John Williams said the central bank has time to weigh data before deciding on another rate hike, signaling no urgency."
    publisher: "Thomson Reuters"
    published_at: "2026-09-29T00:00:00.000Z"
    source_url: "https://theduke.fm/2026/09/29/feds-williams-sees-no-urgency-for-next-fed-rate-hike/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Thomson Reuters"
        source_url: "https://theduke.fm/2026/09/29/feds-williams-sees-no-urgency-for-next-fed-rate-hike/"
        retrieved_at: "2026-10-01T07:47:27+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder pricing is consistent with a hold narrative; the spread between the two ladders signals meaningful uncertainty about the precise cycle peak."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Thomson Reuters: Fed’s Williams sees no urgency for next Fed rate hike | 95.7 Duke FM P"
    url: "https://theduke.fm/2026/09/29/feds-williams-sees-no-urgency-for-next-fed-rate-hike/"
    published_at: "2026-09-29T00:00:00.000Z"
    retrieved_at: "2026-10-01T07:47:27+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
