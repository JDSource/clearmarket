---
signal_id: "CMSIG2026082103"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-29-2026-08-21"
headline: "Hormuz traffic normal by Dec 31: Polymarket 29%"
semantic_title: "Hormuz traffic returning to normal by year-end stays a long shot"
telemetry: "Polymarket 29%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-21T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.29
  volume_24h_usd: 88330.770783
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket places only 29% odds on Strait of Hormuz traffic returning to normal by December 31, 2026."
  - "Trump's 'economic D-Day' threat and Bessent's call to allies to sanction Iran are consistent with a market pricing continued disruption as more likely than resolution."
  - "Hormuz traffic remaining low has pushed US gas prices up nearly a dollar year over year, providing concrete economic reinforcement for the market's skeptical stance."
  - "Resolution via UMA oracle requires verifiable normalization of Hormuz transit data; experts cited by CNN say Iran is unlikely to capitulate quickly, supporting the below-50% price."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Trump threatened Iran with economic consequences while US gas prices are nearly a dollar higher year over year as Strait of Hormuz traffic remains depressed."
    publisher: "apnews.com"
    published_at: "2026-08-21T00:00:00.000Z"
    source_url: "https://apnews.com/article/iran-war-trump-sanctions-economic-fury-oil-d28206ea288a3d4a9b82260ab44ce460"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "apnews.com"
        source_url: "https://apnews.com/article/iran-war-trump-sanctions-economic-fury-oil-d28206ea288a3d4a9b82260ab44ce460"
        retrieved_at: "2026-08-22T08:23:10+00:00"
  - type: "pm_response"
    notes: "Polymarket contract at 29% reflects the market fading Trump's escalatory rhetoric as insufficient to quickly reopen the strait."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "apnews.com: Trump warns Iran of 'economic D-Day,' but it's used to sanctions | AP"
    url: "https://apnews.com/article/iran-war-trump-sanctions-economic-fury-oil-d28206ea288a3d4a9b82260ab44ce460"
    published_at: "2026-08-21T00:00:00.000Z"
    retrieved_at: "2026-08-22T08:23:10+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
