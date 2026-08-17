---
signal_id: "CMSIG2026081403"
signal_slug: "fed-funds-upper-bound-longer-run-kalshi-3-75-4-0-2026-08-14"
headline: "Fed funds upper bound longer-run: Kalshi 3.75-4.0%"
semantic_title: "Longer-run Fed funds upper bound prices in near 3.75-4.0%"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-14T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Fed funds upper bound, longer-run meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.21
  volume_24h_usd: 1.26
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder implies a longer-run Fed funds upper bound near 3.75-4.0%, with 81% above 3.50% but only 51% above 3.75% and 21% above 4.0%."
  - "July CPI at 3.4% keeps inflation comfortably above the 2% target, which is consistent with a market reluctant to price aggressive cuts ahead."
  - "Comparing this ladder to the near-term meeting ladder (98% above 3.50%, 25% above 3.75%) shows the term structure is slightly higher, implying cuts come slowly if at all."
  - "Companion Kalshi contract on a Fed cut greater than 25 basis points in 2026 is priced at just 6%, reinforcing the shallow-easing consensus."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "July CPI came in at 3.4% year-over-year, above prior months, keeping inflation above target even as the Fed weighs a pause."
    publisher: "Federal Newswire Reports"
    published_at: "2026-08-14T00:00:00.000Z"
    source_url: "https://thefederalnewswire.com/july-consumer-prices-rise-3-4-as-workers-lose-purchasing-power/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Federal Newswire Reports"
        source_url: "https://thefederalnewswire.com/july-consumer-prices-rise-3-4-as-workers-lose-purchasing-power/"
        retrieved_at: "2026-08-17T08:37:49+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves via the Federal Reserve's official rate announcement; the 3.75-4.0% implied range reflects persistent inflation as the binding constraint."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Federal Newswire Reports: July Consumer Prices Rise 3.4% as Workers Lose Purchasing Power - thef"
    url: "https://thefederalnewswire.com/july-consumer-prices-rise-3-4-as-workers-lose-purchasing-power/"
    published_at: "2026-08-14T00:00:00.000Z"
    retrieved_at: "2026-08-17T08:37:49+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
