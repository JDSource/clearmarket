---
signal_id: "CMSIG2026101805"
signal_slug: "gop-retains-at-least-one-chamber-kalshi-62-2026-10-18"
headline: "GOP retains at least one chamber: Kalshi 62%"
semantic_title: "Republicans holding at least one chamber after midterms stays favored"
telemetry: "Kalshi 62%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-18T00:00:00.000Z"
event_id: "CM-EVT-T5VXKJT451"
event_slug: "kxbalancepowercombo-27feb"
event_question: "Will Republicans control at least one chamber of Congress after the 2026 midterm elections?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBALANCEPOWERCOMBO-27FEB-DD"
  question_raw: "Will House Control be Democratic AND Senate Control be Democratic for Feb 2027?"
  current_price: 0.62
  volume_24h_usd: 26178.68
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-02-01T15:00:00Z"
bullets:
  - "Kalshi prices 62% odds that Republicans control at least one chamber of Congress after the 2026 midterms, resolving via Bureau of Labor Statistics official congressional records."
  - "Trump's record-low 33% approval rating in the Washington Post poll is a bearish signal for Republicans, yet the market still leans toward GOP retaining at least one chamber."
  - "A companion Kalshi contract (CM-EVT-FV8MR86S63) prices 90% odds that Democrats win the House, implying the market reconciles both by expecting a split outcome with Republicans holding the Senate."
  - "Resolves via Library of Congress official certification of congressional composition after the November 2026 election results are certified."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "A new Washington Post poll puts President Trump's approval at 33%, with 66% disapproving, handing Democrats what the poll frames as a clear midterm edge."
    publisher: "Dan Balz"
    published_at: "2026-10-18T00:00:00.000Z"
    source_url: "https://www.washingtonpost.com/politics/2026/10/18/trump-approval-hits-record-low-handing-democrats-clear-midterm-edge/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Dan Balz"
        source_url: "https://www.washingtonpost.com/politics/2026/10/18/trump-approval-hits-record-low-handing-democrats-clear-midterm-edge/"
        retrieved_at: "2026-10-18T07:47:28+00:00"
  - type: "pm_response"
    notes: "Kalshi covers both the 'at least one chamber' and House-specific contracts; the 62%-vs-90% split is internally consistent only under a scenario where the Senate stays Republican."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Dan Balz: Trump approval hits record low, handing Democrats a clear midterm edge"
    url: "https://www.washingtonpost.com/politics/2026/10/18/trump-approval-hits-record-low-handing-democrats-clear-midterm-edge/"
    published_at: "2026-10-18T00:00:00.000Z"
    retrieved_at: "2026-10-18T07:47:28+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
