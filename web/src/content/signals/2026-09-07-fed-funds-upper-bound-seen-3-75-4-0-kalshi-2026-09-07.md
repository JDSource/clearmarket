---
signal_id: "CMSIG2026090702"
signal_slug: "fed-funds-upper-bound-seen-3-75-4-0-kalshi-2026-09-07"
headline: "Fed funds upper bound seen 3.75-4.0%: Kalshi"
semantic_title: "Fed funds above 4 percent stays a minority bet"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-07T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Fed funds upper bound (forward)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.36
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder pins the Fed funds upper bound most likely in the 3.75-4.00% range: 76% above 3.75% but only 36% above 4.00%."
  - "The blowout payrolls report is consistent with the shift toward 3.75-4.00% pricing, though markets are not yet fully committing to a 4.00%+ outcome."
  - "A companion Kalshi ladder (CM-EVT-4ZQLQPNH91) shows 99% above 3.50% but only 2% above 4.00%, confirming the 3.75% strike as the current consensus ceiling."
  - "Resolution via the named Kalshi source; the key edge case is whether a single hike lands before or after the November midterm elections."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Strong US payrolls and rising rate-hike bets have traders repricing the Federal Reserve's next move ahead of CPI data."
    publisher: "walletinvestor.com"
    published_at: "2026-09-07T00:00:00.000Z"
    source_url: "https://walletinvestor.com/news/finance-news/strong-us-jobs-data-revives-fed-rate-hike-bets-as-traders-wait-on-cpi/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "walletinvestor.com"
        source_url: "https://walletinvestor.com/news/finance-news/strong-us-jobs-data-revives-fed-rate-hike-bets-as-traders-wait-on-cpi/"
        retrieved_at: "2026-09-09T12:40:02+00:00"
  - type: "pm_response"
    notes: "Two Kalshi ladders price the same forward upper bound consistently; the spread between 76% at 3.75% and 36% at 4.00% captures the market's uncertainty about one more hike versus two."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "walletinvestor.com: Strong US jobs data revives Fed rate-hike bets as traders wait on CPI"
    url: "https://walletinvestor.com/news/finance-news/strong-us-jobs-data-revives-fed-rate-hike-bets-as-traders-wait-on-cpi/"
    published_at: "2026-09-07T00:00:00.000Z"
    retrieved_at: "2026-09-09T12:40:02+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
