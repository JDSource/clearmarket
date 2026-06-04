---
signal_id: "CMSIG2026060404"
signal_slug: "aug-2026-cpi-monthly-change-seen-0-3-0-4-kalshi-2026-06-04"
headline: "Aug 2026 CPI monthly change seen 0.3-0.4%: Kalshi"
semantic_title: "August CPI rise above 0.4 percent priced near a coin flip"
telemetry: "Kalshi 45%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-04T04:02:00.000Z"
event_id: "CM-EVT-D057W6W251"
event_slug: "kxcpi-26aug"
event_question: "August 2026 monthly CPI change"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPI-26AUG-T0.4"
  question_raw: "Will CPI rise more than 0.4% in August 2026?"
  current_price: 0.45
  volume_24h_usd: 0.45
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2026-09-11T13:56:00Z"
bullets:
  - "Kalshi implies August 2026 CPI monthly change in the 0.3-0.4% range: 61% above 0.3% but only 45% above 0.4%."
  - "Hot ISM prices-paid readings are consistent with a market expecting continued above-target monthly inflation prints."
  - "The 84% probability above 0.1% signals near-universal rejection of any near-term disinflation."
  - "Resolves via the Bureau of Labor Statistics official CPI release for August 2026."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "ISM PMI surveys beat estimates in May with manufacturing at a four-year high, but employment is contracting while prices stay hot."
    publisher: "Pippo 
 
 June 4, 2026  4:02 AM UTC  in  Analysis"
    published_at: "2026-06-04T04:02:00.000Z"
    source_url: "https://www.babypips.com/analysis/headline-ism-pmi-surveys-beat-estimates-may-fed-dilemma-2026-06-04"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Pippo 
 
 June 4, 2026  4:02 AM UTC  in  Analysis"
        source_url: "https://www.babypips.com/analysis/headline-ism-pmi-surveys-beat-estimates-may-fed-dilemma-2026-06-04"
        retrieved_at: "2026-06-04T11:14:54+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolves against the BLS official CPI monthly change figure."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Pippo 
 
 June 4, 2026  4:02 AM UTC  in  Analysis: ISM PMI Surveys Beat Estimates in May, But Fed’s Dilemma Got Worse - B"
    url: "https://www.babypips.com/analysis/headline-ism-pmi-surveys-beat-estimates-may-fed-dilemma-2026-06-04"
    published_at: "2026-06-04T04:02:00.000Z"
    retrieved_at: "2026-06-04T11:14:54+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
