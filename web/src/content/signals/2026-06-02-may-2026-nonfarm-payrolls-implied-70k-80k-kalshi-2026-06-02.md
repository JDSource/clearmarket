---
signal_id: "CMSIG2026060204"
signal_slug: "may-2026-nonfarm-payrolls-implied-70k-80k-kalshi-2026-06-02"
headline: "May 2026 nonfarm payrolls implied 70k-80k: Kalshi"
semantic_title: "May payrolls above 80K sits near a coin flip in pricing"
telemetry: "Kalshi 45%"
category_tag: "PRE_EVENT_PRICING"
detection_path: "news_cycle"
pre_news_classification: "pre_news"
published_at: "2026-06-02T15:52:11.000Z"
event_id: "CM-EVT-QH49Q7F1N3"
event_slug: "kxpayrolls-26may"
event_question: "May 2026 nonfarm payroll additions"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPAYROLLS-26MAY-T80000"
  question_raw: "Will above 80000 jobs be added in May 2026?"
  current_price: 0.45
  volume_24h_usd: 118.04
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau Of Labor Statistics"
  resolves_at: "2026-06-05T14:00:00Z"
bullets:
  - "Kalshi ladder implies May 2026 payrolls in the 70k-80k range: 77% above 30k, 53% above 70k, only 45% above 80k."
  - "April's 7.6 million job openings print is consistent with the positive-but-modest payroll range the ladder prices; no market shock implied."
  - "Companion ladder CM-EVT-6CSLHX0K76 for October 2026 shows similar 70k-80k implied range, suggesting the market sees no near-term deterioration."
  - "Resolves via BLS Employment Situation report for May 2026; the ladder settles at the reported seasonally adjusted nonfarm payroll change."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "US job openings climbed to 7.6 million in April despite economic fallout from the Iran war, signaling labor market resilience."
    publisher: "pbs.org"
    published_at: "2026-06-02T15:52:11.000Z"
    source_url: "https://www.pbs.org/newshour/economy/u-s-job-openings-climbed-to-7-6-million-in-april-despite-economic-fallout-from-iran-war"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "pbs.org"
        source_url: "https://www.pbs.org/newshour/economy/u-s-job-openings-climbed-to-7-6-million-in-april-despite-economic-fallout-from-iran-war"
        retrieved_at: "2026-06-03T01:50:17+00:00"
  - type: "pm_response"
    notes: "Kalshi May payroll ladder prices a positive but below-trend jobs outcome, broadly confirming the 'weirdly decent' labor market narrative without pricing a breakout."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "pbs.org: U.S. job openings climbed to 7.6 million in April despite economic fal"
    url: "https://www.pbs.org/newshour/economy/u-s-job-openings-climbed-to-7-6-million-in-april-despite-economic-fallout-from-iran-war"
    published_at: "2026-06-02T15:52:11.000Z"
    retrieved_at: "2026-06-03T01:50:17+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
