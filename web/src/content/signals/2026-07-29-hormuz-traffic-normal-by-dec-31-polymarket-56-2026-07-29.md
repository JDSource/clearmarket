---
signal_id: "CMSIG2026072906"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-56-2026-07-29"
headline: "Hormuz traffic normal by Dec 31: Polymarket 56%"
semantic_title: "Strait of Hormuz traffic return by year-end near 50%"
telemetry: "Polymarket 56%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-29T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.56
  volume_24h_usd: 128388.29305899999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices a 56% probability that Strait of Hormuz traffic returns to normal by December 31, 2026."
  - "Iran's rejection of the Omani management proposal and continued missile exchanges are consistent with a market near 50-50 on normalization within the year."
  - "A companion near-term Polymarket contract on Hormuz normalizing by July 31 sits at 0%, showing markets see no imminent resolution."
  - "Resolves via UMA oracle; the 56% by year-end versus 0% by July 31 gap captures the market's view that resolution, if it comes, is months away."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran rejected an Omani proposal to manage the Strait of Hormuz while U.S. and Saudi forces struck Iran-backed militias in Iraq following Iranian missile attacks on U.S. bases."
    publisher: "euronews.com"
    published_at: "2026-07-29T00:00:00.000Z"
    source_url: "https://www.euronews.com/2026/07/29/us-intercepts-iranian-attack-and-launches-joint-strikes-with-saudi-arabia-against-iran-bac"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "euronews.com"
        source_url: "https://www.euronews.com/2026/07/29/us-intercepts-iranian-attack-and-launches-joint-strikes-with-saudi-arabia-against-iran-bac"
        retrieved_at: "2026-07-29T10:35:12+00:00"
  - type: "pm_response"
    notes: "Polymarket covers both a July 31 (0%) and December 31 (56%) Hormuz normalization horizon, with the spread mapping the market's timeline uncertainty."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "euronews.com: US intercepts Iranian attack and launches joint strikes with Saudi Ara"
    url: "https://www.euronews.com/2026/07/29/us-intercepts-iranian-attack-and-launches-joint-strikes-with-saudi-arabia-against-iran-bac"
    published_at: "2026-07-29T00:00:00.000Z"
    retrieved_at: "2026-07-29T10:35:12+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
