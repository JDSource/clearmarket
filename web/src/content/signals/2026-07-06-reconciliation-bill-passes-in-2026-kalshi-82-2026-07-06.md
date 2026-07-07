---
signal_id: "CMSIG2026070605"
signal_slug: "reconciliation-bill-passes-in-2026-kalshi-82-2026-07-06"
headline: "Reconciliation bill passes in 2026: Kalshi 82%"
semantic_title: "Reconciliation passage in 2026 holds near full pricing"
telemetry: "Kalshi 82%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-06T16:51:28.000Z"
event_id: "CM-EVT-1WV8R9JXH3"
event_slug: "kxreccount-27"
event_question: "How many reconciliation bills will be passed in 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXRECCOUNT-27-1"
  question_raw: "Will 1 reconciliation bills be passed in 2027?"
  current_price: 0.82
  volume_24h_usd: 41.0
  arbitration_model: "kalshi_staff"
  resolution_source: "Library of Congress"
  resolves_at: "2027-01-02T15:00:00Z"
bullets:
  - "Kalshi prediction market prices an 82% chance at least one reconciliation bill passes in 2026."
  - "Johnson's commitment to re-pass the SAVE America Act is consistent with Kalshi's high probability, though the repeated restarts highlight legislative fragility."
  - "The 18% residual probability reflects ongoing Republican intra-party friction, as dissenting GOP members publicly call for Trump to change course."
  - "Kalshi resolves via Library of Congress bill-tracking data; the contract counts bills enacted, not passed by one chamber, so Senate passage remains the critical gating step."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "House Speaker Mike Johnson said the House will pass the SAVE America Act again after caving to MAGA hardliners and Trump's latest demands."
    publisher: "democracydocket.com"
    published_at: "2026-07-06T16:51:28.000Z"
    source_url: "https://www.democracydocket.com/news-alerts/mike-johnson-house-pass-donald-trump-voter-supression-save-america-act/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "democracydocket.com"
        source_url: "https://www.democracydocket.com/news-alerts/mike-johnson-house-pass-donald-trump-voter-supression-save-america-act/"
        retrieved_at: "2026-07-07T10:52:00+00:00"
  - type: "pm_response"
    notes: "Kalshi resolves via Library of Congress records; the 82% read reflects passage expectation but not certainty given documented Senate complications."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "democracydocket.com: Johnson says House will pass stalled SAVE America Act ‘one more time’"
    url: "https://www.democracydocket.com/news-alerts/mike-johnson-house-pass-donald-trump-voter-supression-save-america-act/"
    published_at: "2026-07-06T16:51:28.000Z"
    retrieved_at: "2026-07-07T10:52:00+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
