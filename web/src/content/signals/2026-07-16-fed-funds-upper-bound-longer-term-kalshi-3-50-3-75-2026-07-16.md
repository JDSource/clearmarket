---
signal_id: "CMSIG2026071605"
signal_slug: "fed-funds-upper-bound-longer-term-kalshi-3-50-3-75-2026-07-16"
headline: "Fed funds upper bound longer-term: Kalshi 3.50-3.75%"
semantic_title: "Longer-horizon rate path nears full pricing at 3.5 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-16T12:43:40.000Z"
event_id: "CM-EVT-PHWX2H6DM5"
event_slug: "kxfed-26jul"
event_question: "Longer-term Fed funds upper bound"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26JUL-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Jul 29, 2026 meeting?"
  current_price: 0.04
  volume_24h_usd: 1636.02
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-08-05T18:05:00Z"
bullets:
  - "Kalshi's longer-horizon ladder shows 98% above 3.50% but only 4% above 3.75%, tightly pinning the expected upper bound at 3.50-3.75%."
  - "Soft headline retail sales driven by energy price drag did not shift this distribution; the market treats underlying consumer spending as supportive of a gradual, limited easing path."
  - "The near-certainty above 3.50% combined with the cliff at 3.75% reflects consensus that the Fed will cut but stop well above prior cycle lows."
  - "Resolves via Federal Reserve official rate decision at the relevant FOMC meeting date specified in the contract."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "June US retail sales rose only slightly as lower gasoline prices weighed on receipts, though underlying consumer momentum remained, prompting economists to upgrade second-quarter GDP estimates."
    publisher: "AOL"
    published_at: "2026-07-16T12:43:40.000Z"
    source_url: "https://www.aol.com/articles/us-retail-sales-rise-marginally-124340000.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "AOL"
        source_url: "https://www.aol.com/articles/us-retail-sales-rise-marginally-124340000.html"
        retrieved_at: "2026-07-17T09:53:11+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder contract; the 98%/4% split across the 3.50/3.75 strikes is the dominant signal in this distribution."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "AOL: Lower gasoline prices restrain US retail sales, underlying momentum re"
    url: "https://www.aol.com/articles/us-retail-sales-rise-marginally-124340000.html"
    published_at: "2026-07-16T12:43:40.000Z"
    retrieved_at: "2026-07-17T09:53:11+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
