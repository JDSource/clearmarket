---
signal_id: "CMSIG2026072706"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-55-2026-07-27"
headline: "Hormuz traffic normal by Dec 31: Polymarket 55%"
semantic_title: "Strait of Hormuz traffic back to normal by year-end near 50 percent"
telemetry: "Polymarket 55%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-27T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.55
  volume_24h_usd: 79368.04761299999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract puts 55% odds on Strait of Hormuz traffic returning to normal by December 31, resolving via UMA oracle."
  - "Two days of US-Iran ceasefire and active diplomacy are consistent with the slight majority odds on normalization, but the narrow margin reflects continued uncertainty."
  - "Companion ladder CM-EVT-ZP6006CHN9 prices monthly Hormuz transit calls at 30-40, well below pre-conflict levels, showing markets are not yet pricing a swift recovery in throughput."
  - "The 45% probability against normalization by year-end reflects the pace of diplomacy required: a formal deal would need to materialize and shipping confidence restore within roughly five months."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The US and Iran held fire for a second consecutive day as ceasefire talks gained momentum, offering a respite for Gulf shipping and oil markets after nearly two weeks of escalation."
    publisher: "economictimes.indiatimes.com"
    published_at: "2026-07-27T00:00:00.000Z"
    source_url: "https://economictimes.indiatimes.com/news/defence/us-iran-hold-fire-for-second-day-as-ceasefire-talks-gain-momentum/articleshow/132650413.cms"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "economictimes.indiatimes.com"
        source_url: "https://economictimes.indiatimes.com/news/defence/us-iran-hold-fire-for-second-day-as-ceasefire-talks-gain-momentum/articleshow/132650413.cms"
        retrieved_at: "2026-07-27T11:15:45+00:00"
  - type: "pm_response"
    notes: "Polymarket at 55% resolves via UMA oracle and is the cleanest binary on shipping recovery, offering a direct read on ceasefire durability expectations."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "economictimes.indiatimes.com: US, Iran hold fire for second day as ceasefire talks gain momentum - T"
    url: "https://economictimes.indiatimes.com/news/defence/us-iran-hold-fire-for-second-day-as-ceasefire-talks-gain-momentum/articleshow/132650413.cms"
    published_at: "2026-07-27T00:00:00.000Z"
    retrieved_at: "2026-07-27T11:15:45+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
