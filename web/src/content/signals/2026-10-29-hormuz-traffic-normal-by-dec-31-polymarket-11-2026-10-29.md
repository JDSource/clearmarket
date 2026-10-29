---
signal_id: "CMSIG2026102907"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-11-2026-10-29"
headline: "Hormuz traffic normal by Dec 31: Polymarket 11%"
semantic_title: "Strait of Hormuz traffic returning to normal by year-end stays unlikely"
telemetry: "Polymarket 11%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-29T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.11
  volume_24h_usd: 66222.318238
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract on Strait of Hormuz traffic returning to normal by December 31, 2026, prices at just 11%."
  - "The mine-strike report on three tankers is consistent with the market's pessimistic outlook; normalization by year-end looks unlikely given ongoing military and diplomatic tensions."
  - "Separately, Vance's outreach to Iran's security chief on peace talks adds a thin diplomatic thread, but the market at 11% assigns little weight to a rapid resolution."
  - "Resolves via UMA oracle; with the US reportedly weighing new military strikes after midterms, the path to normalized shipping traffic before January is narrow."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran said three oil tankers struck mines in the Strait of Hormuz, adding to ongoing disruption in one of the world's most critical oil shipping lanes."
    publisher: "The Associated Press"
    published_at: "2026-10-29T00:00:00.000Z"
    source_url: "https://apnews.com/article/mideast-iran-israel-elections-netanyahu-october-282026-c11dac838a072af25ba8d0eb81d01035"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "The Associated Press"
        source_url: "https://apnews.com/article/mideast-iran-israel-elections-netanyahu-october-282026-c11dac838a072af25ba8d0eb81d01035"
        retrieved_at: "2026-10-29T14:55:20+00:00"
  - type: "pm_response"
    notes: "Polymarket's UMA oracle resolves on verified shipping traffic data; the 11% price reflects a market that sees diplomacy as insufficient to reopen the strait before year-end."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "The Associated Press: Iran says 3 oil tankers struck mines, and other Mideast news"
    url: "https://apnews.com/article/mideast-iran-israel-elections-netanyahu-october-282026-c11dac838a072af25ba8d0eb81d01035"
    published_at: "2026-10-29T00:00:00.000Z"
    retrieved_at: "2026-10-29T14:55:20+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
