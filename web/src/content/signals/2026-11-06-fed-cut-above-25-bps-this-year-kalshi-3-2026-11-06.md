---
signal_id: "CMSIG2026110602"
signal_slug: "fed-cut-above-25-bps-this-year-kalshi-3-2026-11-06"
headline: "Fed cut above 25 bps this year: Kalshi 3%"
semantic_title: "Market puts long odds against an outsized Fed cut"
telemetry: "Kalshi 3%"
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
  current_price: 0.029
  volume_24h_usd: 11.2
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi prices only a 3% chance the Federal Reserve cuts rates by more than 25 basis points in 2026."
  - "New York Fed President John Williams's hawkish remarks on elevated inflation are fully consistent with the near-zero probability of an outsized cut."
  - "October nonfarm payrolls came in at 165,000, well above the 59,000 forecast, reinforcing the case against aggressive easing."
  - "Resolution via an official Federal Reserve rate decision announcement for any remaining 2026 meeting."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "New York Federal Reserve President John Williams said inflation remains too high and reiterated the 2% target amid multiple price shocks."
    publisher: "Max Rego"
    published_at: "2026-11-06T15:18:36.000Z"
    source_url: "https://thehill.com/business/6203854-fed-williams-inflation-too-high/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Max Rego"
        source_url: "https://thehill.com/business/6203854-fed-williams-inflation-too-high/"
        retrieved_at: "2026-11-09T07:47:40+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolves on a Federal Reserve decision; at 3%, the market is firmly aligned with Williams's hawkish posture."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Max Rego: Fed’s Williams says inflation too high, targets 2 percent"
    url: "https://thehill.com/business/6203854-fed-williams-inflation-too-high/"
    published_at: "2026-11-06T15:18:36.000Z"
    retrieved_at: "2026-11-09T07:47:40+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
