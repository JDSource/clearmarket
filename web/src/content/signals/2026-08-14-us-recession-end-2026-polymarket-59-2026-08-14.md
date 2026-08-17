---
signal_id: "CMSIG2026081402"
signal_slug: "us-recession-end-2026-polymarket-59-2026-08-14"
headline: "US recession end-2026: Polymarket 59%"
semantic_title: "US recession by end of 2026 stays a long shot at 41%"
telemetry: "Polymarket 59%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-14T15:41:15.000Z"
event_id: "CM-EVT-Z32WPK4K45"
event_slug: "us-economic-state-at-the-end-of-2026"
event_question: "Will the US economy be in recession at the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x50e3ee8f93a464d04ea2cea6efff45c902f43642aedbf43f7afdc899e10f71d8"
  question_raw: "Will the US economy be in a soft landing at the end of 2026?"
  current_price: 0.59
  volume_24h_usd: 1914.855858
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
bullets:
  - "Polymarket puts 59% odds on the US economy being in recession by end of 2026, with 41% against."
  - "Soft macro data, including the July retail sales drop, is consistent with recession concern, but the 59% price suggests markets remain divided rather than alarmed."
  - "The S&P 500 crossing 7,800 and soft-landing trade momentum sit in tension with a market that still prices recession as the more likely outcome."
  - "Resolution via UMA oracle; the binary settle on official recession determination leaves meaningful timing ambiguity near year-end."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Fed September rate hike odds fell to 30% as inflation, jobs, and spending cooled, while the S&P 500 topped 7,800 on soft-landing optimism."
    publisher: "tradingkey.com"
    published_at: "2026-08-14T15:41:15.000Z"
    source_url: "https://www.tradingkey.com/analysis/stocks/us-stocks/262108725-fed-september-hike-cools-soft-landing-sp500-7800-tradingkey"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "tradingkey.com"
        source_url: "https://www.tradingkey.com/analysis/stocks/us-stocks/262108725-fed-september-hike-cools-soft-landing-sp500-7800-tradingkey"
        retrieved_at: "2026-08-17T08:37:49+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle on official US recession designation; the 59% price reflects genuine macro uncertainty rather than a consensus call."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "tradingkey.com: Fed September Rate Hike Expectations Drop to 30% as Inflation, Jobs, a"
    url: "https://www.tradingkey.com/analysis/stocks/us-stocks/262108725-fed-september-hike-cools-soft-landing-sp500-7800-tradingkey"
    published_at: "2026-08-14T15:41:15.000Z"
    retrieved_at: "2026-08-17T08:37:49+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
