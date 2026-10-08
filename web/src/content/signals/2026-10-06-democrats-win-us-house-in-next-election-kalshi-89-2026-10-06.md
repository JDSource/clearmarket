---
signal_id: "CMSIG2026100604"
signal_slug: "democrats-win-us-house-in-next-election-kalshi-89-2026-10-06"
headline: "Democrats win US House in next election: Kalshi 89%"
semantic_title: "Democrats heavily favored to retake the House in November"
telemetry: "Kalshi 89%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-06T00:00:00.000Z"
event_id: "CM-EVT-FV8MR86S63"
event_slug: "controlh-2026"
event_question: "Will the Democratic Party win the U.S. House in the next election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "CONTROLH-2026-D"
  question_raw: "Will Democrats win the House in 2026?"
  current_price: 0.89
  volume_24h_usd: 378844.72
  arbitration_model: "kalshi_staff"
  resolution_source: "Library of Congress"
  resolves_at: "2027-02-01T15:00:00Z"
bullets:
  - "Kalshi prices Democrats winning the US House at 89%, a heavily favored outcome one month before the November 3 midterms."
  - "Republican mail-in voting confusion and candidate distancing from Trump reported by Reuters aligns with, not against, this Democratic-favored pricing."
  - "The Kalshi contract on Republicans controlling at least one chamber (CM-EVT-T5VXKJT451) sits at 62%, suggesting the Senate remains the likely Republican backstop."
  - "The Polymarket contract on Senate control (CM-EVT-M9WJY06T90) prices 63% for one party, the cross-venue consistency reinforces a split-Congress base case."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Trump is sowing doubt about mail-in voting while encouraging it, as Republican candidates distance themselves ahead of November midterms."
    publisher: "Katherine Faulders, Nicholas Kerr"
    published_at: "2026-10-06T00:00:00.000Z"
    source_url: "https://www-cdn.abcnews.com/Politics/trump-sows-doubt-mail-voting-encouraging-midterms-approach/story?id=137025278"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Katherine Faulders, Nicholas Kerr"
        source_url: "https://www-cdn.abcnews.com/Politics/trump-sows-doubt-mail-voting-encouraging-midterms-approach/story?id=137025278"
        retrieved_at: "2026-10-08T07:48:09+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolves via Library of Congress; the 89% price reflects a strong Democratic House lean one month out."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Katherine Faulders, Nicholas Kerr: Trump sows doubt about mail-in voting while encouraging it, as midterm"
    url: "https://www-cdn.abcnews.com/Politics/trump-sows-doubt-mail-voting-encouraging-midterms-approach/story?id=137025278"
    published_at: "2026-10-06T00:00:00.000Z"
    retrieved_at: "2026-10-08T07:48:09+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
