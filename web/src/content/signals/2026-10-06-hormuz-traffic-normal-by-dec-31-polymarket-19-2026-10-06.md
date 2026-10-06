---
signal_id: "CMSIG2026100605"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-19-2026-10-06"
headline: "Hormuz traffic normal by Dec 31: Polymarket 19%"
semantic_title: "Strait of Hormuz traffic back to normal by year-end stays unlikely"
telemetry: "Polymarket 19%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-06T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.19
  volume_24h_usd: 203136.320684
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract on Strait of Hormuz traffic returning to normal by December 31 prices at 19%."
  - "Trump's rejection of Iran's seven-day reopening plan is consistent with the low probability, markets are not pricing a near-term diplomatic breakthrough."
  - "A companion Kalshi contract on the US reopening its embassy in Iran (CM-EVT-34SYT4T2T1) sits at 4%, reinforcing broad consensus that a full diplomatic reset is remote."
  - "Resolves via Polymarket's UMA oracle; 'normal' traffic levels will need a credible third-party determination, adding resolution uncertainty."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Trump rejected Iran's seven-day proposal to reopen the Strait of Hormuz, while Tehran pushed for a diplomatic resolution and said military talks were meaningless."
    publisher: "WORLD"
    published_at: "2026-10-06T00:00:00.000Z"
    source_url: "https://ilkha.com/english/world/trump-rejects-iran-s-seven-day-hormuz-plan-as-tehran-pushes-for-diplomatic-resolution-565164"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "WORLD"
        source_url: "https://ilkha.com/english/world/trump-rejects-iran-s-seven-day-hormuz-plan-as-tehran-pushes-for-diplomatic-resolution-565164"
        retrieved_at: "2026-10-06T07:48:15+00:00"
  - type: "pm_response"
    notes: "Polymarket prices only a one-in-five chance of Hormuz normalization by year-end, consistent with the breakdown in US-Iran talks reported across multiple outlets this week."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "WORLD: Trump rejects Iran’s seven-day Hormuz plan as Tehran pushes for diplom"
    url: "https://ilkha.com/english/world/trump-rejects-iran-s-seven-day-hormuz-plan-as-tehran-pushes-for-diplomatic-resolution-565164"
    published_at: "2026-10-06T00:00:00.000Z"
    retrieved_at: "2026-10-06T07:48:15+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
