---
signal_id: "CMSIG2026091402"
signal_slug: "fed-funds-upper-bound-at-3-75-4-0-kalshi-ladder-2026-09-14"
headline: "Fed funds upper bound at 3.75-4.0%: Kalshi ladder"
semantic_title: "Fed funds upper bound seen near 4 percent after hike"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-14T00:00:00.000Z"
event_id: "CM-EVT-4ZQLQPNH91"
event_slug: "kxfed-26sep"
event_question: "Federal funds rate upper bound post-September 2026 meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26SEP-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Sep 16, 2026 meeting?"
  current_price: 0.02
  volume_24h_usd: 3520.56
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-09-23T18:05:00Z"
bullets:
  - "The Kalshi ladder prices the federal funds upper bound in the 3.75-4.00% range: 87% above 3.75% but only 2% above 4.00%."
  - "Today's confirmed hike to 3.75-4.00% is directly consistent with the ladder's sharp break between 3.75% and 4.00% strikes."
  - "Strikes above 4.00% price at just 1-2%, meaning markets see near-zero chance the Fed delivered a larger-than-25-basis-point move."
  - "The Polymarket contract on any 2026 hike at 95% confirms the direction; the ladder adds granularity on the magnitude, with the market pinning a single 25-basis-point step."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Reuters reported the Fed was set for its first rate hike under Chair Kevin Warsh, confirmed today with a move to 3.75-4.00%."
    publisher: "Ann Saphir"
    published_at: "2026-09-14T00:00:00.000Z"
    source_url: "https://www.reuters.com/business/feds-table-is-set-rate-hike-first-under-warsh-2026-09-14/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Ann Saphir"
        source_url: "https://www.reuters.com/business/feds-table-is-set-rate-hike-first-under-warsh-2026-09-14/"
        retrieved_at: "2026-09-16T13:02:46+00:00"
  - type: "pm_response"
    notes: "The Kalshi ladder's sharp cliff at 4.00% precisely captures the market-implied 25-basis-point hike outcome confirmed today."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Ann Saphir: Fed's table is set for a rate hike, a first under Warsh | Reuters"
    url: "https://www.reuters.com/business/feds-table-is-set-rate-hike-first-under-warsh-2026-09-14/"
    published_at: "2026-09-14T00:00:00.000Z"
    retrieved_at: "2026-09-16T13:02:46+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
