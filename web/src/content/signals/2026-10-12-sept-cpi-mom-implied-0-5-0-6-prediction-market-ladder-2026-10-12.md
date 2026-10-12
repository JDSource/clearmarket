---
signal_id: "CMSIG2026101204"
signal_slug: "sept-cpi-mom-implied-0-5-0-6-prediction-market-ladder-2026-10-12"
headline: "Sept CPI MoM implied 0.5-0.6%: prediction market ladder"
semantic_title: "September CPI month-over-month priced in the 0.5 to 0.6 range"
telemetry: "Kalshi ladder"
category_tag: "PRE_EVENT_PRICING"
detection_path: "news_cycle"
pre_news_classification: "pre_news"
published_at: "2026-10-12T06:26:51.000Z"
event_id: "CM-EVT-F9NPW9F1V9"
event_slug: "kxcpi-26sep"
event_question: "September 2026 CPI month-over-month change"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPI-26SEP-T0.6"
  question_raw: "Will CPI rise more than 0.6% in September 2026?"
  current_price: 0.15
  volume_24h_usd: 2542.63
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-01-13T13:56:00Z"
bullets:
  - "The ladder prices September CPI month-over-month in the 0.5-0.6% range: 59% above 0.5% but only 15% above 0.6%, indicating a firm but not extreme print is consensus."
  - "Consumer inflation expectations rising to 4.7% ahead of the print are consistent with the ladder's above-0.5% lean, not at odds with it."
  - "Natixis separately forecast a 0.6% headline CPI for September, sitting squarely at the upper edge of the ladder's modal range."
  - "Resolution is via the Bureau of Labor Statistics September CPI release; the report is scheduled for Wednesday, October 14."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "US inflation expectations rose to 4.7% ahead of the September CPI release, raising concern about a hot print."
    publisher: "investing.com"
    published_at: "2026-10-12T06:26:51.000Z"
    source_url: "https://www.investing.com/analysis/us-inflation-expectations-rise-to-47-ahead-of-cpi-200689364"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "investing.com"
        source_url: "https://www.investing.com/analysis/us-inflation-expectations-rise-to-47-ahead-of-cpi-200689364"
        retrieved_at: "2026-10-12T07:49:04+00:00"
  - type: "pm_response"
    notes: "The prediction market ladder on September CPI month-over-month is the most directly positioned contract ahead of Wednesday's BLS release."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "investing.com: US Inflation Expectations Rise to 4.7% Ahead of CPI | Investing.com"
    url: "https://www.investing.com/analysis/us-inflation-expectations-rise-to-47-ahead-of-cpi-200689364"
    published_at: "2026-10-12T06:26:51.000Z"
    retrieved_at: "2026-10-12T07:49:04+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
