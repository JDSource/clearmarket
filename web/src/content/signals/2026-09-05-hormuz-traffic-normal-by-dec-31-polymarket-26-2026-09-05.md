---
signal_id: "CMSIG2026090508"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-26-2026-09-05"
headline: "Hormuz traffic normal by Dec 31: Polymarket 26%"
semantic_title: "Hormuz traffic returning to normal by year-end stays below 25 percent"
telemetry: "Polymarket 26%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-05T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.26
  volume_24h_usd: 34171.944291
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices 26% odds that Strait of Hormuz traffic returns to normal by December 31, resolving via UMA oracle."
  - "US intelligence reporting that Iran views Hormuz as leverage and is weighing escalation is consistent with the sub-30% pricing, the market is not buying a near-term resolution."
  - "At 26%, the market is treating Hormuz normalization as a long shot for 2026, implying persistent disruption risk in global energy shipping lanes."
  - "Resolution via UMA oracle; 'normal' traffic levels will need a clear, verifiable benchmark, traders should watch how the oracle defines the baseline before the December deadline."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "US intelligence assessments indicate Iran is determined to continue the war and is weighing major escalation, including leverage over the Strait of Hormuz."
    publisher: "ynet"
    published_at: "2026-09-05T00:00:00.000Z"
    source_url: "https://www.ynetnews.com/article/hkn9szfuzg"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "ynet"
        source_url: "https://www.ynetnews.com/article/hkn9szfuzg"
        retrieved_at: "2026-09-05T11:34:19+00:00"
  - type: "pm_response"
    notes: "Polymarket at 26% reflects broad skepticism about a Hormuz resolution this year, aligned with the hawkish US intelligence picture."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "ynet: US intelligence: Iran determined to continue war, weighing major escal"
    url: "https://www.ynetnews.com/article/hkn9szfuzg"
    published_at: "2026-09-05T00:00:00.000Z"
    retrieved_at: "2026-09-05T11:34:19+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
