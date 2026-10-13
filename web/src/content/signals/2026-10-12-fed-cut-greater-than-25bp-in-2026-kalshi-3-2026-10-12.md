---
signal_id: "CMSIG2026101203"
signal_slug: "fed-cut-greater-than-25bp-in-2026-kalshi-3-2026-10-12"
headline: "Fed cut greater than 25bp in 2026: Kalshi 3%"
semantic_title: "A jumbo Fed rate cut this year stays a very long shot"
telemetry: "Kalshi 3%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-12T00:00:00.000Z"
event_id: "CM-EVT-RWRZ1R3SD6"
event_slug: "kxlargecut-26"
event_question: "Will the Federal Reserve do a rate cut greater than 25 basis points this year?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXLARGECUT-26"
  question_raw: "Will the Fed cut rates more than 25 bps in 2026?"
  current_price: 0.028
  volume_24h_usd: 120.2
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi puts only 3% odds on the Fed cutting by more than 25 basis points at any remaining 2026 meeting."
  - "The September hike to 3.75-4.00% and hawkish minutes language leave an outsized cut in 2026 almost entirely off the table per the Kalshi contract."
  - "The Kalshi ladder on the next meeting upper bound pricing 83% above 4.0% further reinforces that cuts, let alone jumbo ones, are not the base case."
  - "Resolves via the Federal Reserve's official policy decisions for all remaining 2026 FOMC meetings; a single cut exceeding 25bp would trigger resolution."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Central bank minutes confirmed the FOMC raised rates 25 basis points in September to 3.75-4.00% and signaled openness to further tightening, ruling out near-term aggressive easing."
    publisher: "Marketing"
    published_at: "2026-10-12T00:00:00.000Z"
    source_url: "https://trivesta.com.au/weekly-market-recap/central-bank-minutes-in-focus-as-equities-advance"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Marketing"
        source_url: "https://trivesta.com.au/weekly-market-recap/central-bank-minutes-in-focus-as-equities-advance"
        retrieved_at: "2026-10-13T07:48:09+00:00"
  - type: "pm_response"
    notes: "Kalshi prices a greater-than-25bp Fed cut in 2026 at just 3%, fully aligned with the tightening posture confirmed in September's minutes."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Marketing: Central Bank Minutes in Focus as Equities Advance - Trivesta"
    url: "https://trivesta.com.au/weekly-market-recap/central-bank-minutes-in-focus-as-equities-advance"
    published_at: "2026-10-12T00:00:00.000Z"
    retrieved_at: "2026-10-13T07:48:09+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
