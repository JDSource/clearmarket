---
signal_id: "CMSIG2026101303"
signal_slug: "sept-cpi-market-implied-near-0-5-0-6-range-ladder-2026-10-13"
headline: "Sept CPI market-implied near 0.5%-0.6% range: ladder"
semantic_title: "September CPI implied around zero to slightly positive by markets"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-13T00:00:00.000Z"
event_id: "CM-EVT-F9NPW9F1V9"
event_slug: "kxcpi-26sep"
event_question: "September 2026 CPI monthly change"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPI-26SEP-T0.6"
  question_raw: "Will CPI rise more than 0.6% in September 2026?"
  current_price: 0.13
  volume_24h_usd: 3890.09
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-01-13T13:56:00Z"
bullets:
  - "Prediction market ladder puts September 2026 CPI monthly change implied at roughly 0.5%-0.6%, with 60% above 0.5% but only 13% above 0.6%."
  - "Fed Governor Christopher Waller's well-anchored inflation message is broadly consistent with the ladder's implied modest positive monthly reading, not a reacceleration."
  - "The IMF separately forecasts U.S. inflation picking up in 2026, but the ladder's distribution does not price a large upside surprise in September."
  - "September CPI data is due this week per market context; the Bureau of Labor Statistics release will settle the prediction market contract."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Fed Governor Christopher Waller said U.S. inflation expectations remain well anchored, speaking at the Istanbul Economic Forum on October 8, 2026."
    publisher: "Kylie Cooper"
    published_at: "2026-10-13T00:00:00.000Z"
    source_url: "https://www.centraloregondaily.com/news/consumer/us-inflation-expectations-are-well-anchored-feds-waller-says/article_5c6433f9-9309-5f24-8ac0-68c460f48d2f.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Kylie Cooper"
        source_url: "https://www.centraloregondaily.com/news/consumer/us-inflation-expectations-are-well-anchored-feds-waller-says/article_5c6433f9-9309-5f24-8ac0-68c460f48d2f.html"
        retrieved_at: "2026-10-13T15:32:34+00:00"
  - type: "pm_response"
    notes: "The prediction market ladder on September 2026 CPI monthly change prices a central estimate near 0.5%, consistent with Waller's anchored-expectations framing."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Kylie Cooper: US inflation expectations are well anchored, Fed's Waller says | Consu"
    url: "https://www.centraloregondaily.com/news/consumer/us-inflation-expectations-are-well-anchored-feds-waller-says/article_5c6433f9-9309-5f24-8ac0-68c460f48d2f.html"
    published_at: "2026-10-13T00:00:00.000Z"
    retrieved_at: "2026-10-13T15:32:34+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
