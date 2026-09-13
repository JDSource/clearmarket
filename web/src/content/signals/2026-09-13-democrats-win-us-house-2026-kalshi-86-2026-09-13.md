---
signal_id: "CMSIG2026091303"
signal_slug: "democrats-win-us-house-2026-kalshi-86-2026-09-13"
headline: "Democrats win US House 2026: Kalshi 86%"
semantic_title: "Democrats heavily favored to win the House in 2026"
telemetry: "Kalshi 86%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-13T00:00:00.000Z"
event_id: "CM-EVT-FV8MR86S63"
event_slug: "controlh-2026"
event_question: "Will the Democratic Party win the U.S. House in the next election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "CONTROLH-2026-D"
  question_raw: "Will Democrats win the House in 2026?"
  current_price: 0.86
  volume_24h_usd: 32681.29
  arbitration_model: "kalshi_staff"
  resolution_source: "Library of Congress"
  resolves_at: "2027-02-01T15:00:00Z"
bullets:
  - "The Kalshi contract prices Democrats winning the House at 86%, resolving via Library of Congress."
  - "CNN analysis flags Republican structural defenses that could cap Democratic gains, but the market is not fading the wave narrative at this price level."
  - "The companion Kalshi contract on Republicans controlling at least one chamber sits at 48%, implying the Senate remains genuinely contested as the House leans Democratic."
  - "The Polymarket contract (CM-EVT-2N6T7M0T15) at 86% for Republicans winning the House appears directionally contradicted by the Kalshi contract at 86% for Democrats; treat both with caution pending clarification of resolution scope."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Analysis finds a Democratic wave building for the 2026 midterms but notes Republicans are constructing structural barriers to limit seat losses."
    publisher: "Ronald Brownstein"
    published_at: "2026-09-13T00:00:00.000Z"
    source_url: "https://www.cnn.com/2026/09/13/politics/democrats-republicans-midterms-2026"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Ronald Brownstein"
        source_url: "https://www.cnn.com/2026/09/13/politics/democrats-republicans-midterms-2026"
        retrieved_at: "2026-09-13T13:04:33+00:00"
  - type: "pm_response"
    notes: "Kalshi resolves via Library of Congress records of House composition following the 2026 midterm elections."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Ronald Brownstein: Why Democrats’ blue wave might not be as big as expected | CNN Politic"
    url: "https://www.cnn.com/2026/09/13/politics/democrats-republicans-midterms-2026"
    published_at: "2026-09-13T00:00:00.000Z"
    retrieved_at: "2026-09-13T13:04:33+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
