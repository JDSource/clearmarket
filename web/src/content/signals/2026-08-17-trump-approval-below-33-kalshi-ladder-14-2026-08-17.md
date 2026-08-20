---
signal_id: "CMSIG2026081707"
signal_slug: "trump-approval-below-33-kalshi-ladder-14-2026-08-17"
headline: "Trump approval below 33%: Kalshi ladder 14%"
semantic_title: "Trump approval odds of dropping below 33 percent build"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-17T00:00:00.000Z"
event_id: "CM-EVT-0DMSQTKVX3"
event_slug: "kxtrumpapprovalbelow-26dec31"
event_question: "Trump approval rating floor"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXTRUMPAPPROVALBELOW-26DEC31-33"
  question_raw: "Will Donald Trump's approval rating on approval rating be below 33% during Dec 2025 to Dec 2026 according to VoteHub?"
  current_price: 0.14
  volume_24h_usd: 149.43
  arbitration_model: "kalshi_staff"
  resolution_source: "<polling organization>"
  resolves_at: "2027-01-07T12:00:00Z"
bullets:
  - "Kalshi ladder prices 14% on Trump approval falling below 33%, with 22% below 34% and 32% below 35%, the market sees 33% as a fragile floor."
  - "Reuters/Ipsos reading of exactly 33% puts the current print right at the threshold the ladder assigns only 14% probability of breaching."
  - "The upper tail ladder prices only 10% on approval above 43%, confirming markets see no recovery scenario in this polling cycle."
  - "Polymarket at 5% on Trump ceasing to be president before 2027 shows markets separate approval collapse from removal risk entirely."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "A Reuters/Ipsos poll found Trump's approval at 33%, his lowest of the presidency, with 64% disapproval."
    publisher: "Jason Lange"
    published_at: "2026-08-17T00:00:00.000Z"
    source_url: "https://www.reuters.com/world/us/trump-approval-falls-33-lowest-his-presidency-reutersipsos-poll-finds-2026-08-17/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Jason Lange"
        source_url: "https://www.reuters.com/world/us/trump-approval-falls-33-lowest-his-presidency-reutersipsos-poll-finds-2026-08-17/"
        retrieved_at: "2026-08-20T08:32:51+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves via approval polling aggregates; the 33% current reading sits at the edge of the distribution's most sensitive zone."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Jason Lange: EXCLUSIVE: Trump approval falls to 33%, lowest of his presidency, Reut"
    url: "https://www.reuters.com/world/us/trump-approval-falls-33-lowest-his-presidency-reutersipsos-poll-finds-2026-08-17/"
    published_at: "2026-08-17T00:00:00.000Z"
    retrieved_at: "2026-08-20T08:32:51+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
