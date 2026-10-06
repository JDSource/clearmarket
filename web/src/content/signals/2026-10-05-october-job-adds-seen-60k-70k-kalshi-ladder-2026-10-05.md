---
signal_id: "CMSIG2026100503"
signal_slug: "october-job-adds-seen-60k-70k-kalshi-ladder-2026-10-05"
headline: "October job adds seen 60K-70K: Kalshi ladder"
semantic_title: "October payrolls consensus holds in the 60K to 70K range"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-05T00:00:00.000Z"
event_id: "CM-EVT-6CSLHX0K76"
event_slug: "kxpayrolls-26oct"
event_question: "October 2026 nonfarm payroll adds"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPAYROLLS-26OCT-T70000"
  question_raw: "Will above 70000 jobs be added in October 2026?"
  current_price: 0.43
  volume_24h_usd: 535.4
  arbitration_model: "kalshi_staff"
  resolution_source: "BLS"
  resolves_at: "2027-02-05T15:00:00Z"
bullets:
  - "Kalshi ladder implies October payroll adds in the 60,000-70,000 range: 52% above 60K but only 43% above 70K."
  - "September's 29,000 print is directionally consistent with the ladder's cautious distribution, which gives only 25% odds of topping 100,000."
  - "The ladder still puts 92% above minus 25,000, so outright job losses remain a tail scenario rather than a base case."
  - "Resolves via FRED (Bureau of Labor Statistics Employment Situation release for October 2026)."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "September nonfarm payrolls came in well below expectations, raising questions about momentum heading into the October report."
    publisher: "kitco.com"
    published_at: "2026-10-05T00:00:00.000Z"
    source_url: "https://www.kitco.com/news/off-the-wire/2026-10-05/us-job-growth-undershoots-expectations-september-labor-market-remains"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "kitco.com"
        source_url: "https://www.kitco.com/news/off-the-wire/2026-10-05/us-job-growth-undershoots-expectations-september-labor-market-remains"
        retrieved_at: "2026-10-06T14:42:27+00:00"
  - type: "pm_response"
    notes: "Kalshi's October payroll ladder reflects subdued but positive job-growth expectations after September's soft print."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "kitco.com: US job growth undershoots expectations in September, but labor market"
    url: "https://www.kitco.com/news/off-the-wire/2026-10-05/us-job-growth-undershoots-expectations-september-labor-market-remains"
    published_at: "2026-10-05T00:00:00.000Z"
    retrieved_at: "2026-10-06T14:42:27+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
