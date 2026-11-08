---
signal_id: "CMSIG2026110601"
signal_slug: "fed-rate-cut-above-25bp-in-2026-kalshi-1-2026-11-06"
headline: "Fed rate cut above 25bp in 2026: Kalshi 1%"
semantic_title: "Odds on outsized Fed cut this year stay near zero"
telemetry: "Kalshi 1%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-06T15:18:36.000Z"
event_id: "CM-EVT-RWRZ1R3SD6"
event_slug: "kxlargecut-26"
event_question: "Will the Federal Reserve do a rate cut greater than 25 basis points this year?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXLARGECUT-26"
  question_raw: "Will the Fed cut rates more than 25 bps in 2026?"
  current_price: 0.013
  volume_24h_usd: 0.69
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi prices only 1% odds on a Fed rate cut greater than 25 basis points in 2026."
  - "New York Fed President John Williams called inflation 'absolutely too high,' yet the Kalshi contract already sits at near-zero, market is fully aligned with the hawkish rhetoric."
  - "Companion context: multiple officials have flagged rate-hike consideration after the October blowout payrolls print of 165,000 jobs versus a 59,000 consensus."
  - "Resolves via Federal Reserve official rate decision; any cut above 25bp in 2026 would be an extraordinary policy reversal from current stance."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "New York Fed President John Williams said inflation remains too high and the Fed is targeting 2 percent, reinforcing a hawkish posture after October's strong jobs report."
    publisher: "Max Rego"
    published_at: "2026-11-06T15:18:36.000Z"
    source_url: "https://thehill.com/business/6203854-fed-williams-inflation-too-high/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Max Rego"
        source_url: "https://thehill.com/business/6203854-fed-williams-inflation-too-high/"
        retrieved_at: "2026-11-08T07:47:56+00:00"
  - type: "pm_response"
    notes: "Kalshi contract at 1% leaves essentially no probability on a large cut, consistent with Williams's public comments and the jobs data."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Max Rego: Fed’s Williams says inflation too high, targets 2 percent"
    url: "https://thehill.com/business/6203854-fed-williams-inflation-too-high/"
    published_at: "2026-11-06T15:18:36.000Z"
    retrieved_at: "2026-11-08T07:47:56+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
