---
signal_id: "CMSIG2026092903"
signal_slug: "september-u-3-unemployment-kalshi-sees-4-0-4-1-range-2026-09-29"
headline: "September U-3 unemployment: Kalshi sees 4.0-4.1% range"
semantic_title: "September unemployment odds cluster near 4 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-29T00:00:00.000Z"
event_id: "CM-EVT-720DZC17Y9"
event_slug: "kxu3-26sep"
event_question: "September 2026 U-3 unemployment rate"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXU3-26SEP-T4.1"
  question_raw: "Will the unemployment rate (U-3) be above 4.1% in September?"
  current_price: 0.39
  volume_24h_usd: 718.57
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-01-01T14:00:00Z"
bullets:
  - "Kalshi ladder puts 70% odds above 4.0% and 39% above 4.1%, placing the market-implied September unemployment rate in the 4.0-4.1% range."
  - "Falling job openings are consistent with modest labor-market softening, aligning with the ladder's pricing just above the 4.0% threshold."
  - "Trading volume on this contract surged 12,270% day-over-day, signaling the JOLTS print drew significant fresh attention to the unemployment question."
  - "Resolution via the Bureau of Labor Statistics September jobs report; any surprise in nonfarm payrolls would reprice the 4.1% tail."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "U.S. job openings slipped to 7.1 million in August, a five-month low, though layoffs remained subdued and the labor market was described as sturdy."
    publisher: "Paul Wiseman, Associated Press"
    published_at: "2026-09-29T00:00:00.000Z"
    source_url: "https://www.news4jax.com/business/2026/09/29/us-job-openings-slipped-to-71-million-in-august-but-labor-market-remains-sturdy/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Paul Wiseman, Associated Press"
        source_url: "https://www.news4jax.com/business/2026/09/29/us-job-openings-slipped-to-71-million-in-august-but-labor-market-remains-sturdy/"
        retrieved_at: "2026-10-01T07:47:27+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder saw a 123.7x volume spike alongside the JOLTS release, marking this as the most actively traded labor-market contract in the batch."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Paul Wiseman, Associated Press: U.S. job openings slipped to 7.1 million in August but labor market re"
    url: "https://www.news4jax.com/business/2026/09/29/us-job-openings-slipped-to-71-million-in-august-but-labor-market-remains-sturdy/"
    published_at: "2026-09-29T00:00:00.000Z"
    retrieved_at: "2026-10-01T07:47:27+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
