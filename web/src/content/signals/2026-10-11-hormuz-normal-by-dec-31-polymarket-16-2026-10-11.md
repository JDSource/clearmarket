---
signal_id: "CMSIG2026101106"
signal_slug: "hormuz-normal-by-dec-31-polymarket-16-2026-10-11"
headline: "Hormuz normal by Dec 31: Polymarket 16%"
semantic_title: "Hormuz traffic back to normal by year-end stays a long shot"
telemetry: "Polymarket 16%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-11T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.16
  volume_24h_usd: 27282.805613
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket puts only 16% odds on Strait of Hormuz traffic returning to normal by December 31, 2026, making it a clear long-shot scenario."
  - "Trump's rejection of Iran's seven-day Hormuz plan is consistent with the market's skepticism; the contract is not pricing a near-term diplomatic breakthrough."
  - "US-Iran ceasefire talks reported in Switzerland (Story 28) provide some upside optionality, but the 16% price reflects the market discounting a deal closing within the year."
  - "A companion Kalshi contract (CM-EVT-34SYT4T2T1) on the US reopening its Iran embassy sits at only 3%, reinforcing that the market sees no near-term normalization across any dimension."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Trump rejected Iran's seven-day proposal to reopen the Strait of Hormuz, even as Tehran pushed for diplomatic resolution."
    publisher: "WORLD"
    published_at: "2026-10-11T00:00:00.000Z"
    source_url: "https://ilkha.com/english/world/trump-rejects-iran-s-seven-day-hormuz-plan-as-tehran-pushes-for-diplomatic-resolution-565164"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "WORLD"
        source_url: "https://ilkha.com/english/world/trump-rejects-iran-s-seven-day-hormuz-plan-as-tehran-pushes-for-diplomatic-resolution-565164"
        retrieved_at: "2026-10-11T07:48:02+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle based on observable Strait of Hormuz shipping traffic data through December 31."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "WORLD: Trump rejects Iran’s seven-day Hormuz plan as Tehran pushes for diplom"
    url: "https://ilkha.com/english/world/trump-rejects-iran-s-seven-day-hormuz-plan-as-tehran-pushes-for-diplomatic-resolution-565164"
    published_at: "2026-10-11T00:00:00.000Z"
    retrieved_at: "2026-10-11T07:48:02+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
