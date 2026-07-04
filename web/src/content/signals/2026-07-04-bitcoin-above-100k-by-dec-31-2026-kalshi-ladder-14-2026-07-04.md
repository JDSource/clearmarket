---
signal_id: "CMSIG2026070407"
signal_slug: "bitcoin-above-100k-by-dec-31-2026-kalshi-ladder-14-2026-07-04"
headline: "Bitcoin above $100K by Dec 31, 2026: Kalshi ladder 14%"
semantic_title: "Bitcoin above $100K by year-end holds at deep discount despite rebound"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-04T00:22:30.000Z"
event_id: "CM-EVT-0MWN62PNG9"
event_slug: "kxbtcmaxy-26dec31"
event_question: "Bitcoin price level by December 31, 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCMAXY-26DEC31-99999.99"
  question_raw: "Will Bitcoin be above $99,999.99 by Dec 31, 2026 at 11:59 PM ET?"
  current_price: 0.14
  volume_24h_usd: 1780.87
  arbitration_model: "kalshi_staff"
  resolution_source: "CF Benchmarks"
  resolves_at: "2027-01-01T04:59:00Z"
bullets:
  - "Kalshi ladder prices only 14% on Bitcoin exceeding $99,999 by December 31, 2026, with the implied modal range sitting below $100K."
  - "The $62K spot surge follows the payroll miss repricing Fed expectations, but year-end prediction market pricing has not shifted to a bull-case consensus."
  - "The ladder's tail shows 10% above $110K and 8% above $120K, indicating the market assigns very low probability to a continuation into prior all-time-high territory."
  - "Resolves via the Kalshi settlement price for Bitcoin on December 31, 2026 at 11:59 PM ET."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Bitcoin surged past $62,000 after weak June payrolls eased Fed rate-hike fears, triggering over $100 million in short liquidations."
    publisher: "Editorial Team"
    published_at: "2026-07-04T00:22:30.000Z"
    source_url: "https://cryptobriefing.com/bitcoin-surges-62k-100m-liquidations/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Editorial Team"
        source_url: "https://cryptobriefing.com/bitcoin-surges-62k-100m-liquidations/"
        retrieved_at: "2026-07-04T10:05:12+00:00"
  - type: "pm_response"
    notes: "Kalshi's year-end Bitcoin ladder sits at 14% above $100K even as spot trades near $62K, a wide gap that reflects skepticism about the payroll-driven rally sustaining through year-end."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Editorial Team: Bitcoin surges past $62K, triggering $100M in liquidations"
    url: "https://cryptobriefing.com/bitcoin-surges-62k-100m-liquidations/"
    published_at: "2026-07-04T00:22:30.000Z"
    retrieved_at: "2026-07-04T10:05:12+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
