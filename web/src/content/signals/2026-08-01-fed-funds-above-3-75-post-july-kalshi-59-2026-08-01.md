---
signal_id: "CMSIG2026080102"
signal_slug: "fed-funds-above-3-75-post-july-kalshi-59-2026-08-01"
headline: "Fed funds above 3.75% post-July: Kalshi 59%"
semantic_title: "Rate cut odds stay low as Trump pressure on Fed continues"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-01T00:00:00.000Z"
event_id: "CM-EVT-4ZQLQPNH91"
event_slug: "kxfed-26sep"
event_question: "Fed funds upper bound post-July 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26SEP-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Sep 16, 2026 meeting?"
  current_price: 0.03
  volume_24h_usd: 492.51
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-09-23T18:05:00Z"
bullets:
  - "Kalshi ladder prices 59% that the fed funds upper bound stays above 3.75% following the July meeting, with only 3% above 4.0%."
  - "Trump's push for rate cuts as economic rocket fuel has not moved the Fed, and Kalshi pricing is consistent with an extended hold rather than any imminent cut."
  - "The ladder shows 98% above 3.50%, meaning the market effectively rules out a cut to or below 3.50% at the next decision point."
  - "Companion Kalshi contract CM-EVT-RWRZ1R3SD6 puts only 6% on a cut greater than 25 basis points this year, reinforcing that deep cut scenarios remain firmly off the table."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "President Donald Trump has sought aggressive rate cuts as economic stimulus but the Fed has held rates steady for five consecutive meetings."
    publisher: "apnews.com"
    published_at: "2026-08-01T00:00:00.000Z"
    source_url: "https://apnews.com/article/trump-interest-rates-midterms-iran-9db7b892114e7863064323396f633c9d"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "apnews.com"
        source_url: "https://apnews.com/article/trump-interest-rates-midterms-iran-9db7b892114e7863064323396f633c9d"
        retrieved_at: "2026-08-01T09:54:52+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves via Federal Reserve; the 3.75% strike at 59% is the pivotal level separating hold-flat from a possible future cut scenario."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "apnews.com: Trump has been losing his battle to cut interest rates | AP News"
    url: "https://apnews.com/article/trump-interest-rates-midterms-iran-9db7b892114e7863064323396f633c9d"
    published_at: "2026-08-01T00:00:00.000Z"
    retrieved_at: "2026-08-01T09:54:52+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
