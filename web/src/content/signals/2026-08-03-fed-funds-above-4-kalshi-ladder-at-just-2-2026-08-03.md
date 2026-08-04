---
signal_id: "CMSIG2026080303"
signal_slug: "fed-funds-above-4-kalshi-ladder-at-just-2-2026-08-03"
headline: "Fed funds above 4%: Kalshi ladder at just 2%"
semantic_title: "Rate markets stay short of 4 percent despite inflation pressure"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-03T00:00:00.000Z"
event_id: "CM-EVT-4ZQLQPNH91"
event_slug: "kxfed-26sep"
event_question: "Federal funds rate upper bound (near-term meeting)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26SEP-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Sep 16, 2026 meeting?"
  current_price: 0.02
  volume_24h_usd: 14.93
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-09-23T18:05:00Z"
bullets:
  - "Kalshi ladder implies the Fed funds upper bound near 3.75-4.0%: 56% above 3.75% but only 2% above 4.0%."
  - "ISM at 55.6 with elevated input prices is a hawkish data point, yet the market is fading a full hike to 4.0%, pricing robust manufacturing as insufficient to push the Fed above current range."
  - "The 98% probability above 3.50% confirms no rate-cut expectation either; the market is priced for a hold near current levels."
  - "Resolution: Federal Reserve FOMC statement upper bound figure settles each strike on this Kalshi ladder."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The July ISM Manufacturing PMI hit 55.6, its highest since May 2022, with managers flagging Covid-era pricing volatility and renewed inflation fears."
    publisher: "Jeff Cox"
    published_at: "2026-08-03T00:00:00.000Z"
    source_url: "https://www.cnbc.com/2026/08/03/manufacturing-survey-shows-inflation-worries-adding-to-pressure-on-fed.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Jeff Cox"
        source_url: "https://www.cnbc.com/2026/08/03/manufacturing-survey-shows-inflation-worries-adding-to-pressure-on-fed.html"
        retrieved_at: "2026-08-04T10:33:12+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder shows the market absorbed a four-year ISM high without meaningfully repricing above 4.0%."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Jeff Cox: Manufacturing survey shows inflation worries adding to pressure on Fed"
    url: "https://www.cnbc.com/2026/08/03/manufacturing-survey-shows-inflation-worries-adding-to-pressure-on-fed.html"
    published_at: "2026-08-03T00:00:00.000Z"
    retrieved_at: "2026-08-04T10:33:12+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
