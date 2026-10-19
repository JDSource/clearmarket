---
signal_id: "CMSIG2026101907"
signal_slug: "midterms-on-schedule-kalshi-90-2026-10-19"
headline: "Midterms on schedule: Kalshi 90%"
semantic_title: "Midterm elections proceeding on schedule stays near certain"
telemetry: "Kalshi 90%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-19T00:00:00.000Z"
event_id: "CM-EVT-HT9T7KMRT5"
event_slug: "kxmidtermhappen-2026"
event_question: "Will the midterm elections happen on schedule?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXMIDTERMHAPPEN-2026-T50"
  question_raw: "Will at least 50 states conduct 2026 U.S. House midterms on time?"
  current_price: 0.9
  volume_24h_usd: 6050.45
  arbitration_model: "kalshi_staff"
  resolution_source: "The Washington Post"
  resolves_at: "2026-11-10T15:00:00Z"
bullets:
  - "Kalshi prices 90% probability that the midterm elections will happen on schedule despite reported federal actions around voting infrastructure."
  - "The CBS News story raises interference concerns, but the prediction market prices an on-schedule election as the strong baseline, not treating federal actions as a credible disruption threat."
  - "Companion Kalshi contracts on specific races (Michigan 10th at 67%, Georgia Governor at 49% via Polymarket) show competitive individual contests, consistent with a normal election proceeding."
  - "Resolves via The Washington Post as the named resolution source; any official postponement or large-scale disruption announcement would be the key settlement trigger."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "CBS News reports federal actions around the voting system are expanding in the weeks before midterms, raising concerns about government interference."
    publisher: "Lesley Stahl Correspondent, 60 Minutes"
    published_at: "2026-10-19T00:00:00.000Z"
    source_url: "https://www.cbsnews.com/news/trump-election-investigations-faith-in-voting-60-minutes/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Lesley Stahl Correspondent, 60 Minutes"
        source_url: "https://www.cbsnews.com/news/trump-election-investigations-faith-in-voting-60-minutes/"
        retrieved_at: "2026-10-19T07:47:26+00:00"
  - type: "pm_response"
    notes: "Kalshi's 90% on-schedule pricing shows the prediction market treats the CBS interference concern as a tail risk, not a base case."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Lesley Stahl Correspondent, 60 Minutes: Federal actions around voting system expand weeks ahead of midterms -"
    url: "https://www.cbsnews.com/news/trump-election-investigations-faith-in-voting-60-minutes/"
    published_at: "2026-10-19T00:00:00.000Z"
    retrieved_at: "2026-10-19T07:47:26+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
