---
signal_id: "CMSIG2026111901"
signal_slug: "fed-funds-upper-bound-above-4-0-kalshi-92-2026-11-19"
headline: "Fed funds upper bound above 4.0%: Kalshi 92%"
semantic_title: "Fed funds above 4 percent stays near full pricing"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-19T08:55:46.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Fed funds upper bound (current cycle peak)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.03
  volume_24h_usd: 116.27
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder pins the Fed funds upper bound at 4.0-4.25%, with 92% pricing above 4.0% but only 3% above 4.25%."
  - "FOMC minutes flagging near-unanimous support for more hikes are consistent with the ladder's strong 4.0% floor pricing."
  - "The sharp cliff from 92% at 4.0% to 3% at 4.25% signals the market sees 4.0-4.25% as the likely terminal range, not an open-ended hiking path."
  - "Resolves via the Fed's official rate announcement; the 1% pricing above 4.5% implies virtually no tail risk for an outsized move."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "FOMC minutes showed 'almost all' Fed policymakers saw further rate hikes as likely to combat persistently high inflation."
    publisher: "RTÉ News"
    published_at: "2026-11-19T08:55:46.000Z"
    source_url: "https://www.rte.ie/news/business/2026/1119/1599800-us-federal-reserve-minutes/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "RTÉ News"
        source_url: "https://www.rte.ie/news/business/2026/1119/1599800-us-federal-reserve-minutes/"
        retrieved_at: "2026-11-22T07:47:40+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder data; distribution sharply concentrated at the 4.0-4.25% band with minimal tail above."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "RTÉ News: Almost all Fed policymakers see more rate hikes as likely"
    url: "https://www.rte.ie/news/business/2026/1119/1599800-us-federal-reserve-minutes/"
    published_at: "2026-11-19T08:55:46.000Z"
    retrieved_at: "2026-11-22T07:47:40+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
