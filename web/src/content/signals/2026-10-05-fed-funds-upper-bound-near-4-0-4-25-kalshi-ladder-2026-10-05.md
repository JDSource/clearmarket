---
signal_id: "CMSIG2026100501"
signal_slug: "fed-funds-upper-bound-near-4-0-4-25-kalshi-ladder-2026-10-05"
headline: "Fed funds upper bound near 4.0-4.25%: Kalshi ladder"
semantic_title: "Fed funds above 4 percent stays likely after jobs miss"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-05T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds upper bound (next meeting)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.2
  volume_24h_usd: 137.73
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder pins the federal funds upper bound in the 4.0-4.25% range: 78% above 4.0% but only 20% above 4.25%."
  - "September payrolls of just 29,000 are consistent with a pause at 4.0-4.25%; the ladder shows the market aligning with a hold, not a hike."
  - "A companion Kalshi ladder (CM-EVT-6BS28TS762) puts 99% above 3.75% but only 21% above 4.0%, suggesting a tighter consensus around the 4.0% ceiling."
  - "Resolution via the Federal Reserve's official post-meeting rate announcement; the spread between the two ladders flags modest ambiguity about the exact upper bound."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Weaker-than-expected September jobs data (29,000 payrolls added) dimmed October Fed rate-hike bets, with Bitcoin rising near $86,000 as a result."
    publisher: "Ayushman Ojha"
    published_at: "2026-10-05T00:00:00.000Z"
    source_url: "https://ca.investing.com/news/cryptocurrency-news/bitcoin-rises-near-86k-as-softer-jobs-data-offsets-pressure-from-high-yields-4864978"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Ayushman Ojha"
        source_url: "https://ca.investing.com/news/cryptocurrency-news/bitcoin-rises-near-86k-as-softer-jobs-data-offsets-pressure-from-high-yields-4864978"
        retrieved_at: "2026-10-05T16:44:30+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder data provided; no single binary price available, but the distribution is internally consistent across both ladder series."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Ayushman Ojha: Bitcoin rises near $86k as softer jobs data offsets pressure from high"
    url: "https://ca.investing.com/news/cryptocurrency-news/bitcoin-rises-near-86k-as-softer-jobs-data-offsets-pressure-from-high-yields-4864978"
    published_at: "2026-10-05T00:00:00.000Z"
    retrieved_at: "2026-10-05T16:44:30+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
