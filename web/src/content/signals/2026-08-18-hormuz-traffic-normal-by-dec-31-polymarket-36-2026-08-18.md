---
signal_id: "CMSIG2026081804"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-36-2026-08-18"
headline: "Hormuz traffic normal by Dec 31: Polymarket 36%"
semantic_title: "Hormuz traffic back to normal by year-end sits below 40 percent"
telemetry: "Polymarket 36%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-18T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.36
  volume_24h_usd: 58332.64292100003
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices only 36% on Strait of Hormuz traffic returning to normal by December 31, resolving via UMA oracle."
  - "Active ship attacks and Trump's public denial of any Iran talks are consistent with the market's below-50% read, the news and the price are aligned on a pessimistic outlook."
  - "Trump's claim that the strait is 'open and operating' and that mines have been removed is contradicted by the ship attack reported the same day, likely reinforcing the market's skepticism."
  - "Resolves via UMA oracle assessing traffic normalization against defined baseline; settlement edge case exists if partial restoration is debated."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "A ship was attacked in the Strait of Hormuz as Iran throttled traffic and Trump said the US had no talks planned with Iran."
    publisher: "apnews.com"
    published_at: "2026-08-18T00:00:00.000Z"
    source_url: "https://apnews.com/article/iran-us-israel-lebanon-gaza-hormuz-august-18-2026-9c48af23b713709e8e170191fbc78c2a"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "apnews.com"
        source_url: "https://apnews.com/article/iran-us-israel-lebanon-gaza-hormuz-august-18-2026-9c48af23b713709e8e170191fbc78c2a"
        retrieved_at: "2026-08-19T08:31:28+00:00"
  - type: "pm_response"
    notes: "Polymarket at 36% reflects sustained disruption risk; the news flow of active attacks and diplomatic breakdown is consistent with this pricing."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "apnews.com: Ship attacked in Hormuz strait as Iran throttles traffic through key w"
    url: "https://apnews.com/article/iran-us-israel-lebanon-gaza-hormuz-august-18-2026-9c48af23b713709e8e170191fbc78c2a"
    published_at: "2026-08-18T00:00:00.000Z"
    retrieved_at: "2026-08-19T08:31:28+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
