---
signal_id: "CMSIG2026110603"
signal_slug: "peak-unemployment-before-2027-kalshi-ladder-below-4-5-2026-11-06"
headline: "Peak unemployment before 2027: Kalshi ladder below 4.5%"
semantic_title: "Unemployment staying well under 5 percent stays the consensus"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-06T13:31:05.000Z"
event_id: "CM-EVT-RBY62SKLC0"
event_slug: "kxu3max-27"
event_question: "Peak US unemployment rate before 2027"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXU3MAX-27-4.5"
  question_raw: "How high will unemployment get before 2027?"
  current_price: 0.09
  volume_24h_usd: 6.58
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-03-09T15:00:00Z"
bullets:
  - "Kalshi ladder puts only 9% on unemployment reaching 4.5% before 2027, with probabilities falling sharply above that level."
  - "October's 165,000 payroll beat and 4.1% unemployment print are consistent with the ladder's strong lean toward sub-4.5% peak unemployment."
  - "Probabilities above 5.0% are in the low single digits, indicating the market is not pricing any near-term labor market breakdown."
  - "Ladder resolution depends on official BLS unemployment readings through the end of 2026."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "US employers added 165,000 jobs in October, far above the 59,000 Wall Street forecast, while the unemployment rate fell to 4.1%."
    publisher: "Jeff Cox"
    published_at: "2026-11-06T13:31:05.000Z"
    source_url: "https://www.cnbc.com/2026/11/06/jobs-report-october-2026.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Jeff Cox"
        source_url: "https://www.cnbc.com/2026/11/06/jobs-report-october-2026.html"
        retrieved_at: "2026-11-09T07:47:40+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder distribution; the strong October jobs report reinforces the market's existing low-unemployment consensus."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Jeff Cox: U.S. economy added 165,000 jobs in October, way more than expected; un"
    url: "https://www.cnbc.com/2026/11/06/jobs-report-october-2026.html"
    published_at: "2026-11-06T13:31:05.000Z"
    retrieved_at: "2026-11-09T07:47:40+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
