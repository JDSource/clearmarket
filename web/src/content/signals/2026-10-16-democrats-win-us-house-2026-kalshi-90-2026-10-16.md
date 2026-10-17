---
signal_id: "CMSIG2026101604"
signal_slug: "democrats-win-us-house-2026-kalshi-90-2026-10-16"
headline: "Democrats win US House 2026: Kalshi 90%"
semantic_title: "Democrats winning the House stays heavily favored heading into midterms"
telemetry: "Kalshi 90%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-16T00:00:00.000Z"
event_id: "CM-EVT-FV8MR86S63"
event_slug: "controlh-2026"
event_question: "Will the Democratic Party win the U.S. House in the next election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "CONTROLH-2026-D"
  question_raw: "Will Democrats win the House in 2026?"
  current_price: 0.903
  volume_24h_usd: 254384.67
  arbitration_model: "kalshi_staff"
  resolution_source: "Library of Congress"
  resolves_at: "2027-02-01T15:00:00Z"
bullets:
  - "The Kalshi contract on Democrats winning the U.S. House in 2026 sits at 90%, resolving via the Library of Congress."
  - "Despite Republican incumbency and Trump's active campaign rallying, the market is heavily tilted toward a Democratic House takeover."
  - "A companion Kalshi contract (CM-EVT-T5VXKJT451) puts Republicans controlling at least one chamber at 62%, suggesting markets see the Senate as the GOP's more likely firewall."
  - "The 90% Democratic House probability versus 62% Republican chamber control implies markets mostly price a split Congress outcome."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Candidates clashed in heated midterm debates with less than three weeks to Election Day, with Republicans aiming to retain House and Senate majorities."
    publisher: "Alex Nitzberg, Paul Steinhauser, Charles Creitz, Robert Schmad, Ashley J. DiMella"
    published_at: "2026-10-16T00:00:00.000Z"
    source_url: "https://www.foxnews.com/live-news/midterm-elections-2026-less-than-three-weeks-away-october-16"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Alex Nitzberg, Paul Steinhauser, Charles Creitz, Robert Schmad, Ashley J. DiMella"
        source_url: "https://www.foxnews.com/live-news/midterm-elections-2026-less-than-three-weeks-away-october-16"
        retrieved_at: "2026-10-17T07:47:54+00:00"
  - type: "pm_response"
    notes: "Kalshi at 90% for a Democratic House is a strong lean with Library of Congress resolution, the gap versus the Republican chamber-control contract is the key cross-market read."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Alex Nitzberg, Paul Steinhauser, Charles Creitz, Robert Schmad, Ashley J. DiMella: As midterm Election Day approaches, candidates clash in debates  | Liv"
    url: "https://www.foxnews.com/live-news/midterm-elections-2026-less-than-three-weeks-away-october-16"
    published_at: "2026-10-16T00:00:00.000Z"
    retrieved_at: "2026-10-17T07:47:54+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
