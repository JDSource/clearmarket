---
signal_id: "CMSIG2026102903"
signal_slug: "negative-us-gdp-growth-in-2026-polymarket-3-2026-10-29"
headline: "Negative US GDP growth in 2026: Polymarket 3%"
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
  - "The Polymarket contract on negative GDP growth in 2026 sits at just 3%, meaning the market puts near-zero odds on a full-year contraction."
  - "The Q3 GDP print of 3.4%, above consensus, is consistent with this extreme long-shot pricing; the news and the market are aligned."
  - "Inflation running above 2% complicates the outlook but does not shift the growth picture materially at these probability levels."
  - "Resolves via the UMA oracle; the contract covers the full calendar year 2026, so two more quarterly prints remain before settlement."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Third-quarter U.S. GDP grew at a stronger-than-expected 3.4% annualized pace, and a pre-election PCE inflation reading showed price pressures running above the Fed's 2% target."
    publisher: "Stephan Bisaha"
    published_at: "2026-10-29T00:00:00.000Z"
    source_url: "https://www.npr.org/2026/10/29/nx-s1-6020539/two-reports-give-insight-on-the-economy-ahead-of-election-day"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Stephan Bisaha"
        source_url: "https://www.npr.org/2026/10/29/nx-s1-6020539/two-reports-give-insight-on-the-economy-ahead-of-election-day"
        retrieved_at: "2026-10-31T14:15:55+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle; at 3%, the contract is essentially pricing a tail risk, not a base case."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Stephan Bisaha: Two reports give insight on the economy ahead of Election Day : NPR"
    url: "https://www.npr.org/2026/10/29/nx-s1-6020539/two-reports-give-insight-on-the-economy-ahead-of-election-day"
    published_at: "2026-10-29T00:00:00.000Z"
    retrieved_at: "2026-10-31T14:15:55+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
