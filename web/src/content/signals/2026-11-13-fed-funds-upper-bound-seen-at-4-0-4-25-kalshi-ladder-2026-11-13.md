---
signal_id: "CMSIG2026111301"
signal_slug: "fed-funds-upper-bound-seen-at-4-0-4-25-kalshi-ladder-2026-11-13"
headline: "Fed funds upper bound seen at 4.0-4.25%: Kalshi ladder"
semantic_title: "Fed funds near 4 to 4.25 percent stays heavily favored"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-13T19:55:01.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Fed funds upper bound (next meeting)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.1
  volume_24h_usd: 185.13
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder pins the Fed funds upper bound in the 4.0-4.25% range: 96% above 4.0%, but only 10% above 4.25%."
  - "Bloomberg's December hike call is consistent with the ladder pricing, though the market stops short of pricing a push above 4.25%."
  - "The sharp drop from 96% to 10% at the 4.25% strike signals the market treats one more hike as near-certain but resists pricing a January follow-through at this level."
  - "A companion Kalshi ladder (CM-EVT-5P6C5JFKT9) shows 50% probability at the 4.25% strike, suggesting a later meeting's terminal rate debate is still live near that threshold."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Bloomberg reports the Fed is on track to hike in December, with debate already shifting to whether January brings another move."
    publisher: "Enda Curran"
    published_at: "2026-11-13T19:55:01.000Z"
    source_url: "https://www.bloomberg.com/news/articles/2026-11-13/fed-set-to-raise-interest-rates-next-month-as-debate-moves-to-january"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Enda Curran"
        source_url: "https://www.bloomberg.com/news/articles/2026-11-13/fed-set-to-raise-interest-rates-next-month-as-debate-moves-to-january"
        retrieved_at: "2026-11-15T07:48:03+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder data provided; no intraday price move claimed, current distribution only."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Enda Curran: Fed on Track to Raise Interest Rates Next Month And Maybe Again in Jan"
    url: "https://www.bloomberg.com/news/articles/2026-11-13/fed-set-to-raise-interest-rates-next-month-as-debate-moves-to-january"
    published_at: "2026-11-13T19:55:01.000Z"
    retrieved_at: "2026-11-15T07:48:03+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
