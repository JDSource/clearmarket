---
signal_id: "CMSIG2026101906"
signal_slug: "trump-approval-above-43-kalshi-ladder-under-10-2026-10-19"
headline: "Trump approval above 43%: Kalshi ladder under 10%"
semantic_title: "Trump approval above 43 percent stays a long shot heading into midterms"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-19T00:00:00.000Z"
event_id: "CM-EVT-VWW9FTFB33"
event_slug: "kxtrumpapprovalyear-26dec31"
event_question: "Trump approval rating level"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXTRUMPAPPROVALYEAR-26DEC31-43"
  question_raw: "Will Donald Trump's approval rating on approval rating be above 43% during Dec 2025 to Dec 2026 according to VoteHub?"
  current_price: 0.031
  volume_24h_usd: 0.31
  arbitration_model: "kalshi_staff"
  resolution_source: "<polling organization>"
  resolves_at: "2027-01-07T12:00:00Z"
bullets:
  - "Kalshi ladder implies Trump approval rating below 43%: only 3% above 43%, 7% above 44%, with no strike above 50% exceeding single digits."
  - "Poll showing majority view Trump as self-enriching aligns with the ladder's heavy pricing below 43%; markets and news are consistent."
  - "The Polymarket contract on Trump approval in 2026 (CM-EVT-VNTLCWF6Y5) sits at just 2%, reinforcing the cross-venue consensus for sustained low approval."
  - "A separate Kalshi binary (CM-EVT-0DMSQTKVX3) at 11% on a below-threshold December approval adds a year-end data point to the same bearish read."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "A new poll finds a majority of Americans believe Donald Trump is using the presidency for personal financial gain, with his approval rating hitting a new low."
    publisher: "Shrai Popat"
    published_at: "2026-10-19T00:00:00.000Z"
    source_url: "https://www.theguardian.com/us-news/live/2026/oct/19/donald-trump-kansas-roger-marshall-golf-ukraine-midterms-latest-news-updates"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Shrai Popat"
        source_url: "https://www.theguardian.com/us-news/live/2026/oct/19/donald-trump-kansas-roger-marshall-golf-ukraine-midterms-latest-news-updates"
        retrieved_at: "2026-10-19T15:14:32+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves via named polling organization; Polymarket contract (CM-EVT-VNTLCWF6Y5) at 2% provides a cross-venue check."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Shrai Popat: Majority of Americans think Donald Trump is using presidency to enrich"
    url: "https://www.theguardian.com/us-news/live/2026/oct/19/donald-trump-kansas-roger-marshall-golf-ukraine-midterms-latest-news-updates"
    published_at: "2026-10-19T00:00:00.000Z"
    retrieved_at: "2026-10-19T15:14:32+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
