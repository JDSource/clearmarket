---
signal_id: "CMSIG2026101408"
signal_slug: "2026-midterms-on-schedule-kalshi-91-2026-10-14"
headline: "2026 midterms on schedule: Kalshi 91%"
semantic_title: "Midterm elections happening on schedule stays heavily favored at 91%"
telemetry: "Kalshi 91%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-14T00:00:00.000Z"
event_id: "CM-EVT-HT9T7KMRT5"
event_slug: "kxmidtermhappen-2026"
event_question: "Will the midterm elections happen on schedule?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXMIDTERMHAPPEN-2026-T50"
  question_raw: "Will at least 50 states conduct 2026 U.S. House midterms on time?"
  current_price: 0.91
  volume_24h_usd: 2471.3
  arbitration_model: "kalshi_staff"
  resolution_source: "The Washington Post"
  resolves_at: "2026-11-10T15:00:00Z"
bullets:
  - "Kalshi puts 91% odds on the 2026 midterm elections proceeding on their scheduled date."
  - "Trump's rejection of international election observers is a procedural controversy, but the market's 91% pricing shows high confidence the elections themselves will occur on time."
  - "The 9% residual reflects tail risk around election disruption, but the market is not treating the OSCE rejection as a credible scheduling threat."
  - "Resolves via The Washington Post; likely requires a credible public report confirming elections were held or formally postponed on the scheduled date."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "President Trump broke with a two-decade tradition by rejecting international OSCE election observers for the 2026 midterm elections, drawing criticism over democratic transparency."
    publisher: "Laura Kelly"
    published_at: "2026-10-14T00:00:00.000Z"
    source_url: "https://thehill.com/policy/international/6145244-trump-breaks-election-observer-tradition/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Laura Kelly"
        source_url: "https://thehill.com/policy/international/6145244-trump-breaks-election-observer-tradition/"
        retrieved_at: "2026-10-14T13:17:09+00:00"
  - type: "pm_response"
    notes: "Kalshi at 91% treats the observer dispute as a transparency controversy, not an elections-at-risk event."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Laura Kelly: Trump breaks 20-year tradition by rejecting international election obs"
    url: "https://thehill.com/policy/international/6145244-trump-breaks-election-observer-tradition/"
    published_at: "2026-10-14T00:00:00.000Z"
    retrieved_at: "2026-10-14T13:17:09+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
