---
signal_id: "CMSIG2026112103"
signal_slug: "fed-funds-upper-bound-above-4-25-kalshi-ladder-85-2026-11-21"
headline: "Fed funds upper bound above 4.25%: Kalshi ladder 85%"
semantic_title: "Fed funds above 4.25 percent stays near 85 percent odds"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-21T13:10:03.000Z"
event_id: "CM-EVT-KWX3HB7XG9"
event_slug: "kxfed-27apr"
event_question: "Federal funds upper bound (current cycle high)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-27APR-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Apr 28, 2027 meeting?"
  current_price: 0.85
  volume_24h_usd: 1.7
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2027-05-05T18:05:00Z"
bullets:
  - "Kalshi ladder prices 85% that the federal funds upper bound will exceed 4.25%, with near-certainty (90-99%) across all rungs from 0% to 4.0%."
  - "Fed Governor Lisa Cook's dissent in favor of holding rates sits in tension with the ladder's strong above-4.25% pricing, implying markets lean toward the hiking camp over the hold camp."
  - "The gap between 97% above 4.0% on the companion ladder (CM-EVT-MR57HVWJT3) and 85% above 4.25% here defines a narrow but meaningful zone of uncertainty around that precise strike."
  - "Resolves via FOMC target rate announcement; Cook's public dissent adds event risk that could shift the 4.25% tail if other governors align with her hold view."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Fed Governor Lisa Cook explained her October FOMC dissent, arguing that holding rates is itself an active policy decision."
    publisher: "Victoria Shinder"
    published_at: "2026-11-21T13:10:03.000Z"
    source_url: "https://ratebrief.org/news/dollar/fed-cook-santiago-dissent-october-hold-preferred-hike-pce-3-8-percent-core-3-2-inflation-67-months-above-target-ai-buildout/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Victoria Shinder"
        source_url: "https://ratebrief.org/news/dollar/fed-cook-santiago-dissent-october-hold-preferred-hike-pce-3-8-percent-core-3-2-inflation-67-months-above-target-ai-buildout/"
        retrieved_at: "2026-11-24T07:47:50+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder; resolution source is the FOMC federal funds rate decision; Cook's dissent is a live risk factor for the 4.25-4.5% rung."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Victoria Shinder: Cook explains her October dissent: holding rates is a policy action to"
    url: "https://ratebrief.org/news/dollar/fed-cook-santiago-dissent-october-hold-preferred-hike-pce-3-8-percent-core-3-2-inflation-67-months-above-target-ai-buildout/"
    published_at: "2026-11-21T13:10:03.000Z"
    retrieved_at: "2026-11-24T07:47:50+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
