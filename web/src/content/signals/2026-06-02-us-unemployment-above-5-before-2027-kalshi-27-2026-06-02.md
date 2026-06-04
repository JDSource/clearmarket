---
signal_id: "CMSIG2026060205"
signal_slug: "us-unemployment-above-5-before-2027-kalshi-27-2026-06-02"
headline: "US unemployment above 5% before 2027: Kalshi 27%"
semantic_title: "Unemployment above 5 percent before 2027 a long shot"
telemetry: "Kalshi 27%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-02T00:00:00.000Z"
event_id: "CM-EVT-RBY62SKLC0"
event_slug: "kxu3max-27"
event_question: "Peak US unemployment rate before 2027"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXU3MAX-27-5"
  question_raw: "How high will unemployment get before 2027?"
  current_price: 0.271
  volume_24h_usd: 14.25
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-01-08T15:00:00Z"
bullets:
  - "Kalshi ladder prices only 27% chance unemployment exceeds 5.0% before 2027, dropping to 10% above 6.0% and near zero above 7.0%."
  - "Strong April job openings data is consistent with the ladder's sub-5% implied peak; the market is not pricing a recession-level unemployment spike."
  - "The ladder's near-zero above 7.0% stands in contrast to the 90% Kalshi odds of more tech layoffs in 2026 versus 2025, suggesting sector-specific stress without macro contagion."
  - "Resolves via FRED unemployment rate data; ladder settles at the highest monthly unemployment rate recorded before January 1, 2027."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "April job openings jumped 731,000 to 7.62 million, the highest since May 2024, though Wolf Street notes the dynamic makes it harder for young people to find jobs."
    publisher: "wolfstreet.com"
    published_at: "2026-06-02T00:00:00.000Z"
    source_url: "https://wolfstreet.com/2026/06/02/and-more-data-showing-a-weirdly-decent-labor-market/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "wolfstreet.com"
        source_url: "https://wolfstreet.com/2026/06/02/and-more-data-showing-a-weirdly-decent-labor-market/"
        retrieved_at: "2026-06-03T01:50:17+00:00"
  - type: "pm_response"
    notes: "Kalshi unemployment ladder assigns minimal probability to any reading above 6%, making the 'weirdly decent' labor market label consistent with prediction market pricing."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "wolfstreet.com: And More Data Showing a Weirdly Decent Labor Market | Wolf Street"
    url: "https://wolfstreet.com/2026/06/02/and-more-data-showing-a-weirdly-decent-labor-market/"
    published_at: "2026-06-02T00:00:00.000Z"
    retrieved_at: "2026-06-03T01:50:17+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
