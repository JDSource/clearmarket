---
signal_id: "CMSIG2026101302"
signal_slug: "sept-cpi-mom-seen-at-0-5-0-6-prediction-market-ladder-2026-10-13"
headline: "Sept CPI MoM seen at 0.5-0.6%: prediction market ladder"
semantic_title: "September CPI month-over-month gain priced near 0.5 to 0.6 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-13T00:00:00.000Z"
event_id: "CM-EVT-F9NPW9F1V9"
event_slug: "kxcpi-26sep"
event_question: "September 2026 CPI month-over-month change"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPI-26SEP-T0.6"
  question_raw: "Will CPI rise more than 0.6% in September 2026?"
  current_price: 0.18
  volume_24h_usd: 6202.91
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-01-13T13:56:00Z"
bullets:
  - "The prediction market ladder implies September CPI month-over-month near 0.5-0.6%: 67% above 0.5% but only 18% above 0.6%."
  - "Governor Waller's 'well anchored' comment is in tension with the ladder, which prices a relatively hot monthly print consistent with the 3.6% year-over-year forecast in Stories 0 and 6."
  - "The sharp drop from 67% to 18% between the 0.5% and 0.6% strikes marks the market's credible upper bound for the monthly figure."
  - "Resolution is via the BLS CPI release; the October FOMC meeting (Story 5) will treat this print as a key input."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Fed Governor Christopher Waller said U.S. inflation expectations remain well anchored even as September CPI data is due Oct. 14."
    publisher: "Kylie Cooper"
    published_at: "2026-10-13T00:00:00.000Z"
    source_url: "https://www.galvnews.com/news_reuters/business/us-inflation-expectations-are-well-anchored-feds-waller-says/article_5b599df4-5617-54f7-bc53-2114e0c06d10.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Kylie Cooper"
        source_url: "https://www.galvnews.com/news_reuters/business/us-inflation-expectations-are-well-anchored-feds-waller-says/article_5b599df4-5617-54f7-bc53-2114e0c06d10.html"
        retrieved_at: "2026-10-14T07:47:32+00:00"
  - type: "pm_response"
    notes: "Prediction market ladder; the distribution's tight clustering around 0.5-0.6% suggests the market has largely digested pre-release analyst forecasts."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Kylie Cooper: US inflation expectations are well anchored, Fed's Waller says | Busin"
    url: "https://www.galvnews.com/news_reuters/business/us-inflation-expectations-are-well-anchored-feds-waller-says/article_5b599df4-5617-54f7-bc53-2114e0c06d10.html"
    published_at: "2026-10-13T00:00:00.000Z"
    retrieved_at: "2026-10-14T07:47:32+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
