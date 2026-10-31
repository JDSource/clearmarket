---
signal_id: "CMSIG2026102902"
signal_slug: "negative-us-gdp-in-2026-polymarket-3-2026-10-29"
headline: "Negative US GDP in 2026: Polymarket 3%"
semantic_title: "Negative GDP growth in 2026 stays a long shot"
telemetry: "Polymarket 3%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "lagging"
published_at: "2026-10-29T00:00:00.000Z"
event_id: "CM-EVT-36YHF72CQ8"
event_slug: "negative-gdp-growth-in-2026"
event_question: "Will there be negative GDP growth in 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xd8c1b0a73653b1fb4fb6e8d13d0063d25810870d7ddf83e61fffb4de4522edf1"
  question_raw: "Negative GDP growth in 2026?"
  current_price: 0.029
  volume_24h_usd: 0.0
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-29T00:00:00Z"
bullets:
  - "The Polymarket contract on negative US GDP growth in 2026 sits at just 3%, via UMA oracle."
  - "A 3.4% Q3 print is consistent with the market's near-complete rejection of a 2026 recession scenario."
  - "With Q3 GDP in hand, only a catastrophic Q4 contraction could flip the annual measure negative, the odds reflect that math."
  - "Resolution requires full-year 2026 GDP to be negative; UMA oracle settles via official BEA data."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Q3 2026 US GDP grew at a better-than-expected 3.4% annualized pace, even as September inflation accelerated."
    publisher: "Stephan Bisaha"
    published_at: "2026-10-29T00:00:00.000Z"
    source_url: "https://www.npr.org/2026/10/29/nx-s1-6020539/two-reports-give-insight-on-the-economy-ahead-of-election-day"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Stephan Bisaha"
        source_url: "https://www.npr.org/2026/10/29/nx-s1-6020539/two-reports-give-insight-on-the-economy-ahead-of-election-day"
        retrieved_at: "2026-10-31T07:48:23+00:00"
  - type: "pm_response"
    notes: "Polymarket prices near-zero probability of 2026 recession; the strong Q3 GDP print is fully aligned with this long-standing market read."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Stephan Bisaha: Two reports give insight on the economy ahead of Election Day : NPR"
    url: "https://www.npr.org/2026/10/29/nx-s1-6020539/two-reports-give-insight-on-the-economy-ahead-of-election-day"
    published_at: "2026-10-29T00:00:00.000Z"
    retrieved_at: "2026-10-31T07:48:23+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
