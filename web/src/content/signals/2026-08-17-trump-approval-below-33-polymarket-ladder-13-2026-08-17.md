---
signal_id: "CMSIG2026081705"
signal_slug: "trump-approval-below-33-polymarket-ladder-13-2026-08-17"
headline: "Trump approval below 33%: Polymarket ladder 13%"
semantic_title: "Trump approval below 33 percent stays unlikely near term"
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
  current_price: 0.13
  volume_24h_usd: 62.59
  arbitration_model: "kalshi_staff"
  resolution_source: "<polling organization>"
  resolves_at: "2027-01-07T12:00:00Z"
bullets:
  - "The prediction market ladder puts only 13% on Trump approval falling below 33% in the current window, per the distribution provided."
  - "The Reuters/Ipsos poll hitting exactly 33% places Trump right at the strike threshold, the market is not yet pricing a sustained breach below that level as the base case."
  - "A companion ladder (CM-EVT-VWW9FTFB33) shows only 10% on approval above 43%, confirming the market frames approval as range-bound in the low-to-mid 30s."
  - "Resolves via the named approval-rating data source; settlement depends on which poll and date are used, methodology differences between pollsters create resolution edge risk."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "A Reuters/Ipsos poll found Trump's approval rating fell to 33%, the lowest of his presidency, with 64% disapproving."
    publisher: "Jason Lange"
    published_at: "2026-08-17T00:00:00.000Z"
    source_url: "https://www.reuters.com/world/us/trump-approval-falls-33-lowest-his-presidency-reutersipsos-poll-finds-2026-08-17/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Jason Lange"
        source_url: "https://www.reuters.com/world/us/trump-approval-falls-33-lowest-his-presidency-reutersipsos-poll-finds-2026-08-17/"
        retrieved_at: "2026-08-19T08:31:28+00:00"
  - type: "pm_response"
    notes: "Ladder pricing at 13% below 33% shows markets see the poll as a floor test, not a confirmed breakdown, consistent with approval stuck in the mid-30s."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Jason Lange: EXCLUSIVE: Trump approval falls to 33%, lowest of his presidency, Reut"
    url: "https://www.reuters.com/world/us/trump-approval-falls-33-lowest-his-presidency-reutersipsos-poll-finds-2026-08-17/"
    published_at: "2026-08-17T00:00:00.000Z"
    retrieved_at: "2026-08-19T08:31:28+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
