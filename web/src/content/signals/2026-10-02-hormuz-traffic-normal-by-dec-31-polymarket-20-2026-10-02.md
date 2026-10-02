---
signal_id: "CMSIG2026100206"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-20-2026-10-02"
headline: "Hormuz traffic normal by Dec 31: Polymarket 20%"
semantic_title: "Strait of Hormuz normal traffic by year-end stays unlikely"
telemetry: "Polymarket 20%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-02T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.2
  volume_24h_usd: 36261.407181
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract on Strait of Hormuz traffic returning to normal by December 31 prices at 20%, a clear long-shot read despite the uptick in oil flows."
  - "The news that oil volumes rose yet Iranian menacing persists is consistent with the 20% probability, partial normalization is not the same as full normalization."
  - "The U.S. deployment of a third aircraft carrier strike group to the Middle East (Story 17) adds military escalation risk, which the 20% price reflects."
  - "Resolves via UMA oracle; traders should note 'normal' traffic is likely defined against a pre-conflict baseline, making partial-flow improvements insufficient for YES resolution."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Oil flows through the Strait of Hormuz are reportedly up in September, but Iranian military activity near the strait continues, with near-daily reports of explosions heard from the sea."
    publisher: "New York Times"
    published_at: "2026-10-02T00:00:00.000Z"
    source_url: "https://dnyuz.com/2026/10/02/oil-flows-are-up-but-iran-is-still-menacing-the-strait-of-hormuz-2/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "New York Times"
        source_url: "https://dnyuz.com/2026/10/02/oil-flows-are-up-but-iran-is-still-menacing-the-strait-of-hormuz-2/"
        retrieved_at: "2026-10-02T14:25:25+00:00"
  - type: "pm_response"
    notes: "Polymarket at 20% for December 31 normalization indicates persistent skepticism despite the reported flow improvement, with escalating U.S. military presence adding downside risk to the contract."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "New York Times: Oil Flows Are Up, but Iran Is Still Menacing the Strait of Hormuz, DN"
    url: "https://dnyuz.com/2026/10/02/oil-flows-are-up-but-iran-is-still-menacing-the-strait-of-hormuz-2/"
    published_at: "2026-10-02T00:00:00.000Z"
    retrieved_at: "2026-10-02T14:25:25+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
