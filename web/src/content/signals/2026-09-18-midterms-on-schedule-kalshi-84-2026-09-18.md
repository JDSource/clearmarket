---
signal_id: "CMSIG2026091804"
signal_slug: "midterms-on-schedule-kalshi-84-2026-09-18"
headline: "Midterms on schedule: Kalshi 84%"
semantic_title: "Midterm elections on schedule priced as near-certain by markets"
telemetry: "Kalshi 84%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-18T00:00:00.000Z"
event_id: "CM-EVT-HT9T7KMRT5"
event_slug: "kxmidtermhappen-2026"
event_question: "Will the midterm elections happen on schedule?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXMIDTERMHAPPEN-2026-T50"
  question_raw: "Will at least 50 states conduct 2026 U.S. House midterms on time?"
  current_price: 0.84
  volume_24h_usd: 5084.62
  arbitration_model: "kalshi_staff"
  resolution_source: "The Washington Post"
  resolves_at: "2026-11-10T15:00:00Z"
bullets:
  - "The Kalshi contract prices an 84% probability that the midterm elections proceed on their scheduled date despite the legal challenge."
  - "The lawsuit targets federal law enforcement deployment at polling sites; Kalshi's 84% implies the market views a schedule disruption as a real but minority risk."
  - "A 16% probability of off-schedule elections is unusually elevated for what is typically a near-certainty, suggesting the market is treating the litigation and political pressure as non-trivial."
  - "Resolves via The Washington Post as the named resolution source; any court-ordered delay or logistical disruption to polling would be the key settlement edge case."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The Trump administration faces a lawsuit over its threat to deploy federal law enforcement at voting sites, raising procedural concerns about the November 2026 midterm elections."
    publisher: "Ariana Baio"
    published_at: "2026-09-18T00:00:00.000Z"
    source_url: "https://www.theguardian.com/us-news/2026/sep/18/trump-administration-sued-federal-law-enforcement-voting"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Ariana Baio"
        source_url: "https://www.theguardian.com/us-news/2026/sep/18/trump-administration-sued-federal-law-enforcement-voting"
        retrieved_at: "2026-09-19T07:47:13+00:00"
  - type: "pm_response"
    notes: "The Kalshi contract at 84% is lower than one might expect for a scheduled constitutional event, reflecting uncertainty introduced by the federal law enforcement controversy."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Ariana Baio: Trump administration sued over threat to deploy federal law enforcemen"
    url: "https://www.theguardian.com/us-news/2026/sep/18/trump-administration-sued-federal-law-enforcement-voting"
    published_at: "2026-09-18T00:00:00.000Z"
    retrieved_at: "2026-09-19T07:47:13+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
