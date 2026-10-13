---
signal_id: "CMSIG2026101305"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-14-2026-10-13"
headline: "Hormuz traffic normal by Dec 31: Polymarket 14%"
semantic_title: "Strait of Hormuz returning to normal by year-end stays unlikely"
telemetry: "Polymarket 14%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-13T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.14
  volume_24h_usd: 4657.125247999999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices only 14% odds that Strait of Hormuz traffic returns to normal by December 31, 2026."
  - "Trump's rejection of the seven-day Iranian reopening plan is consistent with the Polymarket contract's heavily skeptical pricing on a near-term resolution."
  - "Ongoing U.S. airstrikes on Iran for a twelfth consecutive night and an Iranian oil export blockade threat further support the contract's low probability."
  - "Resolves via UMA oracle assessment of whether Hormuz traffic has normalized by December 31; diplomatic breakdown makes year-end resolution increasingly remote."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "President Donald Trump rejected an Iranian proposal to reopen the Strait of Hormuz within seven days, leaving the waterway's status unresolved despite Tehran's diplomatic overtures."
    publisher: "WORLD"
    published_at: "2026-10-13T00:00:00.000Z"
    source_url: "https://ilkha.com/english/world/trump-rejects-iran-s-seven-day-hormuz-plan-as-tehran-pushes-for-diplomatic-resolution-565164"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "WORLD"
        source_url: "https://ilkha.com/english/world/trump-rejects-iran-s-seven-day-hormuz-plan-as-tehran-pushes-for-diplomatic-resolution-565164"
        retrieved_at: "2026-10-13T07:48:09+00:00"
  - type: "pm_response"
    notes: "Polymarket prices Hormuz normalization by year-end at just 14%, consistent with Trump's rejection of Iran's reopening proposal and continued U.S. military strikes."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "WORLD: Trump rejects Iran’s seven-day Hormuz plan as Tehran pushes for diplom"
    url: "https://ilkha.com/english/world/trump-rejects-iran-s-seven-day-hormuz-plan-as-tehran-pushes-for-diplomatic-resolution-565164"
    published_at: "2026-10-13T00:00:00.000Z"
    retrieved_at: "2026-10-13T07:48:09+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
