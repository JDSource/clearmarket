---
signal_id: "CMSIG2026090402"
signal_slug: "later-fed-funds-upper-bound-implied-3-75-4-0-kalshi-72-2026-09-04"
headline: "Later Fed funds upper bound implied 3.75-4.0%: Kalshi 72%"
semantic_title: "Markets put short odds on a rate hike above 4 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-04T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Fed funds upper bound, later 2026 meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.31
  volume_24h_usd: 5.54
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder (CM-EVT-MR57HVWJT3) implies the later-cycle Fed funds upper bound in the 3.75-4.00% range, with 72% above 3.75% but only 31% above 4.00%."
  - "Fed Governor Christopher Waller's pause signal aligns with near-term hold pricing, but this longer-horizon ladder shows meaningful odds a hike above 4.00% is still on the table."
  - "The spread between this ladder and the September ladder (CM-EVT-4ZQLQPNH91, 2% above 4.00%) shows the market pricing pause now but keeping a hike optionality later."
  - "Kalshi contract resolves via the Federal Reserve's official rate announcement for the relevant meeting date."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The US Dollar Index weakened after Fed Governor Christopher Waller signaled a potential rate pause, while market probability for a September Fed rate hike was cited at 50.2% by one source."
    publisher: "fxstreet.com"
    published_at: "2026-09-04T00:00:00.000Z"
    source_url: "https://www.fxstreet.com/news/united-states-dollar-index-weakens-as-feds-waller-signals-rate-pause-202609040225"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "fxstreet.com"
        source_url: "https://www.fxstreet.com/news/united-states-dollar-index-weakens-as-feds-waller-signals-rate-pause-202609040225"
        retrieved_at: "2026-09-04T12:28:22+00:00"
  - type: "pm_response"
    notes: "Kalshi hosts both the near-term September contract and this longer-dated ladder; the divergence between them reflects term-structure uncertainty."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "fxstreet.com: United States Dollar Index weakens as Fed’s Waller signals rate pause"
    url: "https://www.fxstreet.com/news/united-states-dollar-index-weakens-as-feds-waller-signals-rate-pause-202609040225"
    published_at: "2026-09-04T00:00:00.000Z"
    retrieved_at: "2026-09-04T12:28:22+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
