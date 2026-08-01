---
signal_id: "CMSIG2026080106"
signal_slug: "strait-of-hormuz-normal-by-dec-31-polymarket-47-2026-08-01"
headline: "Strait of Hormuz normal by Dec 31: Polymarket 47%"
semantic_title: "Hormuz traffic returning to normal by year-end sits near 50 percent"
telemetry: "Polymarket 47%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-01T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.47
  volume_24h_usd: 52981.31677000001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices 47% on Strait of Hormuz traffic returning to normal by December 31."
  - "Truce collapse and White House warnings of fresh Iran strikes push the resolution scenario further out, keeping the contract near but just below 50%."
  - "At 47%, the Polymarket contract signals genuine two-way uncertainty, with five months remaining and an active military standoff as the key variable."
  - "Companion Kalshi contract CM-EVT-ZP3JDLXZQ0 implies peak single-day transit calls in the 10-15 range, consistent with significantly reduced but not fully halted traffic."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The US-Iran truce collapsed and the White House is weighing fresh strikes on Iran as Hormuz tanker attacks resume, raising new doubts about passage normalization."
    publisher: "indiatoday.in"
    published_at: "2026-08-01T00:00:00.000Z"
    source_url: "https://www.indiatoday.in/world/story/trump-iran-strikes-white-house-warns-tehran-after-hormuz-tanker-attacks-truce-collapse-ptag-2961021-2026-08-01"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "indiatoday.in"
        source_url: "https://www.indiatoday.in/world/story/trump-iran-strikes-white-house-warns-tehran-after-hormuz-tanker-attacks-truce-collapse-ptag-2961021-2026-08-01"
        retrieved_at: "2026-08-01T09:54:52+00:00"
  - type: "pm_response"
    notes: "Polymarket resolves via UMA oracle; 'normal' traffic will require a clear, sustained return to pre-conflict transit levels, which escalating US-Iran military action makes uncertain."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "indiatoday.in: Trump Iran strikes: White House warns Tehran after Hormuz tanker attac"
    url: "https://www.indiatoday.in/world/story/trump-iran-strikes-white-house-warns-tehran-after-hormuz-tanker-attacks-truce-collapse-ptag-2961021-2026-08-01"
    published_at: "2026-08-01T00:00:00.000Z"
    retrieved_at: "2026-08-01T09:54:52+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
