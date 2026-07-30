---
signal_id: "CMSIG2026072901"
signal_slug: "fed-funds-upper-bound-seen-3-75-4-0-kalshi-ladder-2026-07-29"
headline: "Fed funds upper bound seen 3.75-4.0%: Kalshi ladder"
semantic_title: "Fed funds upper bound stays near 3.75 percent after hold"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-29T00:00:00.000Z"
event_id: "CM-EVT-4ZQLQPNH91"
event_slug: "kxfed-26sep"
event_question: "July 2026 Fed funds upper bound"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26SEP-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Sep 16, 2026 meeting?"
  current_price: 0.04
  volume_24h_usd: 378.95
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-09-23T18:05:00Z"
bullets:
  - "Kalshi ladder prices the July 2026 Fed funds upper bound in the 3.75-4.0% range, with 99% above 3.50% but only 4% above 4.0%."
  - "The Fed's 9-3 hold decision keeps the upper bound at 3.75%, consistent with the ladder's sharp drop-off above that level."
  - "Three dissents favoring a hike push modest odds to the 4.0% strike, but the distribution shows markets still see a hike as a tail risk."
  - "The Kalshi contract on a rate cut greater than 25 basis points this year sits at 9%, confirming the market sees little near-term easing."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The Federal Reserve voted 9-3 to hold the federal funds rate at 3.5%-3.75% at its July meeting, with three dissenters favoring a hike."
    publisher: "euronews.com"
    published_at: "2026-07-29T00:00:00.000Z"
    source_url: "https://www.euronews.com/business/2026/07/29/us-federal-reserve-holds-interest-rates-steady-as-three-policymakers-back-hike"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "euronews.com"
        source_url: "https://www.euronews.com/business/2026/07/29/us-federal-reserve-holds-interest-rates-steady-as-three-policymakers-back-hike"
        retrieved_at: "2026-07-30T10:20:48+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves via Federal Reserve policy announcements; the 3.75% upper bound is the current modal outcome with steep probability decay above it."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "euronews.com: US Federal Reserve holds interest rates steady as three policymakers b"
    url: "https://www.euronews.com/business/2026/07/29/us-federal-reserve-holds-interest-rates-steady-as-three-policymakers-back-hike"
    published_at: "2026-07-29T00:00:00.000Z"
    retrieved_at: "2026-07-30T10:20:48+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
