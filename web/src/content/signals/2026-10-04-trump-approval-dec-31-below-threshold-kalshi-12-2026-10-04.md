---
signal_id: "CMSIG2026100404"
signal_slug: "trump-approval-dec-31-below-threshold-kalshi-12-2026-10-04"
headline: "Trump approval Dec 31 below threshold: Kalshi 12%"
semantic_title: "Trump approval below threshold by year-end stays long odds"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-04T13:00:00.000Z"
event_id: "CM-EVT-0DMSQTKVX3"
event_slug: "kxtrumpapprovalbelow-26dec31"
event_question: "Donald Trump approval rating, December 31, 2026 (below threshold)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXTRUMPAPPROVALBELOW-26DEC31-33"
  question_raw: "Will Donald Trump's approval rating on approval rating be below 33% during Dec 2025 to Dec 2026 according to VoteHub?"
  current_price: 0.12
  volume_24h_usd: 46.03
  arbitration_model: "kalshi_staff"
  resolution_source: "<polling organization>"
  resolves_at: "2027-01-07T12:00:00Z"
bullets:
  - "Kalshi contract prices only 12% on Trump approval falling below the defined threshold by December 31, 2026."
  - "Latino voter swing news is consistent with sinking approval polls, yet the market gives only modest odds to the below-threshold outcome."
  - "The 12% price implies the market's baseline is that approval stays above threshold even amid the deteriorating political environment."
  - "Companion Kalshi ladder CM-EVT-VWW9FTFB33 shows under 5% on any strike above 43%, together suggesting approval seen stuck in a narrow low band."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "An NBC News poll shows Democrats with a significant lead among Latino voters in 2026, with economic concerns driving swing away from Republicans."
    publisher: "Ben Kamisar, Bridget Bowman"
    published_at: "2026-10-04T13:00:00.000Z"
    source_url: "https://www.nbcnews.com/politics/2026-election/poll-latino-voters-swing-away-trump-republicans-midterm-shift-rcna599894"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Ben Kamisar, Bridget Bowman"
        source_url: "https://www.nbcnews.com/politics/2026-election/poll-latino-voters-swing-away-trump-republicans-midterm-shift-rcna599894"
        retrieved_at: "2026-10-04T13:39:12+00:00"
  - type: "pm_response"
    notes: "Resolves via polling organization; the 12% price on a below-threshold outcome reflects disagreement on exactly where the floor sits."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Ben Kamisar, Bridget Bowman: Poll: Latino voters swing away from Trump and Republicans"
    url: "https://www.nbcnews.com/politics/2026-election/poll-latino-voters-swing-away-trump-republicans-midterm-shift-rcna599894"
    published_at: "2026-10-04T13:00:00.000Z"
    retrieved_at: "2026-10-04T13:39:12+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
