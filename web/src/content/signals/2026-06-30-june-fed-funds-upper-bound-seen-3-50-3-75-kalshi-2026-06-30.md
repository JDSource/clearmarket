---
signal_id: "CMSIG2026063001"
signal_slug: "june-fed-funds-upper-bound-seen-3-50-3-75-kalshi-2026-06-30"
headline: "June Fed funds upper bound seen 3.50-3.75%: Kalshi"
semantic_title: "Fed funds ceiling anchors at 3.50-3.75% through next meeting"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-30T16:18:22.000Z"
event_id: "CM-EVT-PHWX2H6DM5"
event_slug: "kxfed-26jul"
event_question: "Fed funds upper bound after next meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26JUL-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Jul 29, 2026 meeting?"
  current_price: 0.19
  volume_24h_usd: 1215.51
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-07-29T18:05:00Z"
bullets:
  - "Kalshi ladder pins the post-meeting Fed funds ceiling in the 3.50-3.75% range: 98% above 3.50%, but only 19% above 3.75%."
  - "Jobs data surprise and sticky inflation are consistent with the 3.50-3.75% consensus; the market shows no pricing for a cut to 3.25% or below."
  - "A separate Kalshi contract puts only 25% on any Fed rate cut before 2027, aligning with the ladder's implied hold posture."
  - "Resolves via Federal Reserve official post-meeting rate announcement; any intra-meeting action would be an extreme edge case."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "June jobs preview forecasts unemployment steady at 4.3%, reinforcing a hawkish Fed posture and pushing markets to price out near-term cuts."
    publisher: "interactivecrypto.com"
    published_at: "2026-06-30T16:18:22.000Z"
    source_url: "https://www.interactivecrypto.com/june-jobs-preview-unemployment-rate-steady-at-4-3-markets-brace-for-fed-signal-jun-2026"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "interactivecrypto.com"
        source_url: "https://www.interactivecrypto.com/june-jobs-preview-unemployment-rate-steady-at-4-3-markets-brace-for-fed-signal-jun-2026"
        retrieved_at: "2026-07-01T11:20:57+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder covering post-meeting fed funds upper bound; the 3.50-3.75% band commands the bulk of probability mass."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "interactivecrypto.com: June Jobs Preview: Unemployment Rate Steady at 4.3%, Markets Brace for"
    url: "https://www.interactivecrypto.com/june-jobs-preview-unemployment-rate-steady-at-4-3-markets-brace-for-fed-signal-jun-2026"
    published_at: "2026-06-30T16:18:22.000Z"
    retrieved_at: "2026-07-01T11:20:57+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
