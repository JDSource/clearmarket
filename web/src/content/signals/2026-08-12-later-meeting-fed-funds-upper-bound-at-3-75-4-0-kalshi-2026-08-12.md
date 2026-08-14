---
signal_id: "CMSIG2026081203"
signal_slug: "later-meeting-fed-funds-upper-bound-at-3-75-4-0-kalshi-2026-08-12"
headline: "Later-meeting Fed funds upper bound at 3.75-4.0%: Kalshi"
semantic_title: "Longer-run Fed funds upper bound builds toward 3.75-4.0%"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-12T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Fed funds upper bound at a later FOMC meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.23
  volume_24h_usd: 4.3
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder for a later meeting prices 79% above 3.50% and 53% above 3.75%, implying the mode sits in the 3.75-4.0% range."
  - "News consensus expects a September hold, but the later-meeting ladder shows markets see rates staying elevated well beyond September."
  - "Compare the near-term ladder (CM-EVT-4ZQLQPNH91) at only 29% above 3.75%: the term structure implies cuts arrive slowly, not in one move."
  - "Resolves via Federal Reserve policy announcement for the relevant meeting; the wide spread between 3.75% and 4.0% reflects genuine uncertainty on cut timing."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Economists and market participants expect the Fed to leave rates unchanged in September following soft July inflation data."
    publisher: "economictimes.indiatimes.com"
    published_at: "2026-08-12T00:00:00.000Z"
    source_url: "https://economictimes.indiatimes.com/markets/us-stocks/news/us-fed-expected-to-leave-rates-unchanged-next-month-after-soft-inflation-data/articleshow/133191697.cms"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "economictimes.indiatimes.com"
        source_url: "https://economictimes.indiatimes.com/markets/us-stocks/news/us-fed-expected-to-leave-rates-unchanged-next-month-after-soft-inflation-data/articleshow/133191697.cms"
        retrieved_at: "2026-08-14T09:03:59+00:00"
  - type: "pm_response"
    notes: "Kalshi's later-meeting ladder diverges meaningfully from the near-term one, revealing a slow-cut path rather than a sharp dovish pivot."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "economictimes.indiatimes.com: US Fed expected to leave rates unchanged next month after soft inflati"
    url: "https://economictimes.indiatimes.com/markets/us-stocks/news/us-fed-expected-to-leave-rates-unchanged-next-month-after-soft-inflation-data/articleshow/133191697.cms"
    published_at: "2026-08-12T00:00:00.000Z"
    retrieved_at: "2026-08-14T09:03:59+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
