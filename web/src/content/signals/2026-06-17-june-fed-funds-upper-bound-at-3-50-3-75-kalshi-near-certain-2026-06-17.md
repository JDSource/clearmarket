---
signal_id: "CMSIG2026061701"
signal_slug: "june-fed-funds-upper-bound-at-3-50-3-75-kalshi-near-certain-2026-06-17"
headline: "June Fed funds upper bound at 3.50-3.75%: Kalshi near-certain"
semantic_title: "June Fed funds hold at 3.50-3.75 percent nears full pricing"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-17T06:35:12.000Z"
event_id: "CM-EVT-RJ6SMJGK50"
event_slug: "kxfed-26jun"
event_question: "June 2026 Fed funds upper bound"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26JUN-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Jun 17, 2026 meeting?"
  current_price: 0.01
  volume_24h_usd: 637.79
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-06-17T18:05:00Z"
bullets:
  - "Kalshi pins the June 2026 Fed funds upper bound in the 3.50-3.75% range, pricing 98% above 3.50% but only 1% above 3.75%."
  - "Universal analyst consensus for a hold is fully consistent with the Kalshi distribution; no daylight between punditry and market."
  - "The separate Kalshi cut-before-2027 contract sits at only 28%, signaling markets see the hold as persistent, not a one-meeting pause."
  - "Resolves via Federal Reserve official statement; upper bound printed above 3.75% would be required for the high-strike legs to pay."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The Fed is widely expected to hold rates at 3.50-3.75% for a fourth consecutive meeting at Chair Kevin Warsh's first FOMC presser."
    publisher: "tradingeconomics.com"
    published_at: "2026-06-17T06:35:12.000Z"
    source_url: "https://tradingeconomics.com/united-states/interest-rate/news/559604"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "tradingeconomics.com"
        source_url: "https://tradingeconomics.com/united-states/interest-rate/news/559604"
        retrieved_at: "2026-06-17T12:13:58+00:00"
  - type: "pm_response"
    notes: "Kalshi's ladder distribution is tightly clustered at the 3.50-3.75% band, with negligible probability mass above 3.75%."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "tradingeconomics.com: Fed to Keep Rates Steady at New Chair's First Meeting"
    url: "https://tradingeconomics.com/united-states/interest-rate/news/559604"
    published_at: "2026-06-17T06:35:12.000Z"
    retrieved_at: "2026-06-17T12:13:58+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
