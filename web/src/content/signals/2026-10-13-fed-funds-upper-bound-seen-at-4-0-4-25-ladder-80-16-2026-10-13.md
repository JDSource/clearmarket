---
signal_id: "CMSIG2026101302"
signal_slug: "fed-funds-upper-bound-seen-at-4-0-4-25-ladder-80-16-2026-10-13"
headline: "Fed funds upper bound seen at 4.0-4.25%: ladder 80%/16%"
semantic_title: "Fed funds upper bound stays near 4 percent after hold decision"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-13T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Fed funds upper bound following recent FOMC meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.16
  volume_24h_usd: 12.91
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Prediction market ladder prices 80% odds the fed funds upper bound is above 4.0%, but only 16% above 4.25%, implying consensus sits at exactly the 4.0-4.25% range."
  - "The unanimous hold decision reported under Chair Kevin Warsh is fully consistent with the ladder's pricing, which places negligible probability on rates at 4.5% or higher."
  - "Warsh's signal of openness to future increases is partially reflected in the ladder's 16% at 4.25%, but the market is not pricing a near-term hike as likely."
  - "The September jobs miss of 29,000 provides a cross-market read: weak labor data reduces the probability the 4.25%+ tail gets repriced upward near-term."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "New Fed Chair Kevin Warsh led a unanimous decision to hold rates steady while signaling openness to future increases."
    publisher: "cnnbc.com"
    published_at: "2026-10-13T00:00:00.000Z"
    source_url: "https://cnnbc.com/federal-reserve-holds-rates-steady-as-new-chairman-kevin-warsh-signals-openness-to-future-increases"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "cnnbc.com"
        source_url: "https://cnnbc.com/federal-reserve-holds-rates-steady-as-new-chairman-kevin-warsh-signals-openness-to-future-increases"
        retrieved_at: "2026-10-13T15:32:34+00:00"
  - type: "pm_response"
    notes: "The prediction market ladder, covering the fed funds upper bound following the recent FOMC meeting, is consistent with a hold as reported."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "cnnbc.com: Federal Reserve Holds Rates Steady as New Chairman Kevin Warsh Signals"
    url: "https://cnnbc.com/federal-reserve-holds-rates-steady-as-new-chairman-kevin-warsh-signals-openness-to-future-increases"
    published_at: "2026-10-13T00:00:00.000Z"
    retrieved_at: "2026-10-13T15:32:34+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
