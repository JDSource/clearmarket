---
signal_id: "CMSIG2026060301"
signal_slug: "june-fed-funds-upper-bound-seen-3-50-3-75-kalshi-2026-06-03"
headline: "June Fed funds upper bound seen 3.50-3.75%: Kalshi"
semantic_title: "Fed funds upper bound hardens near 3.50-3.75 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-03T00:00:00.000Z"
event_id: "CM-EVT-RJ6SMJGK50"
event_slug: "kxfed-26jun"
event_question: "June 2026 Fed funds upper bound"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26JUN-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Jun 17, 2026 meeting?"
  current_price: 0.02
  volume_24h_usd: 1599.49
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-06-17T18:05:00Z"
bullets:
  - "Kalshi prices the June 2026 Fed funds upper bound firmly in the 3.50-3.75% range: 98% above 3.50% but only 2% above 3.75%."
  - "Hammack's hike signal is consistent with the upper tail holding at 3.75%, but the market assigns near-zero probability to any actual hike above that level."
  - "Williams separately said policy is 'in the right place,' and the distribution reflects that consensus: a hold near 3.50-3.75%, not a hike cycle."
  - "A companion Kalshi ladder (CM-EVT-4ZQLQPNH91) for a later date shows the upper bound still seen 3.50-3.75% but with 34% above 3.75%, suggesting the market prices more hike risk further out."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Fed Governor Beth Hammack signaled a rate hike may be needed soon as inflation risks intensify."
    publisher: "Anupam Nagar"
    published_at: "2026-06-03T00:00:00.000Z"
    source_url: "https://economictimes.indiatimes.com/markets/us-stocks/news/feds-hammack-signals-rate-hike-may-be-needed-soon-as-inflation-risks-intensify/articleshow/131476088.cms"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Anupam Nagar"
        source_url: "https://economictimes.indiatimes.com/markets/us-stocks/news/feds-hammack-signals-rate-hike-may-be-needed-soon-as-inflation-risks-intensify/articleshow/131476088.cms"
        retrieved_at: "2026-06-05T11:24:05+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolves via Federal Reserve announcement; the sharp cliff between 3.75% and 4.0% is the key distributional signal."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Anupam Nagar: Fed's Hammack signals rate hike may be needed soon as inflation risks"
    url: "https://economictimes.indiatimes.com/markets/us-stocks/news/feds-hammack-signals-rate-hike-may-be-needed-soon-as-inflation-risks-intensify/articleshow/131476088.cms"
    published_at: "2026-06-03T00:00:00.000Z"
    retrieved_at: "2026-06-05T11:24:05+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
