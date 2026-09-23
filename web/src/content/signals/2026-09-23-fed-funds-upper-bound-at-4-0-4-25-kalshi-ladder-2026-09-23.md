---
signal_id: "CMSIG2026092301"
signal_slug: "fed-funds-upper-bound-at-4-0-4-25-kalshi-ladder-2026-09-23"
headline: "Fed funds upper bound at 4.0-4.25%: Kalshi ladder"
semantic_title: "Fed funds upper bound seen at 4.0-4.25% after hike"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-23T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Fed funds upper bound following September 2026 meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.41
  volume_24h_usd: 2364.86
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder pins the fed funds upper bound in the 4.0-4.25% range: 86% above 4.0%, but only 41% above 4.25%, with sharp drop to 9% above 4.5%."
  - "Barkin and Collins backing restrictive policy is consistent with this pricing; trading volume on the ladder surged 517x day-over-day, signaling fresh market attention."
  - "The 41% probability above 4.25% leaves meaningful room for a further hike, reflecting uncertainty about how long the current restrictive stance holds."
  - "The Kalshi contract on a Fed rate cut greater than 25 basis points this year sits at just 2%, consistent with a market pricing out near-term easing."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Richmond Fed President Tom Barkin and Boston Fed President Susan Collins backed more restrictive policy after last week's rate increase, citing inflation risks outweighing employment risks."
    publisher: "John G. Stevens"
    published_at: "2026-09-23T00:00:00.000Z"
    source_url: "https://wrenews.com/fed-inflation-barkin-collins-restrictive-policy-rate-hikes/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "John G. Stevens"
        source_url: "https://wrenews.com/fed-inflation-barkin-collins-restrictive-policy-rate-hikes/"
        retrieved_at: "2026-09-23T07:47:29+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder shows consensus around 4.0-4.25% upper bound, with volume explosion confirming this is the most actively priced Fed path on the market today."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "John G. Stevens: Fed Inflation Concerns Broaden After Rate Hike | WRE News"
    url: "https://wrenews.com/fed-inflation-barkin-collins-restrictive-policy-rate-hikes/"
    published_at: "2026-09-23T00:00:00.000Z"
    retrieved_at: "2026-09-23T07:47:29+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
