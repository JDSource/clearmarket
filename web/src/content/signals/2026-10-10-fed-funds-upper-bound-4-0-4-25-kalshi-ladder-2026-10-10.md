---
signal_id: "CMSIG2026101001"
signal_slug: "fed-funds-upper-bound-4-0-4-25-kalshi-ladder-2026-10-10"
headline: "Fed funds upper bound ~4.0-4.25%: Kalshi ladder"
semantic_title: "Fed funds upper bound seen near 4.0 to 4.25 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-10T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Fed funds rate upper bound (next meeting)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.19
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder prices the Fed funds upper bound in the 4.0-4.25% range: 82% chance above 4.0%, only 19% above 4.25%."
  - "Fed minutes confirmed broad support for September hike and a likely additional hike; Kalshi pricing is broadly consistent, with volume surging 91x day-over-day signaling intense fresh attention."
  - "The 17% gap between 4.0% and 4.25% strikes indicates the market accepts one more hike but is skeptical of two."
  - "Companion Kalshi contract on a cut greater than 25 basis points sits at just 3%, confirming the market sees no near-term easing pivot."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Federal Reserve minutes from the September meeting showed most policymakers supported the rate hike and saw a case for another increase by year-end."
    publisher: "nexusstocksdaily.com"
    published_at: "2026-10-10T00:00:00.000Z"
    source_url: "https://nexusstocksdaily.com/fed-minutes-reveal-split-over-inflation-risks-and-need-for-rate-hikes/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "nexusstocksdaily.com"
        source_url: "https://nexusstocksdaily.com/fed-minutes-reveal-split-over-inflation-risks-and-need-for-rate-hikes/"
        retrieved_at: "2026-10-11T14:35:49+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder, resolves via Federal Reserve; extraordinary volume spike (9013% day-over-day) confirms this is the market's focal rate contract heading into the October 27-28 meeting."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "nexusstocksdaily.com: Fed minutes reveal split over inflation risks and need for rate hikes"
    url: "https://nexusstocksdaily.com/fed-minutes-reveal-split-over-inflation-risks-and-need-for-rate-hikes/"
    published_at: "2026-10-10T00:00:00.000Z"
    retrieved_at: "2026-10-11T14:35:49+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
