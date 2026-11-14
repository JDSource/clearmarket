---
signal_id: "CMSIG2026111301"
signal_slug: "fed-funds-upper-bound-seen-4-0-4-25-kalshi-ladder-2026-11-13"
headline: "Fed funds upper bound seen 4.0-4.25%: Kalshi ladder"
semantic_title: "Fed funds upper bound near 4.0-4.25 percent stays firmly priced"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-13T19:55:01.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Fed funds upper bound after next meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.1
  volume_24h_usd: 1893.33
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder puts 97% odds on the upper bound exceeding 4.0%, but only 10% on exceeding 4.25%, pinning the consensus range at 4.0-4.25%."
  - "Bloomberg's December hike reporting is consistent with the ladder's distribution; the January question keeps 4.25% at just 10%, suggesting markets are not yet fully pricing a second consecutive hike."
  - "Trading volume surged 65.8x day over day on this contract, signaling the Bloomberg report and Fed speaker commentary are drawing significant fresh attention."
  - "The companion Kalshi contract on Fed rate cuts before 2027 sits at just 1%, reinforcing that easing is effectively off the table in the near term."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Bloomberg reports the Fed is on track to raise rates in December and is debating whether to hike again in January 2026."
    publisher: "Enda Curran"
    published_at: "2026-11-13T19:55:01.000Z"
    source_url: "https://www.bloomberg.com/news/articles/2026-11-13/fed-set-to-raise-interest-rates-next-month-as-debate-moves-to-january"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Enda Curran"
        source_url: "https://www.bloomberg.com/news/articles/2026-11-13/fed-set-to-raise-interest-rates-next-month-as-debate-moves-to-january"
        retrieved_at: "2026-11-14T07:47:51+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves via Federal Reserve decision; the sharp cutoff at the 4.25% strike is the key tension point to watch as January meeting debate develops."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Enda Curran: Fed on Track to Raise Interest Rates Next Month And Maybe Again in Jan"
    url: "https://www.bloomberg.com/news/articles/2026-11-13/fed-set-to-raise-interest-rates-next-month-as-debate-moves-to-january"
    published_at: "2026-11-13T19:55:01.000Z"
    retrieved_at: "2026-11-14T07:47:51+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
