---
signal_id: "CMSIG2026073103"
signal_slug: "trump-approval-above-43-ladder-puts-odds-below-16-2026-07-31"
headline: "Trump approval above 43%: ladder puts odds below 16%"
semantic_title: "Trump approval above 43 percent priced as long shot"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-31T09:51:49.048Z"
event_id: "CM-EVT-VWW9FTFB33"
event_slug: "kxtrumpapprovalyear-26dec31"
event_question: "Trump approval rating above threshold"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXTRUMPAPPROVALYEAR-26DEC31-43"
  question_raw: "Will Donald Trump's approval rating on approval rating be above 43% during Dec 2025 to Dec 2026 according to VoteHub?"
  current_price: 0.16
  volume_24h_usd: 2.25
  arbitration_model: "kalshi_staff"
  resolution_source: "<polling organization>"
  resolves_at: "2027-01-07T12:00:00Z"
bullets:
  - "The ladder prices only 16% odds on Trump's approval rating reaching 43%, falling to 9% at 44% and 6% at 45%."
  - "The poll showing 75% of Americans dissatisfied with Trump's focus is consistent with a market that places him well below the 43% threshold."
  - "The distribution shows approval above 50% at just 6%, making any recovery to majority-approval territory a deep long shot by this market."
  - "The Kalshi contract on Republicans controlling at least one chamber after the midterms sits at 46%, suggesting approval drag is already reflected in broader electoral pricing."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "A new poll finds three-quarters of Americans believe President Trump is not focusing on the top issues facing the country."
    publisher: "Richard Luscombe"
    published_at: "2026-07-31T09:51:49.048Z"
    source_url: "https://www.theguardian.com/us-news/2026/jul/30/trump-approval-rating-poll-midterm-elections"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Richard Luscombe"
        source_url: "https://www.theguardian.com/us-news/2026/jul/30/trump-approval-rating-poll-midterm-elections"
        retrieved_at: "2026-08-02T09:52:49+00:00"
  - type: "pm_response"
    notes: "Ladder-implied approval is pinned below 43%, with near-uniform low probabilities across all strikes above that level."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Richard Luscombe: Three-quarters of Americans think Trump isn’t focusing on top US issue"
    url: "https://www.theguardian.com/us-news/2026/jul/30/trump-approval-rating-poll-midterm-elections"
    published_at: "2026-07-31T09:51:49.048Z"
    retrieved_at: "2026-08-02T09:52:49+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
