---
signal_id: "CMSIG2026101907"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-14-2026-10-19"
headline: "Hormuz traffic normal by Dec 31: Polymarket 14%"
semantic_title: "Strait of Hormuz traffic back to normal by year-end stays a long shot"
telemetry: "Polymarket 14%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-19T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.14
  volume_24h_usd: 68886.87929899998
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket puts only 14% odds on Strait of Hormuz traffic returning to normal by December 31, 2026."
  - "Diplomatic activity around Iran continues; the 14% Polymarket read suggests markets treat a full traffic normalization by year-end as unlikely despite talks."
  - "Story 24 reports Iran flagged the Strait as reopening with ceasefire conditions still on the table; the 14% odds indicate markets are not pricing that signal as durable."
  - "The Kalshi contract on Trump visiting Iran (CM-EVT-V9QGT2SSP7) sits at just 2%, suggesting no direct US-Iran diplomatic breakthrough is priced in to support normalization."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Russia's foreign minister is visiting Iran for talks aimed at averting a return to large-scale war, amid reports of ongoing Strait of Hormuz disruptions."
    publisher: "Duarte Dias Digital Journalist"
    published_at: "2026-10-19T00:00:00.000Z"
    source_url: "https://www.cbsnews.com/live-updates/iran-war-us-trump-talks-russia-strait-of-hormuz/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Duarte Dias Digital Journalist"
        source_url: "https://www.cbsnews.com/live-updates/iran-war-us-trump-talks-russia-strait-of-hormuz/"
        retrieved_at: "2026-10-19T15:14:32+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle based on verified Strait transit data; 14% reflects skepticism about a durable reopening by year-end."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Duarte Dias Digital Journalist: Live Updates: Russian foreign minister says he's visiting Iran for tal"
    url: "https://www.cbsnews.com/live-updates/iran-war-us-trump-talks-russia-strait-of-hormuz/"
    published_at: "2026-10-19T00:00:00.000Z"
    retrieved_at: "2026-10-19T15:14:32+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
