---
signal_id: "CMSIG2026052801"
signal_slug: "june-fed-funds-upper-bound-seen-3-50-3-75-kalshi-2026-05-28"
headline: "June Fed funds upper bound seen 3.50-3.75%: Kalshi"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-05-28T16:13:24.000Z"
event_id: "CM-EVT-PHWX2H6DM5"
event_slug: "kxfed-26jul"
event_question: "June 2026 Fed funds upper bound"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26JUL-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Jul 29, 2026 meeting?"
  current_price: 0.14
  volume_24h_usd: 16.1
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-07-29T18:05:00Z"
bullets:
  - "Kalshi prices the June 2026 Fed funds upper bound in the 3.50-3.75% range, with 93% probability above 3.50% but only 14% above 3.75%, firmly anchoring the expected outcome at a hold."
  - "The Fed's preferred inflation gauge printed at 3.8% in April -- well above the 2% target -- yet the Kalshi distribution is consistent with no cut at the June meeting, meaning the market is not pricing in any policy tightening response to the hotter print either."
  - "The 3.50% level is the current upper bound, so the 93% reading there reflects near-certainty of no cut, while the sharp drop to 14% above 3.75% reflects near-zero odds of a hike."
  - "On the companion Kalshi contract for a later meeting (CM-EVT-RJ6SMJGK50), the distribution is nearly identical -- 96% above 3.50% but only 2% above 3.75% -- suggesting term-structure pricing also sees no cuts or hikes through the subsequent meeting window."
  - "The Kalshi contract resolves via Federal Reserve policy announcement; settlement edge cases include emergency inter-meeting rate decisions, which the distribution implies the market assigns near-zero probability."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The Federal Reserve's preferred inflation measure rose to 3.8% in April, its highest reading in years, raising questions about the Fed's policy path ahead of the June meeting."
    publisher: "americanbanker.com"
    published_at: "2026-05-28T16:13:24.000Z"
    source_url: "https://www.americanbanker.com/news/feds-target-inflation-rate-ticks-up-raises-questions-about-policy-stance"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "americanbanker.com"
        source_url: "https://www.americanbanker.com/news/feds-target-inflation-rate-ticks-up-raises-questions-about-policy-stance"
        retrieved_at: "2026-05-29T21:01:04+00:00"
  - type: "pm_response"
    notes: "Kalshi covers both the June and a subsequent Fed meeting; both ladders show the same 3.50-3.75% anchor, with the later contract even more compressed above 3.75%."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "americanbanker.com: Fed's target inflation rate ticks up, raises questions about policy st"
    url: "https://www.americanbanker.com/news/feds-target-inflation-rate-ticks-up-raises-questions-about-policy-stance"
    published_at: "2026-05-28T16:13:24.000Z"
    retrieved_at: "2026-05-29T21:01:04+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
