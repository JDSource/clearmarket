---
signal_id: "CMSIG2026060301"
signal_slug: "june-fed-funds-upper-bound-seen-3-50-3-75-kalshi-2026-06-03"
headline: "June Fed funds upper bound seen 3.50-3.75%: Kalshi"
semantic_title: "Rate hike consensus fractures above 3.75 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-03T00:00:00.000Z"
event_id: "CM-EVT-PHWX2H6DM5"
event_slug: "kxfed-26jul"
event_question: "Fed funds upper bound (near-term meeting)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26JUL-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Jul 29, 2026 meeting?"
  current_price: 0.14
  volume_24h_usd: 14.28
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-07-29T18:05:00Z"
bullets:
  - "Kalshi pins the near-term Fed funds upper bound in the 3.50-3.75% range: 95% above 3.50% but only 14% above 3.75%."
  - "Hammack's rate-hike signal is consistent with a market that prices the current 3.50% floor as a floor, but not a departure above 3.75%."
  - "A companion Kalshi ladder (CM-EVT-4ZQLQPNH91) shows a nearly identical distribution, with only 34% above 3.75%, suggesting the hike call is not yet priced as base case."
  - "Resolves via Federal Reserve official rate announcement; any inter-meeting move or skip would shift the distribution sharply."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Fed's Beth Hammack signaled a rate hike may be needed soon as inflation risks intensify, joining a broader hawkish chorus from Fed officials."
    publisher: "Anupam Nagar"
    published_at: "2026-06-03T00:00:00.000Z"
    source_url: "https://economictimes.indiatimes.com/markets/us-stocks/news/feds-hammack-signals-rate-hike-may-be-needed-soon-as-inflation-risks-intensify/articleshow/131476088.cms"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Anupam Nagar"
        source_url: "https://economictimes.indiatimes.com/markets/us-stocks/news/feds-hammack-signals-rate-hike-may-be-needed-soon-as-inflation-risks-intensify/articleshow/131476088.cms"
        retrieved_at: "2026-06-05T12:03:19+00:00"
  - type: "pm_response"
    notes: "Two independent Kalshi ladders converge on the same 3.50-3.75% implied range, reinforcing the distribution signal despite hawkish Fed commentary."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Anupam Nagar: Fed's Hammack signals rate hike may be needed soon as inflation risks"
    url: "https://economictimes.indiatimes.com/markets/us-stocks/news/feds-hammack-signals-rate-hike-may-be-needed-soon-as-inflation-risks-intensify/articleshow/131476088.cms"
    published_at: "2026-06-03T00:00:00.000Z"
    retrieved_at: "2026-06-05T12:03:19+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
