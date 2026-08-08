---
signal_id: "CMSIG2026080804"
signal_slug: "july-2026-cpi-monthly-change-ladder-implies-0-0-0-1-2026-08-08"
headline: "July 2026 CPI monthly change: ladder implies 0.0%-0.1%"
semantic_title: "July CPI monthly change priced near flat to slightly positive"
telemetry: "Kalshi ladder"
category_tag: "PRE_EVENT_PRICING"
detection_path: "news_cycle"
pre_news_classification: "pre_news"
published_at: "2026-08-08T08:31:16.947Z"
event_id: "CM-EVT-HVKDYMRT39"
event_slug: "kxcpi-26jul"
event_question: "July 2026 CPI monthly change"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPI-26JUL-T0.1"
  question_raw: "Will CPI rise more than 0.1% in July 2026?"
  current_price: 0.21
  volume_24h_usd: 3139.62
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2026-11-11T13:56:00Z"
bullets:
  - "Ladder implies the July 2026 CPI monthly change in the 0.0%-0.1% range: 60% above 0.0% but only 21% above 0.1%."
  - "June CPI of 333.95 was below May's 335.12, consistent with the ladder's lean toward a near-flat monthly print."
  - "Services sector strength and rising input costs (Story 4) provide upside risk, but the ladder puts only 10% probability above 0.2%."
  - "Resolves via BLS CPI release for July 2026; the survey covers urban consumer prices for all items."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "CPI for all urban consumers was 333.95 in June, down from 335.12 in May, continuing a volatile recent trend."
    publisher: "exa.ai"
    published_at: "2026-08-08T08:31:16.947Z"
    source_url: "https://exa.ai/library/markets/economy/inflation?date=2026-08-08"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "exa.ai"
        source_url: "https://exa.ai/library/markets/economy/inflation?date=2026-08-08"
        retrieved_at: "2026-08-08T08:35:11+00:00"
  - type: "pm_response"
    notes: "Ladder distribution via ClearMarket reference layer; July BLS CPI release is the resolution trigger."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "exa.ai: U.S. Inflation, Consumer Price Index for all Urban Consumers: 333.95"
    url: "https://exa.ai/library/markets/economy/inflation?date=2026-08-08"
    published_at: "2026-08-08T08:31:16.947Z"
    retrieved_at: "2026-08-08T08:35:11+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
