---
signal_id: "CMSIG2026101606"
signal_slug: "democrats-win-us-house-kalshi-90-2026-10-16"
headline: "Democrats win US House: Kalshi 90%"
semantic_title: "Democrats winning the US House climbs near 90 percent"
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
  current_price: 0.902
  volume_24h_usd: 112488.66
  arbitration_model: "kalshi_staff"
  resolution_source: "Library of Congress"
  resolves_at: "2027-02-01T15:00:00Z"
bullets:
  - "Kalshi prices a 90% probability that the Democratic Party wins the US House in the 2026 midterms."
  - "Despite Speaker Mike Johnson's public prediction that Republicans will hold the House, the Kalshi contract heavily favors a Democratic takeover."
  - "The 62% Kalshi probability on Republicans controlling at least one chamber implies the Senate is the GOP's likely lifeline in a split Congress outcome."
  - "Resolves via Library of Congress certification of House election results; the 90% pricing reflects the structural drag of a 33% presidential approval rating on House incumbents."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Fox News Digital reported candidates clashing in heated midterm debates with House and Senate majorities in the balance, the GOP aiming to retain its narrow majority with Election Day under three weeks away."
    publisher: "Alex Nitzberg, Paul Steinhauser, Charles Creitz, Robert Schmad, Ashley J. DiMella"
    published_at: "2026-10-16T00:00:00.000Z"
    source_url: "https://www.foxnews.com/live-news/midterm-elections-2026-less-than-three-weeks-away-october-16"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Alex Nitzberg, Paul Steinhauser, Charles Creitz, Robert Schmad, Ashley J. DiMella"
        source_url: "https://www.foxnews.com/live-news/midterm-elections-2026-less-than-three-weeks-away-october-16"
        retrieved_at: "2026-10-18T12:25:52+00:00"
  - type: "pm_response"
    notes: "Kalshi binary at 90% for Democratic House control; the gap with the 62% GOP one-chamber contract isolates Senate retention as the Republican path to relevance."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Alex Nitzberg, Paul Steinhauser, Charles Creitz, Robert Schmad, Ashley J. DiMella: As midterm Election Day approaches, candidates clash in debates  | Liv"
    url: "https://www.foxnews.com/live-news/midterm-elections-2026-less-than-three-weeks-away-october-16"
    published_at: "2026-10-16T00:00:00.000Z"
    retrieved_at: "2026-10-18T12:25:52+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
