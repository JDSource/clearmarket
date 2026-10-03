---
signal_id: "CMSIG2026100201"
signal_slug: "fed-funds-upper-bound-implied-3-75-4-0-kalshi-ladder-2026-10-02"
headline: "Fed funds upper bound implied 3.75-4.0%: Kalshi ladder"
semantic_title: "Fed funds upper bound seen near 4 percent after jobs miss"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-02T00:00:00.000Z"
event_id: "CM-EVT-6BS28TS762"
event_slug: "kxfed-26oct"
event_question: "Federal funds upper bound after next Fed decision"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26OCT-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Oct 28, 2026 meeting?"
  current_price: 0.23
  volume_24h_usd: 2061.89
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-11-04T18:05:00Z"
bullets:
  - "Kalshi ladder pins the federal funds upper bound at 3.75-4.0%, pricing 99% above 3.75% but only 23% above 4.0%."
  - "Fed Vice Chair Philip Jefferson's 'no rush' language is consistent with the ladder: no meaningful probability of a hike to 4.25% or above."
  - "The 29,000 September payroll miss reinforces the hold case; the ladder assigns just 2% odds to 4.25% or higher."
  - "Resolution uses FRED data; any surprise policy shift at the November meeting would reprice the upper rungs sharply."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Fed Vice Chair Philip Jefferson said the central bank is in no rush to raise rates again, suggesting October is off the table after a weak September jobs print of 29,000."
    publisher: "Thao Ta"
    published_at: "2026-10-02T00:00:00.000Z"
    source_url: "https://ph.investing.com/news/economy-news/fed-vice-chair-jefferson-no-rush-to-raise-rates-again-2611399"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Thao Ta"
        source_url: "https://ph.investing.com/news/economy-news/fed-vice-chair-jefferson-no-rush-to-raise-rates-again-2611399"
        retrieved_at: "2026-10-03T07:47:35+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder distribution tightly clusters at 3.75-4.0%, reflecting both the weak jobs data and Jefferson's cautious posture."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Thao Ta: Fed Vice Chair Jefferson: No rush to raise rates again By Investing.co"
    url: "https://ph.investing.com/news/economy-news/fed-vice-chair-jefferson-no-rush-to-raise-rates-again-2611399"
    published_at: "2026-10-02T00:00:00.000Z"
    retrieved_at: "2026-10-03T07:47:35+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
