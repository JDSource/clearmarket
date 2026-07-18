---
signal_id: "CMSIG2026071702"
signal_slug: "fed-funds-above-3-75-by-later-date-kalshi-57-29-2026-07-17"
headline: "Fed funds above 3.75% by later date: Kalshi 57%/29%"
semantic_title: "Rate hike consensus fractures around 3.75-4 percent horizon"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-17T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Later-horizon Fed funds upper bound"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.29
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi prices this later-horizon Fed funds contract at 57% above 3.75% but only 29% above 4.00%, implying a contested 3.75-4.00% range."
  - "Fed official broad-based inflation warning is consistent with elevated uncertainty above 3.75%, but the market stops well short of pricing a decisive hike above 4.00%."
  - "Contrast with the June contract's 6% above 3.75%: the term structure shows markets are open to a later move but not an imminent one."
  - "Resolves via the Fed's official rate announcement for the relevant FOMC meeting date."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "A US Fed official warned of broad-based inflation pressures as business firms urged policy action to contain rising price expectations."
    publisher: "economictimes.indiatimes.com"
    published_at: "2026-07-17T00:00:00.000Z"
    source_url: "https://economictimes.indiatimes.com/markets/us-stocks/news/us-fed-official-warns-of-broad-based-inflation-as-firms-urge-action/articleshow/132465098.cms"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "economictimes.indiatimes.com"
        source_url: "https://economictimes.indiatimes.com/markets/us-stocks/news/us-fed-official-warns-of-broad-based-inflation-as-firms-urge-action/articleshow/132465098.cms"
        retrieved_at: "2026-07-18T09:20:01+00:00"
  - type: "pm_response"
    notes: "Kalshi's later-horizon contract shows a materially wider distribution than the June contract, reflecting genuine uncertainty about the policy path beyond the near term."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "economictimes.indiatimes.com: US Fed official warns of 'broad-based' inflation as firms urge action"
    url: "https://economictimes.indiatimes.com/markets/us-stocks/news/us-fed-official-warns-of-broad-based-inflation-as-firms-urge-action/articleshow/132465098.cms"
    published_at: "2026-07-17T00:00:00.000Z"
    retrieved_at: "2026-07-18T09:20:01+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
